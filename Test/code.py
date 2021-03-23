import os, shutil

for folderName, subfolders, fileName in os.walk(os.getcwd()):
    print('The current folder is ' + folderName + '\n')
    for subfolder in subfolders:
        #print (subfolder)
        shutil.copytree('./' + subfolder, folderName, dirs_exist_ok=True)
        print ('')