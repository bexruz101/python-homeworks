txt = input("Enter a string: ")

for i in 'aeoiu':
  if i in txt:
    txt = txt.replace(i,'*')

print(txt)