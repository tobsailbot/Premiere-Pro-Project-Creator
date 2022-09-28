import os
import easygui as eg
import subprocess
import time
import json
import pathlib


print(pathlib.Path().resolve())
curr_dir = str(pathlib.Path().resolve())

# Data to be written
dictionary = {  "project_path": "",
                "media_folder": ""  }
 
# Serializing json
json_object = json.dumps(dictionary, indent=4)


# Opening JSON file
try:
    with open(curr_dir + '/' + 'settings.json', 'r') as readfile:
        settings_file = json.load(readfile)
except:
    with open(curr_dir + "/" + "settings.json", "w") as outfile:
        outfile.write(json_object)
    with open(curr_dir + '/' + 'settings.json', 'r') as readfile:
        settings_file = json.load(readfile)

 
campos = ['Project Name', 'Project Path', 'Media Folder']

default = ['', settings_file["project_path"], settings_file["media_folder"]]

# Creates a window with multiple input boxes
box = eg.multenterbox(msg='Enter the proj name and path:',title='Premiere Pro Project Creator',fields=campos, values=default)

if not box == None:
    dictionary = {  "project_path": box[1],
                    "media_folder": box[2]  }

    json_object = json.dumps(dictionary, indent=4)

    with open(curr_dir + '/' + "settings.json", "w") as outfile:
        outfile.write(json_object)   

    # pasar string del nombre del proj como interfaz UI
    project_name = box[0]

    proj_dir = box[1] + f'\\{project_name}'
    replace_this = "proyecto_prueba"
    lines = []
    
    # Crea nueva carpeta
    os.makedirs(proj_dir)

    #open file template
    with open(r'project_template.xml', mode='r',encoding='utf8') as f:
        for line in f.readlines(): # iterate thru the lines
            if replace_this in line: # check if is in ans in line
                line = line.replace(replace_this, project_name) # replace the line containing the and with the new line, you can change to what you want. 
            lines.append(line)


    #write to a new file
    with open(proj_dir +'/'+ project_name + '.prproj' , mode='w', encoding='utf8') as new_f:
        new_f.writelines(lines)

    # open the project if Premiere pro is available
    time.sleep(0.5)
    os.startfile(proj_dir +'/'+ project_name + '.prproj' )

    # open the media folders
    time.sleep(0.5)
    subprocess.Popen(f'explorer "{box[2]}"')

