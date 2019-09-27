# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# import os
# di = ('dir_')
# for i in range(1,10):
#     os.mkdir(di+str(i))
#
# print(os.listdir())
#
# for i in range(1,10):
#     os.rmdir(di+str(i))
#
# print(os.listdir())

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import  os.path

list_dir = os.listdir()
for elem in list_dir:
    if os.path.isdir(elem):
        print(elem)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

# import sys, os, shutil
#
# shutil.copyfile(sys.argv[0], sys.argv[0]+'_copy')
# print(os.listdir())