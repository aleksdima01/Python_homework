print("Введите количество кустов:")
n = int(input())
a = list()
for i in range(n):
    berry = int(input(f"Введите количество ягод на {i + 1} кусту:")) 
    a.append(berry)
print(a)
variants = list()
for i in range (len(a) - 1):
    variants.append(a[i] + a[i + 1] + a[i - 1])
variants.append(a[0] + a[- 1] + a[- 2])
print(max(variants))
