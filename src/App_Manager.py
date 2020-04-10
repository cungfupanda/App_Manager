import os
import sys
import PySimpleGUI as sg

sys.path.append(os.getcwd())
from packages.config_parser import Config_Parser

sg.theme('DarkAmber')


#Load applications from config file
filePath = r"packages/applications.json"

cp = Config_Parser()
app_data = cp.parse_file(filePath)
print("Length: {} ".format(len(app_data)))
print(app_data[1][0])


app_titles = ['App 1', 'App 2', 'App 3']
app_versions = [['Ver 1', 'Ver 2', 'Ver 3', 'Ver 4'], ['Release 1', 'Release 2'], ['Ver 1', 'Ver 2', 'Ver 3', 'Ver 4']]

for i in range(len(app_data)):
    print(app_data[i][0])
    #[print(version) for version in app_versions[i]]

    #[print(app_versions[i]) for j in app_versions[i]]
layout = []
location = (10, 10)

for i in range(len(app_data)):
    layout += [sg.Frame(app_data[i][0],[[
    sg.Listbox(values=([version for version in app_versions[i]]), size=(30, 3))  #TODO - Dynamically update based on folder path
    ]]), sg.Button('Open'), sg.Button('Close')],
layout += [[sg.Button('Launch Apps'),sg.Button('Close Apps'), sg.Button('Exit')]]


window = sg.Window('App Manager', layout, location = location)
event, values = window.read()
