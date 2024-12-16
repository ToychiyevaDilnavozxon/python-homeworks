# Write a program that checks if a string starts with one word and ends with another. 
a=input("Write a sentence: ")
b=input(" Which word the sentence start? ")
c=input(" Which word the sentence end? ")
starts_with=a.startswith(b)
ends_with=a.startswith(c)
if starts_with and ends_with:
    print("The sentence start and end with input word")
elif starts_with:
    print("The sentence start with input word, but not end with input word")
elif ends_with:
    print("The sentence end with input word, but not start with input word")
else:
    print("The sentence donot end and start with input words")


