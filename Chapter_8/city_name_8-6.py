def city_country(city, country):
    city_name = f"{city.title()}, {country.title()}"

    return city_name


print(city_country("santiago", "chile"))
print(city_country("beijing", "China"))
print(city_country("london", "britain"))

