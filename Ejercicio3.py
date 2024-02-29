def encontrar_primos(lista):
    b = lista.split(",") # Separa los elementos de la lista por comas
    c = [int(x)for x in b] # Convierte a entero cada elemento de la lista 
    primos = []

    if 2 in c:
        primos.append(2) # Este condicional es para incluir al 2 (si es que lo hubiere) en la lista de primos
    for i in c:
        es_primo = True
        for j in range(2, i): # Este ciclo analiza si el residuo de de la division desde 2, hasta un numero anterior al numero en cuestion es 0, en ese caso no seria primo
            if i % j == 0: 
                es_primo = False 
                break
        if es_primo and i > 1 and i not in primos:
            primos.append(i) # este condicional guarda los primos en la lista de primos
    return primos

if __name__ == "__main__":
    entrada = input()
    print(encontrar_primos(entrada))
    

