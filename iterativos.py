from criterios import criterio_linhas, criterio_sassenfeld
import numpy as np

def jacobi(matriz_A, vetor_b, vetor_x=None, N=10000, p=1e-10): # Função que executa o algoritmo de Jacobi
    n, m = len(matriz_A), len(matriz_A[0]) # n e m são as dimensões da matriz
    aux = 0 # Variável que vai auxiliar a armazenar as subtrações dos valores Aij*xj

    if vetor_x == None: # Se não é fornecido um vetor de aproximação inicial para x, ele é iniciado aqui com todos os elementos iguais a zero
        vetor_x = np.zeros(m)
    
    vetor_aux = np.copy(vetor_x) # Vetor auxiliar igual ao vetor x que representa a iteração k+1

    if criterio_linhas(matriz_A): # Verifica se o critério das linhas é satisfeito
        print("O critério das linhas foi satisfeito: O sistema converge.")
    else:
        print("ATENÇÃO: O critério das linhas não foi satisfeito.")

    for k in range(N): # Executa todas as iterações especificadas na chamada da função (N) se a condição de parada não for satisfeita
        for i in range(n):
            for j in range(n):
                if i != j: # Pula os elementos da diagonal principal pois eles não são utilizados
                    aux += matriz_A[i,j] * vetor_x[j] # Acumula as subtrações dos valores de Aij*xj

            vetor_aux[i] = (vetor_b[i] - aux)/matriz_A[i,i] # Executa a iteração do método com (bi-Aij*xj)/Aii
            aux = 0 # Zera a contagem do somatório dos valores novamente

        for i in range(n):
            if vetor_x[i] != 0 and np.abs(vetor_x[i] - vetor_aux[i])/np.abs(vetor_x[i]) <= p: # Condição de parada caso a variação relativa de uma iteração para outra seja menor que a tolerância p
                print("(Jacobi) Resultado encontrado com o critério de parada, na iteração:", k)
                return vetor_x

        vetor_x = np.copy(vetor_aux) # Atualiza o vetor_x (k) com os valores do vetor_aux (k+1)

    print("(Jacobi) Resultado encontrado com o número máximo de iterações.")
    return vetor_x # Retorna o vetor solução

''' ----------------------------------------------------------------------------------------------------------------------------------------------------------------- '''
    
def seidel(matriz_A, vetor_b, vetor_x=None, N=10000, p=1e-10): # Função que executa o algoritmo de Gauss-Seidel
    n, m = len(matriz_A), len(matriz_A[0]) # n e m são as dimensões da matriz
    aux = 0 # Variável que vai auxiliar a armazenar as subtrações dos valores Aij*xj

    if vetor_x == None: # Se não é fornecido um vetor de aproximação inicial para x, ele é iniciado aqui com todos os elementos iguais a zero
        vetor_x = np.zeros(m)

    vetor_aux = np.copy(vetor_x) # Vetor auxiliar igual ao vetor x que representa a iteração k+1

    if criterio_sassenfeld(matriz_A): # Verifica se o critério de Sassenfeld é satisfeito
        print("O critério de Sassenfeld foi satisfeito.")
    else:
        print("ATENÇÃO: O critério de Sassenfeld não foi satisfeito.")

    for k in range(N): # Executa todas as iterações especificadas na chamada da função
        for i in range(n):
            for j in range(m):
                if i != j: # Pula os elementos da diagonal principal pois eles não são utilizados
                    if i > j:
                        aux += matriz_A[i,j] * vetor_aux[j] # Acumula as subtrações dos valores de Aij*xj utilizando os valores que já foram atualizados (de 0 a i) que ficam no vetor auxiliar
                    else:
                        aux += matriz_A[i,j] * vetor_x[j] # Acumula as subtrações dos valores de Aij*xj utilizando os valores ainda não foram atualizados (de i+1 a n) que ficam no vetor x

            vetor_aux[i] = (vetor_b[i] - aux)/matriz_A[i,i] # Executa a iteração do método com (bi-Aij*xj)/Aii
            aux = 0 # Zera a contagem do somatório dos valores novamente

        for i in range(n): #Verifica elemento por elemento de vetor_x e do vetor_aux
            if vetor_x[i] != 0 and np.abs(vetor_x[i] - vetor_aux[i])/np.abs(vetor_x[i]) <= p: # Condição de parada caso a variação relativa de uma iteração para outra seja menor que a tolerância p
                print("(Seidel) Resultado encontrado com o critério de parada, na iteração:", k)
                return vetor_x

        vetor_x = np.copy(vetor_aux) # Atualiza o vetor_x (k) com os valores do vetor_aux (k+1)

    print("(Seidel) Resultado encontrado com o número máximo de iterações.")
    return vetor_x # Retorna o vetor solução

''' ----------------------------------------------------------------------------------------------------------------------------------------------------------------- '''

def sor(matriz_A, vetor_b, vetor_x=None, N=10000, p=1e-10, w=1.7): # Quando w = 1 é igual ao Seidel
    n, m = len(matriz_A), len(matriz_A[0]) # n e m são as dimensões da matriz
    aux = 0 # Variável que vai auxiliar a armazenar as subtrações dos valores Aij*xj

    if vetor_x == None: # Se não é fornecido um vetor de aproximação inicial para x, ele é iniciado aqui com todos os elementos iguais a zero
        vetor_x = np.zeros(m)

    vetor_aux = np.copy(vetor_x) # Vetor auxiliar igual ao vetor x que representa a iteração k+1

    if criterio_sassenfeld(matriz_A): # Verifica se o critério das linhas é satisfeito
        print("O critério de Sassenfeld foi satisfeito.")
    else:
        print("ATENÇÃO: O critério de Sassenfeld não foi satisfeito.")

    for k in range(N): # Executa todas as iterações especificadas na chamada da função
        for i in range(n):
            for j in range(m):
                if i != j: # Pula os elementos da diagonal principal pois eles não são utilizados
                    if i > j:
                        aux += matriz_A[i,j] * vetor_aux[j] # Acumula as subtrações dos valores de Aij*xj utilizando os valores que já foram atualizados (de 0 a i) que ficam no vetor auxiliar
                    else:
                        aux += matriz_A[i,j] * vetor_x[j] # Acumula as subtrações dos valores de Aij*xj utilizando os valores ainda não foram atualizados (de i+1 a n) que ficam no vetor x

            vetor_aux[i] = (1-w)*vetor_x[i] + (w*(vetor_b[i] - aux))/matriz_A[i,i] # Executa a iteração do método com (1-w)*xi(bi-Aij*xj)/Aii
            aux = 0 # Zera a contagem do somatório dos valores novamente

        for i in range(n): # Verifica elemento por elemento de vetor_x e do vetor_aux
            if vetor_x[i] != 0 and np.abs(vetor_x[i] - vetor_aux[i])/np.abs(vetor_x[i]) <= p: # Condição de parada caso a variação relativa de uma iteração para outra seja menor que a tolerância p
                print("(SOR) Resultado encontrado com o critério de parada, na iteração:", k)
                return vetor_x

        vetor_x = np.copy(vetor_aux) # Atualiza o vetor_x (k) com os valores do vetor_aux (k+1)

    print("(SOR) Resultado encontrado com o número máximo de iterações.")
    return vetor_x # Retorna o vetor solução