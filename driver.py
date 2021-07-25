import os
import tools
import sync

def main():

    settings_exist = tools.dir_scanner()
    if(settings_exist == True):
        paths = tools.reader()
    else:
        paths = tools.initialize()
    while True:
        # move termination condition warning to first prompt 
        sync_token = int(input("For Upload Only Enter '1'\nFor Download Only Enter '2'\nFor Complete Sync Enter '3'\nEnter '0'for quit the app"))
        if (sync_token == 0):
            exit() 
        elif (sync_token == 1 or sync_token == 2 or sync_token == 3):
            break
        else:
            print("You have entered wrong number(for exit enter 0)")
    while True:
        which_to_sync = int(input("Enter:\n0:exit the app\n1:Documents\t2:Pictures\t3:home\t4:all"))
        if(which_to_sync == 0):
            exit()
        elif(which_to_sync == 1 or which_to_sync == 2 or which_to_sync == 3 or which_to_sync == 4 or which_to_sync == 0):
            if(which_to_sync == 1):# wait to fix source-target paths
                sync.documents(sync_token,paths["documents_source"],paths["documents_target"])
            elif(which_to_sync == 2):
                sync.pictures(sync_token,paths["pictures_source"],paths["pictures_target"])
            elif(which_to_sync == 3):
                sync.home(sync_token,paths["home_source"],paths["home_target"])
            elif(which_to_sync == 4):
                sync.home(sync_token,paths["home_source"],paths["home_target"])
                sync.pictures(sync_token,paths["pictures_source"],paths["pictures_target"])
                sync.documents(sync_token,paths["documents_source"],paths["documents_target"])
            else:
                exit()
        else:
            print('You have entered wrong number,(for exit enter 0)')
            continue
        print('Restarting sync engine, press 0 for exit when prompt asked')
main()
