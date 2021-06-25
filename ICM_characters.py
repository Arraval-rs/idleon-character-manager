#####################################################
# ICM_characters.py                                 #
# Code for implementing the characters tab          #
#####################################################
import PySimpleGUI as sg

import ICM_functions as icm_f


icm_f.talents['Filler'] = icm_f.generate_img('images/Filler.png', (56, 56), False)
for i in range(0, 10):
    icm_f.talents[str(i)] = icm_f.generate_img('images/Talents/{}.png'.format(i), (56, 56), False)
for i in range(10, 30):
    icm_f.talents['Mage'][str(i)] = icm_f.generate_img('images/Talents/Mage/{}.png'.format(i), (56, 56), False)
    icm_f.talents['Warrior'][str(i)] = icm_f.generate_img('images/Talents/Warrior/{}.png'.format(i), (56, 56), False)
    icm_f.talents['Archer'][str(i)] = icm_f.generate_img('images/Talents/Archer/{}.png'.format(i), (56, 56), False)
    icm_f.talents['Journeyman'][str(i)] = icm_f.generate_img('images/Talents/Journeyman/{}.png'.format(i), (56, 56), False)
for i in range(30, 45):
    icm_f.talents['Mage']['Shaman'][str(i)] = icm_f.generate_img('images/Talents/Mage/Shaman/{}.png'.format(i), (56, 56), False)
    icm_f.talents['Mage']['Wizard'][str(i)] = icm_f.generate_img('images/Talents/Mage/Wizard/{}.png'.format(i), (56, 56), False)
    icm_f.talents['Warrior']['Barbarian'][str(i)] = icm_f.generate_img('images/Talents/Warrior/Barbarian/{}.png'.format(i), (56, 56), False)
    icm_f.talents['Warrior']['Squire'][str(i)] = icm_f.generate_img('images/Talents/Warrior/Squire/{}.png'.format(i), (56, 56), False)
    icm_f.talents['Archer']['Bowman'][str(i)] = icm_f.generate_img('images/Talents/Archer/Bowman/{}.png'.format(i), (56, 56), False)
    icm_f.talents['Archer']['Hunter'][str(i)] = icm_f.generate_img('images/Talents/Archer/Hunter/{}.png'.format(i), (56, 56), False)

# tabs
talents_1 =         [[sg.Column(
                    [
                        [sg.Image(data = icm_f.talents[str(5 * i + j)], key = 'talent_img{}'.format(str(5 * i + j))) for j in range(0, 5)],
                        [sg.Text('{}/100'.format(icm_f.dictionary['characters'][0]['talentLevels'][str(5 * i + j)] if str(5 * i + j) in icm_f.dictionary['characters'][0]['talentLevels'] else '0'), key = 'talent{}'.format(str(5 * i + j)), size = (7,1), justification = 'center', relief = 'sunken') for j in range(0, 5)],
                    ], element_justification = 'center')]for i in range(0, 2)]
(talents_1.append([sg.Column(
                    [
                        [sg.Image(data = icm_f.talents['Filler'] if icm_f.get_base_class(icm_f.dictionary['characters'][0]['class']) == 'Beginner' else icm_f.talents[icm_f.get_base_class(icm_f.dictionary['characters'][0]['class'])][str(10 + i)], key = 'talent_img{}'.format(str(10 + i))) for i in range(0, 5)],
                        [sg.Text('{}/100'.format(icm_f.dictionary['characters'][0]['talentLevels'][str(10 + i)] if str(10 + i) in icm_f.dictionary['characters'][0]['talentLevels'] and icm_f.get_base_class(icm_f.dictionary['characters'][0]['class']) != 'Beginner' else '0'), key = 'talent{}'.format(str(10 + i)), size = (7,1), justification = 'center', relief = 'sunken') for i in range(0, 5)]
                    ], element_justification = 'center')]))

talents_2 =         [[sg.Column(
                    [
                        [sg.Image(data = icm_f.talents['Filler'] if icm_f.get_base_class(icm_f.dictionary['characters'][0]['class']) == 'Beginner' else icm_f.talents[icm_f.get_base_class(icm_f.dictionary['characters'][0]['class'])][str(15 + 5 * i + j)], key = 'talent_img{}'.format(str(15 + 5 * i + j))) for j in range(0, 5)],
                        [sg.Text('{}/100'.format(icm_f.dictionary['characters'][0]['talentLevels'][str(15 + 5 * i + j)] if str(15 + 5 * i + j) in icm_f.dictionary['characters'][0]['talentLevels'] and icm_f.get_base_class(icm_f.dictionary['characters'][0]['class']) != 'Beginner' else '0'), key = 'talent{}'.format(str(15 + 5 * i + j)), size = (7,1), justification = 'center', relief = 'sunken') for j in range(0, 5)]
                    ], element_justification = 'center')]for i in range(0, 3)]

talents_3 =         [[sg.Column(
                    [
                        [sg.Image(data = icm_f.talents['Filler'] if icm_f.is_base_class(icm_f.dictionary['characters'][0]['class']) else icm_f.talents[icm_f.get_base_class(icm_f.dictionary['characters'][0]['class'])][icm_f.dictionary['characters'][0]['class']][str(30 + 5 * i + j)], key = 'talent_img{}'.format(str(30 + 5 * i + j))) for j in range(0, 5)],
                        [sg.Text('{}/100'.format(icm_f.dictionary['characters'][0]['talentLevels'][str(30 + 5 * i + j)] if str(30 + 5 * i + j) in icm_f.dictionary['characters'][0]['talentLevels'] and icm_f.get_base_class(icm_f.dictionary['characters'][0]['class']) != 'Beginner' else '0'), key = 'talent{}'.format(str(30 + 5 * i + j)), size = (7,1), justification = 'center', relief = 'sunken') for j in range(0, 5)]
                    ], element_justification = 'center')]for i in range(0, 3)]


star_talents =      [
                        [sg.Image(data = icm_f.generate_img('images/Misc_WIP/Meel.gif', (124, 120), False), key = 'meel'), sg.Text('Get spooped lol')]
                    ]



skills_tab =        [
                        [sg.Column([[sg.Image(data = icm_f.generate_img('images/Skills/{}.png'.format(icm_f.skill_names[3*j+i]), (38, 36), False)), sg.Text('{}\nLv. {}'.format(icm_f.skill_names[3*j+i], icm_f.dictionary['characters'][0]['skillLevels'][icm_f.skill_names[3*j+i].lower()]), key = '{}level'.format(icm_f.skill_names[3*j+i]), size = (9, 2), relief = 'sunken')] for i in range(0, 3)])for j in range(0, 3)]
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
                        [sg.Graph((72, 72), (0, 0), (72, 72), change_submits = True, key = 'equipment{}'.format(2*i+j)) for j in range(0, 2)] for i in range(0, 4)
                    ]


tools_tab =         [
                        [sg.Graph((72, 72), (0, 0), (72, 72), change_submits = True, key = 'tools{}'.format(2*i+j)) for j in range(0, 2)] for i in range(0, 4)
                    ]


foods_tab =         [
                        [sg.Graph((72, 72), (0, 0), (72, 72), change_submits = True, key = 'food{}'.format(2*i+j)) for j in range(0, 2)] for i in range(0, 4)
                    ]


character_tab =    [
                        [
                            sg.Column(
                            [[
                                sg.Column(
                                [[
                                    sg.Column(
                                    [
                                        [sg.Column([[sg.Image(data = icm_f.generate_img('images/Classes/{}.png'.format(icm_f.dictionary['characters'][0]['class']), (129, 110), False), key = 'class_image')]], element_justification = 'center')],
                                        [sg.Text(icm_f.get_character_stats(0, icm_f.dictionary), key = 'character_stats')]
                                    ]),sg
                                        .TabGroup(
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
                                        sg.Tab('Equips', equips_tab, key = 'equips_tab'),
                                        sg.Tab('Tools', tools_tab),
                                        sg.Tab('Food', foods_tab)
                                    ]])
                                ]])
                            ],
                            [
                                sg.Frame(layout = 
                                [[
                                    sg.Image(data = icm_f.generate_img('images/Empty Slot.png', (72, 72), False), key = 'selected_equipment'),
                                    sg.Text('STR: 0\t\tReach: 0\nAGI: 0\t\tDefence: 0\nWIS: 0\t\tWeapon Power: 0\nLUK: 0\t\tUpgrade Slots Left: 0', key = 'equipped_item_stats')
                                ]], title = 'None', key = 'equipped_item_frame')
                            ]])
                        ]
                    ]