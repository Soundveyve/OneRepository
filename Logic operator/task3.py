feedback = input("Желаете ли вы пробить товар? (Да/Нет): ")
feedback_v = int (input ("Сколько товаров вы хотели бы пробить? "))
list_yes = ["да", "yes","y","д", "желаю"]
list_price = []
while feedback.lower() in list_yes:
    for i in range (feedback_v):
        price = float (input (f"Введите цену {i+1} товара: "))
        list_price.append(price)
    feedback = input("Желаете ли вы пробить товар? (Да/Нет): ")
if list_price[0] < list_price [1] and list_price[1] < list_price [2]:
    print (f"АКЦИЯ! Сумма к оплате была поделена пополам и сейчас составляет: {(sum(list_price))/2}")
elif list_price [0] > list_price [1] and list_price[1] > list_price [2]:
    print (f"АКЦИЯ! Сумма к оплате была поделена на три и сейчас составляет: {(sum(list_price))/2}")