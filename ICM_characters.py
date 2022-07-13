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
    icm_f.talents['Journeyman']['Maestro'][str(i)] = icm_f.generate_img('images/Talents/Journeyman/Maestro/{}.png'.format(i), (56, 56), False)
for i in range(45, 60):
    icm_f.talents['Mage']['Shaman']['Bubonic Conjuror'][str(i)] = icm_f.generate_img('images/Talents/Mage/Shaman/Bubonic Conjuror/{}.png'.format(i), (56, 56), False)
    icm_f.talents['Mage']['Wizard']['Elemental Sorcerer'][str(i)] = icm_f.generate_img('images/Talents/Mage/Wizard/Elemental Sorcerer/{}.png'.format(i), (56, 56), False)
    icm_f.talents['Warrior']['Barbarian']['Blood Berserker'][str(i)] = icm_f.generate_img('images/Talents/Warrior/Barbarian/Blood Berserker/{}.png'.format(i), (56, 56), False)
    icm_f.talents['Warrior']['Squire']['Divine Knight'][str(i)] = icm_f.generate_img('images/Talents/Warrior/Squire/Divine Knight/{}.png'.format(i), (56, 56), False)
    icm_f.talents['Archer']['Bowman']['Siege Breaker'][str(i)] = icm_f.generate_img('images/Talents/Archer/Bowman/Siege Breaker/{}.png'.format(i), (56, 56), False)
    icm_f.talents['Archer']['Hunter']['Beast Master'][str(i)] = icm_f.generate_img('images/Talents/Archer/Hunter/Beast Master/{}.png'.format(i), (56, 56), False)
for i in range(0, 13):
    for j in range(0, 5):
            icm_f.talents['Star']['Tab{}'.format(str(j+1))][str(i)] = icm_f.generate_img('images/Talents/Star/Tab_{}/{}.png'.format(j+1, i), (56, 56), False)

# tabs
talents_1 =         [[sg.Column(
                    [
                        [sg.Image(data = icm_f.talents[str(5 * i + j)], key = 'talent_img{}'.format(str(5 * i + j))) for j in range(0, 5)],
                        [sg.Text('{}/100'.format(icm_f.dictionary['characters'][0]['talentLevels'][str(5 * i + j + 1)] if str(5 * i + j + 1) in icm_f.dictionary['characters'][0]['talentLevels'] else '0'), key = 'talent{}'.format(str(5 * i + j)), size = (7,1), justification = 'center', relief = 'sunken') for j in range(0, 5)],
                    ], element_justification = 'center')]for i in range(0, 2)]
(talents_1.append([sg.Column(
                    [
                        [sg.Image(data = icm_f.talents['Filler'] if icm_f.get_class_depth(icm_f.dictionary['characters'][0]['class']) < 1 else icm_f.get_class_path(icm_f.dictionary['characters'][0]['class'], 1)[str(10 + i)], key = 'talent_img{}'.format(str(10 + i))) for i in range(0, 5)],
                        [sg.Text('{}/100'.format(icm_f.dictionary['characters'][0]['talentLevels'][str(11 + i)] if str(11 + i) in icm_f.dictionary['characters'][0]['talentLevels'] and icm_f.get_base_class(icm_f.dictionary['characters'][0]['class']) != 'Beginner' else '0'), key = 'talent{}'.format(str(10 + i)), size = (7,1), justification = 'center', relief = 'sunken') for i in range(0, 5)]
                    ], element_justification = 'center')]))

talents_2 =         [[sg.Column(
                    [
                        [sg.Image(data = icm_f.talents['Filler'] if icm_f.get_class_depth(icm_f.dictionary['characters'][0]['class']) < 1 else icm_f.get_class_path(icm_f.dictionary['characters'][0]['class'], 1)[str(15 + 5 * i + j)], key = 'talent_img{}'.format(str(15 + 5 * i + j))) for j in range(0, 5)],
                        [sg.Text('{}/100'.format(icm_f.dictionary['characters'][0]['talentLevels'][str(15 + 5 * i + j)] if str(15 + 5 * i + j) in icm_f.dictionary['characters'][0]['talentLevels'] and icm_f.get_base_class(icm_f.dictionary['characters'][0]['class']) != 'Beginner' else '0'), key = 'talent{}'.format(str(15 + 5 * i + j)), size = (7,1), justification = 'center', relief = 'sunken') for j in range(0, 5)]
                    ], element_justification = 'center')]for i in range(0, 3)]

talents_3 =         [[sg.Column(
                    [
                        [sg.Image(data = icm_f.talents['Filler'] if icm_f.get_class_depth(icm_f.dictionary['characters'][0]['class']) < 2 else icm_f.get_class_path(icm_f.dictionary['characters'][0]['class'], 2)[str(30 + 5 * i + j)], key = 'talent_img{}'.format(str(30 + 5 * i + j))) for j in range(0, 5)],
                        [sg.Text('{}/100'.format(icm_f.dictionary['characters'][0]['talentLevels'][str(30 + 5 * i + j)] if str(30 + 5 * i + j) in icm_f.dictionary['characters'][0]['talentLevels'] and icm_f.get_base_class(icm_f.dictionary['characters'][0]['class']) != 'Beginner' else '0'), key = 'talent{}'.format(str(30 + 5 * i + j)), size = (7,1), justification = 'center', relief = 'sunken') for j in range(0, 5)]
                    ], element_justification = 'center')]for i in range(0, 3)]

talents_4 =         [[sg.Column(
                    [
                        [sg.Image(data = icm_f.talents['Filler'] if icm_f.get_class_depth(icm_f.dictionary['characters'][0]['class']) < 3 else icm_f.get_class_path(icm_f.dictionary['characters'][0]['class'], 3)[str(45 + 5 * i + j)], key = 'talent_img{}'.format(str(45 + 5 * i + j))) for j in range(0, 5)],
                        [sg.Text('{}/100'.format(icm_f.dictionary['characters'][0]['talentLevels'][str(45 + 5 * i + j)] if str(45 + 5 * i + j) in icm_f.dictionary['characters'][0]['talentLevels'] and icm_f.get_base_class(icm_f.dictionary['characters'][0]['class']) != 'Beginner' else '0'), key = 'talent{}'.format(str(45 + 5 * i + j)), size = (7,1), justification = 'center', relief = 'sunken') for j in range(0, 5)]
                    ], element_justification = 'center')]for i in range(0, 3)]

# Add clicking arrows to event loop
star_1 =            [[
                    sg.Column([
                        [sg.Image(data = icm_f.talents['Star']['Tab1'][str(j)], key = 'star_1_img{}'.format(str(j))) for j in range(0, 5)],
                        [sg.Text('{}/100'.format(icm_f.dictionary['characters'][0]['starTalentLevels'][j] if (j) < len(icm_f.dictionary['characters'][0]['starTalentLevels']) else '0'), key = 'star_talent{}'.format(str(j)), size = (7,1), justification = 'center', relief = 'sunken') for j in range(0, 5)],
                        [sg.Image(data = icm_f.talents['Star']['Tab1'][str(5 + j)], key = 'star_1_img{}'.format(str(5 + j))) for j in range(0, 5)],
                        [sg.Text('{}/100'.format(icm_f.dictionary['characters'][0]['starTalentLevels'][5 + j] if (5 + j) < len(icm_f.dictionary['characters'][0]['starTalentLevels']) else '0'), key = 'star_talent{}'.format(str(5 + j)), size = (7,1), justification = 'center', relief = 'sunken') for j in range(0, 5)],
                        [
                            sg.Image(data = icm_f.generate_img('Images/Talents/Star/LeftArrow.png', (56, 56), False), key = 'star_left', enable_events = True), 
                            sg.Image(data = icm_f.talents['Star']['Tab1'][str(10)], key = 'star_1_img10'), 
                            sg.Image(data = icm_f.talents['Star']['Tab1'][str(11)], key = 'star_1_img11'), 
                            sg.Image(data = icm_f.talents['Star']['Tab1'][str(12)], key = 'star_1_img12'), 
                            sg.Image(data = icm_f.generate_img('Images/Talents/Star/RightArrow.png', (56, 56), False), key = 'star_right', enable_events = True)
                        ],
                        [sg.Text('{}/100'.format(icm_f.dictionary['characters'][0]['starTalentLevels'][10 + j] if (10 + j) < len(icm_f.dictionary['characters'][0]['starTalentLevels']) else '0'), key = 'star_talent{}'.format(str(10 + j)), size = (7,1), justification = 'center', relief = 'sunken') for j in range(0, 3)]], element_justification = 'center')
                    ]]

star_2 =            [[
                    sg.Column([
                        [sg.Image(data = icm_f.talents['Star']['Tab2'][str(j)], key = 'star_2_img{}'.format(str(j))) for j in range(0, 5)],
                        [sg.Text('{}/100'.format(icm_f.dictionary['characters'][0]['starTalentLevels'][13 + j] if (13 + j) < len(icm_f.dictionary['characters'][0]['starTalentLevels']) else '0'), key = 'star_talent{}'.format(str(13 + j)), size = (7,1), justification = 'center', relief = 'sunken') for j in range(0, 5)],
                        [sg.Image(data = icm_f.talents['Star']['Tab2'][str(5 + j)], key = 'star_2_img{}'.format(str(5 + j))) for j in range(0, 5)],
                        [sg.Text('{}/100'.format(icm_f.dictionary['characters'][0]['starTalentLevels'][18 + j] if (18 + j) < len(icm_f.dictionary['characters'][0]['starTalentLevels']) else '0'), key = 'star_talent{}'.format(str(18 + j)), size = (7,1), justification = 'center', relief = 'sunken') for j in range(0, 5)],
                        [
                            sg.Image(data = icm_f.generate_img('Images/Talents/Star/LeftArrow.png', (56, 56), False), key = 'star_left', enable_events = True), 
                            sg.Image(data = icm_f.talents['Star']['Tab2'][str(10)], key = 'star_2_img10'), 
                            sg.Image(data = icm_f.talents['Star']['Tab2'][str(11)], key = 'star_2_img11'), 
                            sg.Image(data = icm_f.talents['Star']['Tab2'][str(12)], key = 'star_2_img12'), 
                            sg.Image(data = icm_f.generate_img('Images/Talents/Star/RightArrow.png', (56, 56), False), key = 'star_right', enable_events = True)
                        ],
                        [sg.Text('{}/100'.format(icm_f.dictionary['characters'][0]['starTalentLevels'][23 + j] if (23 + j) < len(icm_f.dictionary['characters'][0]['starTalentLevels']) else '0'), key = 'star_talent{}'.format(str(23 + j)), size = (7,1), justification = 'center', relief = 'sunken') for j in range(0, 3)]], element_justification = 'center')
                    ]]

star_3 =            [[
                    sg.Column([
                        [sg.Image(data = icm_f.talents['Star']['Tab3'][str(j)], key = 'star_3_img{}'.format(str(j))) for j in range(0, 5)],
                        [sg.Text('{}/100'.format(icm_f.dictionary['characters'][0]['starTalentLevels'][26 + j] if (26 + j) < len(icm_f.dictionary['characters'][0]['starTalentLevels']) else '0'), key = 'star_talent{}'.format(str(26 + j)), size = (7,1), justification = 'center', relief = 'sunken') for j in range(0, 5)],
                        [sg.Image(data = icm_f.talents['Star']['Tab3'][str(5 + j)], key = 'star_3_img{}'.format(str(5 + j))) for j in range(0, 5)],
                        [sg.Text('{}/100'.format(icm_f.dictionary['characters'][0]['starTalentLevels'][31 + j] if (31 + j) < len(icm_f.dictionary['characters'][0]['starTalentLevels']) else '0'), key = 'star_talent{}'.format(str(31 + j)), size = (7,1), justification = 'center', relief = 'sunken') for j in range(0, 5)],
                        [
                            sg.Image(data = icm_f.generate_img('Images/Talents/Star/LeftArrow.png', (56, 56), False), key = 'star_left', enable_events = True), 
                            sg.Image(data = icm_f.talents['Star']['Tab3'][str(10)], key = 'star_3_img10'), 
                            sg.Image(data = icm_f.talents['Star']['Tab3'][str(11)], key = 'star_3_img11'), 
                            sg.Image(data = icm_f.talents['Star']['Tab3'][str(12)], key = 'star_3_img12'), 
                            sg.Image(data = icm_f.generate_img('Images/Talents/Star/RightArrow.png', (56, 56), False), key = 'star_right', enable_events = True)
                        ],
                        [sg.Text('{}/100'.format(icm_f.dictionary['characters'][0]['starTalentLevels'][36 + j] if (36 + j) < len(icm_f.dictionary['characters'][0]['starTalentLevels']) else '0'), key = 'star_talent{}'.format(str(36 + j)), size = (7,1), justification = 'center', relief = 'sunken') for j in range(0, 3)]], element_justification = 'center')
                    ]]

star_4 =            [[
                    sg.Column([
                        [sg.Image(data = icm_f.talents['Star']['Tab4'][str(j)], key = 'star_4_img{}'.format(str(j))) for j in range(0, 5)],
                        [sg.Text('{}/100'.format(icm_f.dictionary['characters'][0]['starTalentLevels'][39 + j] if (39 + j) < len(icm_f.dictionary['characters'][0]['starTalentLevels']) else '0'), key = 'star_talent{}'.format(str(39 + j)), size = (7,1), justification = 'center', relief = 'sunken') for j in range(0, 5)],
                        [sg.Image(data = icm_f.talents['Star']['Tab4'][str(5 + j)], key = 'star_4_img{}'.format(str(5 + j))) for j in range(0, 5)],
                        [sg.Text('{}/100'.format(icm_f.dictionary['characters'][0]['starTalentLevels'][44 + j] if (44 + j) < len(icm_f.dictionary['characters'][0]['starTalentLevels']) else '0'), key = 'star_talent{}'.format(str(44 + j)), size = (7,1), justification = 'center', relief = 'sunken') for j in range(0, 5)],
                        [
                            sg.Image(data = icm_f.generate_img('Images/Talents/Star/LeftArrow.png', (56, 56), False), key = 'star_left', enable_events = True), 
                            sg.Image(data = icm_f.talents['Star']['Tab4'][str(10)], key = 'star_4_img10'), 
                            sg.Image(data = icm_f.talents['Star']['Tab4'][str(11)], key = 'star_4_img11'), 
                            sg.Image(data = icm_f.talents['Star']['Tab4'][str(12)], key = 'star_4_img12'), 
                            sg.Image(data = icm_f.generate_img('Images/Talents/Star/RightArrow.png', (56, 56), False), key = 'star_right', enable_events = True)
                        ],
                        [sg.Text('{}/100'.format(icm_f.dictionary['characters'][0]['starTalentLevels'][49 + j] if (49 + j) < len(icm_f.dictionary['characters'][0]['starTalentLevels']) else '0'), key = 'star_talent{}'.format(str(49 + j)), size = (7,1), justification = 'center', relief = 'sunken') for j in range(0, 3)]], element_justification = 'center')
                    ]]

star_5 =            [[
                    sg.Column([
                        [sg.Image(data = icm_f.talents['Star']['Tab5'][str(j)], key = 'star_5_img{}'.format(str(j))) for j in range(0, 5)],
                        [sg.Text('{}/100'.format(icm_f.dictionary['characters'][0]['starTalentLevels'][52 + j] if (52 + j) < len(icm_f.dictionary['characters'][0]['starTalentLevels']) else '0'), key = 'star_talent{}'.format(str(52 + j)), size = (7,1), justification = 'center', relief = 'sunken') for j in range(0, 5)],
                        [sg.Image(data = icm_f.talents['Star']['Tab5'][str(5 + j)], key = 'star_5_img{}'.format(str(5 + j))) for j in range(0, 5)],
                        [sg.Text('{}/100'.format(icm_f.dictionary['characters'][0]['starTalentLevels'][57 + j] if (57 + j) < len(icm_f.dictionary['characters'][0]['starTalentLevels']) else '0'), key = 'star_talent{}'.format(str(57 + j)), size = (7,1), justification = 'center', relief = 'sunken') for j in range(0, 5)],
                        [
                            sg.Image(data = icm_f.generate_img('Images/Talents/Star/LeftArrow.png', (56, 56), False), key = 'star_left', enable_events = True), 
                            sg.Image(data = icm_f.talents['Star']['Tab5'][str(10)], key = 'star_5_img10'), 
                            sg.Image(data = icm_f.talents['Star']['Tab5'][str(11)], key = 'star_5_img11'), 
                            sg.Image(data = icm_f.talents['Star']['Tab5'][str(12)], key = 'star_5_img12'), 
                            sg.Image(data = icm_f.generate_img('Images/Talents/Star/RightArrow.png', (56, 56), False), key = 'star_right', enable_events = True)
                        ],
                        [sg.Text('{}/100'.format(icm_f.dictionary['characters'][0]['starTalentLevels'][60 + j] if (60 + j) < len(icm_f.dictionary['characters'][0]['starTalentLevels']) else '0'), key = 'star_talent{}'.format(str(60 + j)), size = (7,1), justification = 'center', relief = 'sunken') for j in range(0, 3)]], element_justification = 'center')
                    ]]

star_talents =      [
                        [sg.TabGroup(
                        [[
                            sg.Tab('I', star_1, key = 'star_I'),
                            sg.Tab('II', star_2, key = 'star_II'),
                            sg.Tab('III', star_3, key = 'star_III'),
                            sg.Tab('IV', star_4, key = 'star_IV'),
                            sg.Tab('V', star_5, key = 'star_V')
                        ]], key = 'star_talents')]
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
                            sg.Tab('Talents 4', talents_4),
                            sg.Tab('Star Talents', star_talents),
                        ]])]
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
                                ]], title = 'None', key = 'equipped_item_frame'),
                                sg.Text('Action Bars')
                            ]])
                        ]
                    ]