try:
    n = int(input("Enter a length of first list: "))
    if n < 0:
        raise ValueError("Length of list cannot be negative")

    arr = []
    arr2 = []
    both_arr = []

    for i in range(n):
        arr.append(input(f"Enter {i+1} element for first list: "))
    
    n1 = int(input("Enter a length of second list: "))
    if n1 < 0:
        raise ValueError("Length of list cannot be negative")
    

    for i in range(n1):
        arr2.append(input(f"Enter {i+1} element for second list: "))

    both_arr = arr + arr2
    print(both_arr)

except ValueError as e:
    print(f"Error: {e}")
