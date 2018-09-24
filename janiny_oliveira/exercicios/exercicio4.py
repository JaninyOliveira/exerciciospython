print('Programa para que recebe um número de entrada, soma os números entre si, e retorna TRUE, caso seja 0 ou divisível por 9 ou FALSE, caso não seja')
print()

Numero = input("informe um numero: ")
soma = 0
for n in Numero:
    soma += int(n)
     
if soma == 0 or soma % 9 == 0:
    var = "True"
    if soma == 0:
        print ("verifica_numero (",Numero,") #",var,", pois a soma",soma,"é 0")
    else:
        print ("verifica_numero (",Numero,") #",var,", pois a soma",soma,"é divisível por 9")
else:
    var = "False"
    print ("verifica_numero (",Numero,") #",var,", pois a soma",soma,"NÃO é 0 ou divisível por 9 ")

