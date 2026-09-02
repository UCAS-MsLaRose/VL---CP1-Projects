# VL Strings Notes

#Strings are a collection of characters held together by quotation marks

name = "Ms. LaRose" 

age = "15"

print(age + "2")

print(name + " " + age)

first_name = 'Tia'
last_name = 'LaRose'
full_name = first_name + " " + last_name
print(full_name)
# escape char \
sentence = '\tThen he said \n"That isn\'t fair"'
print(sentence)

print("*" * 30)
sentence = "The quick brown fox jumps over the lazy dog"
print(sentence)
print(sentence.find("e"))
print(sentence[10:15])
word = input("what word do you want? ")
start = sentence.find(word)
length = len(word)
print(sentence[start:start+length])