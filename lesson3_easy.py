# def func1(name, age, city):
#     result1 = '{}, {} год(а), проживает в городе {}'.format(name, age, city)
#     return result1
#
# result = func1('Ilya', '32', 'Moscow')
# print (result)

# def func2 (int1, int2, int3):
#     return max (int1, int2, int3)
#
# result = func2 (4, 5, 6)
# print (result)

# def func3 ( *args ) :
#     print(args)
#     list_a = list(args)
#     result = (max(list_a, key=len))
#     return result
#
# result = func3('asdasd', 'erwer', 'sdfsdwerg')
#
# print(result)

x = ['asdasd', 'asdasdasd', 'asdasdasdasda']
print( max(x, key = len))