def elimina_duplicados(lista: list) -> list:
    """
    Devuelve la lista resultante de eliminar los elementos duplicados, 
    conservando para el resto de elementos el orden de la lista original.

    Parámetros:
    lista (list): Lista de elementos que puede contener duplicados.
    
    Devuelve:
    list: La lista sin elementos duplicados, manteniendo el orden original.
    """
    #conjunto = set()      #creamos un conjunto para almacenar los elementos, siempre que aparezcan por primera vez
    #res = []
    #for a in lista:
    #    antes = len(conjunto)
    #    conjunto.add(a)          #añadimos los elementos del conjunto a la lista
    #    ahora = len(conjunto)
    #    if antes != ahora:
    #        res.append(a)
    #return res
    
    #versión optimizada, de esta forma ahorramos dos variables (antes y ahora) 
    #y aprovechamos la velocidad de los conjuntos con los operadores de pertenencia (not in)
    vistos = set()    
    res = []
    for elemento in lista:
        if elemento not in vistos:
            vistos.add(elemento)
            res.append(elemento)
    return res


def une_conjuntos(lista_de_conjuntos: list[set]) -> set:
    """
    Devuelve el conjunto resultante de la unión de todos los conjuntos de la lista.

    Parámetros:
    lista_de_conjuntos (list[set]): Lista de conjuntos a unir.
    
    Devuelve:
    set: El conjunto resultante de la unión de todos los conjuntos.
    """
    res = set()
    for conjunto in lista_de_conjuntos:
        #res = res.union(conjunto) ---> al crear un conjunto ya estamos haciendo que no haya duplicados, no es necesario usar la unión
        res.update(conjunto) #con update se modifica el conjunto original con los nuevos elementos
    return res


def intersecta_conjuntos(lista_de_conjuntos: list[set]) -> set:
    """
    Devuelve el conjunto resultante de la intersección de todos los conjuntos de la lista.

    Parámetros:
    lista_de_conjuntos (list[set]): Lista de conjuntos a intersectar.
    
    Devuelve:
    set: El conjunto resultante de la intersección de todos los conjuntos.
    """
    if not lista_de_conjuntos: #si la lista está vacía devolvemos un conjunto vacío
        return set()
    
    res = lista_de_conjuntos[0]
    for conjunto in lista_de_conjuntos[1:]:
        res = res.intersection(conjunto)
    return res