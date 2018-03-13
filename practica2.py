def busqueda_secuencial(lista, x):
    i = 0
    while (i < len(lista)):
        if (lista[i] == x):
            return i
        i+=1 #incremento


print (busqueda_secuencial([1,2,3,4,5,7,8,9,10], 9))

def busqueda_binaria (lista, x, a, b):

    centro = len(lista)/2
    if (a == b + 1):
        return -1
    elif (lista[centro] == x):
        return centro
    elif (x < lista[centro]):
        return busqueda_binaria(lista,x,a,centro)

    elif (x > lista[centro]):
        return busqueda_binaria(lista,x,b,centro)

def busqueda_exponencial(lista,n,x):
    if (arr[0] == x):
        return 0
    limite = 2 ** 1
    while (limite < n and lista[limite] <= x):
        limite = limite * 2
