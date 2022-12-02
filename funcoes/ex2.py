
def Farenheit(T):

    f = 1.8 * T + 32
    f = str(f"{f:.1f}")
    return print(f"Farenheit: {f}")

Farenheit(32)

def Kelvin(T):
    k = T + 273.15
    k = str(f"{k:.2f}")
    return print(f"Kelvin: {k}")

Kelvin(32)
