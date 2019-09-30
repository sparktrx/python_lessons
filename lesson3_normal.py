

employees_list = ['Ilya', 'Vasiliy', 'Pavel']
salary_list = [300000, 100000, 600000]
salary_dict = dict(zip(employees_list, salary_list))

file = open('salary.txt', 'w')
for key, value in salary_dict.items():
    if value < 500000:
        file.write('{} - {} \n'.format(key, value))
    # else:
    #     file.write('{} - {} \n'.format(key, value))
file.close()

# file = open('salary.txt', 'r', encoding='utf-8')
# for line in file:
#     employee, salary = file.readline().strip().split(' - ')
#     print (employee, int(salary)*0.87)


