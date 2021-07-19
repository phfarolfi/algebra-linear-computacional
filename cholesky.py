import numpy as np
import math
import resolucao_sistemas_triangulares as rst

def decomposicao_cholesky(matriz_a, vetor_b):
    n = len(matriz_a) # n é a ordem da matriz a
    matriz_r = np.copy(np.triu(matriz_a)) # matriz_r é uma cópia triangular superior da matriz A

    for i in range(n):
        for k in range(i): # Não é executado quando i = 0
            matriz_r[i,i] = matriz_r[i,i] - math.pow(matriz_r[k,i],2) # Define os termos da diagonal principal
        if matriz_r[i,i] <= 0: # Se algum elemento da diagonal principal for menor ou igual a zero, por definição, a matriz não é positiva definida
            print("Erro: A matriz não é positiva definida.")
            return
        matriz_r[i,i] = math.sqrt(matriz_r[i,i]) 
        for j in range(i+1,n): # Não é executado quando i = n
            for k in range(i): # Não é executado quando i = 0
                matriz_r[i,j] = matriz_r[i,j] - (matriz_r[k,i] * matriz_r[k,j])
            matriz_r[i,j] = matriz_r[i,j]/matriz_r[i,i]

    return resolve_cholesky(matriz_r, vetor_b)

def resolve_cholesky(matriz_r, vetor_b):
    matriz_rt = np.copy(np.transpose(matriz_r)) # matriz_rt é a matriz R transposta

    vetor_y = rst.resolve_subs_frente(matriz_rt, vetor_b) # Faz o cálculo de Rt * y = b para obter o vetor y
    vetor_x = rst.resolve_subs_tras(matriz_r, vetor_y) # Faz o cálculo de R * x = y para obter o vetor x (resultado)

    return vetor_x # Retorna o vetor x (resultado)