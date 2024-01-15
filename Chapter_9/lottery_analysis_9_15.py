from random import choice

lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'A', 'B', 'C', 'D', 'E']

my_ticket = []
count = 0
while True:
    my_ticket = []

    my_ticket.append(choice(lottery))
    my_ticket.append(choice(lottery))
    my_ticket.append(choice(lottery))
    my_ticket.append(choice(lottery))
    count += 1
    print(f"{count}th Lottery")


    if 4 in my_ticket and 7 in my_ticket and 5 in my_ticket and 'A' in my_ticket:
        break

    
print(my_ticket)



