# JSON functions
import json
import os

def first_write():
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
            continue
        paths = {
            "home": home_path,
            "documents": document_path,
            "pictures" : pictures_path
        }

        with open("settings.json","w") as fd:
            json.dump(paths, fd)
def reader():
    file_name = "settings.json"
    with open(file_name) as fd:
        paths = json.load(fd)
    return paths

