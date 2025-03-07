try:
    n = int(input("Enter a length of list: "))
    if n < 0:
        raise ValueError("Length of list cannot be negative")

    arr = []

    for i in range(n):
        arr.append(int(input(f"Enter {i+1} element for first list: ")))

    max1 = max(arr)
    max2 = 0

    for i in arr:
        if  max1 != i and max2 < i:
            max2 = i
    print(max2)
        
            
    
  


except ValueError as e:
    print(f"Error: {e}")


