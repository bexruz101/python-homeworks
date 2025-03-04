text = input("Enter a string: ")
for i in '1234567890':
  if i in text:
    print(True)
    exit()
print(False)
