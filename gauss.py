import substituicao as subs

def eliminacao_gauss(matriz_A, vetor_b):
    n = len(matriz_A)

    for i in range(n-1):
        for j in range(i+1, n):
            x = matriz_A[j,i]/matriz_A[i,i] # x é o multiplicador necessário para executar a eliminação
            for k in range(i, n):
                matriz_A[j,k] -= matriz_A[i,k] * x # aplica o multiplicador x para zerar os elementos abaixo da diagonal principal
            vetor_b[j] -= vetor_b[i] * x

    return subs.resolve_substituicao(matriz_A, vetor_b) # retorna o vetor resultado