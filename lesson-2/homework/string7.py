# Ask the user to input a sentence and a word to replace. Replace that word with another word provided by the user.  
# Example:  
# - Input sentence: "I love apples."  
# - Replace: "apples"  
# - With: "oranges"  
# - Output: "I love oranges."
a=input("Jumlangizni kiriting: ")
b=input("Qaysi so'zni almashtirmoqchisiz? ")
c=input("Yangi so'zni kiriting: ")
d=a.replace(b,c)
print(f"Yangi jumla: {d}")