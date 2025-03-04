char = input("Enter spearator character: ")
text = input("Enter a string: ").split(char)
string = ''
for i in text:
  string+=i
print(string)
