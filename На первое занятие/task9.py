num = int(input ("Введите число для инвертирования: "))
hund = num // 100
ten = (num // 10) % 10
unit = num % 10
print (f"Инвертированная версия числа: {(unit*100)+(ten * 10)+hund}")