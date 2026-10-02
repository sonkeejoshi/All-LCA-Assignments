stu_list = ["Ria", "Sneha", "Aarav", "Arjun"]
print("\nStudent List: ")
print(stu_list)

stu_tuple = ("Ria", "Sneha", "Aarav", "Arjun")
print("\nStudent Tuple: ")
print(stu_tuple)

stu_dictionary = {1:"Ria", 2:"Sneha", 3:"Aarav", 4:"Arjun"}
print("\nStudent dictionary: ")
print(stu_dictionary)

#update
stu_dictionary[2]= "Rajas"
print(stu_dictionary)

#delete
del stu_dictionary[3]
print(stu_dictionary)

#add
stu_dictionary[5] ="Sara"
print(stu_dictionary)
