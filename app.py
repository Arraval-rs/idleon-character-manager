import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import json

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
	character_menu.add_command(label = "{name}, Lv. {level}".format(name = dictionary['characters'][index]['name'], level = dictionary['characters'][index]['level']))
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


# Must be the last line
root.config(menu = menubar)
root.mainloop()