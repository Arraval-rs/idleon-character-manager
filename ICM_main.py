#####################################################
# ICM_main.py                                       #
# Code for the event loop of the application        #
#####################################################
import os
import io
import json
import PySimpleGUI as sg

# ICM files
import ICM_functions as icm_f
import ICM_windows as icm_w
from ICM_characters import character_tab
from ICM_inventory import inventory_tab
from ICM_crafting import crafting_tab
from ICM_monsters import monsters_tab
from ICM_storage import storage_tab
from ICM_printer import printer_tab
from ICM_refinery import refinery_tab

root_tabs = [
                [
                    sg.Combo(
                        icm_f.character_list,
                        default_value = icm_f.character_list[0],
                        key = 'active_character',
                        enable_events = True,
                        readonly = True
                    ),
                    sg.Image(data = icm_f.generate_img('images/Classes/{}Icon.png'.format(icm_f.dictionary['characters'][0]['class']), (38, 36), False), key = 'class_icon')
                ],
                [
                sg.TabGroup(
                [[
                    sg.Tab('Character', character_tab),
                    sg.Tab('Inventory', inventory_tab),
                    sg.Tab('Monsters', monsters_tab),
                    sg.Tab('Crafting', crafting_tab),
                    sg.Tab('Storage', storage_tab),
                    sg.Tab('Printer', printer_tab),
                    sg.Tab('Refinery', refinery_tab)
                ]])
                ]
            ]

window = sg.Window("Idleon Character Manager", root_tabs)
window.Finalize()

# Draw images for equipment tabs
for i in range(0, 4):
    for j in range(0, 2):
        window['equipment{}'.format(2 * i + j)].draw_image(data = icm_f.generate_img('images/Equipment/{}.png'.format(icm_f.dictionary['characters'][0]['equipment'][2*i+j]['name']), (72, 72), True), location = (0, 72))
        window['tools{}'.format(2 * i + j)].draw_image(data = icm_f.generate_img('images/Tools/{}.png'.format(icm_f.dictionary['characters'][0]['tools'][2*i+j]['name']), (72, 72), True), location = (0, 72))
        window['food{}'.format(2 * i + j)].draw_image(data = icm_f.generate_img('images/Food/{}.png'.format(icm_f.dictionary['characters'][0]['food'][2*i+j]['name']), (72, 72), True), location = (0, 72))

# Draw images for inventory
for i in range(0, 4):
    for j in range(0, 4):
        window['inventory{}'.format(4 * i + j)].draw_image(data = icm_f.get_inventory_item(4 * i + j, icm_f.image_paths, 0), location = (0, 72))

# Draw images for storage
for i in range(0, 4):
    for j in range(0, 6):
        window['storage{}'.format(6 * i + j)].draw_image(data = icm_f.get_storage_item(6 * i + j, icm_f.image_paths), location = (0, 72))

# Get last storage page
for i in range(0, len(icm_f.dictionary['account']['chest'])):
    if icm_f.dictionary['account']['chest'][i]['item'] == 'LockedInvSpace':
        icm_f.last_storage_page = int(i/24 + 0.5)
        break

# Event loop
while True:
    event, values = window.read(timeout = 120)

    if event != "Exit" and event != sg.WIN_CLOSED:
        index = icm_f.character_list.index(values['active_character'])
        # Update gifs
        window['constructor_crow'].UpdateAnimation('images/Misc_WIP/Constructor Crow.gif', time_between_frames = 120)
        window['carpenter_cardinal'].UpdateAnimation('images/Misc_WIP/Carpenter Cardinal.gif', time_between_frames = 120)
    else:
        break

    # Update selected equipment
    if 'equipment' in event or 'tools' in event or 'food' in event:
        icm_f.update_selected_equipment(window, event[:len(event)-1], index, int(event[len(event)-1]))

    # Update selected inventory item
    if 'inventory' in event:
        icm_f.update_selected_inventory_item(window, int(event.replace('inventory', '')) + 16 * (int(window['current_inv'].get()) - 1), icm_f.image_paths, index)

    # Update selected storage item
    if 'storage' in event:
        icm_f.update_selected_storage_item(window, int(event.replace('storage', '')) + 24 * (int(window['current_stor'].get()) - 1), icm_f.image_paths)

    # Update inventory for Prev/Next tab
    if event in ('next_inv', 'prev_inv'):
        if event == 'next_inv' and window['current_inv'].get() != '4':
            window['current_inv'].update('{}'.format(int(window['current_inv'].get()) + 1))
        if event == 'prev_inv' and window['current_inv'].get() != '1':
            window['current_inv'].update('{}'.format(int(window['current_inv'].get()) - 1))
        for i in range(0, 4):
            for j in range(0, 4):
                window['inventory{}'.format(j + 4 * i)].draw_image(data = icm_f.get_inventory_item(4 * i + j + 16 * (int(window['current_inv'].get()) - 1), icm_f.image_paths, index), location = (0, 72))

    # Update storage for Prev/Next tab
    if event in ('next_stor', 'prev_stor'):
        if event == 'next_stor' and int(window['current_stor'].get()) < icm_f.last_storage_page:
            window['current_stor'].update('{}'.format(int(window['current_stor'].get()) + 1))
        if event == 'prev_stor' and window['current_stor'].get() != '1':
            window['current_stor'].update('{}'.format(int(window['current_stor'].get()) - 1))
        for i in range(0, 4):
            for j in range(0, 6):
                window['storage{}'.format(6 * i + j)].draw_image(data = icm_f.get_storage_item(6 * i + j + 24 * (int(window['current_stor'].get()) - 1), icm_f.image_paths), location = (0, 72))

    icm_w.update_crafting_widgets(window, event)
    icm_w.update_monster_widgets(window, event)
    icm_w.update_character_widgets(window, event, index)

    #if event != '__TIMEOUT__':
    #    print(event)

window.close()       