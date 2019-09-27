# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

#import lesson5_normal_lib.py as lesson5_normal_lib

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

def process_user_choice(choise):
    if choise == 1:
        lesson5_normal_lib.change_dir(input('Введите целевую директорию:'))
    elif choise == 2:
        lesson5_normal_lib.list_dir(os.getcwd())
    elif choise == 3:
        index = input('Ведите индекс')
        count = input('Ведите количество')
        lesson5_normal_lib.multiple_dirs(index, count)
    elif choise == 4:
        index = input('Ведите индекс')
        count = input('Ведите количество')
        lesson5_normal_lib.multiple_rem_dirs(index, count)


def menu():
     while True:
                try:
                    choice = int(input('Выберите пункт:\n'
                                        '1. Перейти в папку\n'
                                        '2. Просмотреть содержимое текущей папки\n'
                                        '3. Создать папку\n'
                                        '4. Удалить папку\n'
                                        '5. Выход\n'
                                        '---------------------\n'
                                        'Ваш выбор:'))
                except ValueError:
                    print('Неверный ввод!')
                    continue

                if choice == 5:
                    break
                    process_user_choice(choise)

menu()