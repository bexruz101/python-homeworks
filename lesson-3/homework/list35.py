try:
    a,b =  map(int,input("Enter a range: ").split(" "))

    arr = list(range(a,b))
    print(arr)

except ValueError as e:
    print(f"Error: {e}")


