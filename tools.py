# JSON functions
import json
import os

def initialize():
    #NOTE check for directory existence
    while True:
        document_source_path = input('Enter your documents folder path at your computer:\t')
        if(os.path.isdir(document_source_path) == False):
            print('The path you entered is not available')
            continue
        pictures_source_path = input('Enter your pictures folder path at your computer:\t')
        if(os.path.isdir(pictures_source_path) == False):
            print('The path you entered is not available')
            continue
        home_source_path = input('Enter your home folder path at your computer:\t')
        if(os.path.isdir(home_source_path) == False):
            print('The path you entered is not available')
            continue# add target paths too

        # target paths
        document_target_path = input('Enter your documents folder path you want to upload:\t')
        if(os.path.isdir(document_target_path) == False):
            print('The path you entered is not available')
            continue
        pictures_target_path = input('Enter your pictures folder path you want to upload:\t')
        if(os.path.isdir(pictures_target_path) == False):
            print('The path you entered is not available')
            continue
        home_target_path = input('Enter your home folder path you want to upload:\t')
        if(os.path.isdir(home_target_path) == False):
            print('The path you entered is not available')
            continue
        one_click_sync =int(input('Do you wish one click sync feature?\nIf you enter 1, when you double click drive.py everything will be synced else press 0: \t'))
        if (one_click_sync != 1 or one_click_sync != 0):
            print('You entered wrong number, using one click sync feature')
            one_click_sync = True
        else:
            if one_click_sync == 1:
                one_click_sync == True
            else:
                one_click_sync = False
        paths = {
            "home_source"     : home_source_path,
            "documents_source": document_source_path,
            "pictures_source" : pictures_source_path,
            "home_target"     : home_target_path,
            "documents_target": document_target_path,
            "pictures_target" : pictures_target_path,
            "one_click_sync"  : one_click_sync
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
    # It returns True if file exists, False if does not exist
    # I altered code from this post: https://stackoverflow.com/a/37560251
    file_name = "settings.json"
    cur_dir = os.getcwd()
    while True:
        file_list = os.listdir(cur_dir)
        parent_dir = os.path.dirname(cur_dir)
        if file_name in file_list:
            return True
        else:
            if cur_dir == parent_dir:
                return False
            else:
                cur_dir = parent_dir
