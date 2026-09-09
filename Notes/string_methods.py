# VL, String Methods
"""
sentence = "The quick brown fox jumps over the lazy dog"

word = input("What word do you want?: ").strip().lower()
new_word = input("What word should be in the sentence: ").strip().lower()

location = sentence.find(word)
new_sentence = sentence.replace(word,new_word)
print(new_sentence)
print(sentence.find("over"))

first_name = input("What is your first name: ").strip().title()
last_name = input("What is your last name: ").strip().title()
first_seperated = first_name.split()
fixed = "".join(first_seperated)
last_seperated = last_name.split()
last_fixed = "".join(last_seperated)
full_name = fixed.title() + " " + last_fixed.title()
print("Hello " + full_name.title())

print(full_name.isalpha()) # Checks if the entire thing is characters
print(full_name.isnumeric())# Checks if entire thing is numbers
print(full_name.isupper())# Checks if all all the string is uppercase

print(sentence.lower()) 
print(sentence.upper())
print(sentence.capitalize()) 
print(sentence.title()) 


# formatted string 
print(f"Hello {fixed.title()} {last_fixed} welcome to my program!")"""

letter = input("Give me a letter: ")
letter = letter[0].lower()
number_value = ord(letter)
number_value += 2
new_letter = chr(number_value)
print(f"Your letter was {letter} now it is {new_letter}")