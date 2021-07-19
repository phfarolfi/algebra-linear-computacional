import resolucao_sistemas_triangulares as rst

def eliminacao_gauss(matriz, vetor):
    n = len(matriz)

    for i in range(n-1):
        for j in range(i+1, n):
            x = matriz[j][i]/matriz[i][i] # x é o multiplicador necessário para executar a eliminação

            for k in range(i, n):
                matriz[j][k] -= matriz[i][k] * x # aplica o multiplicador x para zerar os elementos abaixo da diagonal principal
            vetor[j] -= vetor[i] * x

    return rst.resolve_subs_tras(matriz, vetor) # retorna o vetor resultado