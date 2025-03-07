try:
    n = int(input("Enter a length of list: "))
    if n < 0:
        raise ValueError("Length of list cannot be negative")

    arr = []

    for i in range(n):
        arr.append(int(input(f"Enter {i+1} element for first list: ")))

    num = int(input("Enter a number: "))

    new_arr = []

    for i in arr:
      for j in range(num):
        new_arr.append(i)
    print(new_arr)
      
except ValueError as e:
    print(f"Error: {e}")


