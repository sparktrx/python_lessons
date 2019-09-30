# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

# input_list = [1, 2, 4, 0]
# number_list = [x ** 2 for x in input_list]
# print(number_list)

# input_list_1 = ['apple', 'pineapple', 'peach', 'banana', 'persimmon']
# input_list_2 = ['apple', 'pear', 'peach', 'banana', 'persimmon']
# result_list = [fruit_1 for fruit_1 in input_list_1 for fruit_2 in input_list_2 if fruit_1 == fruit_2]
# print (result_list)

# input_list = [9, -9, 12, 4, 8, 21]
# result_list = [x for x in input_list if x > 0 and x % 3 == 0 and x % 4 != 0]
# print (result_list)