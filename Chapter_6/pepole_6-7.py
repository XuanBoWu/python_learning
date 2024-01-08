pepole_1 = {
    'first name': 'wu',
    'last name': 'alex',
    'age': 25,
    'citi': 'ShengZheng'
}

pepole_2 = {
    'first name': 'chen',
    'last name': 'lin',
    'age': 25,
    'citi': 'ShengZheng'
}

pepole_3 = {
    'first name': 'jack',
    'last name': 'john',
    'age': 52,
    'citi': 'New York'
}

pepoles_list = [pepole_1, pepole_2, pepole_3]

for pepole in pepoles_list:
    print(f"Full name: {pepole['first name'].title()} "
        f"{pepole['last name'].title()}:")
    for key, value in pepole.items():
       if key not in ['first name', 'last name']:
            print(f"\t{key.title()}: {value}")