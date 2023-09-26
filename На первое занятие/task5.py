#Функция для вычисления модуля числа (расстояние на числовой оси)
list1 = []
for i in range (2):
    num = int(input(f"Введите {i+1} число для вычисления модуля: "))
    list1.append(num)
max_num = max (list1)
min_num = min (list1)
print (f"Модуль равен:{abs (max_num - min_num)}")