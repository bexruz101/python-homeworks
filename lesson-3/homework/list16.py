try:
    n = int(input("Enter a length of list: "))
    if n < 0:
        raise ValueError("Length of list cannot be negative")

    arr = []

    for i in range(n):
        arr.append(int(input(f"Enter {i+1} element: ")))

    count_odd = 0

    for i in arr:
      if i%2 == 1:
        count_odd+=1
    print(count_odd)

except ValueError as e:
    print(f"Error: {e}")
