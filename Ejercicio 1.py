# Programa de operaciones básicas

print("Utilice \" + \" para suma, \" - \" para resta, \" * \" para producto y \" / \" para cociente")
print("Por favor use punto para los decimales y coma únicamente para separar las entradas.")
num1, num2, operation = input("Ingrese los dos números a operar y la respectiva operación separados por una coma (Ejemplo: \" 2,3,* \"): ").split(",")

x = float(num1)
y = float(num2)  # Aquí se convierten los dos primeros inputs a números flotantes

def function(x, y, operacion):    # Esta función realiza la respectiva operación aritmetica que el usuario digite
  if operation == "+":
    return x+y
  elif operation == "-":
    return x-y
  elif operation == "*":
    return x*y
  elif operation == "/":
    return x/y
if __name__ == "__main__":
  print(function(x, y, operation)) # El print de la función evaluada en las entradas
