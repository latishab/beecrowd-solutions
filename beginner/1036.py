import math

a, b, c = map(float, input().split())

# D = b^2-4ac
# x = (-b (+-) sqrt(b^2-4ac))/2a

# Impossivel calcular 
# 1. Division by zero
# 2. Square root of negative number

# Check if Impossivel calcular
if 2*a == 0 or ((b**2-(4*a*c)) < 0):
    print("Impossivel calcular")
else:
    # Count the roots of bhaskara's formula
    r1 = ((-b) + math.sqrt(b**2-(4*a*c)))/(2*a)
    r2 = ((-b) - math.sqrt(b**2-(4*a*c)))/(2*a)

    r1_f = "{:.5f}".format(r1)
    r2_f = "{:.5f}".format(r2)

    print("R1 =", r1_f)
    print("R2 =", r2_f)
