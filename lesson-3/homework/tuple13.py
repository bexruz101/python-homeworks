tuple1 = (1, 4, 5, 7, 2, 3, 4, 2, 3, 3, 4, 5)
min1 = min(tuple1)
min2 = max(tuple1)
for i in tuple1:
  if min2 > i and i!=min1:
    min2 = i
print(f"Second smallest element is: {min2}")
