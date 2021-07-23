# sync module is for syncing functions
def documents_(bus_letter, stream):
    source = "C:\\Users\\{}\\OneDrive\\Documents".format(_userName) #NOTE define path without Onedrive then modularize it
    # to sync documents, mapped to user\documents
    # if else structure to find upload download
    source = 'C:\\Users\\spaceSpaghetty\\Documents'
    target = "{}:\\Documents".format(bus_letter)
    if(stream == 0):
        # upload
        print('Uploading...')
        sync(source,target,'sync')
        print('Upload complete ')
    elif(stream == 1):# download
        print('Downloading...')
        sync(target, source,'sync')
        print('Download Complete')
    else:# complete sync
        print('Syncing...')    # to sync pictures, mapped to user\pictures
        sync(target, source,'sync')
        sync(source, target,'sync')
        print('Syncing Complete')
def pictures(bus_letter,stream):
    source = "C:\\Users\\{}\\OneDrive\\Pictures".format(_userName)
    target = "{}:\\Pictures".format(bus_letter)
    if(stream == 0):
        # upload
        print('Uploading...')
        sync(source,target,'sync')
        print('Upload complete ')
    elif(stream == 1):# download
        print('Downloading...')
        sync(target, source,'sync')
        print('Download Complete')
    else:# complete sync
        print('Syncing...')    # to sync pictures, mapped to user\pictures
        sync(target, source,'sync')
        sync(source, target,'sync')
        print('Syncing Complete')
    # to sync a main folder which is like main drive path, Onedrive or google drive root.
    # it also includes a seperate documents folder, a pictures f
def home(bus_letter,stream):
    pass