favorite_places = {
    "Alice": ["Paris", "Tokyo", "New York"],
    "Bob": ["Sydney", "Rio de Janeiro"],
    "Charlie": ["London", "Beijing", "Los Angeles"],
}

for key in favorite_places:
    print(f"{key}, your favorite places are:")
    for place in favorite_places[key]:
        print(f"{place.title()}")
    print()