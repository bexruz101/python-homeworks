try:
    n = int(input("Enter a length of list: "))
    if n < 0:
        raise ValueError("Length of list cannot be negative")

    arr = []
    for i in range(n):
        arr.append(int(input(f"Enter {i+1} element: ")))

    min_num = 0

    for i in arr:
        if min_num > i:
          min_num = i
    print(min_num)

except ValueError as e:
    print(f"Error: {e}")