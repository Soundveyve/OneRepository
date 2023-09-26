string0 = "<span>5&nbsp;128&nbsp;P</span>"
list1 = []
for i in string0:
    if i.isdigit():
        list1.append (i)
only_number = int("".join(list1))
only_number += 1
print (f"Готовая сумма: {only_number}")