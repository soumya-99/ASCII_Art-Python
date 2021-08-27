import math
number = float(input("Enter the radius of the circle: "))
def perimter(radius):
    return 2 * math.pi * radius

def area(radius):
    return math.pi * radius ** 2

print(perimter(number))
print(area(number))

print(math.gcd(12, 6)) # GCD
