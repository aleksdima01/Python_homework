first = int(input("Введите первый эл-т прогрессии:"))
step = int(input("Введите шаг прогрессии:"))
count = int(input("Введите количество элементов прогрессии:"))
progression = 0
final_list = []
for i in range(1, count + 1):
    progression = first + (i - 1) * step
    final_list.append(progression)
print(final_list)
