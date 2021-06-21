import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import json

# global variables
active_character = 0
active_item = 0

# Classes for cleaning up various data


# Dictionary
json_file = open("idleon_data.json", "rt")
json_text = json_file.read()
dictionary = json.loads(json_text)

# Parent Window
root = tk.Tk()
root.title("Idleon Character Manager")

# Menubar
menubar = Menu(root)
file_menu = Menu(menubar, tearoff = 0)
file_menu.add_command(label = "Import")
character_menu = Menu(menubar, tearoff = 0)
index = 0
while index < len(dictionary['characters']):
	character_menu.add_command(label = "{name}, Lv. {level}".format(name = \
		dictionary['characters'][index]['name'], level = dictionary['characters'][index]['level']))
	index = index + 1
menubar.add_cascade(label = "File", menu = file_menu)
menubar.add_cascade(label = "Select Character", menu = character_menu)

# Tabs
tab_controls = ttk.Notebook(root)
character_tab = ttk.Frame(tab_controls)
inventory_tab = ttk.Frame(tab_controls)
monster_tab = ttk.Frame(tab_controls)
crafting_tab = ttk.Frame(tab_controls)
storage_tab = ttk.Frame(tab_controls)
tab_controls.add(character_tab, text = 'Characters')
tab_controls.add(inventory_tab, text = 'Inventory')
tab_controls.add(monster_tab, text = 'Monsters')
tab_controls.add(crafting_tab, text = 'Crafting')
tab_controls.add(storage_tab, text = 'Storage')
tab_controls.pack(expand = 1, fill = "both")

# Character Tab
character_title = ttk.Frame(character_tab).grid(column = 0, row = 0, columnspan = 3)
character_title_name_level = ttk.Label(character_title, text = \
	'{name}\nLv. {level}\n{class_name}'.format(name = dictionary['characters'][active_character]['name'], \
	level = dictionary['characters'][active_character]['level'], \
	class_name = dictionary['characters'][active_character]["class"])).pack()

character_stats = ttk.Frame(character_tab).grid(column = 1, row = 0, rowspan = 2)
character_stats_info = ttk.Label(character_stats, \
	text = 'STR: {strength}\nAGI: {agility}\nWIS: {wisdom}\nLUK: {luck}'.format( \
		strength = dictionary['characters'][active_character]['strength'], \
		agility = dictionary['characters'][active_character]['agility'], \
		wisdom = dictionary['characters'][active_character]['wisdom'], \
		luck = dictionary['characters'][active_character]['luck'])).pack()
selected_equipment = ttk.Frame(character_tab).grid(column = 0, row = 3, columnspan = 3)

character_talents = ttk.Notebook(character_tab)
character_talents.grid(column = 1, row = 1, columnspan = 2, rowspan = 2)
skills_tab = ttk.Frame(character_talents)
talents_tab = ttk.Notebook(character_talents)
talents_1 = ttk.Frame(talents_tab)
talents_2 = ttk.Frame(talents_tab)
talents_3 = ttk.Frame(talents_tab)
star_talents = ttk.Frame(talents_tab)
talents_tab.add(talents_1, text = 'Tab1.img')
talents_tab.add(talents_2, text = 'Tab2.img')
talents_tab.add(talents_3, text = 'Tab3.img')
talents_tab.add(star_talents, text = 'Star.img')
talents_tab.pack()
bags_tab = ttk.Frame(character_talents)
pouches_tab = ttk.Frame(character_talents)
character_talents.add(skills_tab, text = 'Skills')
character_talents.add(talents_tab, text = 'Talents')
character_talents.add(bags_tab, text = 'Bags')
character_talents.add(pouches_tab, text = 'Pouches')

character_equipment = ttk.Notebook(character_tab)
equips_tab = ttk.Frame(character_equipment)
tools_tab = ttk.Frame(character_equipment)
foods_tab = ttk.Frame(character_equipment)
character_equipment.add(equips_tab, text = 'Equips')
character_equipment.add(tools_tab, text = 'Tools')
character_equipment.add(foods_tab, text = 'Foods')
character_equipment.grid(column = 3, row = 0, columnspan = 4, rowspan = 2)

helmet_img = PhotoImage(file="images/Helmets/{item}.png".format(item = dictionary['characters'][active_character]['equipment'][0]['name']))
helmet_slot = ttk.Label(equips_tab, image = helmet_img).grid(column = 0, row = 0)
shirt_img = PhotoImage(file="images/Shirts/{item}.png".format(item = dictionary['characters'][active_character]['equipment'][2]['name']))
shirt_slot = ttk.Label(equips_tab, image = shirt_img).grid(column = 0, row = 1)
pant_img = PhotoImage(file="images/Pants/{item}.png".format(item = dictionary['characters'][active_character]['equipment'][4]['name']))
pants_slot = ttk.Label(equips_tab, image = pant_img).grid(column = 0, row = 2)
shoe_img = PhotoImage(file="images/Shoes/{item}.png".format(item = dictionary['characters'][active_character]['equipment'][6]['name']))
shoes_slot = ttk.Label(equips_tab, image = shoe_img).grid(column = 0, row = 3)
weapon_img = PhotoImage(file="images/Weapons/{item}.png".format(item = dictionary['characters'][active_character]['equipment'][1]['name']))
weapon_slot = ttk.Label(equips_tab, image = weapon_img).grid(column = 1, row = 0)
pendant_img = PhotoImage(file="images/Pendants/{item}.png".format(item = dictionary['characters'][active_character]['equipment'][3]['name']))
pendant_slot = ttk.Label(equips_tab, image = pendant_img).grid(column = 1, row = 1)
ring_1_img = PhotoImage(file="images/Rings/{item}.png".format(item = dictionary['characters'][active_character]['equipment'][5]['name']))
ring_1_slot = ttk.Label(equips_tab, image = ring_1_img).grid(column = 1, row = 2)
ring_2_img = PhotoImage(file="images/Rings/{item}.png".format(item = dictionary['characters'][active_character]['equipment'][7]['name']))
ring_2_slot = ttk.Label(equips_tab, image = ring_2_img).grid(column = 1, row = 3)

# Must be the last line
root.config(menu = menubar)
root.mainloop()