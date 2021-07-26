import numpy as np
import criterios as crit

def resolve_substituicao(matriz_A, vetor_b):
    if(crit.verifica_tri_inferior(matriz_A)):
        return resolve_subs_frente(matriz_A, vetor_b)

    elif(crit.verifica_tri_superior(matriz_A)):
        return resolve_subs_tras(matriz_A,vetor_b)
        
    else:
        print("A matriz não é triangular")
        return RuntimeError

def resolve_subs_frente(matriz_A, vetor_b): # Resolve um sistema com matriz triangular inferior
    n = len(matriz_A)
    vetor_resultado = np.array(np.copy(vetor_b), dtype='f8')

    for i in range(n):
        for j in range(i):
            vetor_resultado[i] = vetor_resultado[i] - matriz_A[i,j] * vetor_resultado[j]
        vetor_resultado[i] = vetor_resultado[i]/matriz_A[i,i]
    return vetor_resultado

def resolve_subs_tras(matriz_A,vetor_b): # Resolve um sistema com matriz triangular superior
    n = len(matriz_A)
    vetor_resultado = np.array(np.copy(vetor_b), dtype='f8')

    for i in range(n-1,-1,-1):
        for j in range(n-1,i,-1):
            vetor_resultado[i] = vetor_resultado[i] - matriz_A[i,j] * vetor_resultado[j]
        vetor_resultado[i] = vetor_resultado[i]/matriz_A[i,i]
    return vetor_resultado