#####################################################
# ICM_refinery.py                                 	#
# Code for implementing the 3D refinery tab         #
#####################################################
import PySimpleGUI as sg
import os

import ICM_functions as icm_f

lab_bonus = 3
speed_bonus = 1 / (1 + 0.01 * icm_f.dictionary['account']['alchemy']['vialLevels'][25] + 0.02 * icm_f.dictionary['account']['saltLick'][2] + lab_bonus)
refine_speed = [int(15 * speed_bonus * 100 + 0.5) / 100, int(60 * speed_bonus * 100 + 0.5) / 100]

tab_titles = ['Combustion', 'Synthesis']
salt_names = ['redox', 'explosive', 'spontaneity', 'dioxide', 'purple', 'nullo']

refinery_levels = []
for i in range(0, 6):
    refinery_levels.append(icm_f.dictionary['account']['refinery']['salts'][salt_names[i]]['rank'])

ingredient_col = []
rank_col = []
net_resources = [[]]
net_salts = [[],[]]

for i in range(0, int(len(salt_names) / 3 + 0.5)):
    ingredient_col.append([])
    rank_col.append([])
    for j in range(0, 3):
        rank_col[i].append([
            sg.Text("Rank: {}\nState: {}\nAuto Refine: {}%\n{}/{} ({}%)\n{} cycles / hour".format(
                refinery_levels[3 * i + j], 
                icm_f.dictionary['account']['refinery']['salts'][salt_names[3 * i + j]]['state'].upper(), 
                icm_f.dictionary['account']['refinery']['salts'][salt_names[3 * i + j]]['autoPercent'], 
                icm_f.dictionary['account']['refinery']['salts'][salt_names[3 * i + j]]['refined'], 
                icm_f.refinery['ranks'][refinery_levels[3 * i + j] - 1]['cap'], 
                # weird math and casting for 2 point precision
                int(icm_f.dictionary['account']['refinery']['salts'][salt_names[3 * i + j]]['refined'] / icm_f.refinery['ranks'][refinery_levels[3 * i + j] - 1]['cap'] * 10000 + 0.5) / 100,
                int(60 / refine_speed[i] * 100 + 0.5) / 100
            ), relief = 'sunken', justification = 'center', size = (18, 5), key = 'redox{}'.format(3 * i + j)),
            sg.Image(data =     icm_f.generate_img('images/Materials/{}_Salts.png'.format(salt_names[3 * i + j]), (72, 72), True) 
                                if os.path.exists('images/Materials/{}_Salts.png'.format(salt_names[3 * i + j])) 
                                else icm_f.generate_img('images/Materials/{}_Salt.png'.format(salt_names[3 * i + j]), (72, 72), True) 
                                if os.path.exists('images/Materials/{}_Salt.png'.format(salt_names[3 * i + j])) 
                                else icm_f.generate_img('images/Materials/{}_Synthesis.png'.format(salt_names[3 * i + j]), (72, 72), True))
        ])
        ingredient_col[i].append([sg.Image( data =  icm_f.generate_img('images/Materials/{}.png'.format(icm_f.refinery['salts'][salt_names[3 * i + j]][k]['item']), (36, 36), True) 
                                                    if k < len(icm_f.refinery['salts'][salt_names[3 * i + j]]) 
                                                    else icm_f.generate_img('images/Empty Slot.png', (36, 36), False), 
                                            tooltip =   '{}\n{}'.format(icm_f.refinery['salts'][salt_names[3 * i + j]][k]['item'], icm_f.refinery['salts'][salt_names[3 * i + j]][k]['count'] * icm_f.refinery['ranks'][refinery_levels[3 * i + j] - 1]['cost'])
                                                        if (k < len(icm_f.refinery['salts'][salt_names[3 * i + j]]) and not icm_f.is_salt(icm_f.refinery['salts'][salt_names[3 * i + j]][k]['item']))
                                                        else '{}\n{}'.format(icm_f.refinery['salts'][salt_names[3 * i + j]][k]['item'], icm_f.refinery['salts'][salt_names[3 * i + j]][k]['count'] * icm_f.salt_modifier(refinery_levels[3 * i + j] - 1, 3 * i + j))
                                                        if (k < len(icm_f.refinery['salts'][salt_names[3 * i + j]]))
                                                        else None
                                            ) for k in range(0, 3)])
        ingredient_col[i].append([sg.Image(data =   icm_f.generate_img('images/Materials/{}.png'.format(icm_f.refinery['salts'][salt_names[3 * i + j]][k]['item']), (36, 36), True) 
                                                    if k < len(icm_f.refinery['salts'][salt_names[3 * i + j]]) 
                                                    else icm_f.generate_img('images/Empty Slot.png', (36, 36), False),
                                            tooltip =   '{}\n{}'.format(icm_f.refinery['salts'][salt_names[3 * i + j]][k]['item'], 
                                                        icm_f.refinery['salts'][salt_names[3 * i + j]][k]['count'] * icm_f.refinery['ranks'][refinery_levels[3 * i + j] - 1]['cost'])
                                                        if (k < len(icm_f.refinery['salts'][salt_names[3 * i + j]]) and not icm_f.is_salt(icm_f.refinery['salts'][salt_names[3 * i + j]][k]['item']))
                                                        else '{}\n{}'.format(icm_f.refinery['salts'][salt_names[3 * i + j]][k]['item'], icm_f.refinery['salts'][salt_names[3 * i + j]][k]['count'] * icm_f.salt_modifier(refinery_levels[3 * i + j] - 1, 3 * i + j))
                                                        if (k < len(icm_f.refinery['salts'][salt_names[3 * i + j]]))
                                                        else None
                                            ) for k in range(3, 6)])
        ingredient_col[i].append([sg.VerticalSeparator()])
        
        net_salt = 0
        if icm_f.dictionary['account']['refinery']['salts'][salt_names[3 * i + j]]['state'] == 'on':
            net_salt = icm_f.refinery['ranks'][refinery_levels[3 * i + j] - 1]['power']
        if (3 * i + j) == 2 and icm_f.dictionary['account']['refinery']['salts'][salt_names[3]]['state'] == 'on':
            net_salt = int((60 / refine_speed[0] * net_salt - 60 / refine_speed[1] * icm_f.salt_modifier(refinery_levels[3] - 1, 3)) * 100) / 100
        elif (3 * i + j) < 5 and icm_f.dictionary['account']['refinery']['salts'][salt_names[3 * i + j + 1]]['state'] == 'on':
            net_salt = int((60 / refine_speed[i] * (net_salt - 2 * icm_f.salt_modifier(refinery_levels[3 * i + j + 1] - 1, 3 * i + j + 1))) * 100) / 100

        # use is_salt() and salt_img() to clean this up
        net_salts[0].append([sg.Image(data =   icm_f.generate_img('images/Materials/{}_Salts.png'.format(salt_names[3 * i + j]), (60, 60), True) 
                                            if os.path.exists('images/Materials/{}_Salts.png'.format(salt_names[3 * i + j])) 
                                            else icm_f.generate_img('images/Materials/{}_Salt.png'.format(salt_names[3 * i + j]), (60, 60), True) 
                                            if os.path.exists('images/Materials/{}_Salt.png'.format(salt_names[3 * i + j])) 
                                            else icm_f.generate_img('images/Materials/{}_Synthesis.png'.format(salt_names[3 * i + j]), (60, 60), True))])
        net_salts[1].append([sg.Text('{} / hour'.format(net_salt))])
        if (3 * i + j) < 5:
            net_salts[1].append([sg.VerticalSeparator(pad = (0, 18))])

        for k in range(0, len(icm_f.refinery['salts'][salt_names[3 * i + j]])):
            if not icm_f.is_salt(icm_f.refinery['salts'][salt_names[3 * i + j]][k]['item']):
                printedItem = False
                for item in icm_f.printerTotals:
                    if item['item'] == icm_f.refinery['salts'][salt_names[3 * i + j]][k]['item']:
                        net_resources[-1].append(sg.Image(data = icm_f.generate_img('images/Materials/{}.png'.format(icm_f.refinery['salts'][salt_names[3 * i + j]][k]['item']), (36, 36), True)))
                        net_resources[-1].append(sg.Text('{} / hour'.format(int((item['rate'] - icm_f.refinery['salts'][salt_names[3 * i + j]][k]['count'] * icm_f.refinery['ranks'][refinery_levels[3 * i + j] - 1]['cost'] * 60 / refine_speed[i]) * 100) / 100)))
                        printedItem = True
                        break
                if not printedItem:
                    net_resources[-1].append(sg.Image(data = icm_f.generate_img('images/Materials/{}.png'.format(icm_f.refinery['salts'][salt_names[3 * i + j]][k]['item']), (36, 36), True)))
                    net_resources[-1].append(sg.Text('{} / hour'.format(int((-icm_f.refinery['salts'][salt_names[3 * i + j]][k]['count'] * icm_f.refinery['ranks'][refinery_levels[3 * i + j] - 1]['cost'] * 60 / refine_speed[i]) * 100) / 100)))
                if len(net_resources[-1]) == 6:
                    net_resources.append([])

storage_left_col = []
storage_right_col = []
for i in range(0, 4):
    storage_left_col.append([sg.Image(data = icm_f.generate_img('images/Materials/{}.png'.format(icm_f.dictionary['account']['refinery']['storage'][2 * i]['salt']), (72, 72), True))])
    storage_left_col.append([sg.Text(icm_f.dictionary['account']['refinery']['storage'][2 * i]['count'], relief = 'sunken', justification = 'center')])                 
    storage_right_col.append([sg.Image(data = icm_f.generate_img('images/Materials/{}.png'.format(icm_f.dictionary['account']['refinery']['storage'][2 * i + 1]['salt']), (72, 72), True))])
    storage_right_col.append([sg.Text(icm_f.dictionary['account']['refinery']['storage'][2 * i + 1]['count'], relief = 'sunken', justification = 'center')])

refinery_tab =       [[
                        sg.Column([
                            [
                                sg.TabGroup([[
                                    sg.Tab(tab_titles[i], [[sg.Column(ingredient_col[i]), sg.Column(rank_col[i])]]) for i in range(0, len(ingredient_col))
                                ]])
                            ],
                            [
                                sg.Frame(layout = [[sg.Column(net_resources, element_justification = 'center', scrollable = True, vertical_scroll_only = True)]], title = 'Net Resources', element_justification = 'center')
                            ]
                        ]),
                        sg.Column([[sg.Frame(layout = [[sg.Text("Combustion: {} mins".format(refine_speed[0]), relief = 'sunken'), sg.Text("Synthesis: {} mins".format(refine_speed[1]), relief = 'sunken')]], title = 'Cycle Times', element_justification = 'center')],[sg.Frame(layout = [[sg.Column(storage_left_col, element_justification = 'center'), sg.Column(storage_right_col, element_justification = 'center')]], title = 'Storage', element_justification = 'center'),
                        sg.Frame(layout = [[sg.Column(net_salts[0]), sg.Column(net_salts[1])]], element_justification = 'center', title = 'Net Salts', expand_x = True, expand_y = True)]])
                    ]]