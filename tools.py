# JSON functions
import json
import os

def initialize():
    #NOTE check for directory existence
    while True:
        document_source_path = input('Enter your documents folder path at your computer: ')
        if(os.path.isdir(document_source_path) == False):
            print('The path you entered is not available')
            continue
        pictures_source_path = input('Enter your pictures folder path at your computer: ')
        if(os.path.isdir(pictures_source_path) == False):
            print('The path you entered is not available')
            continue
        home_source_path = input('Enter your home folder path at your computer')
        if(os.path.isdir(home_source_path) == False):
            print('The path you entered is not available')
            continue# add target paths too

        # target paths
        document_target_path = input('Enter your documents folder path you want to upload: ')
        if(os.path.isdir(document_target_path) == False):
            print('The path you entered is not available')
            continue
        pictures_target_path = input('Enter your pictures folder path you want to upload: ')
        if(os.path.isdir(pictures_target_path) == False):
            print('The path you entered is not available')
            continue
        home_target_path = input('Enter your home folder path you want to upload: ')
        if(os.path.isdir(home_target_path) == False):
            print('The path you entered is not available')
            continue
        paths = {
            "home_source"     : home_source_path,
            "documents_source": document_source_path,
            "pictures_source" : pictures_source_path,
            "home_target"     : home_target_path,
            "documents_target": document_target_path,
            "pictures_target" : pictures_target_path
        }

        with open("settings.json","w") as fd:
            json.dump(paths, fd)
        return paths
def reader():
    file_name = "settings.json"
    with open(file_name) as fd:
        paths = json.load(fd)
    return paths
def dir_scanner():
    # This function scans main directory for settings.json file
    # It return 0 if file exists, 1 if does not exist
    # I altered code from this post: https://stackoverflow.com/a/37560251
    file_name = "settings.json"
    cur_dir = os.getcwd()
    while True:
        file_list = os.listdir(cur_dir)
        parent_dir = os.path.dirname(cur_dir)
        if file_name in file_list:
            return 0
        else:
            if cur_dir == parent_dir:
                return 1
            else:
                cur_dir = parent_dir
