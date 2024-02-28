

a_str = input("Please type a int number:")
b_str = input("Please type a int number again:")
    
try:

    a = int(a_str)
    b = int(b_str)
except ValueError:
    print("Plese type a number!")
else:
    print(a + b)



