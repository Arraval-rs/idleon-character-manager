import io
import os
import json
import PySimpleGUI as sg
from PIL import Image, ImageDraw

# Functions
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

def get_character_stats(character):
    stat_str = 'Max HP: {}\n'.format(max_hp(character))
    stat_str += 'Max MP: {}\n'.format(max_mp(character))
    stat_str += 'Damage: {}\n'.format(damage(character))
    stat_str += 'STR: {}\n'.format(dictionary['characters'][character]['strength'])
    stat_str += 'AGI: {}\n'.format(dictionary['characters'][character]['agility'])
    stat_str += 'WIS: {}\n'.format(dictionary['characters'][character]['wisdom'])
    stat_str += 'LUK: {}\n'.format(dictionary['characters'][character]['luck'])
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
        stat_str += '\t\tReach: {}'.format(dictionary['characters'][character][equip_type][index]['stoneData']['Reach'] if 'Reach' in dictionary['characters'][character][equip_type][index]['stoneData'] else 'N/A')
        stat_str += '\nAGI: {}'.format(dictionary['characters'][character][equip_type][index]['stoneData']['AGI'])
        stat_str += '\t\tDefence: {}'.format(dictionary['characters'][character][equip_type][index]['stoneData']['Defence'] if 'Defence' in dictionary['characters'][character][equip_type][index]['stoneData'] else 'N/A')
        stat_str += '\nWIS: {}'.format(dictionary['characters'][character][equip_type][index]['stoneData']['WIS'])
        stat_str += '\t\tWeapon Power: {}'.format(dictionary['characters'][character][equip_type][index]['stoneData']['Weapon_Power'] if 'Weapon Power' in dictionary['characters'][character][equip_type][index]['stoneData'] else 'N/A')
        stat_str += '\nLUK: {}'.format(dictionary['characters'][character][equip_type][index]['stoneData']['LUK'])
        stat_str += '\t\tUpgrade Slots Left: {}'.format(dictionary['characters'][character][equip_type][index]['stoneData']['Upgrade_Slots_Left'] if equip_type == 'equipment' else 0)
    else:
        stat_str = 'Stack Size: {}'.format(dictionary['characters'][character][equip_type][index]['count'])
    return stat_str

def update_selected_equipment(equip_type, character, item):
    window['selected_equipment'].update(data = generate_img('images/{}/{}.png'.format(equip_type, dictionary['characters'][index][equip_type][item]['name']), (72, 72), True))
    window['item_stats'].update(get_item_stats(equip_type, character, item))
    window['item_frame'].update(value = dictionary['characters'][character][equip_type][item]['name'])
    return


# Dictionary for JSON from Idleon API Downloader
json_file = open("idleon_data.json", "rt")
json_text = json_file.read()
dictionary = json.loads(json_text)

# Variables
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

# Dictionary for talent images
talents =   {
                'Mage':{'Shaman':{}, 'Wizard':{}}, 
                'Warrior':{'Barbarian':{}, 'Squire':{}}, 
                'Archer':{'Bowman':{}, 'Hunter':{}},
                'Journeyman':{}
            }
talents['Filler'] = generate_img('images/Filler.png', (56, 56), False)
for i in range(0, 10):
    talents[str(i)] = generate_img('images/Talents/{}.png'.format(i), (56, 56), False)
for i in range(10, 30):
    talents['Mage'][str(i)] = generate_img('images/Talents/Mage/{}.png'.format(i), (56, 56), False)
    talents['Warrior'][str(i)] = generate_img('images/Talents/Warrior/{}.png'.format(i), (56, 56), False)
    talents['Archer'][str(i)] = generate_img('images/Talents/Archer/{}.png'.format(i), (56, 56), False)
    talents['Journeyman'][str(i)] = generate_img('images/Talents/Journeyman/{}.png'.format(i), (56, 56), False)
for i in range(30, 45):
    talents['Mage']['Shaman'][str(i)] = generate_img('images/Talents/Mage/Shaman/{}.png'.format(i), (56, 56), False)
    talents['Mage']['Wizard'][str(i)] = generate_img('images/Talents/Mage/Wizard/{}.png'.format(i), (56, 56), False)
    talents['Warrior']['Barbarian'][str(i)] = generate_img('images/Talents/Warrior/Barbarian/{}.png'.format(i), (56, 56), False)
    talents['Warrior']['Squire'][str(i)] = generate_img('images/Talents/Warrior/Squire/{}.png'.format(i), (56, 56), False)
    talents['Archer']['Bowman'][str(i)] = generate_img('images/Talents/Archer/Bowman/{}.png'.format(i), (56, 56), False)
    talents['Archer']['Hunter'][str(i)] = generate_img('images/Talents/Archer/Hunter/{}.png'.format(i), (56, 56), False)

# tabs
talents_1 =         [[sg.Column(
                    [
                        [sg.Image(data = talents[str(5 * i + j)], key = 'talent_img{}'.format(str(5 * i + j))) for j in range(0, 5)],
                        [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels'][str(5 * i + j)] if str(5 * i + j) in dictionary['characters'][0]['talentLevels'] else '0'), key = 'talent{}'.format(str(5 * i + j)), size = (7,1), justification = 'center', relief = 'sunken') for j in range(0, 5)],
                    ], element_justification = 'center')]for i in range(0, 2)]
(talents_1.append([sg.Column(
                    [
                        [sg.Image(data = talents['Filler'] if character_base_class == 'Beginner' else talents[character_base_class][str(10 + i)], key = 'talent_img{}'.format(str(10 + i))) for i in range(0, 5)],
                        [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels'][str(10 + i)] if str(10 + i) in dictionary['characters'][0]['talentLevels'] and character_base_class != 'Beginner' else '0'), key = 'talent{}'.format(str(10 + i)), size = (7,1), justification = 'center', relief = 'sunken') for i in range(0, 5)]
                    ], element_justification = 'center')]))

talents_2 =         [[sg.Column(
                    [
                        [sg.Image(data = talents['Filler'] if character_base_class == 'Beginner' else talents[character_base_class][str(15 + 5 * i + j)], key = 'talent_img{}'.format(str(15 + 5 * i + j))) for j in range(0, 5)],
                        [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels'][str(15 + 5 * i + j)] if str(15 + 5 * i + j) in dictionary['characters'][0]['talentLevels'] and character_base_class != 'Beginner' else '0'), key = 'talent{}'.format(str(15 + 5 * i + j)), size = (7,1), justification = 'center', relief = 'sunken') for j in range(0, 5)]
                    ], element_justification = 'center')]for i in range(0, 3)]

talents_3 =         [[sg.Column(
                    [
                        [sg.Image(data = talents['Filler'] if is_base_class(character_class) else talents[character_base_class][character_class][str(30 + 5 * i + j)], key = 'talent_img{}'.format(str(30 + 5 * i + j))) for j in range(0, 5)],
                        [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels'][str(30 + 5 * i + j)] if str(30 + 5 * i + j) in dictionary['characters'][0]['talentLevels'] and character_base_class != 'Beginner' else '0'), key = 'talent{}'.format(str(30 + 5 * i + j)), size = (7,1), justification = 'center', relief = 'sunken') for j in range(0, 5)]
                    ], element_justification = 'center')]for i in range(0, 3)]


star_talents =      [
                        [sg.Text('Star Talents')]
                    ]


skill_names =   [
                    'Mining', 'Smithing', 'Chopping', 
                    'Fishing', 'Alchemy', 'Catching', 
                    'Trapping', 'Construction', 'Worship'
                ]
skills_tab =        [
                        [sg.Column([[sg.Image(data = generate_img('images/Skills/{}.png'.format(skill_names[3*j+i]), (38, 36), False)), sg.Text('{}\nLv. {}'.format(skill_names[3*j+i], dictionary['characters'][0]['skillLevels'][skill_names[3*j+i].lower()]), key = '{}level'.format(skill_names[3*j+i]), size = (9, 2), relief = 'sunken')] for i in range(0, 3)])for j in range(0, 3)]
                    ]


talents_tab =       [
                        [sg.TabGroup(
                        [[
                            sg.Tab('Talents 1', talents_1),
                            sg.Tab('Talents 2', talents_2),
                            sg.Tab('Talents 3', talents_3),
                            sg.Tab('Star Talents', star_talents),
                        ]])]
                    ]


bags_tab =          [
                        [sg.Text('Paper not plastic')]
                    ]


pouches_tab =       [
                        [sg.Text('Pouches!')]
                    ]

equips_tab =        [
                        [sg.Graph((72, 72), (0, 0), (72, 72), change_submits = True, key = 'equipment{}'.format(2*i+j)) for j in range(0, 2)] for i in range(0, 4)
                    ]


tools_tab =         [
                        [sg.Graph((72, 72), (0, 0), (72, 72), change_submits = True, key = 'tools{}'.format(2*i+j)) for j in range(0, 2)] for i in range(0, 4)
                    ]


foods_tab =         [
                        [sg.Graph((72, 72), (0, 0), (72, 72), change_submits = True, key = 'food{}'.format(2*i+j)) for j in range(0, 2)] for i in range(0, 4)
                    ]


character_tab =    [
                        [
                            sg.Column(
                            [[
                                sg.Column(
                                [[
                                    sg.Column(
                                    [
                                        [sg.Column([[sg.Image(data = generate_img('images/Classes/{}.png'.format(dictionary['characters'][0]['class']), (129, 110), False), key = 'class_image')]], element_justification = 'center')],
                                        [sg.Text(get_character_stats(0), key = 'character_stats')]
                                    ]),sg
                                        .TabGroup(
                                        [[
                                            sg.Tab('Skills', skills_tab),
                                            sg.Tab('Talents', talents_tab),
                                            sg.Tab('Bags', bags_tab),
                                            sg.Tab('Pouches', pouches_tab)
                                        ]])
                                ]]),
                                sg.Column(
                                [[
                                    sg.TabGroup(
                                    [[
                                        sg.Tab('Equips', equips_tab),
                                        sg.Tab('Tools', tools_tab),
                                        sg.Tab('Food', foods_tab)
                                    ]])
                                ]])
                            ],
                            [
                                sg.Frame(layout = 
                                [[
                                    sg.Image(data = generate_img('images/Empty Slot.png', (72, 72), False), key = 'selected_equipment'),
                                    sg.Text('STR: 0\t\tReach: 0\nAGI: 0\t\tDefence: 0\nWIS: 0\t\tWeapon Power: 0\nLUK: 0\t\tUpgrade Slots Left: 0', key = 'item_stats')
                                ]], title = 'None', key = 'item_frame')
                            ]])
                        ]
                    ]


inventory_tab =     [
                        []
                    ]


monsters_tab =      [
                        []
                    ]


crafting_tab =      [
                        []
                    ]


storage_tab =       [
                        []
                    ]


root_tabs = [
                [
                    sg.Combo(
                        character_list,
                        default_value = character_list[0],
                        key = 'active_character',
                        enable_events = True
                    ),
                    sg.Image(data = generate_img('images/Classes/{}Icon.png'.format(dictionary['characters'][0]['class']), (38, 36), False), key = 'class_icon')
                ],
                [
                sg.TabGroup(
                [[
                    sg.Tab('Character', character_tab),
                    sg.Tab('Inventory', inventory_tab),
                    sg.Tab('Monsters', monsters_tab),
                    sg.Tab('Crafting', crafting_tab),
                    sg.Tab('Storage', storage_tab)
                ]])
                ]
            ]

window = sg.Window("Idleon Character Manager", root_tabs)
window.Finalize()

# Draw graphs for equipment tabs
for i in range(0, 4):
    for j in range(0, 2):
        equips_tab[i][j].draw_image(data = generate_img('images/Equipment/{}.png'.format(dictionary['characters'][0]['equipment'][2*i+j]['name']), (72, 72), True), location = (0, 72))
        tools_tab[i][j].draw_image(data = generate_img('images/Tools/{}.png'.format(dictionary['characters'][0]['tools'][2*i+j]['name']), (72, 72), True), location = (0, 72))
        foods_tab[i][j].draw_image(data = generate_img('images/Food/{}.png'.format(dictionary['characters'][0]['food'][2*i+j]['name']), (72, 72), True), location = (0, 72))


# Event loop
while True:
    event, values = window.read()
    if event != "Exit" and event != sg.WIN_CLOSED:
        index = character_list.index(values['active_character'])
    else:
        break
    if event == 'active_character':
        character_class = dictionary['characters'][index]['class']
        character_base_class = get_base_class(character_class)

        # Update standalone elements
        window['class_icon'].update(data = generate_img('images/Classes/{}Icon.png'.format(dictionary['characters'][index]['class']), (38, 36), False))
        window['class_image'].update(data = generate_img('images/Classes/{}.png'.format(dictionary['characters'][index]['class']), (129, 110), False))
        window['character_stats'].update(get_character_stats(index))
        window['selected_equipment'].update(data = generate_img('images/Empty Slot.png', (72, 72), False))
        window['item_stats'].update('STR: 0\t\tReach: 0\nAGI: 0\t\tDefence: 0\nWIS: 0\t\tWeapon Power: 0\nLUK: 0\t\tUpgrade Slots Left: 0')
        window['item_frame'].update(value = 'None')
        # Update equipment
        for i in range(0, 4):
            for j in range(0, 2):
                equips_tab[i][j].draw_image(data = generate_img('images/Equipment/{}.png'.format(dictionary['characters'][index]['equipment'][2*i+j]['name']), (72, 72), True), location = (0, 72))
                tools_tab[i][j].draw_image(data = generate_img('images/Tools/{}.png'.format(dictionary['characters'][index]['tools'][2*i+j]['name']), (72, 72), True), location = (0, 72))
                foods_tab[i][j].draw_image(data = generate_img('images/Food/{}.png'.format(dictionary['characters'][index]['food'][2*i+j]['name']), (72, 72), True), location = (0, 72))
    
        # Update skills
        for i in range(0, 9):
            window['{}level'.format(skill_names[i])].update('{}\nLv. {}'.format(skill_names[i], dictionary['characters'][index]['skillLevels'][skill_names[i].lower()]))

        # Update talents tab 1
        for i in range(0, 10):
            if str(i) in dictionary['characters'][index]['talentLevels'].keys() and character_base_class != 'Beginner': # some talents aren't in JSON
                window['talent{}'.format(i)].update('{}/100'.format(dictionary['characters'][index]['talentLevels'][str(i)]))
            else:
                window['talent{}'.format(i)].update('0/100')
        
        # Update talents tab 2
        for i in range(10, 30):
            window['talent_img{}'.format(i)].update(data = talents['Filler'] if character_base_class == 'Beginner' else talents[character_base_class][str(i)])
            if str(i) in dictionary['characters'][index]['talentLevels'].keys()  and character_base_class != 'Beginner': # some talents aren't in JSON
                window['talent{}'.format(i)].update('{}/100'.format(dictionary['characters'][index]['talentLevels'][str(i)]))
            else:
                window['talent{}'.format(i)].update('0/100')
        
        # Update talents tab 3
        for i in range(30, 45):
            window['talent_img{}'.format(i)].update(data = talents['Filler'] if is_base_class(character_class) else talents[character_base_class][character_class][str(i)])
            if str(i) in dictionary['characters'][index]['talentLevels'].keys() and not is_base_class(character_class): # some talents aren't in JSON
                window['talent{}'.format(i)].update('{}/100'.format(dictionary['characters'][index]['talentLevels'][str(i)]))
            else:
                window['talent{}'.format(i)].update('0/100')
    if 'equipment' in event or 'tools' in event or 'food' in event:
        update_selected_equipment(event[:len(event)-1], index, int(event[len(event)-1]))
window.close()       