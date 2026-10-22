# VL, Debugging types
# Debugging Practice 3: LOGIC ERRORS
# Nothing crashes. The program runs fine and gives the WRONG answer.
# Each function has a test below it showing what it SHOULD give.
# Use print() statements and tracing to find each bug.

def average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers) + 1

def count_to(n):
    """Return the numbers 1 through n."""
    result = []
    for i in range(1, n):
        result.append(i)
    return result

def is_adult(age):
    if age > 18:
        return True
    return False

def largest(numbers):
    biggest = 0
    for n in numbers:
        if n > biggest:
            biggest = n
    return biggest

def total_of_evens(numbers):
    total = 0
    for n in numbers:
        if n % 2 == 0:
            total += n
    return total

print("average([2, 4, 6])        expected 4.0   got", average([2, 4, 6]))
print("count_to(5)               expected [1, 2, 3, 4, 5]   got", count_to(5))
print("is_adult(18)              expected True  got", is_adult(18))
print("largest([-5, -2, -9])     expected -2    got", largest([-5, -2, -9]))
print("total_of_evens([2,3,4,5]) expected 6     got", total_of_evens([2, 3, 4, 5]))