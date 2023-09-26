finance = float (input ("Введите ваш бюджет: "))
price = float (input ("Введите стоимость товара: "))
num_prod = int(finance // price)
print (f"Количество товаров, доступных для покупки по указанным параметрам: {num_prod}")
