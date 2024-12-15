# Ask the user for a string and replace all the vowels with a symbol (e.g., `*`).  
a=input("So'z kiriting: ")
vowels = "aeiouAEIOU"
b = "".join('*' if char in vowels else char for char in a)
print(b)

