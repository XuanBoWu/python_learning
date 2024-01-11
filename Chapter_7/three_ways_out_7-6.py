active = True
while active:
    age_input = input("How old are you: ")

    try:
        # 将输入转换为整数并验证年龄
        age = int(age_input)
        if age > 12:
            print("The fee is USD 15.")
        elif age >= 3:
            print("The fee is USD 10.")
        else:
            print("Free!")
    except ValueError:
        print("Invalid input! Please enter a number.")

    continue_query = input("Do you want to check another person's ticket price? (yes/no): ")
    if continue_query.lower() != 'yes':
        active = False