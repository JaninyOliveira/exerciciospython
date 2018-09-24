print('Programa para calcular média dos números naturais de uma matriz')
print()
matriz = [ [ 10, 0, -5, 9 ], [ 7, 3, 6, 10 ], [ 0, 3.14, 1.8, 0 ] ]

linhas = len(matriz)
colunas = len(matriz[0])
soma = 0
count = 0

for i in range(linhas):
    for j in range(colunas):
        if (matriz[i][j]) >= 0:
            if int(matriz[i][j]) == (matriz[i][j]):
                soma = (matriz[i][j]) + soma
                count = count + 1
                              
print ("Média(matriz) =",(soma / count))

