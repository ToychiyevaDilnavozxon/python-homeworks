# Write a program to check if a string contains any digits.  
a=input("So'z kiriting: ")
b=any(char.isdigit() for char in a)
if b:
    print("Matnda raqam mavjud")
else:
    print("Matnda raqam yo'q.")    