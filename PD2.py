
def PD(lista):
    soma = lista[0]
    aux = 0
 
    encontrou_positivo = False
    
    for i in range(len(lista)):
        if lista[i] > 0:
            soma = lista[i]
            aux = soma  
            encontrou_positivo = True
            break
            
    if not encontrou_positivo:
        return 0  
            
    
    for i in range(i+1,len(lista)):
        
        if soma + lista[i] >= 0:
            soma = lista[i] + soma
        else:
            soma = 0
        if aux < soma:
            aux = max(aux, soma)
    return aux

n = int(input(''))
lista = list()
lista = list(map(int, input().split()))
aux = PD(lista)
print(aux)


