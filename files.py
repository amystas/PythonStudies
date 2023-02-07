import os

# checking if file exits
path1 = "/Users/amy/Desktop/iran.key"
path2 = "/Users/amy/Desktop/kalendarz"
if os.path.exists(path2):
    print('Location exits')
    if os.path.isfile(path2):
        print('That is a file')
    elif os.path.isdir(path2):
        print('That is a directory')
else:
    print('Location not found')

# reading a file
path = "file.txt"
try:
    with open(path) as file:
        print(file.read())
except FileNotFoundError:
    print('File not found')
except Exception:
    print('Something went wrong')

# writing files
text = "Have a nice day\n"
with open(path, 'a') as file:  # modes: r = read, w = write, a = append
    file.write(text)

# coping files
# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)
import shutil
shutil.copyfile('file.txt', 'copy.txt')  # source , destination

# moving files (and directories)
# import os
source = "move.txt"
destination = "/Users/amy/Desktop/move.txt"
try:
    if os.path.exists(destination):
        print('such file exists')
    else:
        os.replace(source, destination)
        print('moved')
except FileNotFoundError:
    print(source + ' was not found')

# deleting files
# import os
# import shutil
try:
    os.remove('toRemove.txt')  # delete a file
    os.rmdir('empty')  # delete an empty directory
    shutil.rmtree('folder')  # delete a directory containing files
except FileNotFoundError:
    print('file not found')
except PermissionError:
    print('permission denied')
except OSError:
    print('cannot delete using that function')

#modules
# module = file containing python code. May contain functions, classes, etc.
# used with modular programming, which is to separate a program into parts

import messages as msg
# from messages import *
# from messages import hello , bye
msg.hello()
msg.bye()
# help('modules')




