otvet = input ("Введите время приёма пищи (завтрак, обед,ужин): ")
if otvet.lower() == "завтрак":
    print ("Рекомендую кашу")
elif otvet.lower() == "обед" or otvet.lower() == "ужин":
    print ("Рекомендуем плов")
else:
    print ("Рекомендуем котлету с пюре")