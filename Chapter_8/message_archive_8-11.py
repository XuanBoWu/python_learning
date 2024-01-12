def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(original_messages, sent_messages):
    while original_messages:
        message = original_messages.pop()
        sent_messages.append(message)

original_messages = [
    "create mode 100644 Chapter_8/album_8-7.py",
    "create mode 100644 Chapter_8/city_name_8-6.py",
    "create mode 100644 Chapter_8/user_album_8-8.py"
    ]

sent_messages = []
send_messages(original_messages[:], sent_messages)

print("original_messages:")
show_messages(original_messages)

print("\nsent_messages:")
show_messages(sent_messages)