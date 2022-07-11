#####################################################
# ICM_crafting.py                                 	#
# Code for implementing the crafting tab          	#
#####################################################
import PySimpleGUI as sg
import json

import ICM_functions as icm_f

crafting_column = 	sg.Column(
					[
						[
							sg.Image(data = icm_f.generate_img('None', (72, 72), True), key = 'craft{}image'.format(i)), 
							sg.Spin([i for i in range(1, 100)], enable_events = True, initial_value = 1, size = (2, 1), key = 'craft{}count'.format(i)), 
							sg.Button('X', key = 'craft{}remove'.format(i))
						] for i in range(0, 5)
					])

ingredients_column = 	sg.Column(	
						[
							[sg.Column(
							[
								[
									sg.Image(data = icm_f.generate_img('None', (72, 72), True), key = 'ingredient{}image'.format(4 * i + j)), 
									sg.Text('0', relief = 'sunken', size = (5, 1), justification = 'center', key = 'ingredient{}count'.format(4 * i + j))
								] for i in range(0, 5)
							]) for j in range(0 , 4)]
						])

crafting_frame = 	sg.Frame(layout = 
					[
						[crafting_column], 
						[
							sg.Button('Prev', key = 'prev_crafting'), 
							sg.Text('1', relief = 'sunken', size = (3, 1), justification = 'center', key = 'current_crafting'), 
							sg.Button('Next', key = 'next_crafting')
						], 
						[sg.Button('Add Item', key = 'add_item'), sg.Button('Remove All', key = 'remove_all')]
					], title = 'Crafting List', element_justification = 'center')

ingredients_frame = 	sg.Frame(layout = 
						[
							[ingredients_column], 
							[
								sg.Button('Prev', key = 'prev_ingredients'), 
								sg.Text('1', relief = 'sunken', size = (3, 1), justification = 'center', key = 'current_ingredients'), 
								sg.Button('Next', key = 'next_ingredients')
							]
						], title = 'Ingredients', element_justification = 'center')

material_column = 	sg.Column(
					[
						[sg.Text('The list is empty!'), sg.Checkbox('Use Base Materials', default = False, enable_events = True, key = 'toggle_base')],
						[ingredients_frame]
					])

# Use text for if the list is craftable or not (does the user have the materials and inventory spaces required)
# colour it red (not craftable), yellow (empty), or green (craftable)

crafting_tab =      [
                        [crafting_frame, material_column]
                    ]