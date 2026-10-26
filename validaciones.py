"""En este modulo nos encontramos con las funciones que validan el correcto ingreso de los datos solicitados, usese a gusto"""


CANTIDAD_MINIMA = 1
CANTIDAD_MAXIMA = 30
NOTA_MINIMA = 0
NOTA_MAXIMA = 10
LARGO_MINIMO_NOMBRE = 5
# Constantes con valores fijos


def validar_entero(mensaje, minimo, maximo):
    """Se pide un numero ENTERO hasta que sea valido segun que funcion lo necesite"""    
    valido = False
    numero = 0
 
    while not valido:
        texto = input(mensaje)
        es_entero = True

    # Revisamos lo ingresado para verificar que sea un numero entero
        for i in range(len(texto)):
            if not ("0" <= texto[i] <= "9"):
                es_entero = False
 
        if es_entero and len(texto) > 0:
            numero = int(texto)
 
            if minimo <= numero <= maximo:
                valido = True
            else:
                print("¡Error!, ingrese un número entre", minimo, "y", maximo)
        else:
            print("¡Error!, ingrese un número entero")
 
    return numero
 
 
def validar_cantidad():
    """Pide la cantidad de alumnos"""
    # No hacen falta argumentos ya que la funcion validar_entero ya los tiene
    mensaje = "Ingrese la cantidad de alumnos (1 - 30): "
    return validar_entero(mensaje, CANTIDAD_MINIMA, CANTIDAD_MAXIMA)
 
 
def validar_nota(parcial):
    """"Pide la nota de los parciales"""
    # El argumento parcial es "primer" o "segundo" en la funcion cargar_datos
    mensaje = "Ingrese la nota del " + parcial + " parcial: "
    return validar_entero(mensaje, NOTA_MINIMA, NOTA_MAXIMA)


def validar_nombre(nombre):
    """Simplemente chequea que el nombre ingresado cumpla las condiciones correctas"""
    if len(nombre) < LARGO_MINIMO_NOMBRE:
        return False
    
# Recorre el nombre ingresado para ver que no se ponga lo que no se pide
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
    nombre = input("Ingrese el nombre y apellido del alumno: ")

# Pedimos el nombre la cantidad de veces necesarias hasta que validar_nombre de el ok y se pueda proceder
    while not validar_nombre(nombre):
        print("¡Error!, mínimo 5 caracteres, solo letras y espacios")
        nombre = input("Ingrese el nombre y apellido del alumno: ")

    return nombre