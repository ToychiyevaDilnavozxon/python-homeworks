# Ask the user for a sentence and create an acronym from the first letters of each word.  
a=input("Bir necha so'zdan iborat gap yozing: ")
b="".join(word[0].upper() for word in a.split())
print(f'Akronim: {b}')
