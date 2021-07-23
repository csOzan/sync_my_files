from dirsync import sync

# globals
_userName = "spaceSpaghetty"

# add a sync interface
letter = str(input("Enter Drive Path:"))
source_path = "C:\\Users\\spaceSpaghetty\\OneDrive\\Desktop\\testfolder1"
target_path = "{}:\\test".format(letter) 
# upload or download branching
upload = input('Upload:0\nDownload:1\n')
if(upload == '0'): #BUG upload noes not work
# finded the bug, i was comparing string and integer before
    print("Uploaded: ")
    sync(source_path, target_path,'sync')
else:
    print("Downloaded: ")
    sync(target_path,source_path,'sync')

# IDEA: create a first time initalization. And save it to a txt (maybe a json or something). It will be used as saving paths, home documents and pictures
# modularize below

# NOTE
# it syncs folders and other scheninigans too. So it's OK 