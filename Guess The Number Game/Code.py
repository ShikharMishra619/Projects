logo = '''#####  #     # #######  #####   #####     ####### #     # #######    #     # #     # #     # ######  ####### ######  
#     # #     # #       #     # #     #       #    #     # #          ##    # #     # ##   ## #     # #       #     # 
#       #     # #       #       #             #    #     # #          # #   # #     # # # # # #     # #       #     # 
#  #### #     # #####    #####   #####        #    ####### #####      #  #  # #     # #  #  # ######  #####   ######  
#     # #     # #             #       #       #    #     # #          #   # # #     # #     # #     # #       #   #   
#     # #     # #       #     # #     #       #    #     # #          #    ## #     # #     # #     # #       #    #  
 #####   #####  #######  #####   #####        #    #     # #######    #     #  #####  #     # ######  ####### #     #
 
 BY SHIKHAR MISHRA'''
print(logo)
print("\n\n----------------------WELCOME TO THE NUMBER GUESSING GAME---------------------------\n\n")
import random
computer = random.randint(1,100)
attempts = 0
over = 0
while True:
  difficulty = input("Choose the difficulty level, type 'easy' or 'hard'\n").lower()
  if difficulty == "easy":
    attempts = 9
    print("You will get 10 attempts\n")
    break
  elif difficulty == "hard":
    attempts = 4
    print("You will get 5 attempts\n")
    break
  else:
    print("Wrong input\n")
guess = int(input("I am thinking of a number between 1 and 100, can you guess the number ?\n"))
def game():
  global attempts, guess, computer
  while attempts != 0: 
    if guess < computer:
      attempts -= 1
      print(f"You are left with {attempts+1} attempts\n")
      guess = int(input("Your guess was low, guess higher\n"))
    elif guess > computer:
      attempts -= 1
      print(f"You are left with {attempts+1} attempts\n")
      guess = int(input("Your guess was high, guess lower\n"))
    else:
      print("Your guess is right, You won\n")
      return 1
  return 0
over = game()
if over == 0:
  print(f"You lose, My guess was {computer}\n")
