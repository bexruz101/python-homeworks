try:
    n = int(input("Enter a length of list: "))
    if n < 0:
        raise ValueError("Length of list cannot be negative")

    arr = []

    for i in range(n):
        arr.append(input(f"Enter {i+1} element for first list: "))
    
    new_arr = arr[::-1]

    print(new_arr)

except ValueError as e:
    print(f"Error: {e}")


