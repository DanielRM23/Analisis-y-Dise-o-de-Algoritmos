def anagrama(palabra1, palabra2):
    # Convertimos las palabras a minúsculas
    palabra_1 = palabra1.lower()
    palabra_2 = palabra2.lower()

    # Si la longitud de las palabras es distinta, no se puede hacer el anagrama
    if len(palabra_1) != len(palabra_2): 
        return False
    
    # No se considera el caso en que las palabras son iguales
    elif palabra_1 == palabra_2:
        return False
        
    else:
        # Para cada letra de la palabra1, si ésta no está en la palabra2, entonces
        # no se puede formar el anagrama y se devuelve False 
        for i in palabra_1:
            if i not in palabra_2: 
                return False
            break

        return True
    

palabra1 = "hola"
palabra2 = "adios"
print(anagrama(palabra1, palabra2 ))


# Las entradas son arreglos con caracteres en sus entradas
# supongamos que las palabras están dadas en minúsculas sin acentas y eso

def anagrama_version2(palabra1, palabra2):
    n = len(palabra1)
    m = len(palabra2)
    if n != m:
        print("Las palabras no tienen la misma longitud")
    else: 
        i = 0
        j = 0
        k = 0
        while i < n and j < n:
            if palabra1[i] != palabra2[j]:
                i += 1 
            else:
                k += 1
                j += 1
                i = 0
        if k == n:
            return True
        else:
            return False
