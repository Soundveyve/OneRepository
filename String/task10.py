phone_num = "+7 (812) 134 - 12 - 324"
phone_num = phone_num.replace(" ", "")
phone_num = phone_num.replace("+","")
phone_num = phone_num.replace("(", "")
phone_num = phone_num.replace(")", "")
phone_num = phone_num.replace("-", "")
print (f"Номер телефона без лишних символов: {phone_num}")