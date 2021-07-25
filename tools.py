# JSON functions
import json
import os

def initialize():
    #NOTE check for directory existence
    while True:
        document_path = input('Enter your documents folder path: ')
        if(os.path.isdir(document_path) == False):
            print('The path you entered is not available')
            continue
        pictures_path = input('Enter your pictures folder path: ')
        if(os.path.isdir(pictures_path) == False):
            print('The path you entered is not available')
            continue
        home_path = input('Enter your home folder path')
        if(os.path.isdir(home_path) == False):
            print('The path you entered is not available')
            continue# add target paths too
        paths = {
            "home": home_path,
            "documents": document_path,
            "pictures" : pictures_path
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
