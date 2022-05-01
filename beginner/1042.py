a, b, c = map(int, input().split())

# not_sorted
myNums = [a , b , c]

#sorted
myNums_sorted = sorted(myNums)

def asread():
    print(f"\n{myNums[0]}\n{myNums[1]}\n{myNums[2]}")

print(f"{myNums_sorted[0]}\n{myNums_sorted[1]}\n{myNums_sorted[2]}")

asread()
