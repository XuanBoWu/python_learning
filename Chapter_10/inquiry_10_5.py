filename = 'reason.txt'

while True:
    reason = input("Why do you like programming:")

    with open(filename, 'a') as file_object:
        file_object.write(reason.strip() + "\n")

    