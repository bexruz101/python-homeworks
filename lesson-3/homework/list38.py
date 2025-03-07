try:
    n = int(input("Enter a length of list: "))
    if n < 0:
        raise ValueError("Length of list cannot be negative")

    arr = []

    for i in range(n):
        arr.append(int(input(f"Enter {i+1} element for first list: ")))

    
    if arr[:] == arr[::-1]:
      print(True)
    else:
      print(False)


except ValueError as e:
    print(f"Error: {e}")
