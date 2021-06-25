#####################################################
# ICM_monsters.py                                 	#
# Code for implementing the monsters tab          	#
#####################################################
import PySimpleGUI as sg

import ICM_functions as icm_f

monsters_tab =      [
                        [sg.Image(data = icm_f.generate_img('images/Misc_WIP/Builder Bird.gif', (40, 58), False), key = 'builder_bird'), sg.Text('Under Construction')]
                    ]