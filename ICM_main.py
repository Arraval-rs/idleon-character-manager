import os
import io
import json
import PySimpleGUI as sg

# ICM files
import ICM_functions as icm_f
from ICM_characters import character_tab
# from ICM_inventory import inventory_tab
# from ICM_crafting import crafting_tab
# from ICM_monsters import monsters_tab
# from ICM_storage import storage_tab

# Functions
def get_item_stats(equip_type, character, index):
    if equip_type in {'equipment', 'tools'}:
        stat_str = 'STR: {}'.format(icm_f.dictionary['characters'][character][equip_type][index]['stoneData']['STR'])
        stat_str += '\t\tReach: {}'.format(icm_f.dictionary['characters'][character][equip_type][index]['stoneData']['Reach'] if 'Reach' in icm_f.dictionary['characters'][character][equip_type][index]['stoneData'] else '0')
        stat_str += '\nAGI: {}'.format(icm_f.dictionary['characters'][character][equip_type][index]['stoneData']['AGI'])
        stat_str += '\t\tDefence: {}'.format(icm_f.dictionary_read(icm_f.dictionary, ['characters', character, equip_type, index, 'stoneData', 'Defence']))
        stat_str += '\nWIS: {}'.format(icm_f.dictionary['characters'][character][equip_type][index]['stoneData']['WIS'])
        stat_str += '\t\tWeapon Power: {}'.format(icm_f.dictionary['characters'][character][equip_type][index]['stoneData']['Weapon_Power'] if 'Weapon Power' in icm_f.dictionary['characters'][character][equip_type][index]['stoneData'] else '0')
        stat_str += '\nLUK: {}'.format(icm_f.dictionary['characters'][character][equip_type][index]['stoneData']['LUK'])
        stat_str += '\t\tUpgrade Slots Left: {}'.format(icm_f.dictionary['characters'][character][equip_type][index]['stoneData']['Upgrade_Slots_Left'] if equip_type == 'equipment' else 0)
    else:
        stat_str = 'Stack Size: {}'.format(icm_f.dictionary['characters'][character][equip_type][index]['count'])
    return stat_str

def update_selected_equipment(equip_type, character, item):
    window['selected_equipment'].update(data = icm_f.generate_img('images/{}/{}.png'.format(equip_type, icm_f.dictionary['characters'][index][equip_type][item]['name']), (72, 72), True))
    window['equipped_item_stats'].update(get_item_stats(equip_type, character, item))
    window['equipped_item_frame'].update(value = icm_f.dictionary['characters'][character][equip_type][item]['name'])
    return

def update_selected_inventory_item(slot, paths, character):
    window['selected_inventory_item'].update(data = get_inventory_item(slot, paths, character))
    window['inventory_item_stats'].update('Stack Size: {}'.format(icm_f.dictionary['characters'][character]['inventory'][slot]['count']))
    window['inventory_item_frame'].update(value = icm_f.dictionary['characters'][character]['inventory'][slot]['name'])
    return

def update_selected_storage_item(slot, paths):
    window['selected_storage_item'].update(data = get_storage_item(slot, paths))
    window['storage_item_stats'].update('Stack Size: {}'.format(icm_f.dictionary_read(icm_f.dictionary, ['account', 'chest', slot, 'count'])))
    window['storage_item_frame'].update(value = icm_f.dictionary_read(icm_f.dictionary, ['account', 'chest', slot, 'item']))
    return

def get_inventory_item(i, paths, character):
    if 'name' not in icm_f.dictionary['characters'][character]['inventory'][i]:
        return icm_f.generate_img('images/Locked.png', (72, 72), False)
    if icm_f.dictionary['characters'][character]['inventory'][i]['name'] == 'None':
        return icm_f.generate_img('None', (72, 72), False)
    for p in paths:
        path = 'images/{}/{}.png'.format(p, icm_f.dictionary['characters'][character]['inventory'][i]['name'])
        if os.path.exists(path):
            return icm_f.generate_img(path, (72, 72), True)
    return icm_f.generate_img('images/Missing.png', (72, 72), True)

def get_storage_item(i, paths):
    if 'item' not in icm_f.dictionary['account']['chest'][i]:
        return icm_f.generate_img('images/Locked.png', (72, 72), False)
    if icm_f.dictionary['account']['chest'][i]['item'] == 'None':
        return icm_f.generate_img('None', (72, 72), False)
    for p in paths:
        path = 'images/{}/{}.png'.format(p, icm_f.dictionary['account']['chest'][i]['item'])
        if os.path.exists(path):
            return icm_f.generate_img(path, (72, 72), True)
    return icm_f.generate_img('images/Missing.png', (72, 72), True)

inventory_tab =     [[
                        sg.Frame(layout = 
                        [
                            [sg.Column([[sg.Graph((72, 72), (0, 0), (72, 72), change_submits = True, key = 'inventory{}'.format(4 * i + j)) for j in range(0, 4)] for i in range(0, 4)])],
                            [sg.Button('Prev', key = 'prev_inv'), sg.Text('1', key = 'current_inv', relief = 'sunken', size = (3, 1), justification = 'center'), sg.Button('Next', key = 'next_inv')],
                            [sg.Frame(layout = [[sg.Image(data = icm_f.generate_img('images/Empty Slot.png', (72, 72), False), key = 'selected_inventory_item'), sg.Text('Stack Size: 0', size = (20, 1), key = 'inventory_item_stats')]], title = 'None', key = 'inventory_item_frame')]
                        ], title = 'Inventory', element_justification = 'center'),
                        sg.Image(data = icm_f.generate_img('images/Misc_WIP/Carpenter Cardinal.gif', (38, 66), False), key = 'carpenter_cardinal'), sg.Text('More to come')
                    ]]


monsters_tab =      [
                        [sg.Image(data = icm_f.generate_img('images/Misc_WIP/Builder Bird.gif', (40, 58), False), key = 'builder_bird'), sg.Text('Under Construction')]
                    ]


crafting_tab =      [
                        [sg.Image(data = icm_f.generate_img('images/Misc_WIP/Constructor Crow.gif', (38, 62), False), key = 'constructor_crow'), sg.Text('Under Construction')]
                    ]


storage_tab =       [[
                        sg.Frame(layout = 
                        [
                            [sg.Column([[sg.Graph((72, 72), (0, 0), (72, 72), change_submits = True, key = 'storage{}'.format(6 * i + j)) for j in range(0, 6)] for i in range(0, 4)])],
                            [sg.Button('Prev', key = 'prev_stor'), sg.Text('1', key = 'current_stor', relief = 'sunken', size = (3, 1), justification = 'center'), sg.Button('Next', key = 'next_stor')],
                            [sg.Frame(layout = [[sg.Image(data = icm_f.generate_img('images/Locked.png', (72, 72), False), key = 'selected_storage_item'), sg.Text('Stack Size: 0', size = (20, 1), key = 'storage_item_stats')]], title = 'None', key = 'storage_item_frame')]
                        ], title = 'Inventory', element_justification = 'center'),
                        sg.Image(data = icm_f.generate_img('images/Misc_WIP/Carpenter Cardinal.gif', (38, 66), False), key = 'carpenter_cardinal1'), sg.Text('More to come')
                    ]]


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
        window['inventory{}'.format(4 * i + j)].draw_image(data = get_inventory_item(4 * i + j, icm_f.image_paths, 0), location = (0, 72))

# Draw images for storage
for i in range(0, 4):
    for j in range(0, 6):
        window['storage{}'.format(6 * i + j)].draw_image(data = get_storage_item(6 * i + j, icm_f.image_paths), location = (0, 72))

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
        window['carpenter_cardinal1'].UpdateAnimation('images/Misc_WIP/Carpenter Cardinal.gif', time_between_frames = 100)
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
                window['inventory{}'.format(j + 4 * i)].draw_image(data = get_inventory_item(j + 4 * i + 16 * (int(window['current_inv'].get()) - 1), icm_f.image_paths, index), location = (0, 72))

    # Update selected equipment
    if 'equipment' in event or 'tools' in event or 'food' in event:
        update_selected_equipment(event[:len(event)-1], index, int(event[len(event)-1]))

    # Update selected inventory item
    if 'inventory' in event:
        update_selected_inventory_item(int(event.replace('inventory', '')) + 16 * (int(window['current_inv'].get()) - 1), icm_f.image_paths, index)

    # Update selected storage item
    if 'storage' in event:
        update_selected_storage_item(int(event.replace('storage', '')) + 24 * (int(window['current_stor'].get()) - 1), icm_f.image_paths)


    # Update inventory for Prev/Next tab
    if event in ('next_inv', 'prev_inv'):
        if event == 'next_inv' and window['current_inv'].get() != '4':
            window['current_inv'].update('{}'.format(int(window['current_inv'].get()) + 1))
        if event == 'prev_inv' and window['current_inv'].get() != '1':
            window['current_inv'].update('{}'.format(int(window['current_inv'].get()) - 1))
        for i in range(0, 4):
            for j in range(0, 4):
                window['inventory{}'.format(j + 4 * i)].draw_image(data = get_inventory_item(4 * i + j + 16 * (int(window['current_inv'].get()) - 1), icm_f.image_paths, index), location = (0, 72))

    # Update storage for Prev/Next tab
    if event in ('next_stor', 'prev_stor'):
        if event == 'next_stor' and window['current_stor'].get() != '10':
            window['current_stor'].update('{}'.format(int(window['current_stor'].get()) + 1))
        if event == 'prev_stor' and window['current_stor'].get() != '1':
            window['current_stor'].update('{}'.format(int(window['current_stor'].get()) - 1))
        for i in range(0, 4):
            for j in range(0, 6):
                window['storage{}'.format(6 * i + j)].draw_image(data = get_storage_item(6 * i + j + 24 * (int(window['current_stor'].get()) - 1), icm_f.image_paths), location = (0, 72))

window.close()       