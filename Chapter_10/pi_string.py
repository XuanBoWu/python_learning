file_name = 'pi_million_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:100]}")
print(len(pi_string))

birthday = '031199'

if birthday in pi_string:
    print("yes")
else:
    print("no")
