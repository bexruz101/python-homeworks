try:
    n = int(input("Enter a length of list: "))
    if n < 0:
        raise ValueError("Length of list cannot be negative")

    arr = []

    for i in range(n):
        arr.append(int(input(f"Enter {i+1} element for first list: ")))

    a = int(input("Enter an index: "))

    if a < len(arr) - 1:
      arr.pop(a)
      print(arr)
    else:
      print("Index out of range")
      
except ValueError as e:
    print(f"Error: {e}")


