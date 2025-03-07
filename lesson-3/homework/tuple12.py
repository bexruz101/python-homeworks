tuple1 = (1, 4, 5, 7, 2, 3, 4, 2, 3, 3, 4, 5)
max1 = max(tuple1)
max2 = 0
for i in tuple1:
  if max2 < i and i!=max1:
    max2 = i
print(f"Second largest element is: {max2}")
