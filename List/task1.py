game = input("Введите название настольной игры для добавления в список: ")
list_game = []
while game != "0":
    if game in list_game:
        print ("Игра уже имеется в списке")
        game = input ("\nВведите название другой игры или 0 для завершения: ")
    else:
        list_game.append(game)
        game = input ("\nВведите название настольной игры или 0 для завершения: ")
print (f"Весь список ваших игр: {list_game}")