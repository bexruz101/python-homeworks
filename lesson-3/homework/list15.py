try:
    n = int(input("Enter a length of list: "))
    if n < 0:
        raise ValueError("Length of list cannot be negative")

    arr = []

    for i in range(n):
        arr.append(int(input(f"Enter {i+1} element: ")))

    count_even = 0

    for i in arr:
      if i%2 == 0:
        count_even+=1
    print(count_even)

except ValueError as e:
    print(f"Error: {e}")
