import os
import sys
import PySimpleGUI as sg

sys.path.append(os.getcwd())
from packages.config_parser import Config_Parser
from packages.find_versions import Find_Versions

sg.theme('DarkAmber')


#Load applications from config file
filePath = r"packages/applications.json"


cp = Config_Parser()
app_data = cp.parse_file(filePath)

layout = []
location = (10, 10)

for i in range(len(app_data)):
    path = app_data[i][1]
        
    fv = Find_Versions(path)
    versions = fv.return_versions(app_data[i][4])
    exe_paths = fv.return_exe_path(app_data[i][2])

    if len(versions) != len(exe_paths):
        print("Warning! : Your application count does not match your version count. {}".format(app_data[i][0]))
        print("Versions: {} ; Applications: {}".format(len(versions), len(exe_paths)))

    layout += [sg.Frame(app_data[i][0],[[
    sg.Listbox(values=([os.path.basename(version) for version in versions]), size=(30, 3))  #TODO - Dynamically update based on folder path
    ]]), sg.Button('Open'), sg.Button('Close')],
layout += [[sg.Button('Launch Apps'),sg.Button('Close Apps'), sg.Button('Exit')]]



app_titles = ['App 1', 'App 2', 'App 3']
app_versions = [['Ver 1', 'Ver 2', 'Ver 3', 'Ver 4'], ['Release 1', 'Release 2'], ['Ver 1', 'Ver 2', 'Ver 3', 'Ver 4']]
    

window = sg.Window('App Manager', layout, location = location)
event, values = window.read()
