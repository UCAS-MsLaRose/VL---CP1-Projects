# VL, Nesting Notes

win = False
text = True

if win: 
    if text:
        print("Hallalujah")
    else:
        print("Try Again")
else:
    print("You failed")

names = ["Alex", "Katie", "Andrew", "Tia", "Treyson", "Xavier", "Jake"]


while True:
    for name in names:
        print(f"{name} LaRose")
    again = input("Do you need to see them again: ")
    if again.lower() == "yes":
        pass
    else:
        break