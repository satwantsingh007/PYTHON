#Calculator
from art import logo
print(logo)

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
def calculator():
    num1 = eval((input("What's the first number?: \n")))
    for symbol in operations:
      print(symbol)
    proceed = False
    while not proceed:
        operation_symbol = input("Pick an operation: \n")
        num2 = eval((input("What's the next number?: \n")))
        calculation_function = operations[operation_symbol]
        first_answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {first_answer}")
        ask = input(f"Do you want to continue with the result {first_answer} type y or n for starting new calculation \n")
        if ask == 'y':
            num1 = first_answer
        else:
            calculator()
calculator()