def convert_far_to_cel(faranheit):
    celsius = (faranheit - 32) * 5/9
    return celsius
faranheit=float(input("Enter a temperature in degrees F: "))
celsius=convert_far_to_cel(faranheit)
print(f" {faranheit} degrees F= {celsius:.2f} degrees C ")

def convert_cel_to_far(celsius):
    faranheit  = celsius * 9/5 + 32
    return faranheit
celsius=float(input("Enter a temperature in degrees C: "))
faranheit=convert_cel_to_far(celsius)
print(f" {celsius} degrees C= {faranheit:.2f} degrees F ")