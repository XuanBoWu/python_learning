file_name = 'learning_python.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip().replace('Python', 'C'))
