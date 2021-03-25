import os
import sys
from itertools import chain

def list_files(startpath):
    with open(startpath+"index.md","w") as tree:
        tree.write("<h1 align=\"center\" style=\"font-size:60px\">Contents</h1>\n\n")
        for root, dirs, files in os.walk(startpath):
            level = root.replace(startpath, '').count(os.sep)
            indent = ' ' * 4 * (level)
            if os.path.basename(root) not in ['', 'scripts']:
                tree.write('{}* [{}](/{})\n'.format(indent, os.path.basename(root).capitalize(), os.path.join(os.path.basename(root),'index')))
            else:
                continue

            subindent = ' ' * 4 * (level + 1)
            for f in files:
                #print(os.path.basename(root))
                #print('`{}`'.format(os.path.basename(root)))
                if f[0] != '.' and f not in ['', 'index.md'] and os.path.basename(root) not in ['scripts']:
                    tree.write('{}* [{}](/{})\n'.format(subindent, f.split('.')[0].capitalize(), os.path.join(os.path.basename(root),f.split('.')[0])))

list_files("./content/")

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
