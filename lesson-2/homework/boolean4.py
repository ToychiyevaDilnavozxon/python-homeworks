# Write a program that takes three numbers and checks if all of them are different.
a=input("son yoz")
b=input("2-sonni yoz")
c=input("3-sonni yoz")
if a==b and a==c:
    print("Ular teng")
elif a==b and a!=c:
    print("1- va 2-son teng")
elif a!=b and a==c:
    print("1- va 3-son teng")
elif b==c and a!=b:
    print("2- va 3-son teng")
else:
    print("Ular teng emas")

