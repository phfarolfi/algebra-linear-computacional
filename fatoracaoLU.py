import numpy as np
import resolucao_sistemas_triangulares as rst

def fatoracaoLU(matriz_a, vetor_b):
    n = len(matriz_a)
    matriz_u = np.copy(matriz_a)
    matriz_l = np.identity(n)

    for i in range(n-1):
        for j in range(i+1, n):
            m = matriz_u[j,i]/matriz_u[i,i] # x é o multiplicador necessário para executar a eliminação
            matriz_l[j,i] = m # os números multiplicadores são armazenados abaixo da diagonal principal da matriz L

            for k in range(i, n):
                matriz_u[j,k] -= matriz_u[i,k] * m # aplica o multiplicador x para zerar os elementos abaixo da diagonal principal da matriz U

    return resolve_lu(matriz_u, matriz_l, vetor_b) # A matriz U é triangular superior e a matriz L é triangular inferior

def resolve_lu(matriz_u, matriz_l, vetor_b):
    vetor_y = rst.resolve_subs_frente(matriz_l, vetor_b) # resolve o sistema Ly = b pela substituicao para frente
    vetor_x = rst.resolve_subs_tras(matriz_u, vetor_y) # resolve o sistema Ux = y pela substituicao para tras

    return vetor_x # Retorna o vetor x (resultado)