# (weight*grade) / weight

a = float(input())
b = float(input())

ans = ((a*3.5)+(b*7.5))/(3.5+7.5)
ans_f = "{:.5f}".format(ans)

print("MEDIA =", ans_f)
