
import math
print("Enter the coefficients a, b, and c respectively:")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = (b**2) - (4*a*c)
if d == 0:
    r = -b / (2*a)
    print("The equation has one real root: x =", r)
elif d > 0:
    sroot = math.sqrt(d)
    r1 = (-b + sroot) / (2*a)
    r2 = (-b - sroot) / (2*a)
    print("The equation has two real roots: x =", r1, "and x =", r2)
else:
    real = -b / (2*a)
    imaginary = math.sqrt(-d) / (2*a)
    r1 = f"{real} + {imaginary}i"
    r2 = f"{real} - {imaginary}i"
    print("The equation has two complex roots: x =", r1, "and x =", r2)
