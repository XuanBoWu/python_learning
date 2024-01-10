number = input("Please input a number, I will tell you whether it is a multiple of 10: ")

number = int(number)

if number % 10 == 0 and number != 0:
    print(f"{number} is a multiple of 10!")
else:
    print(f"{number} not is a multiple of 10!")