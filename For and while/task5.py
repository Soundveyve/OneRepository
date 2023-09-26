price = float (input("Введите стоимость товара: "))
discount = 0.2
sum = 0
while price != 0:
    sum += price - (price * discount)
    print (f"Общая сумма покупки с применением скидки в {discount * 100}% для товара: {sum}")
    price = float (input("\nВведите стоимость нового товара или 0 для подсчёта итоговой суммы: "))
print(f"\nИтоговая сумма к оплате: {sum}")