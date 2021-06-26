#####################################################
# ICM_crafting.py                                 	#
# Code for implementing the crafting tab          	#
#####################################################
import PySimpleGUI as sg
import json

import ICM_functions as icm_f

# Dictionary for crafting recepies
json_file = open("data/crafting_data.json", "rt")
json_text = json_file.read()
craftables = json.loads(json_text)

crafting_column = 	sg.Column(
					[
						[sg.Image(data = icm_f.generate_img('None', (72, 72), True)), sg.Text('None'), sg.Spin([i for i in range(0, 11)], initial_value = 1, size = (2, 1)), sg.Button('X')] for i in range(0, 5)
					])

ingredients_column = 	sg.Column(	
						[
							[sg.Column([[sg.Image(data = icm_f.generate_img('None', (72, 72), True)), sg.Text('None'), sg.Text('0', relief = 'sunken', size = (5, 1), justification = 'center')] for i in range(0, 5)]) for j in range(0 , 3)]
						])

crafting_frame = sg.Frame(layout = [[crafting_column], [sg.Button('Prev'), sg.Text('1', relief = 'sunken', size = (3, 1), justification = 'center'), sg.Button('Next')], [sg.Button('Add Item'), sg.Button('Remove All')]], title = 'Crafting List', element_justification = 'center')

ingredients_frame = sg.Frame(layout = [[ingredients_column], [sg.Button('Prev'), sg.Text('1', relief = 'sunken', size = (3, 1), justification = 'center'), sg.Button('Next')]], title = 'Ingredients', element_justification = 'center')

# [sg.Checkbox('Use Base Materials', default = False)]
# [sg.Text('The list is empty!')]
# Use aboxe text for if the list is craftable or not (does the user have the materials required)
# colour it red (not craftable), yellow (empty), or green (craftable)

crafting_tab =      [
                        [crafting_frame, ingredients_frame]
                    ]