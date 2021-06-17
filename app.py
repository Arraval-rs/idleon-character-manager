from tkinter import *
from tkinter import ttk
import json

json_file = open("idleon_data.json", "rt")
json_text = json_file.read()

dictionary = json.loads(json_text)

window = tk.Tk()

window.mainloop()