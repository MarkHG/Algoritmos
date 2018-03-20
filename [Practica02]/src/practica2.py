import sys


def lectura(archivo):
    'Lectura de un archivo'
    lista=[]
    archivo= open(archivo,"r")
    for linea in archivo:
        linea2=linea.split(" ")
        for elem in linea2:
            if(elem is not "\n"):
                entero=int(elem)
                lista.append(entero)
    return lista


def busqueda_secuencial(lista, x):
    'Algoritmo Busqueda Secuencial'
    i = 0
    while (i < len(lista)):
        if (lista[i] == x):
            return i
        i+=1 #incremento


def busqueda_binaria (lista, x, a, b):
    'Algoritmo Busqueda Binaria'
    centro = (a+b)//2
    if (a > b + 1):
        return -1
    elif (lista[centro] == x):
        return centro
    elif (x < lista[centro]):
        return busqueda_binaria(lista,x,a,centro)
    elif (x > lista[centro]):
        return busqueda_binaria(lista,x,centro,b)

def min (x, y):
    'Funcion que regresa el menor entre dos numeros'
    if (x < y):
        return x
    else:
         return y

def busqueda_exponencial(lista,n,x):
    'Algoritmo Busqueda Exponencial'
    if (lista[0] == x):
        return 0
    limite = 1
    while (limite < n and lista[limite] <= x):
        limite *= 2
    return busqueda_binaria(lista,x,limite//2, min(limite,len(lista)))



def busqueda_interpolacion(z, X, n):
    'Algoritmo de Busqueda por Interpolacion'
    izq = 0
    der = n-1
    p = 0
    while X[der] >= z and z >= X[izq]:
        j = izq + ((z - X[izq]) * (der - izq) / (X[der]-X[izq]))
        i= int(j)
        if z > X[i]:
            izq = i + 1
        elif z < X[i]:
            der = i - 1
        else:
            return (i,p+1)
        p += 1
    if X[izq] == z:
        return (izq,p)
    else:
        return (-1,p)

s = []
for i in range(500):
    if i < 100:
        s.append(i)
    elif i < 200:
        s.append(s[i-1] + 2*i)
    elif i < 300:
        s.append(s[i-1] + 3*i)
    elif i < 400:
        s.append(s[i-1] + 4*i)
    else:
        s.append(s[i-1] + 5*i)

t = []
for i in range(500):
    if i == 499:
        t.append(2**i)
    else:
        t.append(i)


if __name__ == "__main__":
    s=sys.argv
    archiv=s[1]
    numero=int(s[2])
    algoritmo=s[3]

    lista=lectura(archiv)
    x=len(lista)
    print(lista)

    if(algoritmo == "secuencial"):
        print (busqueda_secuencial(lista,numero))
    elif(algoritmo == "binaria"):
        print (busqueda_binaria(lista,numero,0,x))
    elif(algoritmo == "exponencial"):
        print (busqueda_exponencial(lista,len(lista),numero))
    elif(algoritmo == "interpolacion"):
        print (busqueda_interpolacion(numero,lista,x))
    else:
        print("no reconocido")
