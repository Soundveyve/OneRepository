number_str = input("Введите оценки через пробел: ")
number_list = [int(num) for num in number_str.split()]
sum_performance = 0
for num in number_list:
    if num == 5:
        sum_performance += 1
print (f"Процент полученных пяторок: {(sum_performance / len (number_list)) * 100}")