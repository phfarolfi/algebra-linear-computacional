import numpy as np

def verifica_quadrada(matriz_A):
    linhas, colunas = np.shape(matriz_A)
    return linhas == colunas

def verifica_inversa(matriz_A):
    if verifica_quadrada(matriz_A):
        print("A matriz é quadrada")
        det = np.linalg.det(matriz_A)
        print("O determinante da matriz é:", det)
        return det != 0
    print("A matriz não é quadrada")
    return False

def verifica_simetria(matriz_A):
    if verifica_quadrada(matriz_A):
        n = len(matriz_A)
        for i in range(n):
            for j in range(n):
                if (i != j) and (matriz_A[i,j] != matriz_A[j,i]):
                    print("A matriz não é simétrica")
                    return False
        print("A matriz é simétrica")
        return True
    print("A matriz não é quadrada")
    return False

def verifica_pos_def(matriz_A):
    if verifica_quadrada(matriz_A) and verifica_inversa(matriz_A) and verifica_simetria(matriz_A):
        n = len(matriz_A)
        for i in range(n):
            soma = 0
            for j in range(n):
                soma += matriz_A[i,j]
            if(soma == 0):
                return False
        return True
    return False

def verifica_tridiagonal(matriz_A):
    linhas, colunas = np.shape(matriz_A)

    for i in range(linhas):
        for j in range(colunas):
            if np.abs(i-j) <= 1 and matriz_A[i,j] == 0:
                return False
            if np.abs(i-j) >= 2 and matriz_A[i,j] != 0:
                return False
    return True

def verifica_tri_superior(matriz_A, tol=1e-10):
    linhas = len(matriz_A)

    for i in range(linhas):
        for j in range(i):
            if np.fabs(matriz_A[i,j]) > tol:
                return False
    return True

def verifica_tri_inferior(matriz_A, tol=1e-10):
    colunas = len(matriz_A[0])

    for j in range(colunas):
        for i in range(j):
            if np.fabs(matriz_A[i,j]) > tol:
                return False
    return True

def traco(matriz_A):
    linhas, colunas = np.shape(matriz_A)
    n, traco = min((linhas, colunas)), 0

    print(matriz_A)
    for i in range(n):
        traco += matriz_A[i,i]
    return traco

def traco_maior_que_quatro(traco):
    if traco > 4:
        print("O traço da matriz é "+ str(traco) +", portanto é maior que 4")
        return True
    print("O traço da matriz é "+ str(traco) +", portanto não é maior que 4")
    return False

''' CRITÉRIOS DE CONVERGÊNCIA DOS MÉTODOS ITERATIVOS '''

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
    
    print("Maior betão:", np.max(vetor_betao))
    if np.max(vetor_betao) < 1: # Verifica se a condição do critério de Sassenfeld (max(B) < 1) é satisfeita
        return True
    return False