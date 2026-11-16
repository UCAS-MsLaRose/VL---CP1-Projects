#VL, Dictionaries Notes

# Collection of key and value pairs 

car = {
    "make": "Jeep",
    "model": "Wrangler",
    "color": "silver",
    "year": 2023
}

values = list(car.values())

print(values)
print(len(car))
if "transmission" in car:
    print(car["transmission"])
else:
    car["transmission"] = "automatic"

car.pop("color")
print(car.items())
keys = list(car.keys())
for key in keys:
    print(f"{key} is {car[key]}")



avatar = {
    "Water": {
        "Katara": "Water bender",
        "Sokka": "Leader. Boomerage guy. Idea guy. Sword master",
    },
    "Earth":{
        "Toph": "Earth bender. The GOAT!",
        "Suki": "Warrior from Kyoshi Island",
        "Cabbage Merchent": "My CABBAGES!!!!!!"
    },
    "Air":{
        "Aang": "Air bender, the Avatar."
    },
    "Fire":{
        "Zuko": "Fire bender, future fire lord.",
        "Iroh": "The actual GOAT. Fire Bender, Dragon of the West.",
        "Azula": "Fire lord for 1 hour. Amazing fire bender"
    }
}

print(avatar["Fire"]["Iroh"])
print(avatar.get("Earth").get("Bumi"))