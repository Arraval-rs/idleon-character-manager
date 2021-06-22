import io
import os
import json
import PySimpleGUI as sg
from PIL import Image

# Functions
def generate_img(f):
    img = Image.open(f)
    img.thumbnail((72, 72))
    bio = io.BytesIO()
    img.save(bio, format = "PNG")
    return bio

# Dictionary
json_file = open("idleon_data.json", "rt")
json_text = json_file.read()
dictionary = json.loads(json_text)

# Variables
character_class = dictionary['characters'][0]['class']
if character_class == 'Wizard' or character_class == 'Shaman':
    character_base_class = 'Mage'
elif character_class == 'Bowman' or character_class == 'Hunter':
    character_base_class = 'Archer'
elif character_class == 'Barbarian' or character_class == 'Squire':
    character_base_class = 'Warrior'
elif character_class == 'Journeyman':
    character_base_class = character_class
character_list = []
i = 0
while i < len(dictionary['characters']):
    character_list.append('{name} Lv. {level} {class_name}'.format(\
        name = dictionary['characters'][i]['name'], \
        level = dictionary['characters'][i]['level'], \
        class_name = dictionary['characters'][i]['class']))
    i = i + 1

# Default Images
helmet_img = generate_img('images/Helmets/{}.png'.format(dictionary['characters'][0]['equipment'][0]['name']))
weapon_img = generate_img('images/Weapons/{}.png'.format(dictionary['characters'][0]['equipment'][1]['name']))
shirt_img = generate_img('images/Shirts/{}.png'.format(dictionary['characters'][0]['equipment'][2]['name']))
pendant_img = generate_img('images/Pendants/{}.png'.format(dictionary['characters'][0]['equipment'][3]['name']))
pant_img = generate_img('images/Pants/{}.png'.format(dictionary['characters'][0]['equipment'][4]['name']))
ring1_img = generate_img('images/Rings/{}.png'.format(dictionary['characters'][0]['equipment'][5]['name']))
shoe_img = generate_img('images/Shoes/{}.png'.format(dictionary['characters'][0]['equipment'][6]['name']))
ring2_img = generate_img('images/Rings/{}.png'.format(dictionary['characters'][0]['equipment'][7]['name']))

talent_0_img = generate_img('images/Talents/0.png')
talent_1_img = generate_img('images/Talents/1.png')
talent_2_img = generate_img('images/Talents/2.png')
talent_3_img = generate_img('images/Talents/3.png')
talent_4_img = generate_img('images/Talents/4.png')
talent_5_img = generate_img('images/Talents/5.png')
talent_6_img = generate_img('images/Talents/6.png')
talent_7_img = generate_img('images/Talents/7.png')
talent_8_img = generate_img('images/Talents/8.png')
talent_9_img = generate_img('images/Talents/9.png')
talent_10_img = generate_img('images/Talents/{}/10.png'.format(character_base_class))
talent_11_img = generate_img('images/Talents/{}/11.png'.format(character_base_class))
talent_12_img = generate_img('images/Talents/{}/12.png'.format(character_base_class))
talent_13_img = generate_img('images/Talents/{}/13.png'.format(character_base_class))
talent_14_img = generate_img('images/Talents/{}/14.png'.format(character_base_class))

# tabs
talents_1 =         [[
                        sg.Column(
                        [
                            [sg.Image(data = talent_0_img.getvalue())],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['0']), key = 'talent0', size = (7,1), justification = 'center')],
                            [sg.Image(data = talent_5_img.getvalue())],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['5']), key = 'talent5', size = (7,1), justification = 'center')],
                            [sg.Image(data = talent_10_img.getvalue(), key = 'talent_img10')],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['10']), key = 'talent10', size = (7,1), justification = 'center')]
                        ], element_justification = 'center'),
                        sg.Column(
                        [
                            [sg.Image(data = talent_1_img.getvalue())],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['1']), key = 'talent1', size = (7,1), justification = 'center')],
                            [sg.Image(data = talent_6_img.getvalue())],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['6']), key = 'talent6', size = (7,1), justification = 'center')],
                            [sg.Image(data = talent_11_img.getvalue(), key = 'talent_img11')],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['11']), key = 'talent11', size = (7,1), justification = 'center')]
                        ], element_justification = 'center'),
                        sg.Column(
                        [
                            [sg.Image(data = talent_2_img.getvalue())],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['2']), key = 'talent2', size = (7,1), justification = 'center')],
                            [sg.Image(data = talent_7_img.getvalue())],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['7']), key = 'talent7', size = (7,1), justification = 'center')],
                            [sg.Image(data = talent_12_img.getvalue(), key = 'talent_img12')],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['12']), key = 'talent12', size = (7,1), justification = 'center')]
                        ], element_justification = 'center'),
                        sg.Column(
                        [
                            [sg.Image(data = talent_3_img.getvalue())],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['3']), key = 'talent3', size = (7,1), justification = 'center')],
                            [sg.Image(data = talent_8_img.getvalue())],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['8']), key = 'talent8', size = (7,1), justification = 'center')],
                            [sg.Image(data = talent_13_img.getvalue(), key = 'talent_img13')],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['13']), key = 'talent13', size = (7,1), justification = 'center')]
                        ], element_justification = 'center'),
                        sg.Column(
                        [
                            [sg.Image(data = talent_4_img.getvalue())],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['4']), key = 'talent4', size = (7,1), justification = 'center')],
                            [sg.Image(data = talent_9_img.getvalue())],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['9']), key = 'talent9', size = (7,1), justification = 'center')],
                            [sg.Image(data = talent_14_img.getvalue(), key = 'talent_img14')],
                            [sg.Text('{}/100'.format(dictionary['characters'][0]['talentLevels']['14']), key = 'talent14', size = (7,1), justification = 'center')]
                        ], element_justification = 'center'),
                    ]]

talents_2 =         [
                        [sg.Text('Class Talents')]
                    ]

talents_3 =         [
                        [sg.Text('Subclass Talents')]
                    ]

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
        if character_class == 'Wizard' or character_class == 'Shaman':
            character_base_class = 'Mage'
        elif character_class == 'Bowman' or character_class == 'Hunter':
            character_base_class = 'Archer'
        elif character_class == 'Barbarian' or character_class == 'Squire':
            character_base_class = 'Warrior'
        elif character_class == 'Journeyman':
            character_base_class = character_class
        # Generate new images
        helmet_img = generate_img('images/Helmets/{}.png'.format(dictionary['characters'][index]['equipment'][0]['name']))
        weapon_img = generate_img('images/Weapons/{}.png'.format(dictionary['characters'][index]['equipment'][1]['name']))
        shirt_img = generate_img('images/Shirts/{}.png'.format(dictionary['characters'][index]['equipment'][2]['name']))
        pendant_img = generate_img('images/Pendants/{}.png'.format(dictionary['characters'][index]['equipment'][3]['name']))
        pant_img = generate_img('images/Pants/{}.png'.format(dictionary['characters'][index]['equipment'][4]['name']))
        ring1_img = generate_img('images/Rings/{}.png'.format(dictionary['characters'][index]['equipment'][5]['name']))
        shoe_img = generate_img('images/Shoes/{}.png'.format(dictionary['characters'][index]['equipment'][6]['name']))
        ring2_img = generate_img('images/Rings/{}.png'.format(dictionary['characters'][index]['equipment'][7]['name']))
        
        talent_10_img = generate_img('images/Talents/{}/10.png'.format(character_base_class))
        talent_11_img = generate_img('images/Talents/{}/11.png'.format(character_base_class))
        talent_12_img = generate_img('images/Talents/{}/12.png'.format(character_base_class))
        talent_13_img = generate_img('images/Talents/{}/13.png'.format(character_base_class))
        talent_14_img = generate_img('images/Talents/{}/14.png'.format(character_base_class))

        # Update character tab
        window['helmet'].update(data = helmet_img.getvalue())
        window['weapon'].update(data = weapon_img.getvalue())
        window['shirt'].update(data = shirt_img.getvalue())
        window['pendant'].update(data = pendant_img.getvalue())
        window['pant'].update(data = pant_img.getvalue())
        window['ring1'].update(data = ring1_img.getvalue())
        window['shoe'].update(data = shoe_img.getvalue())
        window['ring2'].update(data = ring2_img.getvalue())

        window['talent_img10'].update(data = talent_10_img.getvalue())
        window['talent_img11'].update(data = talent_11_img.getvalue())
        window['talent_img12'].update(data = talent_12_img.getvalue())
        window['talent_img13'].update(data = talent_13_img.getvalue())
        window['talent_img14'].update(data = talent_14_img.getvalue())
        i = 0
        while i <= 14:
            if str(i) in dictionary['characters'][index]['talentLevels'].keys(): # some talents aren't in JSON
                window['talent{}'.format(i)].update('{}/100'.format(dictionary['characters'][index]['talentLevels'][str(i)]))
            else:
                window['talent{}'.format(i)].update('?/100')
            i = i + 1 

window.close()       