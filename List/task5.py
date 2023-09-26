list_num = []
num_for_list = input ("Введите оценку для добавления в список: ")
list_for_no = ["no", "нет", "n", "н"]
while num_for_list not in list_for_no:
    list_num.append(int(num_for_list))
    num_for_list = input ("Введите оценку для добавляения в список или 'нет' для завершения: ")
if list_num == sorted(list_num) and len(list_num) > 1:
    print ("Список чисел, введённый вручную, возрастающий")
else:
    print ("Список чисел, введённый вручную, не является возрастающим")
    print(f"Возрастающий список выглядит так: {sorted(list_num)}") #Спасибо, заработало