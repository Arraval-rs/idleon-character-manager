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

def update_monster_widgets(window, event):
	if event == '__TIMEOUT__' and icm_f.current_monster[0] != '':
		if'Amarok' not in icm_f.monsters[icm_f.current_monster[0]][icm_f.current_monster[1]]['Name'] and \
		'Efaunt' not in icm_f.monsters[icm_f.current_monster[0]][icm_f.current_monster[1]]['Name'] and \
		'Chizoar' not in icm_f.monsters[icm_f.current_monster[0]][icm_f.current_monster[1]]['Name']:
			if icm_f.current_monster[0] == 'Boss':
				window['monster_gif'].update_animation_no_buffering('images/Monsters/Boss/{}.gif'.format(icm_f.monsters['Boss'][icm_f.current_monster[1]]['Name']))
			elif 'Blueberry' not in icm_f.monsters[icm_f.current_monster[0]][icm_f.current_monster[1]]['Name'] and 'Plasti' not in icm_f.monsters[icm_f.current_monster[0]][icm_f.current_monster[1]]['Name']:
				window['monster_gif'].update_animation_no_buffering('images/Monsters/{}/{} {}.gif'.format(icm_f.current_monster[0], icm_f.monsters[icm_f.current_monster[0]][icm_f.current_monster[1]]['Name'], window['anim_style'].get()), time_between_frames = 120)
	elif event in monster_events:
		if 'W1' in event:
			icm_f.current_monster = ['W1', int(event[3:len(event)])]
		if 'W2' in event:
			icm_f.current_monster = ['W2', int(event[3:len(event)])]
		if 'W3' in event:
			icm_f.current_monster = ['W3', int(event[3:len(event)])]
		if 'W4' in event:
			icm_f.current_monster = ['W4', int(event[3:len(event)])]
		if 'Event' in event:
			icm_f.current_monster = ['Event', int(event[6:len(event)])]
			if 'Blueberry' in icm_f.monsters[icm_f.current_monster[0]][icm_f.current_monster[1]]['Name'] or 'Plasti' in icm_f.monsters[icm_f.current_monster[0]][icm_f.current_monster[1]]['Name']:
				window['monster_gif'].update(data = icm_f.generate_img('images/Monsters/Event/{} Idle.png'.format(icm_f.monsters['Event'][icm_f.current_monster[1]]['Name']), (150, 150), False))
		if 'Boss' in event and event != 'Boss':
			icm_f.current_monster = ['Boss', int(event[5:len(event)])]
			if 'Amarok' in icm_f.monsters['Boss'][icm_f.current_monster[1]]['Name'] or \
			'Efaunt' in icm_f.monsters['Boss'][icm_f.current_monster[1]]['Name'] or \
			'Chizoar' in icm_f.monsters['Boss'][icm_f.current_monster[1]]['Name']:
				window['monster_gif'].update(data = icm_f.generate_img('images/Monsters/Boss/{}.png'.format(icm_f.monsters['Boss'][icm_f.current_monster[1]]['Name']), (150, 150), False))
		window['mon_name'].update(icm_f.monsters[icm_f.current_monster[0]][icm_f.current_monster[1]]['Name'])
		window['mon_health'].update('Health: {}'.format(f'{int(icm_f.monsters[icm_f.current_monster[0]][icm_f.current_monster[1]]["Health"]):,}'))
		window['mon_exp'].update('Experience: {}'.format(f'{int(icm_f.monsters[icm_f.current_monster[0]][icm_f.current_monster[1]]["Experience"]):,}'))
		window['hit_chance'].update('Hit Chance: {}%'.format(icm_f.calculate_hit_chance(window['char_acc'].get(), icm_f.monsters[icm_f.current_monster[0]][icm_f.current_monster[1]]['Accuracy 100%'])))
		window['acc_needed'].update('Accuracy Needed: {}'.format(icm_f.calculate_accuracy_needed(window['char_acc'].get(), int(icm_f.monsters[icm_f.current_monster[0]][icm_f.current_monster[1]]['Accuracy 100%']))))
		window['def_needed'].update('Defence Needed: {}'.format(icm_f.calculate_defence_needed(window['char_def'].get(), int(icm_f.monsters[icm_f.current_monster[0]][icm_f.current_monster[1]]['Defence for 0']))))
		if icm_f.current_monster[0] == 'Boss' and \
		('Amarok' in icm_f.monsters['Boss'][icm_f.current_monster[1]]['Name'] or \
		'Efaunt' in icm_f.monsters['Boss'][icm_f.current_monster[1]]['Name'] or \
		'Chizoar' in icm_f.monsters['Boss'][icm_f.current_monster[1]]['Name']):
			atk_string = ''
			for i in range(0, len(icm_f.monsters['Boss'][icm_f.current_monster[1]]['Attacks'])):
				damage = icm_f.monsters['Boss'][icm_f.current_monster[1]]['Attacks'][i]['Attack']
				atk_string += '{}) {}: {}\nDamage Taken: {}\n'.format(i + 1, icm_f.monsters['Boss'][icm_f.current_monster[1]]['Attacks'][i]['Name'], damage, icm_f.calculate_damage_taken(window['char_def'].get(), int(damage)))
			window['mon_attack'].update(atk_string)
		else:
			damage = icm_f.monsters[icm_f.current_monster[0]][icm_f.current_monster[1]]['Attack']
			window['mon_attack'].update('Attack: {}\nDamage Taken: {}'.format(damage, icm_f.calculate_damage_taken(window['char_def'].get(), int(damage))))
			window['mon_speed'].update('Speed: {}'.format(icm_f.monsters[icm_f.current_monster[0]][icm_f.current_monster[1]]['Speed']))
			window['mon_respawn'].update('Respawn: {}'.format(f'{int(icm_f.monsters[icm_f.current_monster[0]][icm_f.current_monster[1]]["Respawn"]):,}'))

def update_crafting_widgets(window, event):
	if event in crafting_events:
		if 'craft' in event and 'remove' in event:
			if len(icm_f.current_recipies) > int(event[5]):
				icm_f.current_recipies.pop(5 * (int(window['current_crafting'].get()) - 1) + int(event[5]))
				icm_f.total_ingredients =  icm_f.update_ingredient_counts(icm_f.current_recipies, window['toggle_base'].get(), window['crafting_text'])
				window['current_crafting'].update(max(1, int(len(icm_f.current_recipies)/5) + (len(icm_f.current_recipies)%5 > 0)))
				window['current_ingredients'].update(max(1, int(len(icm_f.total_ingredients)/20) + (len(icm_f.total_ingredients)%20 > 0)))
		if 'count' in event:
			if 5 * (int(window['current_crafting'].get()) - 1) + int(event[5]) < len(icm_f.current_recipies):
				icm_f.current_recipies[5 * (int(window['current_crafting'].get()) - 1) + int(event[5])][1] = window[event].get()
			else:
				window[event].update(1)
			icm_f.total_ingredients = icm_f.update_ingredient_counts(icm_f.current_recipies, window['toggle_base'].get(), window['crafting_text'])
		if event == 'remove_all':
			icm_f.current_recipies = []
			icm_f.total_ingredients = []
			window['current_crafting'].update(1)
			window['current_ingredients'].update(1)
			window['crafting_text'].update('List is empty!')
			for i in range(0, 5):
				window['craft{}count'.format(i)].update(1)
			for i in range(0, 20):
				window['ingredient{}count'.format(i)].update(0)
		if event in ('next_crafting', 'prev_crafting'):
			if event == 'next_crafting' and int(window['current_crafting'].get()) < len(icm_f.current_recipies)/5:
				window['current_crafting'].update(int(window['current_crafting'].get()) + 1)
			if event == 'prev_crafting' and int(window['current_crafting'].get()) > 1:
				window['current_crafting'].update(int(window['current_crafting'].get()) - 1)
			icm_f.total_ingredients = icm_f.update_ingredient_counts(icm_f.current_recipies, window['toggle_base'].get(), window['crafting_text'])
		if event == 'next_ingredients' and int(window['current_ingredients'].get()) < len(icm_f.total_ingredients)/20:
			window['current_ingredients'].update(int(window['current_ingredients'].get()) + 1)
		if event == 'prev_ingredients' and int(window['current_ingredients'].get()) > 1:
			window['current_ingredients'].update(int(window['current_ingredients'].get()) - 1)
		if event == 'add_item':
			item_to_add = crafting_popup()
			if item_to_add[0] != 'None':
				found = False
				if len(icm_f.current_recipies) != 0:
					for i in range(0, len(icm_f.current_recipies)):
						if icm_f.current_recipies[i][0] == item_to_add[0]:
							found = True
							if icm_f.current_recipies[i][1] < 99:
								icm_f.current_recipies[i][1] += 1
								icm_f.total_ingredients = icm_f.update_ingredient_counts(icm_f.current_recipies, window['toggle_base'].get(), window['crafting_text'])
							break
				if not found:
					icm_f.current_recipies.append([item_to_add[0], 1]) 
					icm_f.total_ingredients = icm_f.update_ingredient_counts(icm_f.current_recipies, window['toggle_base'].get(), window['crafting_text'])
		if event == 'toggle_base':
			icm_f.total_ingredients = icm_f.update_ingredient_counts(icm_f.current_recipies, window['toggle_base'].get(), window['crafting_text'])

	    # Update crafting images/counts
		for i in range(0, 5):
			if i + 5 * (int(window['current_crafting'].get()) - 1) < len(icm_f.current_recipies):
				window['craft{}image'.format(i)].update(data = icm_f.generate_img(icm_f.find_image(icm_f.current_recipies[i + 5 * (int(window['current_crafting'].get()) - 1)][0], icm_f.image_paths), (72, 72), True))
				window['craft{}image'.format(i)].set_tooltip(icm_f.current_recipies[i + 5 * (int(window['current_crafting'].get()) - 1)][0])
				window['craft{}count'.format(i)].update(icm_f.current_recipies[i + 5 * (int(window['current_crafting'].get()) - 1)][1])
			else:
				window['craft{}image'.format(i)].update(data = icm_f.generate_img('images/Empty Slot.png', (72, 72), False))
				window['craft{}count'.format(i)].update(1)
		# Update ingredients images/counts
		for i in range(0, 20):
			if i + 20 * (int(window['current_ingredients'].get()) - 1) < len(icm_f.total_ingredients):
				window['ingredient{}image'.format(i)].update(data = icm_f.generate_img(icm_f.find_image(icm_f.total_ingredients[i + 20 * (int(window['current_ingredients'].get()) - 1)]['name'], icm_f.image_paths), (72, 72), True))
				window['ingredient{}image'.format(i)].set_tooltip(icm_f.total_ingredients[i + 20 * (int(window['current_ingredients'].get()) - 1)]['name'])
				window['ingredient{}count'.format(i)].update(icm_f.total_ingredients[i + 20 * (int(window['current_ingredients'].get()) - 1)]['count'])
			else:
				window['ingredient{}image'.format(i)].update(data = icm_f.generate_img('images/Empty Slot.png', (72, 72), True))
				window['ingredient{}count'.format(i)].update(0)

def crafting_popup():
    preview_frame = sg.Frame('None', layout = [[sg.Sizer(50), 
                                                sg.Image(data = icm_f.generate_img('images/Empty Slot.png', (72, 72), False), key = 'preview_image'), 
                                                sg.Sizer(50)]], key = 'preview_frame', element_justification = 'center')
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
    for i in range(0, 4):
        tab.append(sg.Column([[sg.Graph((72, 72), (0, 0), (72, 72), enable_events = True, key = 'tab{}_item{}'.format(i, 4 * k + j)) for j in range(0 , 4)] for k in range(0, 4)]))
    anvil_tab_1 = sg.Tab('I', layout = [[tab[0]]])
    anvil_tab_2 = sg.Tab('II', layout = [[tab[1]]])
    anvil_tab_3 = sg.Tab('III', layout = [[tab[2]]])
    anvil_tab_4 = sg.Tab('IV', layout = [[tab[3]]])
    left_col = sg.Column([[preview_frame], [cost_frame], [sg.Button('Confirm', key = 'confirm_craft')]], element_justification = 'left')
    right_col = sg.Column(
                [
                    [sg.TabGroup([[anvil_tab_1, anvil_tab_2, anvil_tab_3, anvil_tab_4]])], 
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
    for i in range(0, 4):
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
        	if 16 * (int(window['current_page'].get()) - 1) + int(event[9:]) < len(icm_f.craftables[icm_f.tab_titles[int(event[3])]]):
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
            for i in range(0, 4):
                for j in range(0, 4):
                    for k in range(0, 4):
                        window['tab{}_item{}'.format(i, 4 * j + k)].draw_image(data = icm_f.get_crafting_item(icm_f.tab_titles[i], 16 * (int(window['current_page'].get()) - 1) + 4 * j + k, icm_f.image_paths), location = (0, 72))
    window.close()
    return ['None', 0]

def update_character_widgets(window, event, index):
	# Update active star talent page on arrow pressed
	if 'star_left' in event:
		active_tab = window['star_talents'].get()
		if active_tab == 'star_V':
			window['star_IV'].select()
		elif active_tab == 'star_IV':
			window['star_III'].select()
		elif active_tab == 'star_III':
			window['star_II'].select()
		elif active_tab == 'star_II':
			window['star_I'].select()
	elif 'star_right' in event:
		active_tab = window['star_talents'].get()
		if active_tab == 'star_I':
			window['star_II'].select()
		elif active_tab == 'star_II':
			window['star_III'].select()
		elif active_tab == 'star_III':
			window['star_IV'].select()
		elif active_tab == 'star_IV':
			window['star_V'].select()
	elif event == 'active_character':
		character_class = icm_f.dictionary['characters'][index]['class']
		character_base_class = icm_f.get_class_path(character_class, 1)

		# Update standalone character elements
		window['class_icon'].update(data = icm_f.generate_img('images/Classes/{}Icon.png'.format(icm_f.dictionary['characters'][index]['class']), (38, 36), False))
		window['class_image'].update(data = icm_f.generate_img('images/Classes/{}.png'.format(icm_f.dictionary['characters'][index]['class']), (129, 110), False))
		window['character_stats'].update(icm_f.get_character_stats(index, icm_f.dictionary))
		window['selected_equipment'].update(data = icm_f.generate_img('images/Empty Slot.png', (72, 72), False))
		window['equipped_item_stats'].update('STR: 0\t\tReach: 0\nAGI: 0\t\tDefence: 0\nWIS: 0\t\tWeapon Power: 0\nLUK: 0\t\tUpgrade Slots Left: 0')
		window['equipped_item_frame'].update(value = 'None')
		window['selected_inventory_item'].update(data = icm_f.generate_img('images/Empty Slot.png', (72, 72), False))
		window['inventory_item_stats'].update('Stack Size: 0')
		window['inventory_item_frame'].update('None')

		# Update equipment
		for i in range(0, 4):
			for j in range(0, 2):
				window['equipment{}'.format(2 * i + j)].update(data = icm_f.generate_img('images/Equipment/{}.png'.format(icm_f.dictionary['characters'][index]['equipment'][2*i+j]['name']), (72, 72), True))
				window['equipment{}'.format(2 * i + j + 8)].update(data = icm_f.generate_img('images/Equipment/{}.png'.format(icm_f.dictionary['characters'][index]['equipment'][2*i+j+8]['name']), (72, 72), True))
				window['tools{}'.format(2 * i + j)].draw_image(data = icm_f.generate_img('images/Tools/{}.png'.format(icm_f.dictionary['characters'][index]['tools'][2*i+j]['name']), (72, 72), True), location = (0, 72))
				window['food{}'.format(2 * i + j)].draw_image(data = icm_f.generate_img('images/Food/{}.png'.format(icm_f.dictionary['characters'][index]['food'][2*i+j]['name']), (72, 72), True), location = (0, 72))
    
		# Update skills
		for i in range(0, 9):
			window['{}level'.format(icm_f.skill_names[i])].update('{}\nLv. {}'.format(icm_f.skill_names[i], icm_f.dictionary['characters'][index]['skillLevels'][icm_f.skill_names[i].lower()]))

		# Update icm_f.talents tab 1 that are shared between classes
		for i in range(0, 10):
			if str(i) in icm_f.dictionary['characters'][index]['talentLevels'].keys(): # some icm_f.talents aren't in JSON
				window['talent{}'.format(i)].update('{}/100'.format(icm_f.dictionary['characters'][index]['talentLevels'][str(i)]))
			else:
				window['talent{}'.format(i)].update('0/100')
        
		# Update icm_f.talents tab 1 that are not shared between classes and tab 2
		for i in range(10, 30):
			window['talent_img{}'.format(i)].update(data = icm_f.talents['Filler'] if icm_f.get_class_depth(character_class) < 1 else icm_f.get_class_path(character_class, 1)[str(i)])
			if str(i) in icm_f.dictionary['characters'][index]['talentLevels'].keys()  and icm_f.get_class_depth(character_class) > 0: # some icm_f.talents aren't in JSON
				window['talent{}'.format(i)].update('{}/100'.format(icm_f.dictionary['characters'][index]['talentLevels'][str(i)]))
			else:
				window['talent{}'.format(i)].update('0/100')
        
		# Update icm_f.talents tab 3
		for i in range(30, 45):
			window['talent_img{}'.format(i)].update(data = icm_f.talents['Filler'] if icm_f.get_class_depth(character_class) < 2 else icm_f.get_class_path(character_class, 2)[str(i)])
			if str(i) in icm_f.dictionary['characters'][index]['talentLevels'].keys() and icm_f.get_class_depth(character_class) > 1: # some icm_f.talents aren't in JSON
				window['talent{}'.format(i)].update('{}/100'.format(icm_f.dictionary['characters'][index]['talentLevels'][str(i)]))
			else:
				window['talent{}'.format(i)].update('0/100')

		# Update icm_f.talents tab 3
		for i in range(45, 60):
			window['talent_img{}'.format(i)].update(data = icm_f.talents['Filler'] if icm_f.get_class_depth(character_class) < 3 else icm_f.get_class_path(character_class, 3)[str(i)])
			if str(i) in icm_f.dictionary['characters'][index]['talentLevels'].keys() and icm_f.get_class_depth(character_class) > 2: # some icm_f.talents aren't in JSON
				window['talent{}'.format(i)].update('{}/100'.format(icm_f.dictionary['characters'][index]['talentLevels'][str(i)]))
			else:
				window['talent{}'.format(i)].update('0/100')

		# Update icm_f.starTalents
		for i in range(0, 63):
			if i < len(icm_f.dictionary['characters'][index]['starTalentLevels']):
				window['star_talent{}'.format(i)].update('{}/100'.format(icm_f.dictionary['characters'][index]['starTalentLevels'][i]))
			else:
				window['star_talent{}'.format(i)].update('0/100')

		# Update inventory for new character
		window['current_inv'].update('1')
		for i in range(0, 4):
			for j in range(0, 4):
				window['inventory{}'.format(j + 4 * i)].draw_image(data = icm_f.get_inventory_item(j + 4 * i + 16 * (int(window['current_inv'].get()) - 1), icm_f.image_paths, index), location = (0, 72))

# Some event lists
crafting_events = ['add_item', 'prev_crafting', 'next_crafting', 'prev_ingredients', 'next_ingredients', 'remove_all', 'toggle_base']
for i in range(0, 5):
	crafting_events.append('craft{}count'.format(i))
	crafting_events.append('craft{}remove'.format(i))

monster_events = ['char_acc', 'char_def']
for i in range(0, 17):
	monster_events.append('W1_{}'.format(i))
	monster_events.append('W2_{}'.format(i))
	monster_events.append('W3_{}'.format(i))
	monster_events.append('W4_{}'.format(i))
	monster_events.append('Boss_{}'.format(i))
	monster_events.append('Event_{}'.format(i))