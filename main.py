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
    while True:
        # move termination condition warning to first prompt 
        sync_token = int(input("For Upload Only Enter '1'\nFor Download Only Enter '2'\nFor Complete Sync Enter '3'"))
        if (sync_token == 0):
            exit() 
        elif (sync_token == 1 or sync_token == 2 or sync_token == 3):
            break
        else:
            print("You have entered wrong number(for exit enter 0)")
    while True:
        which_to_sync = int(input("Enter:\n1:Documents\t2:Pictures\t3:home\t4:all"))
        if(which_to_sync == 0):
            exit()
        elif(which_to_sync == 1 or which_to_sync == 2 or which_to_sync == 3 or which_to_sync == 4):
            if(which_to_sync == 1):# wait to fix source-target paths
                sync.documents(sync_token,paths["documents"],)

        else:
            print('You have entered wrong number,(for exit enter 0)')
            continue
        print('Restarting sync engine, press 0 for exit when prompt asked')
