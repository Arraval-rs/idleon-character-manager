#####################################################
# ICM_storage.py                                 	#
# Code for implementing the storage tab          	#
#####################################################
import PySimpleGUI as sg

import ICM_functions as icm_f

storage_tab =       [[
                        sg.Frame(layout = 
                        [
                            [sg.Column([[sg.Image(data = icm_f.generate_img('images/Empty Slot.png', (72, 72), False), enable_events = True, key = 'storage{}'.format(6 * i + j)) for j in range(0, 6)] for i in range(0, 4)])],
                            [sg.Button('Prev', key = 'prev_stor'), sg.Text('1', key = 'current_stor', relief = 'sunken', size = (3, 1), justification = 'center'), sg.Button('Next', key = 'next_stor')],
                            [sg.Frame(layout = [[sg.Image(data = icm_f.generate_img('images/Locked.png', (72, 72), False), key = 'selected_storage_item'), sg.Text('Stack Size: 0', size = (20, 1), key = 'storage_item_stats')]], title = 'None', key = 'storage_item_frame')]
                        ], title = 'Inventory', element_justification = 'center'),
                        sg.Image(data = icm_f.generate_img('images/Misc_WIP/Constructor Crow.gif', (38, 66), False), key = 'constructor_crow'), sg.Text('More to come')
                    ]]