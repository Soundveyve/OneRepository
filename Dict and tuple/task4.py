my_dict = dict () #Как поменять местами элементы словаря? Как использовать словарные
#представления без их "оборачивания" в list?
for i in range (5):
    my_dict [i] = i * i
my_dict_key = list(my_dict.keys())
my_dict_value = list(my_dict.values())
print (f"Словарь до изменения{my_dict}")
print (f"Словарь после перестановки первого и последнего элемента {my_dict}")