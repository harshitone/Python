# Ask user for a filename and copy it to a backup folder.

import shutil
import os

usrInput = input("Please enter the file name: ")

backup_folder = "backup"

os.makedirs(backup_folder, exist_ok=True )

if os.path.isfile(usrInput):
    shutil.copy(usrInput, backup_folder)
    print(f"{usrInput} file is successfuly backup in {backup_folder} folder.")

else:
    print("File does not exist")