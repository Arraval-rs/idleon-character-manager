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

root_tabs = [
                [
                    sg.Combo(
                        icm_f.character_list,
                        default_value = icm_f.character_list[0],
                        key = 'active_character',
                        enable_events = True
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
                    sg.Tab('Storage', storage_tab)
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

# Event loop
while True:
    event, values = window.read(timeout = 100)

    if event != "Exit" and event != sg.WIN_CLOSED:
        index = icm_f.character_list.index(values['active_character'])
        # Update WIP gifs
        window['meel'].UpdateAnimation('images/Misc_WIP/Meel.gif', time_between_frames = 100)
        window['builder_bird'].UpdateAnimation('images/Misc_WIP/Builder Bird.gif', time_between_frames = 100)
        window['constructor_crow'].UpdateAnimation('images/Misc_WIP/Constructor Crow.gif', time_between_frames = 100)
        window['carpenter_cardinal'].UpdateAnimation('images/Misc_WIP/Carpenter Cardinal.gif', time_between_frames = 100)
    else:
        break
    if event == 'active_character':
        character_class = icm_f.dictionary['characters'][index]['class']
        character_base_class = icm_f.get_base_class(character_class)

        # Update standalone character elements
        window['class_icon'].update(data = icm_f.generate_img('images/Classes/{}Icon.png'.format(icm_f.dictionary['characters'][index]['class']), (38, 36), False))
        window['class_image'].update(data = icm_f.generate_img('images/Classes/{}.png'.format(icm_f.dictionary['characters'][index]['class']), (129, 110), False))
        window['character_stats'].update(icm_f.get_character_stats(index, icm_f.dictionary))
        window['selected_equipment'].update(data = icm_f.generate_img('images/Empty Slot.png', (72, 72), False))
        window['equipped_item_stats'].update('STR: 0\t\tReach: 0\nAGI: 0\t\tDefence: 0\nWIS: 0\t\tWeapon Power: 0\nLUK: 0\t\tUpgrade Slots Left: 0')
        window['equipped_item_frame'].update(value = 'None')
        window['selected_inventory_item'].update(data = icm_f.generate_img('images/Empty Slot.png', (72, 72), False))
        window['inventory_item_stats'].update('Stack Size: 0')
        window['inventory_item_frame'].update('None')

        # Update equipment
        for i in range(0, 4):
            for j in range(0, 2):
                window['equipment{}'.format(2 * i + j)].draw_image(data = icm_f.generate_img('images/Equipment/{}.png'.format(icm_f.dictionary['characters'][index]['equipment'][2*i+j]['name']), (72, 72), True), location = (0, 72))
                window['tools{}'.format(2 * i + j)].draw_image(data = icm_f.generate_img('images/Tools/{}.png'.format(icm_f.dictionary['characters'][index]['tools'][2*i+j]['name']), (72, 72), True), location = (0, 72))
                window['food{}'.format(2 * i + j)].draw_image(data = icm_f.generate_img('images/Food/{}.png'.format(icm_f.dictionary['characters'][index]['food'][2*i+j]['name']), (72, 72), True), location = (0, 72))
    
        # Update skills
        for i in range(0, 9):
            window['{}level'.format(icm_f.skill_names[i])].update('{}\nLv. {}'.format(icm_f.skill_names[i], icm_f.dictionary['characters'][index]['skillLevels'][icm_f.skill_names[i].lower()]))

        # Update icm_f.talents tab 1
        for i in range(0, 10):
            if str(i) in icm_f.dictionary['characters'][index]['talentLevels'].keys() and character_base_class != 'Beginner': # some icm_f.talents aren't in JSON
                window['talent{}'.format(i)].update('{}/100'.format(icm_f.dictionary['characters'][index]['talentLevels'][str(i)]))
            else:
                window['talent{}'.format(i)].update('0/100')
        
        # Update icm_f.talents tab 2
        for i in range(10, 30):
            window['talent_img{}'.format(i)].update(data = icm_f.talents['Filler'] if character_base_class == 'Beginner' else icm_f.talents[character_base_class][str(i)])
            if str(i) in icm_f.dictionary['characters'][index]['talentLevels'].keys()  and character_base_class != 'Beginner': # some icm_f.talents aren't in JSON
                window['talent{}'.format(i)].update('{}/100'.format(icm_f.dictionary['characters'][index]['talentLevels'][str(i)]))
            else:
                window['talent{}'.format(i)].update('0/100')
        
        # Update icm_f.talents tab 3
        for i in range(30, 45):
            window['talent_img{}'.format(i)].update(data = icm_f.talents['Filler'] if icm_f.is_base_class(character_class) else icm_f.talents[character_base_class][character_class][str(i)])
            if str(i) in icm_f.dictionary['characters'][index]['talentLevels'].keys() and not icm_f.is_base_class(character_class): # some icm_f.talents aren't in JSON
                window['talent{}'.format(i)].update('{}/100'.format(icm_f.dictionary['characters'][index]['talentLevels'][str(i)]))
            else:
                window['talent{}'.format(i)].update('0/100')

        # Update inventory for new character
        window['current_inv'].update('1')
        for i in range(0, 4):
            for j in range(0, 4):
                window['inventory{}'.format(j + 4 * i)].draw_image(data = icm_f.get_inventory_item(j + 4 * i + 16 * (int(window['current_inv'].get()) - 1), icm_f.image_paths, index), location = (0, 72))

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
        if event == 'next_stor' and window['current_stor'].get() != '10':
            window['current_stor'].update('{}'.format(int(window['current_stor'].get()) + 1))
        if event == 'prev_stor' and window['current_stor'].get() != '1':
            window['current_stor'].update('{}'.format(int(window['current_stor'].get()) - 1))
        for i in range(0, 4):
            for j in range(0, 6):
                window['storage{}'.format(6 * i + j)].draw_image(data = icm_f.get_storage_item(6 * i + j + 24 * (int(window['current_stor'].get()) - 1), icm_f.image_paths), location = (0, 72))

    icm_w.update_crafting_widgets(window, event)

        # print(icm_f.total_ingredients)
#    if event != '__TIMEOUT__':
#        print(event)

window.close()       