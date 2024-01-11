active = True
while active:
    age = input("How old are you: ")
    age = int(age)

    if age > 12:
        print("The fee is USD 15.")
    elif age >= 3:
        print("The fee is USD 10.")
    else:
        print("Free!")
