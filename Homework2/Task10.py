from random import randint
coin_count=int(input("Введите количество монеток:"))
a= [randint(0,1) for i in range(coin_count)]
print(a)
count1 = 0 
count2 = 0
i = 0
while i < len(a):
    if a[i] == 0:
        count1 += 1
    if a[i] == 1:
        count2 +=1
    i += 1
print(f"Количество 0:{count1}")
print(count2)