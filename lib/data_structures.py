spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names_list = []
    for food in spicy_foods:
        names_list.append(food["name"])
    return names_list

def get_spiciest_foods(spicy_foods):
    spiciest_list = []
    for food in spicy_foods:
        if food["heat_level"] > 5 :
            spiciest_list.append(food)
    return spiciest_list

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat = ''
        for i in range (food["heat_level"]):
            heat += "🌶"
        print (f'{food["name"]} ({food["cuisine"]}) | Heat Level: {heat}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine : 
            return food

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5 :
            heat = ''
            for i in range (food["heat_level"]):
                heat += "🌶"
            print (f'{food["name"]} ({food["cuisine"]}) | Heat Level: {heat}')

def get_average_heat_level(spicy_foods):
    count = 0
    total_heat = 0
    for food in spicy_foods:
        total_heat += food["heat_level"]
        count += 1
    return total_heat / count 

def create_spicy_food(spicy_foods, spicy_food):
    return [*spicy_foods, spicy_food]
