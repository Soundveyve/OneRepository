numbers_list = list("0139412831055230677798")
list_number_for_count = list (range (10))
my_dict = {}
for i in numbers_list:
    count_number = numbers_list.count(i)
    my_dict [i] = count_number
print (my_dict)