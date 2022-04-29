# input values
in_str = input().split(" ")
a_str, b_str, c_str = in_str

# convert values to strings
a = int(a_str)
b = int(b_str)
c = int(c_str)

# count The Greatest
maior1 = (a + b + abs(a - b))/2
maior2 = (maior1 + c + abs(maior1 - c))/2

print(int(maior2), "eh o maior")
