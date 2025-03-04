txt = input("Enter string: ")
for i in range(len(txt)):
    if txt[i] != txt[-i - 1]:
        print("not polindrome")
        exit()
print("Polindrome")
