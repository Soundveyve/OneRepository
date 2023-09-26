number = input ("Введите число для проверки: ")
list_num = list(number)
sum_num = 0
for i in list_num:
    sum_num += int(i)
if int(number [-1]) % 2 == 0 and sum_num % 3 == 0:
    print ("Число делится на 6")