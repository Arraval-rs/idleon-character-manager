import os
import io
import json
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
    return '()'



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

# Dictionary for JSON from Idleon API Downloader
json_file = open("data/idleon_data.json", "rt")
json_text = json_file.read()
dictionary = json.loads(json_text)

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

# General Variables
character_class = dictionary['characters'][0]['class']
character_base_class = get_base_class(character_class)
character_list = []
i = 0
while i < len(dictionary['characters']):
    character_list.append('{name} Lv. {level} {class_name}'.format(\
        name = dictionary['characters'][i]['name'], \
        level = dictionary['characters'][i]['level'], \
        class_name = dictionary['characters'][i]['class']))
    i = i + 1

skill_names =   [
                    'Mining', 'Smithing', 'Chopping', 
                    'Fishing', 'Alchemy', 'Catching', 
                    'Trapping', 'Construction', 'Worship'
                ]