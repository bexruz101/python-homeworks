try:
    n = int(input("Enter a length of list: "))
    if n < 0:
        raise ValueError("Length of list cannot be negative")

    arr = []
    custom_set = {}
    for i in range(n):
        arr.append(input(f"Enter {i+1} element: "))

    custom_set = set(arr)

    for i in custom_set:
        print(f"{i} appeared {arr.count(i)} times in a list")
except ValueError as e:
    print(f"Error: {e}")
