cities = {
    "Tokyo": {
        "country": "Japan",
        "population": "约 1390万（2021年）",
        "fact": "东京是日本的首都和最大城市，也是世界上人口最多的城市之一。"
    },
    "New York City": {
        "country": "United States",
        "population": "约 850万（2021年）",
        "fact": "纽约市是美国最大的城市，以其金融、艺术、文化和娱乐中心而闻名于世。"
    },
    "Mumbai": {
        "country": "India",
        "population": "约 2000万（2021年）",
        "fact": "孟买是印度的最大城市，也是印度的商业和娱乐业之都，宝莱坞所在地。"
    },
}

for city, city_info in cities.items():
    print(f"{city.title()}:")
    for key, value in city_info.items():
        print(f"\t{key.title()}: {value}")