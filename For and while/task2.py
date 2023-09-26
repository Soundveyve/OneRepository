import random
otvet = input("Хотите ли вы развлечься? ")
list_yes = ["да", "д", "yes", "y"]
while otvet.lower() in list_yes:
    feedback = input("Введите тип развлечения (game, music, movie): ")
    if feedback.lower() == "game" or feedback.lower() == "игра":
        print ("Добро пожаловать в игру 'Угадай число'! ")
        num_rand = random.randint (1, 100)
        num_inp = int (input("Введите целое число: "))
        if num_inp == num_rand:
            print ("Вы угадали число!")
            otvet = input("Хотите сыграть вновь? (да/нет): ")
        else:
            print (f"К сожалению, ответ неверный... Мы загадали {num_rand} ")
            otvet = input ("Хотите сыграть вновь? ")
    else:
        print (f"Нам оооочень жаль, но раздел находится в разработке...\nПридётся играть в Угадай число")
        otvet = input("Вы всё ещё хотите развлечься?")
print ("Приятного дня! Возращайтесь поскорее!")