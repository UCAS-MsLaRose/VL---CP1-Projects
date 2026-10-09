# VL, While Loops

import random
import time 

goose = random.randint(1,20)
duck = 1

while goose > duck:
    print("duck. . . ")
    time.sleep(0.1)
    duck += 1
    if duck == 15:
        print("Game over")
        break
else:
    print("GOOSE!")


count = 30

while count >= 1:
    print(count)
    time.sleep(.1)
    count -= 1


number = random.randint(1,101)

while True:
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            if guess < 0 or guess > 100:
                print("You should read the instructions!")
                continue
            break
        except:
            print("That isn't a number")
    if guess == number:
        print("You win!")
        break
    elif guess < number:
        print("That number is too low")
    elif guess > number:
        print("That number is too high")
    else:
        print("I don't know how you got here. . . but you did something horribly wrong.")