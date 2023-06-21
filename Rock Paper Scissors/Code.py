import random
print("Welcome to the game of rock, paper and scissors!!!")
print("--------------------------------------------------")
choose = input("Type 0 for Rock\nType 1 for Paper\nType 2 for Scissors\n")
if choose=="0":
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
elif choose=="1":
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
elif choose=="2":
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
my_list = ["0","1","2"]
comp_choice = random.choice(my_list)
print("\nComputer Chose -->\n")
if comp_choice=="0":
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
elif comp_choice=="1":
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
elif comp_choice=="2":
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

if choose=="0" and comp_choice=="1":
    print("--You Lose--")
elif choose=="0" and comp_choice=="0":
    print("--Its Draw--")
elif choose=="0" and comp_choice=="2":
    print("--You Win--")

if choose=="1" and comp_choice=="2":
    print("--You Lose--")
elif choose=="1" and comp_choice=="1":
    print("--Its Draw--")
elif choose=="1" and comp_choice=="0":
    print("--You Win--")

if choose=="2" and comp_choice=="0":
    print("--You Lose--")
elif choose=="2" and comp_choice=="2":
    print("--Its Draw--")
elif choose=="2" and comp_choice=="1":
    print("--You Win--")
