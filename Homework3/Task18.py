from random import randint
n = int(input("Введите количество элементов списка:"))
mass = [randint(1, 100) for i in range(n)]
print(mass)
x = int(input("Введите число для поиска:"))
find = mass[0]
for i in mass:
    if abs(i-x) < abs(find-x):
        find = i
print(find)