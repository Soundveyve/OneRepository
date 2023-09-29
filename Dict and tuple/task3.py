my_dict = {}
name = 1
place_chart = 1
performer = 1
while name != "off" and place_chart != "off" and performer != "off":
    name = input ("Введите название трека")
    place_chart = input("Введите номер в чарте")
    performer = input("Введите имя исполнителя")
    my_dict [(name, place_chart)] = performer
print(my_dict)