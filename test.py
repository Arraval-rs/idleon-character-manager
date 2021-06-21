import PySimpleGUI as sg

skills_tab =        [
                        [sg.Text('Skills!')]
                    ]

talents_tab =       [
                        [sg.Text('Talents!')]
                    ]

bags_tab =          [
                        [sg.Text('Bags!')]
                    ]

pouches_tab =       [
                        [sg.Text('Pouches!')]
                    ]

equips_tab =        [
                        [sg.Text('Equipment!')]
                    ]

tools_tab =         [
                        [sg.Text('Tools!')]
                    ]

foods_tab =         [
                        [sg.Text('Food!')]
                    ]

characters_tab =    [
                        [
                        sg.Text('Character 1\nLv. X'),
                        sg.Text('Class\nImage'),
                        sg.Text('Class Name'),
                        sg.TabGroup([[
                                        sg.Tab('Equips', equips_tab),
                                        sg.Tab('Tools', tools_tab),
                                        sg.Tab('Food', foods_tab)
                                    ]])],
                        [
                        sg.Text("Blah Blah Stats and Shit"),
                        sg.TabGroup([[
                                        sg.Tab('Skills', skills_tab),
                                        sg.Tab('Talents', talents_tab),
                                        sg.Tab('Bags', bags_tab),
                                        sg.Tab('Pouches', pouches_tab)
                                    ]])
                        ]
                    ]

inventory_tab =     [
                        []
                    ]

monsters_tab =      [
                        []
                    ]

crafting_tab =      [
                        []
                    ]

storage_tab =       [
                        []
                    ]
root_tabs = [
                [
                sg.TabGroup([[
                                sg.Tab('Characters', characters_tab),
                                sg.Tab('Inventory', inventory_tab),
                                sg.Tab('Monsters', monsters_tab),
                                sg.Tab('Crafting', crafting_tab),
                                sg.Tab('Storage', storage_tab)
                            ]])
                ]
            ]

window = sg.Window("Idleon Character Manager", root_tabs)
event, values = window.read()
window.close()       