def down_half (sum):
    while sum % 2 == 0:
        sum = sum / 2
    return sum
price = float (input("Введите стоимость товара: "))
discount = 0.15
sum = 0
while price != 0:
    sum += price
    print (f"Сумма вашей покупки на данный момент: {sum}")
    price = float (input("\nВведите стоимость следующего товара или 0 для подсёта итоговой суммы: "))
if sum % 2 == 0:
    final_sum = down_half(sum)
    print (f"Поздравляем! Сумма вашей покупки с учётом лотереи: {final_sum}")
else:
    print (f"К оплате с учётом скидки в {discount * 100}% : {sum}")