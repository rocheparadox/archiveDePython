import os

dictionary = {} # tree alike which directory structure has to be created!
base_path = ''

def create_directories(dictionary,base_path):
    directories = dictionary.keys()
    for directory in directories:
        abs_path = base_path + '/' + directory
        print(abs_path)
        os.mkdir(abs_path)
        create_directories(dictionary[directory],abs_path)

create_directories(dictionary,base_path)