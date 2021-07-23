import os
import tools
import sync

def main():
    #NOTE I have to check if settings.json exists
    # Until that, I presume from here that if 
    # file doesn't exists, first_try will be True
    first_try = True
    if(first_try == True):
        paths = tools.initialize()
    else:
        paths = tools.reader()
    
    sync_token = int(input("For Upload Only Enter '1'\nFor Download Only Enter '2'\nFor Complete Sync Enter '3'"))
    if (sync_token == 1):
        sync.documents
    elif (sync_token == 2):
        pass
    elif (sync_token == 3):
        pass
    else:
        print('You have entered wrong number aborting...')