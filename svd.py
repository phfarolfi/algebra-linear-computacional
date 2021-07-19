import numpy as np

'''
    SVD é a representação de uma matriz A em um produto de três matrizes: U, S e Vt

    U: Matriz m x m que são os autovetores de A*At normalizados
    S: Matriz diagonal m x n que contém a raiz quadrada dos autovalores de U e V em ordem decrescente
    V: Matriz n x n que são os autovetores de At*A normalizados
'''

def calcula_sigma(w1, w2, n, m): # Função que ajusta a matriz sigma e já a retorna com o número certo de linhas e colunas, com os autovalores ordenados na diagonal principal, do maior para o menor
    matriz_S = np.zeros((n, m)) # Cria a matriz sigma com dimensão n x m (necessário para conseguir fazer a multiplicação USV) com todos os termos iguais a zero

    for i in range (len(w2)): # Junta todos os autovalores diferentes de zero encontrados de A*At e At*A no array w1
        if w2[i] != 0:
            w1 = np.append(w1, np.round(w2[i])) # Coloquei pra arredondar os valores porque ele tava dando como diferente 9.99999995 e 10 *emoji de palhaço*

    w1 = np.unique(w1) # Elimina os valores repetidos no array w1

    for i in range (n):
        matriz_S[i][i] = np.sqrt(w1[n-1-i]) # Adiciona os autovalores do maior para o menor na diagonal principal da matriz sigma

    return matriz_S # Retorna a matriz sigma

matriz_A = np.loadtxt("matriz_exemplo.txt", dtype='f8') # Carrega a matriz que eu estava usando de exemplo

A_At = np.matmul(matriz_A, np.transpose(matriz_A)) # A_At é a multiplicação de A por A(transposta)
At_A = np.matmul(np.transpose(matriz_A), matriz_A) # At_A é a multiplicação de A(transposta) por A

w1, matriz_U = np.linalg.eig(A_At) # Aqui eu utilizo a função da própria numpy que retorna os autovalores (w1) e autovetores (matriz U já normalizada) de A*At
w2, matriz_V = np.linalg.eig(At_A) # Aqui eu utilizo a função da própria numpy que retorna os autovalores (w1) e autovetores (matriz V já normalizada) de At*A

matriz_S = calcula_sigma(w1, w2, len(matriz_A), len(matriz_A[0])) # Chamei a função que cria a matriz sigma com os autovalores encontrados em w1 e w2

# Mostra os resultados encontrados pelo que eu fiz acima
print("Matriz U: \n", matriz_U, "\n")
print("Matriz S: \n", matriz_S, "\n")
print("Matriz Vt: \n", np.transpose(matriz_V))
print("\n", "-"*60, "\n")

# Aqui eu já utilizo diretamente a função SVD da numpy
U, s, V = np.linalg.svd(matriz_A)
S = np.diag(s)
Vt = np.transpose(V)

# Mostra os resultados da função SVD da numpy
print("Matriz U (numpy): \n", U, "\n")
print("Matriz S (numpy): \n", S, "\n")
print("Matriz Vt (numpy): \n",Vt, "\n")
print("\n", "-"*60, "\n")

numpy_US = np.matmul(U, matriz_S) # Multiplica U por S
numpy_USVt = np.matmul(numpy_US, V) # Multiplica (U*S) por Vt

matriz_US = np.matmul(matriz_U, matriz_S)
matriz_USVt = np.matmul(matriz_US, np.transpose(matriz_V))

print("Matriz_A: \n", matriz_A)
print("Matriz USVt = A(predo): \n", matriz_USVt)
print("Matriz USVt = A(numpy): \n", numpy_USVt) # O resultado deveria ser a matriz A, mas tá diferente (porém próximo)