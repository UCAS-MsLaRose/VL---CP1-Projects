#VL Functions Notes
name = input("Tell me your name: ")
attempts = 0

def increase():
    """This is used to increase the attempts variable by 1"""
    return attempts + 1

def birthday(name, age=35):
    """This sings happy birthday to a user and says their age"""
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print(f"Happy Birthday dear {name}!")
    print("Happy Birthday to you!")
    print(f"You are now {age} years old!")

def stupid_proof(user_answer, correct):
    """Checks if the user has typed in a correct option for an input"""
    user_answer = user_answer.strip().title()
    if user_answer in correct:
        return True, user_answer, increase()
    else:
        return False, user_answer, increase()

print("November")
birthday("Tia", 30)
print("December")
birthday("Xavier", 24)
print("January")
birthday("Treyson", 20)
birthday(name)

while True:
    capital = input("What is the capital of Utah: ")
    correct, capital, attempts = stupid_proof(capital, ["Salt Lake City", "Slc", "Salt Lake"])
    if correct:
        print(f"Good job {capital} is the capital of Utah!")
        break
    else:
        print(f"Try Again. {capital} is not the capital of Utah. You have tried {attempts} times.")


