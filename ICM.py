import io
import os
import json
import PySimpleGUI as sg
from PIL import Image

# Dictionary
json_file = open("idleon_data.json", "rt")
json_text = json_file.read()
dictionary = json.loads(json_text)

# Variables
character_list = []
i = 0
while i < len(dictionary['characters']):
    character_list.append(dictionary['characters'][i]['name'])
    i = i + 1

# Functions
def generate_img(f):
    img = Image.open(f)
    img.thumbnail((72, 72))
    bio = io.BytesIO()
    img.save(bio, format = "PNG")
    return bio

# tabs
skills_tab =        [
                        [sg.Text('Skills!')]
                    ]

talents_tab =       [
                        [sg.Text('Talents!')]
                    ]

bags_tab =          [
                        [sg.Text('Bags!')]
                    ]

pouches_tab =       [
                        [sg.Text('Pouches!')]
                    ]

# default equipment images
helmet_img = generate_img('images/Helmets/{}.png'.format(dictionary['characters'][0]['equipment'][0]['name']))
weapon_img = generate_img('images/Weapons/{}.png'.format(dictionary['characters'][0]['equipment'][1]['name']))
shirt_img = generate_img('images/Shirts/{}.png'.format(dictionary['characters'][0]['equipment'][2]['name']))
pendant_img = generate_img('images/Pendants/{}.png'.format(dictionary['characters'][0]['equipment'][3]['name']))
pant_img = generate_img('images/Pants/{}.png'.format(dictionary['characters'][0]['equipment'][4]['name']))
ring1_img = generate_img('images/Rings/{}.png'.format(dictionary['characters'][0]['equipment'][5]['name']))
shoe_img = generate_img('images/Shoes/{}.png'.format(dictionary['characters'][0]['equipment'][6]['name']))
ring2_img = generate_img('images/Rings/{}.png'.format(dictionary['characters'][0]['equipment'][7]['name']))
equips_tab =        [
                        [sg.Image(data = helmet_img.getvalue(), key = "helmet"), sg.Image(data = weapon_img.getvalue(), key = "weapon")],
                        [sg.Image(data = shirt_img.getvalue(), key = "shirt"), sg.Image(data = pendant_img.getvalue(), key = "pendant")],
                        [sg.Image(data = pant_img.getvalue(), key = "pant"), sg.Image(data = ring1_img.getvalue(), key = "ring1")],
                        [sg.Image(data = shoe_img.getvalue(), key = "shoe"), sg.Image(data = ring2_img.getvalue(), key = "ring2")]
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
                        default_value = dictionary['characters'][0]['name'],
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
        # Update character tab
        index = character_list.index(values['active_character'])
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

window.close()       