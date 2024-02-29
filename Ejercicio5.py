# Programa para encontrar palabras con caracteres iguales

def encontrar_palabras_repetidas(cadena):
    b = cadena.split(",") # Creamos una lista del input de la cadena, serapada por comas
    palabras = []
    nuevas_palabras = [] # Lista vacía para incluir las palabras que se repiten
    for i in b:
        c = sorted(list(set(i)))
        palabras.append(c) # Este método vuelve cada elemento de la lista una secuencia de caracteres que no se repiten, ordenados alfabéticamente

    for x in range(len(palabras)): # Todo este ciclo compara las listas de caracteres y encuentra las similitudes
        for z in range(len(palabras)):
            if x != z and palabras[x] == palabras[z]:
                a = b[x]
                nuevas_palabras.append(a)
                break 

    return nuevas_palabras #Por último, la función retorna las palabras que tienen los mismos caracteres

if __name__ == "__main__":
    print("Ingrese las palabras separadas por comas, sin espacios entre ellas: ")
    entrada = input()
    final = encontrar_palabras_repetidas(entrada)
    print(",".join(final)) #Imprime todos los elementos de la nueva lista separados por comas.
