#####################################################
# ICM_functions.py                                  #
# All functions used by the app for easy searching  #
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
        f = 'images/Missing.png'
    img = Image.open(f).resize(s)
    if bg:
        item_bg = Image.open('images/Empty Slot.png')
        item_bg.paste(img, (0, 0), img.convert('RGBA'))
        img = item_bg
    img.thumbnail(s)
    bio = io.BytesIO()
    img.save(bio, format = "PNG")
    return bio.getvalue()

def get_base_class(c): # returns the base class of a given class
    if c == 'Wizard' or c == 'Shaman':
        return 'Mage'
    elif c == 'Bowman' or c == 'Hunter':
        return 'Archer'
    elif c == 'Barbarian' or c == 'Squire':
        return 'Warrior'
    elif c == 'Maestro':
        return 'Journeyman'
    return c

def is_base_class(c): # returns true if the given class is a base class (Beginner, Warrior, Mage, Archer, Journeyman)
    if c in ('Beginner', 'Warrior', 'Mage', 'Archer', 'Journeyman'):
        return True
    return False

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
    if 'name' not in dictionary['characters'][character]['inventory'][i]:
        return generate_img('images/Locked.png', (72, 72), False)
    if dictionary['characters'][character]['inventory'][i]['name'] == 'None':
        return generate_img('None', (72, 72), False)
    for p in paths:
        path = 'images/{}/{}.png'.format(p, dictionary['characters'][character]['inventory'][i]['name'])
        if os.path.exists(path):
            return generate_img(path, (72, 72), True)
    return generate_img('images/Missing.png', (72, 72), True)

def get_storage_item(i, paths):
    if 'item' not in dictionary['account']['chest'][i]:
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

def get_crafting_ingredient(tab, item, index, paths):
    if index > len(craftables[tab][item]['ingredients']) - 1:
        return generate_img('images/Locked.png', (72, 72), False)
    for p in paths:
        path = 'images/{}/{}.png'.format(p, craftables[tab][item]['ingredients'][index]['name'])
        if os.path.exists(path):
            return generate_img(path, (72, 72), True)
    return generate_img('images/Missing.png', (72, 72), True)

def update_selected_crafting_item():
    return

def crafting_popup():
    preview_frame = sg.Frame('None', layout = [[sg.Sizer(40), 
                                                sg.Image(data = generate_img('images/Empty Slot.png', (72, 72), False), key = 'preview_image'), 
                                                sg.Sizer(40)]], key = 'preview_frame', element_justification = 'center')
    ingredient_col = []
    for i in range(0, 2):
        for j in range(0, 2):
            ingredient_col.append(sg.Column(
                                    [
                                        [sg.Image(data = generate_img('images/Locked.png', (72, 72), False), key = 'ingredient{}'.format(2 * i + j))], 
                                        [sg.Text('0', size = (5, 1), relief = 'sunken', justification = 'center', key = 'ingredient{}cost'.format(2 * i + j))]], 
                                    element_justification = 'center'))
    cost_frame = sg.Frame('Costs', layout = [[ingredient_col[0], ingredient_col[1]], [ingredient_col[2], ingredient_col[3]]])
    tab = []
    for i in range(0, 3):
        tab.append(sg.Column([[sg.Graph((72, 72), (0, 0), (72, 72), change_submits = True, key = 'tab{}_item{}'.format(i, 4 * k + j)) for j in range(0 , 4)] for k in range(0, 4)]))
    anvil_tab_1 = sg.Tab('I', layout = [[tab[0]]])
    anvil_tab_2 = sg.Tab('II', layout = [[tab[1]]])
    anvil_tab_3 = sg.Tab('III', layout = [[tab[2]]])
    left_col = sg.Column([[preview_frame], [cost_frame], [sg.Button('Confirm', key = 'confirm_craft')]], element_justification = 'left')
    right_col = sg.Column(
                [
                    [sg.TabGroup([[anvil_tab_1, anvil_tab_2, anvil_tab_3]])], 
                    [
                        sg.Column(
                        [[
                                sg.Button('Prev'), 
                                sg.Text('1', relief = 'sunken', size = (3, 1), justification = 'center', key = 'current_page'), 
                                sg.Button('Next')
                        ]], pad = ((0, 150), (0, 0))), 
                        sg.Column([[sg.Button('Cancel', key = 'Exit')]])]
                ], element_justification = 'right')
    layout = [[left_col, right_col]]
    window = sg.Window('Crafting Menu', layout, modal = True)
    window.Finalize()
    # Draw canvases
    for i in range(0, 3):
        for j in range(0, 4):
            for k in range(0, 4):
                window['tab{}_item{}'.format(i, 4 * j + k)].draw_image(data = get_crafting_item(tab_titles[i], 4 * j + k, image_paths), location = (0, 72))
    current_selection = [-1, 0]
    # Event loop
    while True:
        event, values = window.read()
        if event in ('Exit', sg.WIN_CLOSED):
            break
        if event == 'confirm_craft' and current_selection[0] != 'None':
            window.close()
            return current_selection
        if 'tab' in event:
            current_selection = [int(event[3]), 16 * (int(window['current_page'].get()) - 1) + int(event[9:])]
            window['preview_frame'].update(value = craftables[tab_titles[current_selection[0]]][current_selection[1]]['name'])
            window['preview_image'].update(data = get_crafting_item(tab_titles[int(event[3])], 16 * (int(window['current_page'].get()) - 1) + int(event[9:]), image_paths))
            for i in range(0, 2):
                for j in range(0, 2):
                    window['ingredient{}'.format(2 * i + j)].update(data = get_crafting_ingredient(tab_titles[current_selection[0]], current_selection[1], 2 * i + j, image_paths))
                    if 2 * i + j > len(craftables[tab_titles[current_selection[0]]][current_selection[1]]['ingredients']) - 1:
                        window['ingredient{}'.format(2 * i + j)].set_tooltip(None)
                        window['ingredient{}cost'.format(2 * i + j)].update('0')
                    else:
                        window['ingredient{}'.format(2 * i + j)].set_tooltip(craftables[tab_titles[current_selection[0]]][current_selection[1]]['ingredients'][2 * i + j]['name'])
                        window['ingredient{}cost'.format(2 * i + j)].update(craftables[tab_titles[current_selection[0]]][current_selection[1]]['ingredients'][2 * i + j]['count'])              
        if event == 'Next' and int(window['current_page'].get()) < 6 or event =='Prev' and int(window['current_page'].get()) > 1:
            if event == 'Next':
                window['current_page'].update(int(window['current_page'].get()) + 1)
            else:
                window['current_page'].update(int(window['current_page'].get()) - 1)
            for i in range(0, 3):
                for j in range(0, 4):
                    for k in range(0, 4):
                        window['tab{}_item{}'.format(i, 4 * j + k)].draw_image(data = get_crafting_item(tab_titles[i], 16 * (int(window['current_page'].get()) - 1) + 4 * j + k, image_paths), location = (0, 72))
    window.close()
    return 'None'


# General Variables from here on

# Dictionary for JSON from Idleon API Downloader
json_file = open("data/idleon_data.json", "rt")
json_text = json_file.read()
dictionary = json.loads(json_text)

# Dictionary for crafting recepies
json_file = open("data/crafting_data.json", "rt")
json_text = json_file.read()
craftables = json.loads(json_text)
tab_titles = ['Beginner Tier', 'Novice Tier', 'Apprentice Tier', 'Adept Tier']

# All image paths
image_paths = [ 'Materials', 'Statues', 'Food', 'Tools', \
                'Equipment', 'Pouches', 'Inventory', 'Stamps', \
                'Storage', 'Consumables', 'Upgrades', 'Misc Items',
                'Quest Items', 'Event']

# Dictionary for talent images
talents =   {
                'Mage':{'Shaman':{}, 'Wizard':{}}, 
                'Warrior':{'Barbarian':{}, 'Squire':{}}, 
                'Archer':{'Bowman':{}, 'Hunter':{}},
                'Journeyman':{}
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