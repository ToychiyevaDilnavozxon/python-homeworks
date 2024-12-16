# Write a program that accepts a username and password and checks if both are not empty.
a=input("Write your username: ").strip()
b=input("Write your password: ").strip()
if a and b:
    print("Username and password accepted.")
elif not a and not b:
    print("Both username and password are empty. ") 
elif not a:
    print("Username is empty. ")
else:
    print("Password is empty. ")  
