my_pizzas = ["Pizza Hut", "domino", "Papa John"]

friend_pizzas = my_pizzas[:] 

my_pizzas.append("Supreme Pizza")
friend_pizzas.append("Jamo Pizza")

print("My favorite pizzas are:")
for pizza in my_pizzas:
	print(pizza)

print("\n")

print("Friend favorite pizzas are")
for pizza in friend_pizzas:
	print(pizza)

