favorite_languages = {
    'alex': 'python',
    'alice': 'c',
    'jack': 'java',
    'bob': 'cpp',
    'lisa': 'java'
}

name_list = ['jack', 'alice', 'max', 'joe', 'john']

investigated_list = favorite_languages.keys()

for name in name_list:
    if name in investigated_list:
        print(f"{name}, thank you for taking the poll!")
    else:
        print(f"{name}, please take our poll!")
    




