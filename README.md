# exerciciospython
Questão 1

Escreva uma função Python que receba por parâmetro um nome, um valor de salário
fixo (número com precisão) e outro valor que é o total de vendas no mês de um
vendedor. Sabemos que devemos retirar 10% do salário fixo para impostos e que o
vendedor recebe 15% de comissão de suas vendas, mas que também devemos diminuir
10% em cima do valor líquido recebido nas comissões, pois o governo precisa arrecadar
impostos. Seu objetivo é calcular o lucro total do vendedor ao final do mês. Exemplo:
lucro(“Capitão América”, 500, 1000) # 585


Questão 2

Escreva uma função Python que receba por parâmetro qualquer número positivo que
representa a idade de uma pessoa em dias e retorne uma string com a equivalência dessa
idade, no formato ano(s), mes(es) e dia(s). Para simplificar, assuma que os anos sempre
têm 365 dias e os meses sempre têm 30 dias. Exemplos:
idade(400) # “1 ano(s), 1 mes(es) e 5 dia(s)”
idade(800) # “2 ano(s), 2 mes(es) e 10 dia(s)”
idade(30) # “0 ano(s), 1 mes(es) e 0 dia(s)”


Questão 3

Escreva uma função Python que retorne a média dos números naturais de uma matriz
informada. Exemplo de como o código deve funcionar:
matriz = [ [ 1, 0, -5, 2 ], [ 7, 3, 6, 10 ], [ 0, 3.14, 1, 0 ] ]
media(matriz) # 3


Questão 4

Escreva uma função Python que receba um número de entrada e retorne:
True​ caso a soma de todos dígitos do número seja 0 ou múltiplo de 9
False​ para todos outros casos.
Exemplo:
verifica_numero(1892376) # True,​ pois 1+8+9+2+3+7+6 = 36, que é divisível por 9
verifica_numero(11) # False​, pois 1+1 não é divisível por 9


Questão 5

Escreva uma função Python que receba duas listas de números de entrada e retorne uma
outra lista com a interseção entre elas, ordenada do maior para o menor, exemplo:
lista_a = [ 4, 7, -2, 3, 0, 1900, -2, 7 ]
lista_b = [ 7, 0, 2000, -34.40, 0, -2, 1900 ]
intersec_desc(lista_a, lista_b) # [ 1900, 7, 0, -2, 7 ]
