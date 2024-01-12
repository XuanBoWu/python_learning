def sandwich_fillings(*fillings):
    print("Sandwich fillings are as follows:")
    for filling in fillings:
        print(f"- {filling}")

sandwich_fillings("Ham", "cheese", "tomato")
sandwich_fillings("lettuce", "cheese", "tomato")
sandwich_fillings("Ham", "lettuce", "tomato")
