import os, os.path

def change_dir(directory):
    os.chdir(directory)
    return directory

def list_dir(directory):
    dir_list = []
    all_list = os.listdir(directory)
    for elem in all_list:
        if os.path.isdir(elem):
            dir_list.append(elem)

    return dir_list

def multiple_dirs(dir_index,i):
    di = str(dir_index)
    for k in range(1,i):
         os.mkdir(di + str(k))

def multiple_rem_dirs(dir_index,i):
    di = str(dir_index)
    for k in range(1, i):
        os.rmdir(di + str(k))