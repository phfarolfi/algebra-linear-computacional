import numpy as np

def verifica_quadrada(matriz):
    row, col = np.shape(matriz)
    print(row, col)
    return row == col

def verifica_inversa(matriz):
    if verifica_quadrada(matriz):
        det = np.linalg.det(matriz)
        return det != 0
    return False

def verifica_simetria(matriz):
    if verifica_quadrada(matriz):
        n = len(matriz)
        for i in range(n):
            for j in range(n):
                if (i != j) and (matriz[i,j] != matriz[j,i]):
                    return False
        return True
    return False

def verifica_pos_def(matriz):
    if verifica_quadrada(matriz) and verifica_inversa(matriz) and verifica_simetria(matriz):
        n = len(matriz)
        for i in range(n):
            soma = 0
            for j in range(n):
                soma = soma + matriz[i,j]
            if(soma == 0):
                return False
        return True
    return False

''' Critérios de métodos iterativos '''

def criterio_linhas(matriz_A): # Verificar o critério das linhas para o método de Jacobi
    n, m = len(matriz_A), len(matriz_A[0]) # n e m são as dimensões da matriz
    soma = 0

    for i in range(n): # Percorre toda a matriz
        for j in range(m):
            if i != j: # Desconsidera os termos da diagonal principal
                soma += np.abs(matriz_A[i,j])

        if soma >= np.abs(matriz_A[i,i]): # Verifica se a soma de todos os termos (sem contar o termo da diagonal principal) de cada linha é menor ou maior que o termo da diagonal principal (Critério das linhas)
            return False

        soma = 0
    return True

def criterio_sassenfeld(matriz_A):
    n, m = len(matriz_A), len(matriz_A[0]) # n e m são as dimensões da matriz
    aux = 0 # Variável que auxilia nos somatórios dos termos tanto de Aij*Beta, quanto de Aij
    vetor_betao = np.zeros(m) # Vetor de Betas iniciado com termos iguais a zero

    for i in range(n):
        for j in range(i): # j vai até i-1 (desconsidera a primeira iteração)
            aux += np.abs(matriz_A[i,j]) * vetor_betao[j] # A partir da segunda iteração, inclui a multiplicação de Aij pelos Betas anteriores no somatório (já que na primeira iteração não há Betas anteriores, obviamente)
        for j in range(i,n):
            aux += np.abs(matriz_A[i,j]) # Somatório dos módulos dos termos de Aij
        vetor_betao[i] = aux/np.abs(matriz_A[i,i]) #Divide o valor da soma pelo termo da diagonal principal
        aux = 0 # Zera a variável auxiliar pra próxima iteração
    
    print("Maior betão:",np.max(vetor_betao))
    if np.max(vetor_betao) < 1: # Verifica se a condição do critério de Sassenfeld (max(B) < 1) é satisfeita
        return True
    return False