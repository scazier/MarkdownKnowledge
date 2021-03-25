import os
import sys
from itertools import chain

baseDir = './content/'

def sub_create_summary(startpath, f, depth, indent):
    if depth == 0:
        path = startpath.split('/')
        name = path[-1] if path[-1] != '' else path[-2]
        f.write("<h1 align=\"center\" style=\"font-size:60px\">"+name.capitalize()+"</h1>\n\n")
   
    elts = os.listdir(startpath)
    if elts != []:
        for elt in elts:
            filepath = startpath+elt
            if os.path.isfile(startpath+elt):
                if filepath.find('index') == -1 and elt[0] != '.':
                    f.write('{}* [{}]({})\n'.format(indent*4*' ', elt.replace('.md','').capitalize(), filepath.replace(baseDir, '').replace('.md','')))
            else:
                if elt not in ['scripts']:
                    filepath = filepath + '/index'
                    f.write('{}* [{}]({})\n'.format(indent*4*' ', elt.capitalize(), filepath.replace(baseDir, '')))
                    sub_test_summary(startpath+elt+'/', f, depth+1, indent+1)
    else:
        return

def create_summary(startpath):
    with open(startpath+"index.md","w") as tree:
        sub_test_summary(startpath, tree, 0, 0)

def list_directories(startpath):
    dirs = [x[0].replace('./content/','') for x in os.walk(startpath)]
    for i in range(len(dirs)-1):
        if dirs[i] in ['.','..', '']:
            dirs.remove(dirs[i])
        
    return dirs

def list_files(startpath):
    files = list(chain.from_iterable([x[2] for x in os.walk(startpath)]))
    for i in range(len(files)-1):
        if files[i][0] == '.':
            files.remove(files[i])
        
        files[i] = files[i].split('.')[0]

    return files
