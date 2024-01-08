pets = [
    {'type': 'Dog', 'owner': 'Alice'},
    {'type': 'Cat', 'owner': 'Bob'},
    {'type': 'Bird', 'owner': 'Charlie'},
    {'type': 'Fish', 'owner': 'David'},
]

for pet in pets:
    for key, value in pet.items():
        print(f"{key.title()} : {value.title()}")
    print()