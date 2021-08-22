import numpy as np
import pandas as pd

def ler(file_matrix, file_array):
    df_matriz = pd.read_excel(r"dados/"+file_matrix+".xlsx", header=None) # Le o arquivo do excel que contém a matriz A sem cabeçalho
    df_vetor = pd.read_excel(r"dados/"+file_array+".xlsx", header=None) # Le o arquivo do excel que contém o vetor b sem cabeçalho
    matriz = np.array(df_matriz, dtype='f8') # Converte a matriz A em um array da numpy
    vetor = np.ravel(np.array(df_vetor, dtype='f8')) # Converte o vetor b em um array da numpy
    return matriz, vetor

def eliminacao_gauss(matriz_A):
    n = len(matriz_A)
    Am = np.copy(matriz_A)

    for i in range(n):
        for j in range(i+1, n):
            if Am[i,i] == 0:
                Am[i,i] = 1e-18

            x = Am[j,i]/Am[i,i] # x é o multiplicador necessário para executar a eliminação
            for k in range(n):
               Am[j,k] -= Am[i,k] * x # aplica o multiplicador x para zerar os elementos abaixo da diagonal principal

    return calcula_determinante(Am, n) # retorna o vetor resultado

def calcula_determinante(matriz_A, n):
    det = 1.0
    for i in range(n):
        det *= matriz_A[i,i]
    return det

a = np.array([[1,3,5,9], [1,3,1,7], [4,3,9,7], [5,2,0,9]])
matriz, vetor = ler("matriz_A", "vetor_b")
det = np.linalg.det(a)
print(det)
det = eliminacao_gauss(a)
print(det)