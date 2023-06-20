from replit import clear
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("\n\n")
my_list = []
choice = "Yes"
print("Welcome to Secret Auction\n")
while choice == "Yes":
  name = input("What is your name ? ")
  bid = int(input("What is your bid in USD($) ? "))
  my_list.append({"name":name,"bid":bid})
  choice = input("Are there more bidders, type 'Yes' or 'No' ")
  if choice == "Yes":
    clear()
maz = 0
winner = ""
for n in my_list:
  if n["bid"]>maz:
    maz = n["bid"]
    winner = n["name"]
clear()
print(f"The winner of Secret Auction is {winner} with ${maz} bid")
