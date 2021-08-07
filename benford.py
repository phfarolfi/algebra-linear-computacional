import numpy as np
import pandas as pd

def ler_dados_benford(file_name): # Le o arquivo do excel que contém os dados para testar o algoritmo de ocorrências (Benford)
    df_benford = pd.read_excel(r"dados/"+file_name+".xlsx", header=None)
    dataset_benford = np.array(df_benford) # Converte a matriz de dados em um array numpy
    return dataset_benford

def benford(dados):
    n, m = np.shape(dados)
    primeiro_digito = np.zeros((n,m)) # Matriz auxiliar para armazenar o primeiro dígito de cada posição da matriz de dados

    # Looping para armazenar os primeiros dígitos dos elementos da matriz de dados na matriz primeiro_digito
    for j in range(m):
        for i in range(n):
            num = [x for x in str(dados[i,j])]
            for value in num:
                if value != '0' and value != '.' and value != '-':
                    primeiro_digito[i,j] = int(value)
                    break

    # Verifica as ocorrências de 1 a 9 na matriz primeiro_digito por colunas
    for i in range(1, 10):
        count = np.count_nonzero(primeiro_digito == i, axis=0)
        # Mostra a porcentagem de ocorrências pra cada ocorrência de 1 a 9 da matriz primeiro_digito
        for j in range(m):
            if j == 0:
                print('Porcentagem de ocorrência de "'+str(i)+'" em cada coluna:', end=' ')
            print("{:.4f}".format((count[j]/n)*100)+'%', end=' | ')
        print('')
