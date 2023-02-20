from random import randint
n = int(input("Введите количество элементов списка:"))
mass = [randint(1, 100) for i in range(n)]
print(mass)
x = int(input("Введите число для поиска:"))
count=0
for i in range(n):
    if x == mass[i]:
        count += 1
print(count)