# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

Summ = int(input("Введите количество журавликов:"))
while Summ % 6 != 0:
    Summ = int(input("Введенное количество журавликов не удовлетворяет условиям  задачи! Введите количество журавликов:"))
P = S = Summ // 6
K = Summ - (P + S)
print(f"Катя сделала {K} журавликов\nПетя сделал {P} журавликов\nСерёжа сделал {S} журавликов")