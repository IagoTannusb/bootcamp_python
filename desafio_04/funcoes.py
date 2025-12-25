# Implementação do algoritmo de ordenação por seleção
lista = [64, 34, 25, 12, 22, 11, 90]

def ordernar_lista(lista: list) -> list:
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]

    return lista

# Ordenando a lista
print("Lista ordenada com função personalizada:", ordernar_lista(lista))

