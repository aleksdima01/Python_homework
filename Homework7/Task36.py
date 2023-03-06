# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию,
# вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция,
# у которой ровно два аргумента, как, например, у операции умножения.
# *Пример:*
# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

def print_operation_table(operation, num_rows, num_columns):
       print(operation(num_rows,num_columns)) 
       

def production(a,b):
    my_list = [] 
    for i in range(1,a+1): 
        my_list.append(list(map(int, ((i*(b-b+j)) for j in range(1,b+1)))))
    return print('\n'.join('\t'.join(map(str, row)) for row in my_list))


def sum(a,b):
    my_list = [] 
    for i in range(1,a+1): 
        my_list.append(list(map(int, ((i+(b-b+j)) for j in range(1,b+1)))))
    return print('\n'.join('\t'.join(map(str, row)) for row in my_list))


def difference(a,b):
    my_list = [] 
    for i in range(1,a+1): 
        my_list.append(list(map(int, ((i-(b-b+j)) for j in range(1,b+1)))))
    return print('\n'.join('\t'.join(map(str, row)) for row in my_list))
    

def division(a,b):
    my_list = [] 
    for i in range(1,a+1): 
        my_list.append(list(map(float,(round((i/(b-b+j)),3) for j in range(1,b+1)))))
    return print('\n'.join('\t'.join(map(str, row)) for row in my_list))


def pow(a,b):
    my_list = [] 
    for i in range(1,a+1): 
        my_list.append(list(map(int,((i**(b-b+j)) for j in range(1,b+1)))))
    return print('\n'.join('\t'.join(map(str, row)) for row in my_list))


print_operation_table(pow,7,7)
