# VL Using the Debugger
scores = [12, 45, 7, 68, 33, 90, 21]

running_total = 0
highest_score = 0

for score in scores:
    running_total += score
    if score > highest_score: # Logic bug fixed: less then turned to greater than
        highest_score = score

print(f"Total: {running_total}")
print(f"Highest score: {highest_score}")