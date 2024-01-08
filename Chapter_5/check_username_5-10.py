current_users = ['Admin', 'Alex', 'Alice', 'Jack', 'Max']
new_users = ['alex', 'alice', 'lisa', 'bob', 'mike']

current_users_lower = []

for user in current_users:
    current_users_lower.append(user.lower())

for user in new_users:
    if user in current_users_lower:
        print('Need to enter another username.')
    else:
        print('This username is not in use.')

