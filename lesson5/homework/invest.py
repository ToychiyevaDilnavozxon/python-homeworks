amount = float(input(" Investitsiya miqdori: "))
rate = float(input("Foiz stavkasi: "))
years= int(input(" Yillar: "))
def invest(amount, rate, years):
    for yil in range(1,years+1):
        result = amount*(1+rate/100) ** yil
        print(f"Year {yil} : $ {result:.2f}")
    return result
invest(amount, rate, years)