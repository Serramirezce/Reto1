# Programa palíndromo

word = input("Ingrese una palabra: ")

word = word.lower()

def invert_word(word):
    inverted = ""
    for i in range(len(word)-1, -1, -1):
        inverted += word[i]
    return inverted

def verdict(inverted):
  if word == inverted:
    return "La palabra es un palíndromo"
  else :
    return "La palabra no es un palíndromo"

if __name__ == "__main__":
  print(verdict(invert_word(word)))