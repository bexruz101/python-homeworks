try:
    n = int(input("Enter a length of list: "))
    if n < 0:
        raise ValueError("Length of list cannot be negative")

    arr = []
    for i in range(n):
        arr.append(int(input(f"Enter {i+1} element: ")))

    sum = 0

    for i in arr:
        sum += i
    print("Total of all the elements: ", sum)

except ValueError as e:
    print(f"Error: {e}")
