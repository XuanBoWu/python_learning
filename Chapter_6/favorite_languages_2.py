favorite_languages = {
    'alex': ['python', 'java'],
    'alice': ['c'],
    'jack': ['java'],
    'bob': ['cpp', 'c']
}

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"{name}'s, favorite languages are:")
        for language in languages:
            print(language)        
    else:
        print(f"{name}\'s, favorite languages is {languages[0]}.")
