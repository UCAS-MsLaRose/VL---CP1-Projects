# VL, Elif and Logical Operators Notes

age = 17
license = True

if age >= 18:
    print("You are an adult and can vote!")
elif age >= 15 and license:
    print("You can drive! But you are a minor, so go to school!")
elif age >= 15 and not license:
    print("You could drive. . .but you haven't done the paperwork :( Also go to school.")
else:
    print("You are too young to drive. Go to school.")


win = True
hp = 1

if win or hp <= 0:
    print("Game Over")
    if hp > 0:
        pass
    else:
        print("You lost :(")
else:
    print("The game is still going")