river = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'changjiang': 'china',
}

for key in river:
    print(f"The {key.title()} runs through {river[key].title()}")

print()
for key in river:
    print(key)

print()
for value in river.values():
    print(value)
