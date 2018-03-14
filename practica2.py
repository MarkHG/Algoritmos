def busqueda_secuencial(lista, x):
    i = 0
    while (i < len(lista)):
        if (lista[i] == x):
            return i
        i+=1 #incremento


print (busqueda_secuencial([1,2,3,4,5,6,7,8,9,10],9))

def busqueda_binaria (lista, x, a, b):

    centro = int(len(lista)/2)
    if (a == b + 1):
        return -1
    elif (lista[centro] == x):
        return centro
    elif (x < lista[centro]):
        return busqueda_binaria(lista,x,a,centro)

    elif (x > lista[centro]):
        return busqueda_binaria(lista,x,b,centro)

print (busqueda_binaria([1,2,3,4,5,6,7,8,9,10],1,6,8))

def busqueda_exponencial(lista,n,x):
    if (lista[0] == x):
        return 0
    limite = 2 ** 1
    while (limite < n and lista[limite] <= x):
        limite = limite * 2
print (busqueda_exponencial([1,2,3,4,5,6,7,8,9,10],2,3))
