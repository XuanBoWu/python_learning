from name_function import get_formatted_name

def is_quit(text):
    text = text.lower()
    if text == 'q':
        return True
    return False

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a frist name: ")
    if is_quit(first):
        break

    last = input("\nPlease type your last name: ")
    if is_quit(last):
        break
    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")
    
