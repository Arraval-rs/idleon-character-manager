#####################################################
# ICM_inventory.py                                  #
# Code for implementing the inventory tab           #
#####################################################
import PySimpleGUI as sg

import ICM_functions as icm_f

inventory_tab =     [[
                        sg.Frame(layout = 
                        [
                            [sg.Column([[sg.Graph((72, 72), (0, 0), (72, 72), change_submits = True, key = 'inventory{}'.format(4 * i + j)) for j in range(0, 4)] for i in range(0, 4)])],
                            [sg.Button('Prev', key = 'prev_inv'), sg.Text('1', key = 'current_inv', relief = 'sunken', size = (3, 1), justification = 'center'), sg.Button('Next', key = 'next_inv')],
                            [sg.Frame(layout = [[sg.Image(data = icm_f.generate_img('images/Empty Slot.png', (72, 72), False), key = 'selected_inventory_item'), sg.Text('Stack Size: 0', size = (20, 1), key = 'inventory_item_stats')]], title = 'None', key = 'inventory_item_frame')]
                        ], title = 'Inventory', element_justification = 'center'),
                        sg.Image(data = icm_f.generate_img('images/Misc_WIP/Carpenter Cardinal.gif', (38, 66), False), key = 'carpenter_cardinal'), sg.Text('More to come ($$shmoney$$ and account items)')
                    ]]