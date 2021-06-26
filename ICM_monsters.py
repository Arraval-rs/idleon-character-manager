#####################################################
# ICM_monsters.py                                 	#
# Code for implementing the monsters tab          	#
#####################################################
import PySimpleGUI as sg
import json

import ICM_functions as icm_f

# Dictionary for monsters
json_file = open("data/monster_data.json", "rt")
json_text = json_file.read()
craftables = json.loads(json_text)

monsters_tab =      [
                        [sg.Image(data = icm_f.generate_img('images/Misc_WIP/Builder Bird.gif', (40, 58), False), key = 'builder_bird'), sg.Text('Under Construction')]
                    ]