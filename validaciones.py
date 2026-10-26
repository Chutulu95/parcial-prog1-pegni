CANTIDAD_MINIMA = 1
CANTIDAD_MAXIMA = 30
NOTA_MINIMA = 0
NOTA_MAXIMA = 10
LARGO_MINIMO_NOMBRE = 5


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


def validar_nombre(nombre):
    """Devuelve True si el nombre tiene 5 o más caracteres y solo letras."""
    if len(nombre) < LARGO_MINIMO_NOMBRE:
        return False

    for i in range(len(nombre)):
        caracter = nombre[i]

        minuscula = "a" <= caracter <= "z"
        mayuscula = "A" <= caracter <= "Z"
        espacio = caracter == " "

        if not (minuscula or mayuscula or espacio):
            return False

    return True


def pedir_nombre():
    """Pide el nombre de un alumno hasta que sea válido."""
    nombre = input("Ingrese el nombre del alumno: ")

    while not validar_nombre(nombre):
        print("Error, mínimo 5 caracteres y solo letras y espacios")
        nombre = input("Ingrese el nombre del alumno: ")

    return nombre