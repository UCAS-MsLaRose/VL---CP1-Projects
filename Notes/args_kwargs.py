# VL, *args **kwargs notes

def hello(last_name, *first_name):
    for first in first_name:
        print(f"Hello {first} {last_name}!")

hello("LaRose", "Alex", "Katie", "Andrew", "Tia", "Treyson", "Xavier", "Jake")

hello("Kringle", "Kris")


def clean(data, decimals= 0,**kwargs):
    if kwargs.get("type") == "str":
        return data.strip().lower()
    elif kwargs.get("type") == "int":
        return int(data)
    elif kwargs.get("type") == "float":
        if kwargs.get("decimals"):
            decimals = kwargs.get("decimals")
        return round(float(data), decimals)
    elif kwargs.get("type") == "list":
        return str(f"{x}, " for x in data)
    elif kwargs.get("type") == "bool":
        return f"{data}"
    else:
        return "No data type given"

print(clean("3.1415", decimals=3, type="float"))
print(clean("utah", type = "str"))
print(clean([4, 5 , 8]))