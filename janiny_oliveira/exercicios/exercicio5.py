lista_a = [ 4, 7, -2, 3, 0, 1900, -2, 7 ]
lista_b = [ 7, 0, 2000, -34.40, 0, -2, 1900 ]

tam_lista_a = len(lista_a)
tam_lista_b = len(lista_b)
lista_int = []
k = 0

for i in range (tam_lista_a):
    for j in range (tam_lista_b):
        if lista_a[i] == lista_b[j]:
            lista_int.append(lista_a[i])
            k = k+1
lista_int.sort()
print ("intersec_desc(lista_a,lista_b) #",lista_int)

