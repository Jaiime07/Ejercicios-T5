from collections import Counter


def sustituye_palabras(texto: str, diccionario: dict[str, str]) -> str:
    """Sustituye en el texto las palabras que aparecen en el diccionario como claves por sus valores asociados.

    Parámetros:
        texto: Texto en el que se van a sustituir las palabras.
        diccionario: Diccionario con las palabras a sustituir como claves y las palabras sustitutas como valores.

    Devuelve:
        Texto resultante de las sustituciones.
    """
    for clave, valor in diccionario.items():
        #if clave in texto:     el if sobra: si replace no encuentra la clave en el texto, no hace nada
            texto = texto.replace(clave, valor)
    return texto


def indexa_por_iniciales(texto: str) -> dict[str, set[str]]:
    """
    Construye un diccionario que indexa las distintas palabras del texto
    (pasado a minúsculas) por sus iniciales.
    
    Parámetros:
        texto: Texto del que se van a extraer las palabras.
    
    Devuelve:
        Diccionario que asocia a cada inicial el conjunto de palabras
         que comienzan por dicha inicial.
    
    """
    res = {}
    texto = texto.lower()
    palabras = texto.split()
    for palabra in palabras:
         if palabra.isalnum():
            inicial = palabra[0]
            if inicial not in res:
                res[inicial] = {palabra}
            else:
                res[inicial].add(palabra)
    return res
                   

                   

def construye_frecuencias_bigramas(texto: str) -> dict[str, float]:
    """
    Construye un diccionario con las frecuencias normalizadas de cada bigrama 
    en el texto dado, ignorando mayúsculas y minúsculas.

    Un bigrama es una secuencia de dos letras consecutivas en el texto.

    Cada frecuencia estará contenida entre 0 y 1.
    
    Parámetros:
        texto: Texto del que se van a contar los bigramas.
    Devuelve:
        Diccionario que asocia a cada bigrama su frecuencia normalizada en el texto.
    """
    texto = texto.lower()
    bigramas = []
    recuento_frecuencia = {}
    for a, b in zip(texto, texto[1:]):
        if (a+b).isalpha():
            bigramas.append(a+b)

    recuento = Counter(bigramas)

    for bigrama, apariciones in recuento.items():
        frecuencia = apariciones / len(bigramas)
        recuento_frecuencia[bigrama] = frecuencia
    return recuento_frecuencia
        



def calcula_distancia_media_frecuencias(freq1: dict[str, float], freq2: dict[str, float]) -> float:
    """
    Calcula la distancia media entre las frecuencias normalizadas
    representadas por dos diccionarios de frecuencias.

    Parámetros:
        freq1: Primer diccionario de frecuencias.
        freq2: Segundo diccionario de frecuencias.

    Devuelve:
        Distancia media entre los dos vectores de frecuencias, o 0.0 si ambos diccionarios están vacíos.
    """
    if len(freq1) == 0 and len(freq2) == 0:
        return 0.0
    todas_claves = set(freq1).union(set(freq2))
    suma = 0
    for bigrama in todas_claves:
        suma += abs(freq1.get(bigrama, 0) - freq2.get(bigrama, 0))
    return suma / len(todas_claves)


def identifica_idioma(textos_ejemplo: dict[str, str], texto_a_identificar: str) -> str:
    """
    Identifica el idioma de un texto comparando sus frecuencias de bigramas
    con las frecuencias de bigramas de textos de ejemplo en distintos idiomas.

    Parámetros:
        textos_ejemplo: Diccionario que asocia a cada idioma (por ejemplo 'es') un texto de ejemplo en ese idioma.
        texto_a_identificar: Texto cuyo idioma se quiere identificar.

    Devuelve:
        El idioma identificado del texto.
    """
    




