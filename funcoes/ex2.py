
t = input()
t = float(t)


def fahrenheit(T):
    f = 1.8 * T + 32
    f = str(f"{f:.1f}")
    return f


def kelvin(T):
    k = T + 273.15
    k = str(f"{k:.2f}")
    return k


print(f"Fahrenheit: {fahrenheit(t)}")
print(f"Kelvin: {kelvin(t)}")