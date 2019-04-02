import os

dir_to_make = 'build/zoho/sdplive_automation/webhost/SDPLIVE_AUTOMATION_STANDALONE_BRANCH/Mar_18_2019_1'
base_dir='/home/local/ZOHOCORP/roche-6660/localHostBase'

present_directory = base_dir
directories = dir_to_make.split('/')

for directory in directories:
    present_directory = present_directory + '/' + directory
    os.mkdir(present_directory)
    print(present_directory)