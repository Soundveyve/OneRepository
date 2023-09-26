categ = input ("Введите категорию товара: ")
if categ.lower() == "продукты":
    price = float (input ("Введите цену товара: "))
    if price < 100.0:
        print ("Попробуйте нашу выпечку ")
    elif price >= 100 and price < 500:
        print("Как насчёт орехов в шоколаде")
    elif price >= 500:
        print ("Попробуйте экзотические фрукты")
    else:
        print ("Загляните в товары для дома")