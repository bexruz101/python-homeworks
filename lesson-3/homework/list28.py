try:
    n = int(input("Enter a length of list: "))
    if n < 0:
        raise ValueError("Length of list cannot be negative")

    arr = []

    for i in range(n):
        arr.append(int(input(f"Enter {i+1} element for first list: ")))

    a,b = map(int,input("Enter a range for sublist: ").split(" "))

    min_element = min(arr[a:b+1])

    print(min_element)

except ValueError as e:
    print(f"Error: {e}")


