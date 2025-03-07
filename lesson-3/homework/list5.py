try:
    n = int(input("Enter a length of list: "))
    if n < 0:
        raise ValueError("Length of list cannot be negative")

    arr = []
    for i in range(n):
        arr.append(int(input(f"Enter {i+1} element: ")))
    
    element = int(input('Enter number for checking: '))

    if element in arr:
      print('Present')
    else:
      print("Not present")

except ValueError as e:
    print(f"Error: {e}")