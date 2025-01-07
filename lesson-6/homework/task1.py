def check(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except ZeroDivisionError:
            print("Denominator can't be zero")
            return None
    return wrapper

@check
def div(a, b):
    return a / b

print(div(10, 2))  
print(div(10, 0))