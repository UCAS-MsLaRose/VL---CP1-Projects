# VL Mapping Notes
import math
def times(number):
    return number *2

numbers = range(1,6)

multiplied_numbers = map(times,numbers)

print(*list(multiplied_numbers))
new_numbers = []
for number in numbers:
    new_numbers.append(number*2)

print(*new_numbers)

siblings = ["Alex", "Katie", "Andrew", "Tia", "Treyson", "Xavier", "Jake"]

length = list(map(len, siblings))
print(length)

print(math.factorial(5))