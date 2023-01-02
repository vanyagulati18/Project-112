import os
import shutil
from_dir="C:/Users/Dell/Downloads"
to_dir="C:/Users/Dell/Desktop"
list_of_files=os.listdir(from_dir)
print(list_of_files)
for x in list_of_files:

    name, extension = os.path.splitext(x)
    print(name)
    print(extension)
    if extension == '':
        continue
    if extension in ['.txt', '.doc', '.docx', '.pdf']:

        path1 = from_dir + '/' + x                            
        path2 = to_dir + '/' + "Document_Files"                         
        path3 = to_dir + '/' + "Document_Files" + '/'+  x
        print("path1 " , path1)
        print("path2 " , path2)
        print("path3 ", path3)

        if os.path.exists(path2):
            print("Moving" + x + '....')

            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Moving" + x + '....')
            shutil.move(path1,path3)
