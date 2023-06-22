logo = """
 _____________________
|  _________________  |
| | ShikharCalc   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
def add(n1, n2):
  return n1+n2
def subtract(n1, n2):
  return n1-n2
def multiply(n1, n2):
  return n1*n2
def divide(n1, n2):
  return n1/n2
operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}
def calculator():
  print(logo)
  num1 = float(input("What is the first number ?\n"))
  for op in operations:
    print(op)
  while True:
    operation_op = input("Pick an operation :\n")
    num2 = float(input("What is the next number ?\n"))
    answer = operations[operation_op](num1,num2)
    print(f"{num1} {operation_op} {num2} = {answer}\n")
    choose = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation : \n").lower()
    if choose == 'y':
      num1 = answer
    else:
      calculator()
calculator()
