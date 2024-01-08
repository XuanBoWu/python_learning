users = {
        'aeinstein': {
            'first': 'albert',
            'last': 'einstein',
            'location': 'princeton',
            },

        'mcurie': {
            'first': 'marie',
            'last': 'curie',
            'location': 'paris',
            },

        }

for name, user_info in users.items():
    print(f"Username: {name}")
    print(f"\tFull name: {user_info['first'].title()} "
        f"{user_info['last'].title()}")
    print(f"\tLocation: {user_info['location'].title()}")

