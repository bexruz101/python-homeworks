#task-1  Return uncommon elements of lists. Order of elements does not matter.
# list1 = input().split()
# list2 = input().split()
# list3 = []

# for i in list1:
#   if i not in list2:
#     list3.append(i)

# for i in list2:
#   if i not in list1:
#     list3.append(i)

# print(list3)

#task-2 Print the square of each number which is less than n on a separate line.
# try:
#   n = int(input())
#   for i in range(1,n):
#     print(i**2)
# except ValueError as e:
#   print(e)

#task-3 txt nomli string saqlovchi o'zgaruvchi berilgan. txtdagi har uchinchi belgidan keyin pastgi chiziqcha (underscore) qo'yilsin. Agar belgi unli harf yoki orqasidan ostki chiziqcha qo'yilgan harf bo'lsa, ostki chiziqcha keyingi harfdan keyin qo'yilsin. Agar belgi satrdagi oxirgi belgi bo'lsa chiziqcha qo'yilmasin.
# txt = input()
# new_txt = ''
# unlilar = 'aeiou'
# letters = []
# isMoved = False
# if len(txt) < 3:
#   print(txt)
  
# for i in range(len(txt)):
#   new_txt += txt[i]
#   if txt[i] == txt[-1]:
#     break
#   elif txt[i] in unlilar:
#     continue
#   elif (i+1)%3 == 0 or isMoved:
#     if txt[i] not in letters: 
#       new_txt+='_'
#       letters.append(txt[i])
#       isMoved = False
#     else:
#       if (i+1)%3 == 0:
#         isMoved = True 
  
# print(new_txt)


#task-4 Number Guessing Game Create a simple number guessing game.
# import random 
# try: 
#   isAgain = True
#   while isAgain:
#     num = random.randint(1,100)
#     for i in range(10):
#       user_num = int(input('Guess number from 1 to 100: '))
#       if user_num == num:
#         print('You guessed it right!')
#         isAgain = False
#         break
#       elif user_num > num and i != 9:
#         print('Too high!')
#       elif user_num < num and i != 9:
#         print('Too low!')
#       else:
#         choice = input('You lost. Want to play again? ')
#         if choice == 'Y' or choice == 'YES' or choice == 'y' or choice == 'yes' or choice == 'ok':
#           isAgain = True
#         else:
#           isAgain = False
#         break
          
# except ValueError as e:
#   print(e)

#task-5 Password Checker Task: Create a simple password checker.
# password = input('Enter a strong password: ')
# upper_words = 'QWERTYUIOPASDFGHJKLMNBVCXZ'
# if len(password) < 8:
#   print('Password is too short.')
# else:
#   for i in password:
#     if i in upper_words:
#       print('Password is strong.')
#       break
#   else:
#     print('Password must contain an uppercase letter.')

#task-6 Prime Numbers Task: Write a Python program that prints all prime numbers between 1 and 100.
# for i in range(2,100):
#   isPrime = True
#   for j in range(2,i):
#     if i % j == 0:
#       isPrime = False
#       break
#   if isPrime:
#     print(i)


#Bonus Challenge
# import random

# choices = ["rock", "paper", "scissors"]

# player_score = 0
# computer_score = 0

# print("Welcome to Rock, Paper, Scissors! First to 5 points wins.")

# while player_score < 5 and computer_score < 5:

#     computer_choice = random.choice(choices)

#     player_choice = input("Enter rock, paper, or scissors: ").lower()

#     if player_choice not in choices:
#         print("Invalid choice. Please choose rock, paper, or scissors.")
#         continue

#     print(f"\nYou chose: {player_choice}")
#     print(f"Computer chose: {computer_choice}")

#     if player_choice == computer_choice:
#         print("It's a tie!")
#     elif (player_choice == "rock" and computer_choice == "scissors") or \
#          (player_choice == "paper" and computer_choice == "rock") or \
#          (player_choice == "scissors" and computer_choice == "paper"):
#         print("You win this round! ")
#         player_score += 1
#     else:
#         print("Computer wins this round!")
#         computer_score += 1

#     print(f"Score You: {player_score} | Computer: {computer_score}\n")

# if player_score == 5:
#     print("Congratulations! You won the game!")
# else:
#     print("Computer wins the match! Better luck next time.")
