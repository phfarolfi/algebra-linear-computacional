import numpy as np
import math

def euclidiana(vetor): # norma-2 vetorial
    n, x = len(vetor), 0

    for i in range(n):
        x += math.fabs(vetor[i]) ** 2

    return x ** (1/2)

def manhattan(vetor): # norma-1 vetorial
    n, x = len(vetor), 0

    for i in range(n):
        x += math.fabs(vetor[i])

    return x

def p(vetor, p): #norma-p vetorial
    n, x = len(vetor), 0

    for i in range(n):
        x += math.fabs(math.pow(vetor[i], p))

    return x ** (1/p)

def infinita(vetor): # norma-infinita vetorial
    n, max = len(vetor), vetor[0]
    
    for i in range(1, n):
        if math.fabs(vetor[i]) > max:
            max = math.fabs(vetor[i])

    return max

def frobenius(matriz_a): # norma-2 matricial
    n, x = len(matriz_a), 0

    for i in range(n):
        for j in range(n):
            x += math.pow(math.fabs(matriz_a[i,j]), 2)

    return x ** (1/2)

def soma_coluna(matriz_a): # norma-1 matricial
    n, max, x = len(matriz_a), 0, 0

    for j in range(n):
        for i in range(n):
            x += math.fabs(matriz_a[i,j])
        
        if x > max:
            max = x
    
    return max

def soma_linha(matriz_a): # norma-infinita matricial
    n, max, x = len(matriz_a), 0, 0

    for i in range(n):
        for j in range(n):
            x += math.fabs(matriz_a[i,j])
        
        if x > max:
            max = x

    return max

def residual(matriz_a, vetor_b, delta_x): #norma-residual matricial
    n, k = len(matriz_a), np.linalg.cond(matriz_a)
    delta_b = np.matmul(matriz_a, delta_x)
    vetor_r = vetor_b - delta_b

    vetor_x = np.ones(n)
    vetor_x_menos_delta_x = vetor_x - delta_x
    residuo_r_b = euclidiana(vetor_r)/euclidiana(vetor_b)

    print("Vetor residual:\n", vetor_r)
    print("Resíduo da solução x:", residuo_r_b)

    if euclidiana(vetor_x_menos_delta_x)/euclidiana(vetor_x) <= k*residuo_r_b:
        print("A solução encontrada é precisa.")
    else:
        print("A solução encontrada não é precisa.")