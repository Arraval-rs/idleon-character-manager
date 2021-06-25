#####################################################
# ICM_crafting.py                                 	#
# Code for implementing the crafting tab          	#
#####################################################
import PySimpleGUI as sg

import ICM_functions as icm_f

crafting_tab =      [
                        [sg.Image(data = icm_f.generate_img('images/Misc_WIP/Constructor Crow.gif', (38, 62), False), key = 'constructor_crow'), sg.Text('Under Construction')]
                    ]