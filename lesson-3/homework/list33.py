try:
    n = int(input("Enter a length of list: "))
    if n < 0:
        raise ValueError("Length of list cannot be negative")

    arr = []

    for i in range(n):
        arr.append(input(f"Enter {i+1} element for first list: "))
    
    el = input("Enter an element: ")

    index_arr = []

    for i in range(len(arr)):
      if arr[i] == el:
        index_arr.append(i)
    
    print(index_arr)


except ValueError as e:
    print(f"Error: {e}")


