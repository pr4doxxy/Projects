#Função de cada operação
def subtraction(x, y):
    return  x - y

def sum(x, y):
    return x + y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Error (division by 0)"
    return  x / y

#Função principal da calculadora
def calculator():
    print("Select the operation: ")
    print("1 - Subtraction")
    print("2 - Sum")
    print("3 - Multiplication")
    print("4 - Division")
  
    operation = input("Choose the operation:")

    #verificação
    if operation not in ("1", "2","3","4"):
      print("Inexistence operation")
      return

    #armazenando números
    try:
        numb1 = float(input("Type the first number:"))
        numb2 = float(input("Type the second number:"))
    except ValueError:
        print("Please, just valid numbers.")
        return 
   
    #tipos de operações 
    if operation =="1":
      print(f"{numb1} + {numb2} = {subtraction(numb1, numb2)}")

    elif operation == "2":
     print(f"{numb1} - {numb2} = {sum(numb1, numb2)}") 

    elif operation == "3":
     print(f"{numb1} * {numb2} = {multiplication(numb1, numb2)}")

    elif operation == "4": 
      print(f"{numb1} / {numb2} = {division(numb1 , numb2)}")

#operation loop
while True:
    calculator()

    repeat = input("You want to do another operation? (Yes/No): ").lower()
    if repeat != "Yes" :
       print("Thanks for used the calculator")
       break
    