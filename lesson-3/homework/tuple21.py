tuple1 = (3,4,3,2,4,4,5,3,4,2,2,)
list1 = []
number = 3
for i in tuple1:
  if tuple1.count(i) == number and i not in  list1:
    list1.append(i)
    print(i)

