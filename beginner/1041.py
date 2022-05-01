# Origem -> (0,0)
# Eixo X -> (a, 0)
# Eixo Y -> (0,a)

# Q1 -> (+a, +b)
# Q2 -> (-a, +b)
# Q3 -> (-a, -b)
# Q4 -> (+a, -b)

a, b = map(float, input().split(" "))

if a == 0 and b == 0:
    print("Origem")
elif b == 0:
    print("Eixo X")
elif a == 0:
    print("Eixo Y")
else:
    if a > 0 and b > 0:
        print("Q1")
    elif a < 0 and b > 0:
        print("Q2")
    elif a < 0 and b < 0:
        print("Q3")
    else:
        print("Q4")
