import os
import sys

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