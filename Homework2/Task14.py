n = int(input("Введите до какой степени будем возводить число 2:"))
for i in range(n+1):
    result = 2 ** (i)
    print(f"Два в степени {i} = {result}")
