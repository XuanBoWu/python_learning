filename = 'guest.txt'

guest_name = input("Please input your name:")

with open(filename, 'a') as file_object:
    file_object.write(guest_name.strip() + "\n")

print(f"Welecome! {guest_name.title()}")


