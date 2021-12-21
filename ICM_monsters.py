#####################################################
# ICM_monsters.py                                 	#
# Code for implementing the monsters tab          	#
#####################################################
import PySimpleGUI as sg
import json

import ICM_functions as icm_f

world1_tab = [[], [], [], [], [], []]

world2_tab = [[], [], [], [], [], []]

world3_tab = [[], [], [], [], [], []]

boss_tab = [[], [], [], [], [], []]

event_tab = [[], [], [], [], [], []]

for i in range(0, 6):
	for j in range(0, 3):
		if 3 * i + j < len(icm_f.monsters['W1']):
			world1_tab[i].append(sg.Image(data = icm_f.generate_img('images/Cards/{} Card.png'.format(icm_f.monsters['W1'][3 * i + j]['Name']), (56, 72), False), key = 'W1_{}'.format(3 * i + j), enable_events = True))
		if 3 * i + j < len(icm_f.monsters['W2']):
			world2_tab[i].append(sg.Image(data = icm_f.generate_img('images/Cards/{} Card.png'.format(icm_f.monsters['W2'][3 * i + j]['Name']), (56, 72), False), key = 'W2_{}'.format(3 * i + j), enable_events = True))
		if 3 * i + j < len(icm_f.monsters['W3']):
			world3_tab[i].append(sg.Image(data = icm_f.generate_img('images/Cards/{} Card.png'.format(icm_f.monsters['W3'][3 * i + j]['Name']), (56, 72), False), key = 'W3_{}'.format(3 * i + j), enable_events = True))
		if 3 * i + j < len(icm_f.monsters['Boss']):
			boss_tab[i].append(sg.Image(data = icm_f.generate_img('images/Cards/{} Card.png'.format(icm_f.monsters['Boss'][3 * i + j]['Name']), (56, 72), False), key = 'Boss_{}'.format(3 * i + j), enable_events = True))	
		if 3 * i + j < len(icm_f.monsters['Event']):
			event_tab[i].append(sg.Image(data = icm_f.generate_img('images/Cards/{} Card.png'.format(icm_f.monsters['Event'][3 * i + j]['Name']), (56, 72), False), key = 'Event_{}'.format(3 * i + j), enable_events = True))

attack_frame = [[sg.Text('Attack: 0\nDamage Taken: 0', size = (25, 16), key = 'mon_attack')]]

image_col = sg.Column(
			[
				[sg.Image(data = icm_f.generate_img('images/Empty Slot.png', (150, 150), False), key = 'monster_gif')], 
				[sg.Frame('Attacks', layout = attack_frame)]
			])

info_col = 	sg.Column(
			[
				[sg.Text('None', size = (15, 1), key = 'mon_name')], 
				[sg.Combo(['Walking', 'Idle'],
                        default_value = 'Idle',
                        key = 'anim_style',
                        readonly = True)],
				[sg.Column([[]], pad = (0, 30))], 
				[sg.Text('Health: 0', size = (18, 1), key = 'mon_health')], 
				[sg.Text('Speed: 0', size = (10, 1), key = 'mon_speed')], 
				[sg.Text('Experience: 0', size = (18, 1), key = 'mon_exp')], 
				[sg.Text('Respawn: 0', size = (18, 1), key = 'mon_respawn')], 
				[sg.Column([[]], pad = (0, 30))], 
				[sg.Text('Hit Chance: 0%', key = 'hit_chance')], 
				[sg.Text('Accuracy Needed: 0', key = 'acc_needed')], 
				[sg.Text('Defence Needed: 0', key = 'def_needed')]
			])

selected_monster = [[info_col, image_col]]

monsters_tab =      [[
					sg.TabGroup(
                        [[
                        	sg.Tab('W1', world1_tab),
                        	sg.Tab('W2', world2_tab),
                        	sg.Tab('W3', world3_tab),
                        	sg.Tab('Boss', boss_tab),
                        	sg.Tab('Event', event_tab)
                        ]]), sg.Frame('', layout = selected_monster)

					]]