login_inp = input ("Введите ваш логин" + \
                   "\nПомните, что нельзя использовать следующие символы: =?*^$№@_ : ")
list_error_log = ["=","?","*","^","$","№","@","_", "#"]
list_error = []
for i in login_inp:
    if i in list_error_log:
        list_error.append(i)
if bool(list_error):
    print (f"К несчастью, у вас использовались запрещённые символы: {list_error}")