a, b, c = map(int, input("Enter three numbers: ").split(" "))

if a >= b and b >= c:
    print(a, c)
elif b >= c and c >= a:
    print(b, a)
else:
    print(b, c)
