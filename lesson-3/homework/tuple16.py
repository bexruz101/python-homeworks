tuple1 = (4,5,6,10,8,19)
in_order = True

for i in range(len(tuple1)-1):
  if tuple1[i] > tuple1[i+1]:
     print(False)
     in_order = False
     break

if in_order != False:
   print(True)




