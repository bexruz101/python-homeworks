txt = input("Enter a string: ")
vowels = "aoieu"
count_of_v = 0
length = len(txt)

for i in vowels:
    count_of_v += txt.count(i)

print(f"Vowels: {count_of_v}\nConsonants: {length-count_of_v}")
