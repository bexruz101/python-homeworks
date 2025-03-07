try:
    n = int(input("Enter a length of list: "))
    if n < 0:
        raise ValueError("Length of list cannot be negative")

    arr = []

    for i in range(n):
        arr.append(int(input(f"Enter {i+1} element for first list: ")))

    
    num = int(input("Enter a number for sublist: "))

    nested_list = []

    for i in range(0,len(arr),num):
      nested_list.append(arr[i:i+num])
    
    print(nested_list)

except ValueError as e:
    print(f"Error: {e}")
