import os
import easygui as eg
import tkinter.messagebox
import subprocess
import time
import json

settings = open('settings.txt', 'w')
settings.writelines(['readme', 'settings'])

campos = ['Project Name', 'Project Path', 'Media Folder']

default = ['',r'D:\TOBI-PC\Descargas\3-VIDEO PROJECTS',r'F:\VIDEO MEDIA\OBS VIDEOS']

# Creates a window with multiple input boxes
box = eg.multenterbox(msg='Enter the proj name and path:',title='Premiere Pro Project Creator',fields=campos, values=default)

if not box == None:
    print(box)
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
                print(line)
                line = line.replace(replace_this, project_name) # replace the line containing the and with the new line, you can change to what you want. 
                print(line)
            lines.append(line)


    #write to a new file
    with open(proj_dir +'/'+ project_name + '.prproj' , mode='w', encoding='utf8') as new_f:
        new_f.writelines(lines)

    time.sleep(0.5)

    # open the media folders
    subprocess.Popen(f'explorer "{box[2]}"')
    os.startfile(proj_dir +'/'+ project_name + '.prproj' )
