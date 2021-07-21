import numpy as np
import substituicao as subs

def fatoracaoLU(matriz_A, vetor_b):
    n = len(matriz_A)
    matriz_U = np.copy(matriz_A)
    matriz_L = np.identity(n)

    for i in range(n-1):
        for j in range(i+1, n):
            m = matriz_U[j,i]/matriz_U[i,i] # x é o multiplicador necessário para executar a eliminação
            matriz_L[j,i] = m # os números multiplicadores são armazenados abaixo da diagonal principal da matriz L

            for k in range(i, n):
                matriz_U[j,k] -= matriz_U[i,k] * m # aplica o multiplicador x para zerar os elementos abaixo da diagonal principal da matriz U

    return resolve_LU(matriz_U, matriz_L, vetor_b) # A matriz U é triangular superior e a matriz L é triangular inferior

def resolve_LU(matriz_U, matriz_L, vetor_b):
    vetor_y = subs.resolve_substituicao(matriz_L, vetor_b) # resolve o sistema Ly = b pela substituicao para frente
    vetor_x = subs.resolve_substituicao(matriz_U, vetor_y) # resolve o sistema Ux = y pela substituicao para tras

    return vetor_x # Retorna o vetor x (resultado)