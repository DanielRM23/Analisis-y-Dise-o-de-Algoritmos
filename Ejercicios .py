#!/usr/bin/env python
# coding: utf-8

# # Tarea 2

def lexicografico(A,B):
    n = len(A)
    contador = 0
    for i in range(0,n):
        if A[i] <= B[i]:
            contador += 1
    return contador
    
    
def estrictamente_lexicografico(A,B):
    n = len(A)
    if lexicografico(A,B) == n:
        contador = 0
        for i in range(0,n):
            if A[i] < B[i]:
                return 1
            if A[i] == B[i]:
                contador += 1
                            
        if contador == n:
            return 2
    else:
        return 3


A = [1,0]
B = [0,1]
estrictamente_lexicografico(A,B)


A = [1,2,3,100]
B = [1,2,3,4]
estrictamente_lexicografico(A,B)


# # Tarea 3

# ### Ejercicio 2


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
        
palabra1 = ['a', 'm', 'o', 'r']
palabra2 = ['r', 'o', 'm', 'a']
print(anagrama_version2(palabra1, palabra2))

palabra1 = ['c', 'i', 'n', 'e', 'm', 'a']
palabra2 = ['i', 'c', 'e', 'm', 'a', 'n']
print(anagrama_version2(palabra1, palabra2))

palabra1 = ['m', 'u', 'n', 'd', 'o']
palabra2 = ['d', 'u', 'd', 'a', 'r']
print(anagrama_version2(palabra1, palabra2))

palabra1 = ['f', 'r', 'e', 's', 'a']
palabra2 = ['l', 'e', 'n', 't', 'e']
print(anagrama_version2(palabra1, palabra2))


# ### Problema 3

def declive(A):
    n = len(A)
    
    max = 0
    i = 0
    j = 0

    while i < n:
        if j < n:
            if A[i] - A[j] < max:
                j += 1
            else:
                max = A[i] - A[j]
                j += 1
        elif j == n: 
            i += 1
            j = i + 1
    
    return max

A = [19, 12, 13, 11, 20, 10] 
declive(A)

