try:
    n = int(input("Enter a length of list: "))
    if n < 0:
        raise ValueError("Length of list cannot be negative")

    arr = []

    for i in range(n):
        arr.append(int(input(f"Enter {i+1} element for first list: ")))

    arr_even = list(filter(lambda x:x%2==1,arr))

    print(arr_even)   

except ValueError as e:
    print(f"Error: {e}")


