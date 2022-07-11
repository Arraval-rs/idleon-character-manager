#####################################################
# ICM_functions.py                                  #
# Various functions used by the app                 #
# Also includes some variables used across the app  # 
#####################################################
import os
import io
import json
import PySimpleGUI as sg
from PIL import Image, ImageDraw

# General Functions
def dictionary_contains(dict, dict_path):
    try:
        if int(dict_path[0]) > len(dict):
            print('Index {} outside of dictionary'.format(dict_path))
            return False
    except ValueError:
        if dict_path[0] not in dict:
            print('Missing {} from dictionary'.format(dict_path))
            return False
    if len(dict_path) == 1:
        return True
    return dictionary_contains(dict[dict_path[0]], dict_path[1:len(dict_path)])

def dictionary_read(dict, dict_path):
    if dictionary_contains(dict, dict_path):
        val = dict
        for p in dict_path:
            val = val[p]
        return val
    return '(_)'

def generate_img(f, s, bg): # Generates image using PIL
    if "None" in f:
        f = 'images/Empty Slot.png'
    if not os.path.exists(f):
        print('ERROR: Cannot find {}'.format(f))
        f = 'images/Missing.png'
    img = Image.open(f).resize(s)
    if bg:
        item_bg = Image.open('images/Empty Slot.png').resize(s)
        item_bg.paste(img, (0, 0), img.convert('RGBA'))
        img = item_bg
    img.thumbnail(s)
    bio = io.BytesIO()
    img.save(bio, format = "PNG")
    return bio.getvalue()

def find_image(name, paths):
    for p in paths:
        path = 'images/{}/{}.png'.format(p, name)
        if os.path.exists(path):
            return path
    return 'images/Missing.png'

def get_class_path(c, depth): # returns the path to talent images for given class and class depth
    if depth == 1: # base class
        if c in ('Mage', 'Wizard', 'Elemental Sorcerer', 'Shaman', 'Bubonic Conjuror'):
            return talents['Mage']
        if c in ('Bowman', 'Hunter', 'Siege Breaker', 'Beast Master'):
            return talents['Archer']
        if c in ('Barbarian', 'Squire', 'Blood Berserker', 'Divine Knight'):
            return talents['Warrior']
        if c in ('Journeyman', 'Maestro'):
            return talents['Journeyman']
        print("ERROR: given class '{}' is not a base class".format(c))
    if depth == 2: # sub class
        if c in ('Wizard', 'Elemental Sorcerer'):
            return talents['Mage']['Wizard']
        if c in ('Shaman', 'Bubonic Conjuror'):
            return talents['Mage']['Shaman']
        if c in ('Bowman', 'Siege Breaker'):
            return talents['Archer']['Bowman']
        if c in ('Hunter', 'Beast Master'):
            return talents['Archer']['Hunter']
        if c in ('Barbarian', 'Blood Berserker'):
            return talents['Warrior']['Barbarian']
        if c in ('Squire', 'Divine Knight'):
            return talents['Warrior']['Squire']
        if c in ('Maestro'):
            return talents['Journeyman']['Maestro']
        print("ERROR: given class '{}' is not a sub class".format(c))
    if depth == 3: # elite class
        if c in ('Elemental Sorcerer'):
            return talents['Mage']['Wizard']['Elemental Sorcerer']
        if c in ('Bubonic Conjuror'):
            return talents['Mage']['Shaman']['Bubonic Conjuror']
        if c in ('Siege Breaker'):
            return talents['Archer']['Bowman']['Siege Breaker']
        if c in ('Beast Master'):
            return talents['Archer']['Hunter']['Beast Master']
        if c in ('Blood Berserker'):
            return talents['Warrior']['Barbarian']['Blood Berserker']
        if c in ('Divine Knight'):
            return talents['Warrior']['Squire']['Divine Knight']
        print("ERROR: given class '{}' is not an elite class".format(c))

def get_class_depth(c):
    if c in ('Mage', 'Archer', 'Warrior', 'Journeyman'):
        return 1 # Base class
    if c in ('Wizard', 'Shaman', 'Hunter', 'Bowman', 'Berserker', 'Squire', 'Maestro'):
        return 2 # Sub class
    if c in ('Elemental Sorcerer', 'Bubonic Conjuror', 'Beast Master', 'Siege Breaker', 'Blood Berserker', 'Divine Knight'):
        return 3 # Elite class
    return 0 # Beginner

def get_base_class(c): # returns the base class of a given class
    if c in ('Wizard', 'Shaman', 'Bubonic Conjuror', 'Elemental Sorcerer'):
        return 'Mage'
    if c in ('Bowman', 'Hunter', 'Siege Breaker', 'Beast Master'):
        return 'Archer'
    if c in ('Barbarian', 'Squire', 'Blood Berserker', 'Divine Knight'):
        return 'Warrior'
    if c in ('Maestro'):
        return 'Journeyman'
    return c

def get_sub_class(c): # returns the sub class of a given class
    if c in ('Bubonic Conjuror'):
        return 'Shaman'
    if c in ('Elemental Sorcerer'):
        return 'Wizard'
    if c in ('Siege Breaker'):
        return 'Bowman'
    if c in ('Beast Master'):
        return 'Hunter'
    if c in ('Blood Berserker'):
        return 'Barbarian'
    if c in ('Divine Knight'):
        return 'Squire'
    return c

def is_base_class(c): # returns true if the given class is a base class (Beginner, Warrior, Mage, Archer, Journeyman)
    if c in ('Beginner', 'Warrior', 'Mage', 'Archer', 'Journeyman'):
        return True
    return False

def is_sub_class(c): # returns true if the given class is a sub class
    if c in ('Barbarian', 'Squire', 'Bowman', 'Hunter', 'Shaman', 'Wizard', 'Maestro'):
        return True
    return False

def is_elite_class(c): # returns true if the given class is an elite class
    if c in ('Blood Berserker', 'Divine Knight', 'Siege Breaker', 'Beast Master', 'Bubonic Conjuror', 'Elemental Sorcerer'):
        return True
    return False

def calculate_hit_chance(char_acc, acc_100):
    if acc_100 != 0:
        try:
            char_acc = int(char_acc)
        except:
            char_acc = 0
        hit_chance = int(max(0, min(100, 142.5 * char_acc / acc_100 - 42.5)))
        if hit_chance >= 5:
            return hit_chance
    return 0

def calculate_accuracy_needed(char_acc, acc_100):
    try:
        char_acc = int(char_acc)
    except:
        char_acc = 0
    return max(0, acc_100 - char_acc)

def calculate_damage_taken(char_def, atk_dam):
    try: 
        char_def = int(char_def)
    except:
        char_def = 0
    return max(0, int((atk_dam - 2.5 * char_def**0.8) / max(1, 1 + char_def**2.5 / max(100, 100*atk_dam))))

def calculate_defence_needed(char_def, def_0):
    try: 
        char_def = int(char_def)
    except:
        char_def = 0
    return max(0, def_0 - char_def)

def max_hp(character):
    return 0 # placeholder

def max_mp(character):
    return 0 # placeholder

def damage(character):
    max_damage = 0 # placeholder
    mastery = 0 # placeholder
    return '{}-{}'.format(max_damage, mastery*max_damage)

def crit_chance(character):
    return 0 # placeholder

def crit_damage(character):
    return 0 # placeholder

def accuracy(character):
    return 0 # placeholder

def defence(character):
    return 0 # placeholder

def movement_speed(character):
    return 0 # placeholder

def drop_rarity(character):
    return 0 # placeholder

def class_exp(character):
    return 0 # placeholder

def get_character_stats(character, dict):
    stat_str = 'Max HP: {}\n'.format(max_hp(character))
    stat_str += 'Max MP: {}\n'.format(max_mp(character))
    stat_str += 'Damage: {}\n'.format(damage(character))
    stat_str += 'STR: {}\n'.format(dict['characters'][character]['strength'])
    stat_str += 'AGI: {}\n'.format(dict['characters'][character]['agility'])
    stat_str += 'WIS: {}\n'.format(dict['characters'][character]['wisdom'])
    stat_str += 'LUK: {}\n'.format(dict['characters'][character]['luck'])
    stat_str += 'Crit Chance: {}\n'.format(crit_chance(character))
    stat_str += 'Crit Damage: {}\n'.format(crit_damage(character))
    stat_str += 'Accuracy: {}\n'.format(accuracy(character))
    stat_str += 'Defence: {}\n'.format(defence(character))
    stat_str += 'Movement Speed: {}\n'.format(movement_speed(character))
    stat_str += 'Drop Rarity: {}\n'.format(drop_rarity(character))
    stat_str += 'Class EXP: {}\n'.format(class_exp(character))
    return stat_str

def get_item_stats(equip_type, character, index):
    if equip_type in {'equipment', 'tools'}:
        stat_str = 'STR: {}'.format(dictionary['characters'][character][equip_type][index]['stoneData']['STR'])
        stat_str += '\t\tReach: {}'.format(dictionary['characters'][character][equip_type][index]['stoneData']['Reach'] if 'Reach' in dictionary['characters'][character][equip_type][index]['stoneData'] else '0')
        stat_str += '\nAGI: {}'.format(dictionary['characters'][character][equip_type][index]['stoneData']['AGI'])
        stat_str += '\t\tDefence: {}'.format(dictionary_read(dictionary, ['characters', character, equip_type, index, 'stoneData', 'Defence']))
        stat_str += '\nWIS: {}'.format(dictionary['characters'][character][equip_type][index]['stoneData']['WIS'])
        stat_str += '\t\tWeapon Power: {}'.format(dictionary['characters'][character][equip_type][index]['stoneData']['Weapon_Power'] if 'Weapon Power' in dictionary['characters'][character][equip_type][index]['stoneData'] else '0')
        stat_str += '\nLUK: {}'.format(dictionary['characters'][character][equip_type][index]['stoneData']['LUK'])
        stat_str += '\t\tUpgrade Slots Left: {}'.format(dictionary['characters'][character][equip_type][index]['stoneData']['Upgrade_Slots_Left'] if equip_type == 'equipment' else 0)
    else:
        stat_str = 'Stack Size: {}'.format(dictionary['characters'][character][equip_type][index]['count'])
    return stat_str

def update_selected_equipment(window, equip_type, character, item):
    window['selected_equipment'].update(data = generate_img('images/{}/{}.png'.format(equip_type, dictionary['characters'][character][equip_type][item]['name']), (72, 72), True))
    window['equipped_item_stats'].update(get_item_stats(equip_type, character, item))
    window['equipped_item_frame'].update(value = dictionary_read(dictionary, ['characters', character, equip_type, item, 'name']))
    return

def update_selected_inventory_item(window, slot, paths, character):
    window['selected_inventory_item'].update(data = get_inventory_item(slot, paths, character))
    window['inventory_item_stats'].update('Stack Size: {}'.format(dictionary['characters'][character]['inventory'][slot]['count']))
    item_name = dictionary_read(dictionary, ['characters', character, 'inventory', slot, 'name'])
    if item_name == '(_)':
        window['inventory_item_frame'].update(value = 'Locked')
    else:
        window['inventory_item_frame'].update(value = item_name)
    return

def update_selected_storage_item(window, slot, paths):
    window['selected_storage_item'].update(data = get_storage_item(slot, paths))
    window['storage_item_stats'].update('Stack Size: {}'.format(dictionary_read(dictionary, ['account', 'chest', slot, 'count'])))
    item_name = dictionary_read(dictionary, ['account', 'chest', slot, 'item'])
    if item_name == '(_)':
        window['storage_item_frame'].update(value = 'Locked')
    else:
        window['storage_item_frame'].update(value = item_name)
    return

def get_inventory_item(i, paths, character):
    if 'name' not in dictionary['characters'][character]['inventory'][i] or dictionary['characters'][character]['inventory'][i]['name'] == 'LockedInvSpace':
        return generate_img('images/Locked.png', (72, 72), False)
    if dictionary['characters'][character]['inventory'][i]['name'] == 'None':
        return generate_img('None', (72, 72), False)
    for p in paths:
        path = 'images/{}/{}.png'.format(p, dictionary['characters'][character]['inventory'][i]['name'])
        if os.path.exists(path):
            return generate_img(path, (72, 72), True)
    return generate_img('images/Missing.png', (72, 72), True)

def get_storage_item(i, paths):
    if 'item' not in dictionary['account']['chest'][i] or dictionary['account']['chest'][i]['item'] == 'LockedInvSpace':
        return generate_img('images/Locked.png', (72, 72), False)
    if dictionary['account']['chest'][i]['item'] == 'None':
        return generate_img('None', (72, 72), False)
    for p in paths:
        path = 'images/{}/{}.png'.format(p, dictionary['account']['chest'][i]['item'])
        if os.path.exists(path):
            return generate_img(path, (72, 72), True)
    return generate_img('images/Missing.png', (72, 72), True)

def get_crafting_item(tab, i, paths):
    if i >= len(craftables[tab]):
        return generate_img('images/Locked.png', (72, 72), False)
    if craftables[tab][i]['name'] == 'None':
        return generate_img('None', (72, 72), False)
    for p in paths:
        path = 'images/{}/{}.png'.format(p, craftables[tab][i]['name'])
        if os.path.exists(path):
            return generate_img(path, (72, 72), True)
    return generate_img('images/Missing.png', (72, 72), True)

def get_ingredient_image(tab, item, index, paths):
    if index > len(craftables[tab][item]['ingredients']) - 1:
        return generate_img('images/Locked.png', (72, 72), False)
    for p in paths:
        path = 'images/{}/{}.png'.format(p, craftables[tab][item]['ingredients'][index]['name'])
        if os.path.exists(path):
            return generate_img(path, (72, 72), True)
    return generate_img('images/Missing.png', (72, 72), True)

def is_craftable(item):
    for tab in tab_titles:
        for craft_item in craftables[tab]:
            if craft_item['name'] == item['name']:
                return True
    return False

def have_materials(materials):
    craft_possible = True
    for craft_mat in materials:
        num_held = 0
        # iterate through storage
        for stored_item in dictionary['account']['chest']:
            if stored_item['item'] == craft_mat['name']:
                num_held += stored_item['count']
        # iterate through player inventories
        for character in dictionary['characters']:
            for held_item in character['inventory']:
                if held_item['name'] == craft_mat['name']:
                    num_held += held_item['count']
        if num_held < craft_mat['count']:
            craft_possible = False
            craft_mat['acquired'] = False
    return craft_possible

def update_ingredient_counts(crafts, recursive, craftable_text):
    new_counts = []
    if recursive: #determine if item is craftable and update accordingly
        craftable_materials = []
        for item in crafts:
            for tab in tab_titles:
                for craft_item in craftables[tab]:
                    if craft_item['name'] == item[0]:
                        for new_ingredient in craft_item['ingredients']:
                            if is_craftable(new_ingredient):
                                craftable_materials.append([new_ingredient['name'], new_ingredient['count']])
                                craftable_materials[-1][1] = craftable_materials[-1][1] * item[1]
                            else:
                                found = False
                                for current_ingredient in new_counts:
                                    if new_ingredient['name'] == current_ingredient['name']:
                                        found = True
                                        current_ingredient['count'] += new_ingredient['count'] * item[1]
                                        break
                                if not found:
                                    new_counts.append({'name':new_ingredient['name'], 'count':new_ingredient['count'], 'acquired':True})
                                    new_counts[-1]['count'] = new_ingredient['count'] * item[1]
        if len(craftable_materials) > 0:
            for new_ingredient in update_ingredient_counts(craftable_materials, True, craftable_text):
                found = False
                for current_ingredient in new_counts:
                    if new_ingredient['name'] == current_ingredient['name']:
                        found = True
                        current_ingredient['count'] += new_ingredient['count']
                if not found:
                    new_counts.append(new_ingredient)
    else:
        for item in crafts:
            for tab in tab_titles:
                for craft_item in craftables[tab]:
                    if craft_item['name'] == item[0]:
                        for new_ingredient in craft_item['ingredients']:
                            found = False
                            for current_ingredient in new_counts:
                                if new_ingredient['name'] == current_ingredient['name']:
                                    found = True
                                    current_ingredient['count'] += new_ingredient['count'] * item[1]
                                    break
                            if not found:
                                new_counts.append({'name':new_ingredient['name'], 'count':new_ingredient['count'], 'acquired':True})
                                new_counts[-1]['count'] = new_ingredient['count'] * item[1]
    if len(new_counts) == 0:
        craftable_text.update('List is empty!')
    elif have_materials(new_counts):
        craftable_text.update('Items are craftable!')
    else:
        craftable_text.update('Not enough materials!')
    # if !have_space():
    #   craftable_text.update('Not enough inventory space!')
    return new_counts


# General Variables from here on

# Dictionary for JSON from Idleon API Downloader
json_file = open("data/idleon_data.json", "rt")
json_text = json_file.read()
dictionary = json.loads(json_text)

# Dictionary for crafting recepies
json_file = open("data/crafting_data.json", "rt")
json_text = json_file.read()
craftables = json.loads(json_text)
tab_titles = ['Beginner Tier', 'Novice Tier', 'Apprentice Tier', 'Journeyman Tier', 'Adept Tier']

# Dictionary for monsters
json_file = open("data/monster_data.json", "rt")
json_text = json_file.read()
monsters = json.loads(json_text)

# All image paths
image_paths = [ 'Materials', 'Statues', 'Food', 'Tools', \
                'Equipment', 'Pouches', 'Inventory', 'Stamps', \
                'Storage', 'Consumables', 'Upgrades', 'Misc Items',
                'Quest Items', 'Event']

# Dictionary for talent images
talents =   {
                'Mage':{'Shaman':{'Bubonic Conjuror':{}}, 'Wizard':{'Elemental Sorcerer':{}}}, 
                'Warrior':{'Barbarian':{'Blood Berserker':{}}, 'Squire':{'Divine Knight':{}}}, 
                'Archer':{'Bowman':{'Siege Breaker':{}}, 'Hunter':{'Beast Master':{}}},
                'Journeyman':{'Maestro':{}},
                'Star':{'Tab1':{}, 'Tab2':{}, 'Tab3':{}, 'Tab4':{}, 'Tab5':{}}
            }

# List of characters for the combobox
character_list = []
for i in range(0, len(dictionary['characters'])):
    character_list.append('{name} Lv. {level} {class_name}'.format(\
        name = dictionary['characters'][i]['name'], \
        level = dictionary['characters'][i]['level'], \
        class_name = dictionary['characters'][i]['class']))
    i = i + 1

# List of skill names in order
skill_names =   [
                    'Mining', 'Smithing', 'Chopping', 
                    'Fishing', 'Alchemy', 'Catching', 
                    'Trapping', 'Construction', 'Worship'
                ]

# List of currently selected crafting recipies
current_recipies = []

# List of ingredients for currently selected recipies
total_ingredients = []

# List of the two possible monster animations
current_monster = ['', 0]

# Last storage page
last_storage_page = 0