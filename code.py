import os, shutil

cwdInput = input("Do you want to see the CWD? Y/N ")
if cwdInput == 'Y': 
    print(os.getcwd())
else:
    for folderName, subfolders, filenames in os.walk('./Test'):
        print('The current folder is ' + folderName + '\n')
        for subfolder in subfolders:
            shutil.copytree('./' + folderName + '/' + subfolder, './' + folderName, dirs_exist_ok=True)
            print ('')