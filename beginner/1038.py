myItems = {
    1: "4.00",
    2: "4.50",
    3: "5.00",
    4: "2.00",
    5: "1.50"
}

# reads item code and amount
code, amount = map(int, input().split())

ans = float(myItems[code]) * amount
ans_f = "{:.2f}".format(ans)

print("Total: R$", ans_f)
