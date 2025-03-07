try:
    n = int(input("Enter a length of list: "))
    if n < 0:
        raise ValueError("Length of list cannot be negative")

    arr = []

    for i in range(n):
        arr.append(int(input(f"Enter {i+1} element for first list: ")))

    min1 = min(arr)
    min2 = max(arr)

    for i in arr:
        if  min1 != i and min2 > i:
            min2 = i
    print(min2)
       

except ValueError as e:
    print(f"Error: {e}")


