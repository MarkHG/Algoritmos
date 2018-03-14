def busqueda_secuencial(lista, x):
    i = 0
    while (i < len(lista)):
        if (lista[i] == x):
            return i
        i+=1 #incremento


print (busqueda_secuencial([1,2,3,4,5,6,7,8,9,10],9))

def busqueda_binaria (lista, x, a, b):

    centro = (a+b)//2
    if (a > b + 1):
        return -1
    elif (lista[centro] == x):
        return centro
    elif (x < lista[centro]):
        return busqueda_binaria(lista,x,a,centro)
    elif (x > lista[centro]):
        return busqueda_binaria(lista,x,centro,b)

print (busqueda_binaria([1,2,3,4,5,6,7,8,9,10],2,0,9))

def busqueda_exponencial(lista,n,x):
    if (lista[0] == x):
        return 0
    limite = 1
    while (limite < n and lista[limite] <= x):
        limite *= 2
    return busqueda_binaria(lista, x, limite//2,limite)

print (busqueda_exponencial([1,2,3,4,5,6,7,8,9,10],9,1))


