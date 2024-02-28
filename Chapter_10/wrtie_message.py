file_name = 'programming.txt'

with open(file_name, 'w') as file_object:
    file_object.write("Hello World!")

with open(file_name, 'a') as file_object:
    file_object.write("\nI love programming!")