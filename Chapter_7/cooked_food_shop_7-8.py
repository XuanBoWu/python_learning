sandwich_orders = ['Club Sandwich', 'Ham and Cheese', 'Grilled Cheese', 
    'Turkey and Avocado']

finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich}")
    finished_sandwiches.append(sandwich)

print("All sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
