# Create a program that accepts a number and checks if it’s divisible by both 3 and 5.
a=int(input("Son yozing: "))
if a%3==0 and a%5==0:
    print("Ikkisiga ham bo'linadi")
elif a%3==0 and a%5!=0:
    print("3ga bo'linib 5ga bo'linmaydi")
elif a%3!=0 and a%5==0:
    print("5ga bo'linib 3ga bo'linmaydi")
else:
    print("3ga ham 5 ga ham bo'linmaydi")
