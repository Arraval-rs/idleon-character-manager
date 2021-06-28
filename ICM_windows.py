#####################################################
# ICM_windows.py                                  	#
# All functions used for updating widgets  			# 
#####################################################
import os
import io
import json
import PySimpleGUI as sg
from PIL import Image, ImageDraw

import ICM_functions as icm_f

def update_crafting_widgets(window, event): # TODO: Add tooltips to craft/ingredients (easy)
	if event in crafting_events:
		if 'craft' in event and 'remove' in event:
			if len(icm_f.current_recipies) > int(event[5]):
				icm_f.current_recipies.pop(int(event[5]))
				icm_f.total_ingredients =  icm_f.update_ingredient_counts(icm_f.current_recipies)
				# if removal results in an empty page(for crafts or ingredients), go back a page
				# Update spinboxes
		if 'count' in event:
			if 5 * (int(window['current_crafting'].get()) - 1) + int(event[5]) < len(icm_f.current_recipies):
				icm_f.current_recipies[5 * (int(window['current_crafting'].get()) - 1) + int(event[5])][1] = window[event].get()
			else:
				window[event].update(1)
			icm_f.total_ingredients = icm_f.update_ingredient_counts(icm_f.current_recipies)
		if event == 'remove_all':
			icm_f.current_recipies = []
			icm_f.total_ingredients = []
			window['current_crafting'].update(1)
			window['current_ingredients'].update(1)
			for i in range(0, 5):
				window['craft{}count'.format(i)].update(1)
			for i in range(0, 20):
				window['ingredient{}count'.format(i)].update(0)
		if event in ('next_crafting', 'prev_crafting'):
			if event == 'next_crafting' and int(window['current_crafting'].get()) < len(icm_f.current_recipies)/5:
				window['current_crafting'].update(int(window['current_crafting'].get()) + 1)
			if event == 'prev_crafting' and int(window['current_crafting'].get()) > 1:
				window['current_crafting'].update(int(window['current_crafting'].get()) - 1)
			icm_f.total_ingredients = icm_f.update_ingredient_counts(icm_f.current_recipies)
			# Update spinboxes
		if event == 'next_ingredients' and int(window['current_ingredients'].get()) < len(icm_f.total_ingredients)/20:
			window['current_ingredients'].update(int(window['current_ingredients'].get()) + 1)
		if event == 'prev_ingredients' and int(window['current_ingredients'].get()) > 1:
			window['current_ingredients'].update(int(window['current_ingredients'].get()) - 1)
		if event == 'add_item':
			item_to_add = crafting_popup()
			if item_to_add[0] != 'None':
				if len(icm_f.current_recipies) != 0 and item_to_add[0] in icm_f.current_recipies[0:len(icm_f.current_recipies)][0]:
					for i in range(0, len(icm_f.current_recipies)):
						if icm_f.current_recipies[i][0] == item_to_add[0]:
							if icm_f.current_recipies[i][1] < 99:
								icm_f.current_recipies[i][1] += 1
								window['craft{}count'.format(i)].update(icm_f.current_recipies[i][1])
								icm_f.total_ingredients = icm_f.update_ingredient_counts(icm_f.current_recipies)
							break
				else:
					icm_f.current_recipies.append([item_to_add[0], 1]) 
					icm_f.total_ingredients = icm_f.update_ingredient_counts(icm_f.current_recipies)
	    # Update crafting images/counts
		for i in range(0, 5):
			if i + 5 * (int(window['current_crafting'].get()) - 1) < len(icm_f.current_recipies):
				window['craft{}image'.format(i)].update(data = icm_f.generate_img(icm_f.find_image(icm_f.current_recipies[i + 5 * (int(window['current_crafting'].get()) - 1)][0], icm_f.image_paths), (72, 72), True))
			else:
				window['craft{}image'.format(i)].update(data = icm_f.generate_img('images/Empty Slot.png', (72, 72), False))
		# Update ingredients images/counts
		for i in range(0, 20):
			if i + 20 * (int(window['current_ingredients'].get()) - 1) < len(icm_f.total_ingredients):
				window['ingredient{}image'.format(i)].update(data = icm_f.generate_img(icm_f.find_image(icm_f.total_ingredients[i + 20 * (int(window['current_ingredients'].get()) - 1)]['name'], icm_f.image_paths), (72, 72), True))
				window['ingredient{}count'.format(i)].update(icm_f.total_ingredients[i + 20 * (int(window['current_ingredients'].get()) - 1)]['count'])
			else:
				window['ingredient{}image'.format(i)].update(data = icm_f.generate_img('images/Empty Slot.png', (72, 72), True))
				window['ingredient{}count'.format(i)].update(0)

def crafting_popup():
    preview_frame = sg.Frame('None', layout = [[sg.Sizer(40), 
                                                sg.Image(data = icm_f.generate_img('images/Empty Slot.png', (72, 72), False), key = 'preview_image'), 
                                                sg.Sizer(40)]], key = 'preview_frame', element_justification = 'center')
    ingredient_col = []
    for i in range(0, 2):
        for j in range(0, 2):
            ingredient_col.append(sg.Column(
                                    [
                                        [sg.Image(data = icm_f.generate_img('images/Locked.png', (72, 72), False), key = 'ingredient{}'.format(2 * i + j))], 
                                        [sg.Text('0', size = (5, 1), relief = 'sunken', justification = 'center', key = 'ingredient{}cost'.format(2 * i + j))]
                                    ], 
                                    element_justification = 'center'))
    cost_frame = sg.Frame('Costs', layout = [[ingredient_col[0], ingredient_col[1]], [ingredient_col[2], ingredient_col[3]]])
    tab = []
    for i in range(0, 3):
        tab.append(sg.Column([[sg.Graph((72, 72), (0, 0), (72, 72), enable_events = True, key = 'tab{}_item{}'.format(i, 4 * k + j)) for j in range(0 , 4)] for k in range(0, 4)]))
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
                window['tab{}_item{}'.format(i, 4 * j + k)].draw_image(data = icm_f.get_crafting_item(icm_f.tab_titles[i], 4 * j + k, icm_f.image_paths), location = (0, 72))
    current_selection = [-1, 0]
    # Event loop
    while True:
        event, values = window.read()
        if event in ('Exit', sg.WIN_CLOSED):
            break
        if event == 'confirm_craft' and current_selection[0] != -1:
            window.close()
            return [icm_f.craftables[icm_f.tab_titles[current_selection[0]]][current_selection[1]]['name'], icm_f.craftables[icm_f.tab_titles[current_selection[0]]][current_selection[1]]['ingredients']]
        if 'tab' in event:
            current_selection = [int(event[3]), 16 * (int(window['current_page'].get()) - 1) + int(event[9:])]
            window['preview_frame'].update(value = icm_f.craftables[icm_f.tab_titles[current_selection[0]]][current_selection[1]]['name'])
            window['preview_image'].update(data = icm_f.get_crafting_item(icm_f.tab_titles[int(event[3])], 16 * (int(window['current_page'].get()) - 1) + int(event[9:]), icm_f.image_paths))
            for i in range(0, 2):
                for j in range(0, 2):
                    window['ingredient{}'.format(2 * i + j)].update(data = icm_f.get_ingredient_image(icm_f.tab_titles[current_selection[0]], current_selection[1], 2 * i + j, icm_f.image_paths))
                    if 2 * i + j > len(icm_f.craftables[icm_f.tab_titles[current_selection[0]]][current_selection[1]]['ingredients']) - 1:
                        window['ingredient{}'.format(2 * i + j)].set_tooltip(None)
                        window['ingredient{}cost'.format(2 * i + j)].update('0')
                    else:
                        window['ingredient{}'.format(2 * i + j)].set_tooltip(icm_f.craftables[icm_f.tab_titles[current_selection[0]]][current_selection[1]]['ingredients'][2 * i + j]['name'])
                        window['ingredient{}cost'.format(2 * i + j)].update(icm_f.craftables[icm_f.tab_titles[current_selection[0]]][current_selection[1]]['ingredients'][2 * i + j]['count'])              
        if event == 'Next' and int(window['current_page'].get()) < 6 or event =='Prev' and int(window['current_page'].get()) > 1:
            if event == 'Next':
                window['current_page'].update(int(window['current_page'].get()) + 1)
            else:
                window['current_page'].update(int(window['current_page'].get()) - 1)
            for i in range(0, 3):
                for j in range(0, 4):
                    for k in range(0, 4):
                        window['tab{}_item{}'.format(i, 4 * j + k)].draw_image(data = icm_f.get_crafting_item(icm_f.tab_titles[i], 16 * (int(window['current_page'].get()) - 1) + 4 * j + k, icm_f.image_paths), location = (0, 72))
    window.close()
    return ['None', 0]

# Some event lists
crafting_events = ['add_item', 'prev_crafting', 'next_crafting', 'prev_ingredients', 'next_ingredients', 'remove_all']
for i in range(0, 5):
	crafting_events.append('craft{}count'.format(i))
	crafting_events.append('craft{}remove'.format(i))
