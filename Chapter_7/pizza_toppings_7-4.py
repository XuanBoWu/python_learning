
active = True
toppings = set()
while active:
    topping = input("Tell me what toping you want are: ")
    if topping == 'quit':
        active = False
    else:
        toppings.add(topping)
        print(f"Already joined {topping}")
    

print(f"All added ingredients:")
for topping in toppings:
    print(topping.title())

