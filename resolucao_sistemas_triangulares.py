import numpy as np

def resolve_subs_frente(matriz_a, vetor_b): # Resolve um sistema com matriz triangular inferior
    n = len(matriz_a)
    vetor_resultado = np.array(np.copy(vetor_b), dtype='f8')

    for i in range(n):
        for j in range(i):
            vetor_resultado[i] = vetor_resultado[i] - matriz_a[i,j] * vetor_resultado[j]
        vetor_resultado[i] = vetor_resultado[i]/matriz_a[i,i]
    return vetor_resultado

def resolve_subs_tras(matriz_a,vetor_b): # Resolve um sistema com matriz triangular superior
    n = len(matriz_a)
    vetor_resultado = np.array(np.copy(vetor_b), dtype= 'f8')

    for i in range(n-1,-1,-1):
        for j in range(n-1,i,-1):
            vetor_resultado[i] = vetor_resultado[i] - matriz_a[i,j] * vetor_resultado[j]
        vetor_resultado[i] = vetor_resultado[i]/matriz_a[i,i]
    return vetor_resultado