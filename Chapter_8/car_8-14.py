def make_car(manufacturer, model, **optional):
    optional['manufacturer'] = manufacturer
    optional['model'] = model

    return optional


print(make_car("BYD", "Han", color="red", version="Ultimate version"))