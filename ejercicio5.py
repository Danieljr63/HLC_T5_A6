def bubble_sort(lista):
    numero = len(lista)
    for i in range(numero):
        for j in range(numero-1-i):
            if lista[j] < lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

lista = [8,3,2,4,55,667888,22]
print(bubble_sort(lista))