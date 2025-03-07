try:
    n = int(input("Enter a length of list: "))
    if n < 0:
        raise ValueError("Length of list cannot be negative")

    arr = []

    for i in range(n):
        arr.append(input(f"Enter {i+1} element for first list: "))

    if len(arr) % 2 == 0:
      print(arr[len(arr)//2],arr[len(arr)//2-1])
    else:
      print(arr[len(arr)//2])

except ValueError as e:
    print(f"Error: {e}")


