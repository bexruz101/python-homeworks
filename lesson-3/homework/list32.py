try:
    n = int(input("Enter a length of list: "))
    if n < 0:
        raise ValueError("Length of list cannot be negative")

    arr = []

    for i in range(n):
        arr.append(int(input(f"Enter {i+1} element for first list: ")))
    
    n1 = int(input("Enter a length of list: "))
    if n1 < 0:
        raise ValueError("Length of list cannot be negative")

    arr2 = []

    for i in range(n1):
        arr.append(int(input(f"Enter {i+1} element for first list: ")))

    merged = sorted((arr+arr2))

    print(merged)
      
except ValueError as e:
    print(f"Error: {e}")


