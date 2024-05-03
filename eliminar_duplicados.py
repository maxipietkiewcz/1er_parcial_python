list = [1, 2, 3, 4, 4, 5, 6, 6, 7]

def eliminar_duplicados(lista):
    lista = (set(lista))
    return lista


print(eliminar_duplicados(list))