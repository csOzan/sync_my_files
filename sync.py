from dirsync import sync
# sync module is for syncing functions
def documents(sync_token, source,target):
    if(sync_token == 1):
        print('Uploading new files to drive...')
        sync(source,target,'sync')
        print('Upload complete ')
    elif(sync_token == 2):
        print('Downloading missing files from drive...')
        sync(target, source,'sync')
        print('Download Complete')
    else:
        print('Syncing Documents...')
        sync(target, source,'sync')
        sync(source, target,'sync')
        print('Syncing Complete')
def pictures(sync_token, source, target):
    if(sync_token == 1):
        print('Uploading new files to drive...')
        sync(source,target,'sync')
        print('Upload complete ')
    elif(sync_token == 2):
        print('Downloading missing files from drive...')
        sync(target, source,'sync')
        print('Download Complete')
    else:
        print('Syncing Pictures...')
        sync(target, source,'sync')
        sync(source, target,'sync')
        print('Syncing Complete')
def home(sync_token, source, target):
    if(sync_token == 1):
        print('Uploading new files to drive...')
        sync(source,target,'sync')
        print('Upload complete ')
    elif(sync_token == 2):
        print('Downloading missing files from drive...')
        sync(target, source,'sync')
        print('Download Complete')
    else:
        print('Syncing home directory...')
        sync(target, source,'sync')
        sync(source, target,'sync')
        print('Syncing Complete')