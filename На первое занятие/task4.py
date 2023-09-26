list1 = []
for i in range (3):
    num = int(input(f"Введите {i+1} цифру для подсчётов: "))
    list1.append(num)

print (f"Сумма указанных значений: {sum(list1)}")
print (f"Максимальное значение из указанных: {max (list1)}")
print (f"Минимальное значение из указанных: {min(list1)}")
print (f"Всего значений введено: {len(list1)}")