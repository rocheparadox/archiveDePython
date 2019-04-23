import os
import sys

def get_tree(path):
    tree={}
    dir_files = os.listdir(path)

    for dir_file in dir_files:
        abs_path = path + "/" + dir_file

        if os.path.isdir(abs_path):
            #print(abs_path)
            tree[dir_file] = get_tree(abs_path)
    return tree

path = os.getcwd()
if len(sys.argv) > 1:
    path = sys.argv[1]

path = '/home/local/ZOHOCORP/roche-6660/Documents/automater_python/test_sheets'
tree = get_tree(path)
print(tree)