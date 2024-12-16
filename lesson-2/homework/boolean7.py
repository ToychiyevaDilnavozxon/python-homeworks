# Write a program that checks if the sum of two numbers is greater than 50.8. Create a program that checks if a given number is between 10 and 20 (inclusive)
a=float(input("Son kiriting: "))
b=float(input("2-sonni kiriting: "))
c=a+b
if c>50.8:
    print(f"{a} va {b} sonlarning yig'indisi {c} > 50.8 ")
else:
    print("Yig'indi 50.8 dan katta emas")