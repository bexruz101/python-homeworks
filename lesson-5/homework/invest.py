def invest(amount,rate,years):
  for i in range(years):
    amount+=amount * rate 
    print(f"year {i+1}: ${amount:.2f}")

a = float(input('Enter a amount of money: '))
r = float(input('Enter a rate: '))
y = int(input('Enter a years: '))

invest(a,r,y)
