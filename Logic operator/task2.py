time_in = int(input ("Введите текущее время: "))
price = int (input ("Введите суммы оплаты: "))
if time_in >= 10 and time_in <= 12:
    print (f"Сумма вашей покупки: {price/2}")
elif time_in >= 20 and time_in < 22:
    print (f"Сумма вашей покупки: {price/4}")
else:
    print(f"Сумма вашей покупки:{price}")