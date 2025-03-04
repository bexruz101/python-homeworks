t1 = input("Enter first string: ")
t2 = input("Enter second string: ")

for i in range(len(t1)):
    if t1[i] != t2[i]:
        print(False)
        exit()
print(True)
