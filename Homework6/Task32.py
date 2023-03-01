# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint
n = int(input("Введите количество элементов списка:"))
list1 = [randint(1, 40) for i in range(n)]
#list1 = [3, 3, 26, 30, 5, 5, 4, 25, 4, 7, 5, 24, 25, 25, 36, 17, 40, 34, 40, 4]
range1 = list(map(int, input("Введите диапазон поиска через пробел:").split()))
print(f'Исходный список: {list1}')
range1 = [i for i in range(range1[0], range1[1]+1)]
print(f'Диапазон поиска: {range1}')
final_list= [i for i in range(0, len(list1)) if list1[i] in range1]
print(f'Индексы найденных элементов: {final_list}')
