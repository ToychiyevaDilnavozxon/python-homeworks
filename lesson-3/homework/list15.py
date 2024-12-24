a=[1,2,3,4,4,3,2,3,1,4,5]
b = 0


for number in a:
    if number % 2 == 0:
        b += 1

print(b)