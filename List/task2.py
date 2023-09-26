note = int(input("Введите оценку: "))
list_note = []
while note > 0 and note <= 5:
    if note > 2:
        list_note.append(1)
        note = int (input ("Введите новую оценку или 0 для завершения: "))
    else:
        list_note.append(0)
        note = int (input("Введите новую оценку: "))
print (f"Ваша успеваемость равна: {(sum(list_note)/ len(list_note)) * 100}")