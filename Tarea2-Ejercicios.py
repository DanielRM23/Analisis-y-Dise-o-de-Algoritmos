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

