try:
    n = int(input("Enter a length of list: "))
    if n < 0:
        raise ValueError("Length of list cannot be negative")

    arr = []
    arr2 = []

    for i in range(n):
        arr.append(input(f"Enter {i+1} element for first list: "))
    
    n1 = int(input("Enter a length of sublist: "))
    if n1 < 0:
        raise ValueError("Length of list cannot be negative")
    

    for i in range(n1):
        arr2.append(input(f"Enter {i+1} element for sublist: "))

    for i in arr2:
      if i not in arr:
        print(False)
        exit(1)
    print(True)

    
      

except ValueError as e:
    print(f"Error: {e}")
