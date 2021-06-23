import io
import os
import json
import PySimpleGUI as sg
from PIL import Image

# Functions
def generate_img(f): # returns the bytes object for a given image file
    img = Image.open(f)
    img.thumbnail((72, 72))
    bio = io.BytesIO()
    img.save(bio, format = "PNG")
    return bio

def get_base_class(c): # returns the base class of a given class
    if c == 'Wizard' or c == 'Shaman':
        return 'Mage'
    elif c == 'Bowman' or c == 'Hunter':
        return 'Archer'
    elif c == 'Barbarian' or c == 'Squire':
        return 'Warrior'
    return c

def is_base_class(c): # returns true if the given class is a base class (Beginner, Warrior, Mage, Archer, Journeyman)
    if c in ('Beginner', 'Warrior', 'Mage', 'Archer', 'Journeyman'):
        return True
    return False

# Dictionary
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

# Dictionary
talents =   {
                'Mage':{'Shaman':{}, 'Wizard':{}}, 
                'Warrior':{'Barbarian':{}, 'Squire':{}}, 
                'Archer':{'Bowman':{}, 'Hunter':{}},
                'Journeyman':{}
            }
talents['Filler'] = generate_img('images/Filler.png')
for i in range(0, 10):
    talents[str(i)] = generate_img('images/Talents/{}.png'.format(i))
for i in range(10, 30):
    talents['Mage'][str(i)] = generate_img('images/Talents/Mage/{}.png'.format(i))
    talents['Warrior'][str(i)] = generate_img('images/Talents/Warrior/{}.png'.format(i))
    talents['Archer'][str(i)] = generate_img('images/Talents/Archer/{}.png'.format(i))
    talents['Journeyman'][str(i)] = generate_img('images/Talents/Journeyman/{}.png'.format(i))
for i in range(30, 45):
    talents['Mage']['Shaman'][str(i)] = generate_img('images/Talents/Mage/Shaman/{}.png'.format(i))
    #talents['Mage']['Wizard'][str(i)] = generate_img('images/Talents/Mage/Wizard/{}.png'.format(i))
    talents['Warrior']['Barbarian'][str(i)] = generate_img('images/Talents/Warrior/Barbarian/{}.png'.format(i))
    #talents['Warrior']['Squire'][str(i)] = generate_img('images/Talents/Warrior/Squire/{}.png'.format(i))
    #talents['Archer']['Bowman'][str(i)] = generate_img('images/Talents/Archer/Bowman/{}.png'.format(i))
    #talents['Archer']['Hunter'][str(i)] = generate_img('images/Talents/Archer/Hunter/{}.png'.format(i))

# Default Images
helmet_img = generate_img('images/Helmets/{}.png'.format(dictionary['characters'][0]['equipment'][0]['name']))
weapon_img = generate_img('images/Weapons/{}.png'.format(dictionary['characters'][0]['equipment'][1]['name']))
shirt_img = generate_img('images/Shirts/{}.png'.format(dictionary['characters'][0]['equipment'][2]['name']))
pendant_img = generate_img('images/Pendants/{}.png'.format(dictionary['characters'][0]['equipment'][3]['name']))
pant_img = generate_img('images/Pants/{}.png'.format(dictionary['characters'][0]['equipment'][4]['name']))
ring1_img = generate_img('images/Rings/{}.png'.format(dictionary['characters'][0]['equipment'][5]['name']))
shoe_img = generate_img('images/Shoes/{}.png'.format(dictionary['characters'][0]['equipment'][6]['name']))
ring2_img = generate_img('images/Rings/{}.png'.format(dictionary['characters'][0]['equipment'][7]['name']))

# tabs
talents_1 =         [[
                        sg.Column(
                        [
                            [sg.Image(data = talents['0'].getvalue())],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['0']), key = 'talent0', size = (7,1), justification = 'center')],
                            [sg.Image(data = talents['5'].getvalue())],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['5']), key = 'talent5', size = (7,1), justification = 'center')],
                            [sg.Image(data = talents['Filler'].getvalue() if character_base_class == 'Beginner' else talents[character_base_class]['10'].getvalue(), key = 'talent_img10')],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['10']), key = 'talent10', size = (7,1), justification = 'center')]
                        ], element_justification = 'center'),
                        sg.Column(
                        [
                            [sg.Image(data = talents['1'].getvalue())],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['1']), key = 'talent1', size = (7,1), justification = 'center')],
                            [sg.Image(data = talents['6'].getvalue())],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['6']), key = 'talent6', size = (7,1), justification = 'center')],
                            [sg.Image(data = talents['Filler'].getvalue() if character_base_class == 'Beginner' else talents[character_base_class]['11'].getvalue(), key = 'talent_img11')],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['11']), key = 'talent11', size = (7,1), justification = 'center')]
                        ], element_justification = 'center'),
                        sg.Column(
                        [
                            [sg.Image(data = talents['2'].getvalue())],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['2']), key = 'talent2', size = (7,1), justification = 'center')],
                            [sg.Image(data = talents['7'].getvalue())],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['7']), key = 'talent7', size = (7,1), justification = 'center')],
                            [sg.Image(data = talents['Filler'].getvalue() if character_base_class == 'Beginner' else talents[character_base_class]['12'].getvalue(), key = 'talent_img12')],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['12']), key = 'talent12', size = (7,1), justification = 'center')]
                        ], element_justification = 'center'),
                        sg.Column(
                        [
                            [sg.Image(data = talents['3'].getvalue())],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['3']), key = 'talent3', size = (7,1), justification = 'center')],
                            [sg.Image(data = talents['8'].getvalue())],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['8']), key = 'talent8', size = (7,1), justification = 'center')],
                            [sg.Image(data = talents['Filler'].getvalue() if character_base_class == 'Beginner' else talents[character_base_class]['13'].getvalue(), key = 'talent_img13')],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['13']), key = 'talent13', size = (7,1), justification = 'center')]
                        ], element_justification = 'center'),
                        sg.Column(
                        [
                            [sg.Image(data = talents['4'].getvalue())],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['4']), key = 'talent4', size = (7,1), justification = 'center')],
                            [sg.Image(data = talents['9'].getvalue())],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['9']), key = 'talent9', size = (7,1), justification = 'center')],
                            [sg.Image(data = talents['Filler'].getvalue() if character_base_class == 'Beginner' else talents[character_base_class]['14'].getvalue(), key = 'talent_img14')],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['14']), key = 'talent14', size = (7,1), justification = 'center')]
                        ], element_justification = 'center')
                    ]]


talents_2 =         [[
                        sg.Column(
                        [
                            [sg.Image(data = talents['Filler'].getvalue() if character_base_class == 'Beginner' else talents[character_base_class]['15'].getvalue(), key = 'talent_img15')],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['15']), key = 'talent15', size = (7,1), justification = 'center')],
                            [sg.Image(data = talents['Filler'].getvalue() if character_base_class == 'Beginner' else talents[character_base_class]['20'].getvalue(), key = 'talent_img20')],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['20']), key = 'talent20', size = (7,1), justification = 'center')],
                            [sg.Image(data = talents['Filler'].getvalue() if character_base_class == 'Beginner' else talents[character_base_class]['25'].getvalue(), key = 'talent_img25')],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['25']), key = 'talent25', size = (7,1), justification = 'center')]
                        ], element_justification = 'center'),
                        sg.Column(
                        [
                            [sg.Image(data = talents['Filler'].getvalue() if character_base_class == 'Beginner' else talents[character_base_class]['16'].getvalue(), key = 'talent_img16')],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['16']), key = 'talent16', size = (7,1), justification = 'center')],
                            [sg.Image(data = talents['Filler'].getvalue() if character_base_class == 'Beginner' else talents[character_base_class]['21'].getvalue(), key = 'talent_img21')],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['21']), key = 'talent21', size = (7,1), justification = 'center')],
                            [sg.Image(data = talents['Filler'].getvalue() if character_base_class == 'Beginner' else talents[character_base_class]['26'].getvalue(), key = 'talent_img26')],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['26']), key = 'talent26', size = (7,1), justification = 'center')]
                        ], element_justification = 'center'),
                        sg.Column(
                        [
                            [sg.Image(data = talents['Filler'].getvalue() if character_base_class == 'Beginner' else talents[character_base_class]['17'].getvalue(), key = 'talent_img17')],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['17']), key = 'talent17', size = (7,1), justification = 'center')],
                            [sg.Image(data = talents['Filler'].getvalue() if character_base_class == 'Beginner' else talents[character_base_class]['22'].getvalue(), key = 'talent_img22')],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['22']), key = 'talent22', size = (7,1), justification = 'center')],
                            [sg.Image(data = talents['Filler'].getvalue() if character_base_class == 'Beginner' else talents[character_base_class]['27'].getvalue(), key = 'talent_img27')],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['27']), key = 'talent27', size = (7,1), justification = 'center')]
                        ], element_justification = 'center'),
                        sg.Column(
                        [
                            [sg.Image(data = talents['Filler'].getvalue() if character_base_class == 'Beginner' else talents[character_base_class]['18'].getvalue(), key = 'talent_img18')],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['18']), key = 'talent18', size = (7,1), justification = 'center')],
                            [sg.Image(data = talents['Filler'].getvalue() if character_base_class == 'Beginner' else talents[character_base_class]['23'].getvalue(), key = 'talent_img23')],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['0']), key = 'talent23', size = (7,1), justification = 'center')], # MISSING FROM JSON
                            [sg.Image(data = talents['Filler'].getvalue() if character_base_class == 'Beginner' else talents[character_base_class]['28'].getvalue(), key = 'talent_img28')],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['28']), key = 'talent28', size = (7,1), justification = 'center')]
                        ], element_justification = 'center'),
                        sg.Column(
                        [
                            [sg.Image(data = talents['Filler'].getvalue() if character_base_class == 'Beginner' else talents[character_base_class]['19'].getvalue(), key = 'talent_img19')],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['19']), key = 'talent19', size = (7,1), justification = 'center')],
                            [sg.Image(data = talents['Filler'].getvalue() if character_base_class == 'Beginner' else talents[character_base_class]['24'].getvalue(), key = 'talent_img24')],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['24']), key = 'talent24', size = (7,1), justification = 'center')],
                            [sg.Image(data = talents['Filler'].getvalue() if character_base_class == 'Beginner' else talents[character_base_class]['29'].getvalue(), key = 'talent_img29')],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['29']), key = 'talent29', size = (7,1), justification = 'center')]
                        ], element_justification = 'center')
                    ]]


talents_3 =         [[
                        sg.Column(
                        [
                            [sg.Image(data = talents['Filler'].getvalue() if is_base_class(character_class) else talents[character_base_class][character_class]['30'].getvalue(), key = 'talent_img30')],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['30']), key = 'talent30', size = (7,1), justification = 'center')],
                            [sg.Image(data = talents['Filler'].getvalue() if is_base_class(character_class) else talents[character_base_class][character_class]['35'].getvalue(), key = 'talent_img35')],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['35']), key = 'talent35', size = (7,1), justification = 'center')],
                            [sg.Image(data = talents['Filler'].getvalue() if is_base_class(character_class) else talents[character_base_class][character_class]['40'].getvalue(), key = 'talent_img40')],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['40']), key = 'talent40', size = (7,1), justification = 'center')]
                        ], element_justification = 'center'),
                        sg.Column(
                        [
                            [sg.Image(data = talents['Filler'].getvalue() if is_base_class(character_class) else talents[character_base_class][character_class]['31'].getvalue(), key = 'talent_img31')],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['31']), key = 'talent31', size = (7,1), justification = 'center')],
                            [sg.Image(data = talents['Filler'].getvalue() if is_base_class(character_class) else talents[character_base_class][character_class]['36'].getvalue(), key = 'talent_img36')],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['0']), key = 'talent36', size = (7,1), justification = 'center')], # MISSING FROM JSON
                            [sg.Image(data = talents['Filler'].getvalue() if is_base_class(character_class) else talents[character_base_class][character_class]['41'].getvalue(), key = 'talent_img41')],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['41']), key = 'talent41', size = (7,1), justification = 'center')]
                        ], element_justification = 'center'),
                        sg.Column(
                        [
                            [sg.Image(data = talents['Filler'].getvalue() if is_base_class(character_class) else talents[character_base_class][character_class]['32'].getvalue(), key = 'talent_img32')],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['32']), key = 'talent32', size = (7,1), justification = 'center')],
                            [sg.Image(data = talents['Filler'].getvalue() if is_base_class(character_class) else talents[character_base_class][character_class]['37'].getvalue(), key = 'talent_img37')],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['0']), key = 'talent37', size = (7,1), justification = 'center')], # MISSING FROM JSON
                            [sg.Image(data = talents['Filler'].getvalue() if is_base_class(character_class) else talents[character_base_class][character_class]['42'].getvalue(), key = 'talent_img42')],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['42']), key = 'talent42', size = (7,1), justification = 'center')]
                        ], element_justification = 'center'),
                        sg.Column(
                        [
                            [sg.Image(data = talents['Filler'].getvalue() if is_base_class(character_class) else talents[character_base_class][character_class]['33'].getvalue(), key = 'talent_img33')],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['0']), key = 'talent33', size = (7,1), justification = 'center')], # MISSING FROM JSON
                            [sg.Image(data = talents['Filler'].getvalue() if is_base_class(character_class) else talents[character_base_class][character_class]['38'].getvalue(), key = 'talent_img38')],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['0']), key = 'talent38', size = (7,1), justification = 'center')], # MISSING FROM JSON
                            [sg.Image(data = talents['Filler'].getvalue() if is_base_class(character_class) else talents[character_base_class][character_class]['43'].getvalue(), key = 'talent_img43')],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['43']), key = 'talent43', size = (7,1), justification = 'center')]
                        ], element_justification = 'center'),
                        sg.Column(
                        [
                            [sg.Image(data = talents['Filler'].getvalue() if is_base_class(character_class) else talents[character_base_class][character_class]['34'].getvalue(), key = 'talent_img34')],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['0']), key = 'talent34', size = (7,1), justification = 'center')], # MISSING FROM JSON
                            [sg.Image(data = talents['Filler'].getvalue() if is_base_class(character_class) else talents[character_base_class][character_class]['39'].getvalue(), key = 'talent_img39')],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['0']), key = 'talent39', size = (7,1), justification = 'center')], # MISSING FROM JSON
                            [sg.Image(data = talents['Filler'].getvalue() if is_base_class(character_class) else talents[character_base_class][character_class]['44'].getvalue(), key = 'talent_img44')],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['44']), key = 'talent44', size = (7,1), justification = 'center')]
                        ], element_justification = 'center')
                    ]]


star_talents =      [
                        [sg.Text('Star Talents')]
                    ]


skills_tab =        [
                        [sg.Text('Skills!')]
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
                        [sg.Image(data = helmet_img.getvalue(), key = 'helmet'), sg.Image(data = weapon_img.getvalue(), key = 'weapon')],
                        [sg.Image(data = shirt_img.getvalue(), key = 'shirt'), sg.Image(data = pendant_img.getvalue(), key = 'pendant')],
                        [sg.Image(data = pant_img.getvalue(), key = 'pant'), sg.Image(data = ring1_img.getvalue(), key = 'ring1')],
                        [sg.Image(data = shoe_img.getvalue(), key = 'shoe'), sg.Image(data = ring2_img.getvalue(), key = 'ring2')]
                    ]


tools_tab =         [
                        [sg.Text("You're a tool")]
                    ]


foods_tab =         [
                        [sg.Text('Food!')]
                    ]


characters_tab =    [
                        [
                            sg.Column(
                            [[
                                sg.Text('Character 1\nLv. X'),
                                sg.Text('Class\nImage'),
                                sg.Text('Class Name'),
                            ],
                            [
                                sg.Text("Blah Blah Stats and Shit"),
                                sg.TabGroup(
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
                    )
                ],
                [
                sg.TabGroup(
                [[
                    sg.Tab('Characters', characters_tab),
                    sg.Tab('Inventory', inventory_tab),
                    sg.Tab('Monsters', monsters_tab),
                    sg.Tab('Crafting', crafting_tab),
                    sg.Tab('Storage', storage_tab)
                ]])
                ]
            ]

window = sg.Window("Idleon Character Manager", root_tabs)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == 'active_character':
        index = character_list.index(values['active_character'])
        character_class = dictionary['characters'][index]['class']
        character_base_class = get_base_class(character_class)

        # Update equipment
        helmet_img = generate_img('images/Helmets/{}.png'.format(dictionary['characters'][index]['equipment'][0]['name']))
        weapon_img = generate_img('images/Weapons/{}.png'.format(dictionary['characters'][index]['equipment'][1]['name']))
        shirt_img = generate_img('images/Shirts/{}.png'.format(dictionary['characters'][index]['equipment'][2]['name']))
        pendant_img = generate_img('images/Pendants/{}.png'.format(dictionary['characters'][index]['equipment'][3]['name']))
        pant_img = generate_img('images/Pants/{}.png'.format(dictionary['characters'][index]['equipment'][4]['name']))
        ring1_img = generate_img('images/Rings/{}.png'.format(dictionary['characters'][index]['equipment'][5]['name']))
        shoe_img = generate_img('images/Shoes/{}.png'.format(dictionary['characters'][index]['equipment'][6]['name']))
        ring2_img = generate_img('images/Rings/{}.png'.format(dictionary['characters'][index]['equipment'][7]['name']))
        window['helmet'].update(data = helmet_img.getvalue())
        window['weapon'].update(data = weapon_img.getvalue())
        window['shirt'].update(data = shirt_img.getvalue())
        window['pendant'].update(data = pendant_img.getvalue())
        window['pant'].update(data = pant_img.getvalue())
        window['ring1'].update(data = ring1_img.getvalue())
        window['shoe'].update(data = shoe_img.getvalue())
        window['ring2'].update(data = ring2_img.getvalue())

        # Update talents
        for i in range(0, 10):
            if str(i) in dictionary['characters'][index]['talentLevels'].keys(): # some talents aren't in JSON
                window['talent{}'.format(i)].update('{}/100'.format(dictionary['characters'][index]['talentLevels'][str(i)]))
            else:
                window['talent{}'.format(i)].update('?/100')
        for i in range(10, 30):
            window['talent_img{}'.format(i)].update(data = talents['Filler'].getvalue() if character_base_class == 'Beginner' else talents[character_base_class][str(i)].getvalue())
            if str(i) in dictionary['characters'][index]['talentLevels'].keys(): # some talents aren't in JSON
                window['talent{}'.format(i)].update('{}/100'.format(dictionary['characters'][index]['talentLevels'][str(i)]))
            else:
                window['talent{}'.format(i)].update('?/100')
        for i in range(30, 45):
            window['talent_img{}'.format(i)].update(data = talents['Filler'].getvalue() if is_base_class(character_class) == 'Beginner' else talents[character_base_class][character_class][str(i)].getvalue())
            if str(i) in dictionary['characters'][index]['talentLevels'].keys(): # some talents aren't in JSON
                window['talent{}'.format(i)].update('{}/100'.format(dictionary['characters'][index]['talentLevels'][str(i)]))
            else:
                window['talent{}'.format(i)].update('?/100')

window.close()       