import numpy as np
import math
import substituicao as subs

def decomposicao_cholesky(matriz_A, vetor_b):
    n = len(matriz_A) # n é a ordem da matriz a
    matriz_R = np.copy(np.triu(matriz_A)) # matriz_r é uma cópia triangular superior da matriz A

    for i in range(n):
        for k in range(i): # Não é executado quando i = 0
            matriz_R[i,i] = matriz_R[i,i] - math.pow(matriz_R[k,i],2) # Define os termos da diagonal principal
        if matriz_R[i,i] <= 0: # Se algum elemento da diagonal principal for menor ou igual a zero, por definição, a matriz não é positiva definida
            print("Erro: A matriz não é positiva definida.")
            return
        matriz_R[i,i] = math.sqrt(matriz_R[i,i]) 
        for j in range(i+1,n): # Não é executado quando i = n
            for k in range(i): # Não é executado quando i = 0
                matriz_R[i,j] = matriz_R[i,j] - (matriz_R[k,i] * matriz_R[k,j])
            matriz_R[i,j] = matriz_R[i,j]/matriz_R[i,i]

    return resolve_cholesky(matriz_R, vetor_b)

def resolve_cholesky(matriz_R, vetor_b):
    matriz_Rt = np.copy(np.transpose(matriz_R)) # matriz_rt é a matriz R transposta

    vetor_y = subs.resolve_substituicao(matriz_Rt, vetor_b) # Faz o cálculo de Rt * y = b para obter o vetor y
    vetor_x = subs.resolve_substituicao(matriz_R, vetor_y) # Faz o cálculo de R * x = y para obter o vetor x (resultado)

    return vetor_x # Retorna o vetor x (resultado)