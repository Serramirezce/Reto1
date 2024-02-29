# Programa palíndromo

word = input("Ingrese una palabra: ")

word = word.lower() # Este método se usa para llevar todo el input a minúsculas y que al verificar que sea palíndromo, no tenga problemas con mayúsculas y minúsculas

def invert_word(word): #Esfta función invierte la palabra
    inverted = ""
    for i in range(len(word)-1, -1, -1):
        inverted += word[i]
    return inverted

def verdict(inverted):  # Esta función evalúa si la palabra que retorna la función anterior es igual a la ingresada por el usuario
  if word == inverted:
    return "La palabra es un palíndromo"
  else :
    return "La palabra no es un palíndromo"

if __name__ == "__main__":
  print(verdict(invert_word(word)))
