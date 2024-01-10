pepole_number = input("How many pepole are dining: ")

pepole_number = int(pepole_number)

if pepole_number > 8:
    print(f"Sorry, There are no more {pepole_number} seats available.")
else:
    print("Ok, there are enough vacancies.")