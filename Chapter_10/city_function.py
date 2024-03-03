def formatted_city_country(city, country, population=""):
    format_city_name = f"{city}, {country}"
    format_population = ""
    if population != "":
        format_population = f" - population {population}"
    return format_city_name.title() + format_population