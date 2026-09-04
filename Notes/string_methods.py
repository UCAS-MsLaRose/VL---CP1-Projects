# VL, String Methods

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

print(full_name.isalpha())
print(full_name.isnumeric())
print(full_name.isupper())

print(sentence.lower()) 
print(sentence.upper())
print(sentence.capitalize()) 
print(sentence.title()) 