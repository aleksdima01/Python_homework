my_dictionary = {'letters':'аяуюоеёэиы'}
line = input("Введите строку:").lower().split()
print(line)
count_list = []
count = 0
for i in range(len(line)):
    for j in range(len(line[i])):
        if line[i][j] in my_dictionary['letters']:
            count += 1
    count_list.append(count)
    count = 0
count_list = set(count_list)
if len(count_list) == 1:
    print("Парам пам-пам")
else:
    print("Пам парам")
