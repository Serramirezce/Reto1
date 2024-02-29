# Programa de operaciones básicas

print("Utilice \" + \" para suma, \" - \" para resta, \" * \" para producto y \" / \" para cociente")
num1, num2, operation = input("Ingrese los dos números a operar y la respectiva operación separados por una coma: ").split(",")

x = float(num1)
y = float(num2)

def function(x, y, operacion):
  if operation == "+":
    return x+y
  elif operation == "-":
    return x-y
  elif operation == "*":
    return x*y
  elif operation == "/":
    return x/y
if __name__ == "__main__":
  print(function(x, y, operation))