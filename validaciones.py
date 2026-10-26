CANTIDAD_MINIMA = 1
CANTIDAD_MAXIMA = 30
NOTA_MINIMA = 0
NOTA_MAXIMA = 10


def validar_entero_en_rango(mensaje, minimo, maximo):
    valido = False
    numero = 0
 
    while not valido:
        texto = input(mensaje)
        es_entero = True
 
        for i in range(len(texto)):
            if not ("0" <= texto[i] <= "9"):
                es_entero = False
 
        if es_entero and len(texto) > 0:
            numero = int(texto)
 
            if minimo <= numero <= maximo:
                valido = True
            else:
                print("Error, ingrese un número entre", minimo, "y", maximo)
        else:
            print("Error, ingrese un número entero")
 
    return numero
 
 
def validar_cantidad():
    mensaje = "Ingrese la cantidad de alumnos (1 - 30): "
    return validar_entero_en_rango(mensaje, CANTIDAD_MINIMA, CANTIDAD_MAXIMA)
 
 
def validar_nota(numero_parcial):
    mensaje = "Ingrese la nota del " + numero_parcial + " parcial (0 - 10): "
    return validar_entero_en_rango(mensaje, NOTA_MINIMA, NOTA_MAXIMA)