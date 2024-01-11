sandwich_orders = ['Club Sandwich', 'pastrami', 'pastrami', 'Ham and Cheese', 'Grilled Cheese', 
    'pastrami']

print("pastrami sold out.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)