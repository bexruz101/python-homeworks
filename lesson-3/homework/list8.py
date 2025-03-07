try:
    n = int(input("Enter a length of list: "))
    if n < 3:
        raise ValueError("Length of list less than 3")

    arr = []
    for i in range(n):
        arr.append(input(f"Enter {i+1} element: "))

    arr2 = arr[:3]
    print(arr2)


except ValueError as e:
    print(f"Error: {e}")
    
