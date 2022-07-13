#####################################################
# ICM_printer.py                                 	#
# Code for implementing the 3D printer tab         	#
#####################################################
import PySimpleGUI as sg

import ICM_functions as icm_f

tab_1 = [[
            sg.Column([
                [
                    sg.Image(data = icm_f.generate_img('images/Materials/{}.png'.format(icm_f.dictionary['account']['printer']['samples'][5 * j  + i]['item']), (72,72), True), tooltip = '{}\n{} / hour'.format(icm_f.dictionary['account']['printer']['samples'][5 * j  + i]['item'], icm_f.dictionary['account']['printer']['samples'][5 * j  + i]['rate'])) for i in range(0, 5)
                ] for j in range (0, 6)
            ]),
            sg.Column([
                [
                    sg.Image(data = icm_f.generate_img('images/Materials/{}.png'.format(icm_f.dictionary['account']['printer']['printing'][2 * j + i]['item']), (72, 72), True), tooltip = '{}\n{} / hour'.format(icm_f.dictionary['account']['printer']['printing'][2 * j  + i]['item'], icm_f.dictionary['account']['printer']['printing'][2 * j  + i]['rate'])) for i in range (0,2)
                ] for j in range(0,6)
            ])
        ]]

tab_2 = [[
            sg.Column([
                [
                    sg.Image(data = icm_f.generate_img('images/Materials/{}.png'.format(icm_f.dictionary['account']['printer']['samples'][5 * j  + i]['item']), (72,72), True), tooltip = '{}\n{} / hour'.format(icm_f.dictionary['account']['printer']['samples'][5 * j  + i]['item'], icm_f.dictionary['account']['printer']['samples'][5 * j  + i]['rate'])) for i in range(0, 5)
                ] for j in range(6, 9)
            ]),
            sg.Column([
                [
                    sg.Image(data = icm_f.generate_img('images/Materials/{}.png'.format(icm_f.dictionary['account']['printer']['printing'][2 * j + i]['item']), (72, 72), True), tooltip = '{}\n{} / hour'.format(icm_f.dictionary['account']['printer']['printing'][2 * j  + i]['item'], icm_f.dictionary['account']['printer']['printing'][2 * j  + i]['rate'])) for i in range (0,2)
                ] for j in range(6,9)
            ])
        ]]

totals = []
for item in icm_f.dictionary['account']['printer']['printing']:
    found = False
    for counted in totals:
        if counted['item'] == item['item']:
            counted['rate'] += item['rate']
            found = True
    if not found:
        totals.append(item)

total_frame =     [
                    [
                        sg.Image(icm_f.generate_img('images/Materials/{}.png'.format(item['item']), (36, 36), True)),
                        sg.Text('{} / hour'.format(item['rate']), justification = 'center', relief = 'sunken')
                    ] for item in totals
                ]
printer_tab =       [[
                        sg.TabGroup([[
                            sg.Tab('I', tab_1),
                            sg.Tab('II', tab_2)
                        ]]),
                        sg.Frame(layout = [[sg.Column(total_frame, scrollable = True, vertical_scroll_only = True, expand_x = True, expand_y = True, element_justification = 'center')]], title = 'totals', expand_x = True, expand_y = True, element_justification = 'center')
                    ]]