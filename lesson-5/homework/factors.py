def factor(num):
    for i in range(1, num + 1):
        if num % i == 0:
            print(f"{i} is a factor of {num}")


try:
    n = int(input("Enter a positive integer: "))
    factor(n)
except ValueError as e:
    print(e)
