def PD(lista):
    soma = lista[0]
    aux = 0

    for i in range(1,len(lista)):
        if soma + lista[i] > 0:
            soma = lista[i] + soma
        else:
            soma = 0
        if aux < soma:
            aux = soma
    return aux

n = int(input())
lista = list()
num = 0
for i in range(n):
    num = int(input())
    lista.append(num)
    
print(PD(lista))


