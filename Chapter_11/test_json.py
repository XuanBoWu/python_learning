import json

def number_writer():
    numbers = [1, 2, 3, 4, 5]
    filename = "numbers.json"
    with open(filename, 'w') as f:
        json.dump(numbers, f)
    
def number_reader():
    filename = "numbers.json"
    with open(filename) as f:
        numbers = json.load(f)
    print(numbers)

number_writer()
number_reader()