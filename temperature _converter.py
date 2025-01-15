def c_f(x):
  return  1.8 * x + 32
    
def c_k(x):
  return x + 273.15

def f_c(x):
    return (x - 32) * 5 / 9     


def f_k(x):
    return (x - 32) * 5 / 9 + 273.15

def k_c(x):
    return x - 273.15

def k_f(x):
    return (x - 273.15) * 9 / 5 + 32


def temp_conv():
    print("Select the operation: ")
    print("1 - celsius -> fahrenheit")
    print("2 - celsius -> kelvins")
    print("3 - fahrenheit -> celsius")
    print("4 - fahrenheit -> kelvins")
    print("5 - kelvin -> celsius")
    print("6 - kelvin -> fahrenheit")

    operation = input("Choose the operation:")

    if operation not in ("1","2","3","4","5","6"):
      print("Inexistence operation")
      return
    
    try:
        numb1 = float(input("Type the value:"))
    except ValueError:
        print("Please, just valid numbers.")
        return 

    if operation == "1":
        print(f"{numb1}°C = {c_f(numb1)}°F")
    elif operation == "2":
        print(f"{numb1}°C = {c_k(numb1)}K")
    elif operation == "3":
        print(f"{numb1}°F = {f_c(numb1)}°C")
    elif operation == "4":
        print(f"{numb1}°F = {f_k(numb1)}K")
    elif operation == "5":
        print(f"{numb1}K = {k_c(numb1)}°C")
    elif operation == "6":
        print(f"{numb1}K = {k_f(numb1)}°F")


while True:
    temp_conv()

    repeat = input("Do you want to do another operation? (yes/no): ").lower()
    if repeat not in ("yes", "y", "sim"):
        print("Thanks for using the temperature converter!")
        break
