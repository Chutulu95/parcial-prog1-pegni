"""En este modulo esta el nucleo de todo el programa, por favor usese con respeto, cualquier consulta contactenos"""


from validaciones import pedir_nombre, validar_nota


VOCALES = "aeiouAEIOU"
PROMEDIO_PROMOCION = 6
PROMEDIO_APROBACION = 4
# Constanstes con valores fijos


def crear_lista(cantidad, valor_inicial):
    """Crea una lista vacia con la cantidad necesaria"""
    # La lista va a estar vacia hasta que se rellene con los datos que se piden despues
    lista = []
    for i in range(cantidad):
        lista = lista + [valor_inicial]
    return lista


def cargar_datos(nombres, nota1, nota2, cantidad):
    """Pide los datos de los alumnos"""
    # Recorre el dato para validarlo con las funciones correspodientes
    # Guarda esos datos en las listas creadas anteriormente, modificandolas sin necesidad de retornar nada
    for i in range(cantidad):
        print()
        print("Alumno", i + 1)
        nombres[i] = pedir_nombre()
        nota1[i] = validar_nota("primer")
        nota2[i] = validar_nota("segundo")


def hay_alumnos(cantidad):
    "Chequea que haya datos cargados, si no hay se avisa"
    # Sirve para los case 2-6, ya que esos funcionan solo si hay datos almacenados en las lista
    if cantidad == 0:
        print("No ingresaste nada, volve a la opcion 1 para continuar.")
        return False
    return True


def calcular_promedios(notas1, notas2):
    """Guarda los promedios de los alumnos en una lista"""
    # Los promedios se calculan una vez y se guardan para reutilizarlos
    promedios = []
    for i in range(len(notas1)):
        promedio = (notas1[i] + notas2[i]) / 2
        promedios = promedios + [promedio]
    return promedios


def calcular_promedio_general(promedios):
    """"Calcula el promedio general del curso"""
    # Va sumando todos los promedios y despues los divide por la cantidad de alumnos (promedios)
    acumulador = 0
    for i in range(len(promedios)):
        acumulador = acumulador + promedios[i]
    return acumulador / len(promedios)


def buscar_posicion_mejor(promedios):
    """Da la posicion del mejor promedio"""
    # Recorre la lista de promedios buscando el numero mas alto
    posicion_mejor = 0
    for i in range(1, len(promedios)):
        if promedios[i] > promedios[posicion_mejor]:
            posicion_mejor = i
    return posicion_mejor


def buscar_posicion_peor(promedios):
    """Da la posicion del peor promedio"""
    # Recorre la lista de promedios buscando el numero mas bajo
    posicion_peor = 0
    for i in range(1, len(promedios)):
        if promedios[i] < promedios[posicion_peor]:
            posicion_peor = i
    return posicion_peor


def contar_promocionan(promedios):
    """Cuenta la cantidad de alumnos con promedio = or > 6"""
    # For recorre todos los promedios y si cumple la condicon se suma a contador
    contador = 0
    for i in range(len(promedios)):
        if promedios[i] >= PROMEDIO_PROMOCION:
            contador = contador + 1
    return contador


def contar_aprueban(promedios):
    """Cuenta la cantidad de alumnos con promedio entre 4 y 6"""
    # For recorre todos los promedios y si cumple la condicon se suma a contador
    contador = 0
    for i in range(len(promedios)):
        if PROMEDIO_APROBACION <= promedios[i] < PROMEDIO_PROMOCION:
            contador = contador + 1
    return contador


def contar_desaprueban(promedios):
    """Cuenta la cantidad de alumnos con promedio < 4"""
    # For recorre todos los promedios y si cumple la condicon se suma a contador
    contador = 0
    for i in range(len(promedios)):
        if promedios[i] < PROMEDIO_APROBACION:
            contador = contador + 1
    return contador


def mostrar_alumno(nombres, nota1, nota2, promedios, posicion):
    """Busca el alumno ingresado en las listas guardadas"""
    # Con el dato ingresado busca la posicion y luego muestra todo lo necesitado
    print("Alumno:", nombres[posicion])
    print("Parcial 1:", nota1[posicion])
    print("Parcial 2:", nota2[posicion])
    print("Promedio:", promedios[posicion])


def mostrar_listado(nombres, nota1, nota2, promedios):
    """Muestra todos los alumnos usando de argumentos las listas que tremos de main"""
    # Por cada vuelta del for muestra un alumno
    for i in range(len(nombres)):
        if i > 0:
            print()
            # Linea en blanco para separar entre alumnos
        mostrar_alumno(nombres, nota1, nota2, promedios, i)


def mostrar_estadisticas(nombres, promedios):
    """Llama a todas las funciones de datos y los muestra"""
    # No calcula nada, todo ya esta en su funcion
    posicion_mejor = buscar_posicion_mejor(promedios)
    posicion_peor = buscar_posicion_peor(promedios)
    print("Promedio general:", calcular_promedio_general(promedios))
    print("Mejor promedio:", nombres[posicion_mejor],
          "con", promedios[posicion_mejor])
    print("Peor promedio:", nombres[posicion_peor],
          "con", promedios[posicion_peor])
    print("Promocionan:", contar_promocionan(promedios))
    print("Aprueban:", contar_aprueban(promedios))
    print("Desaprueban:", contar_desaprueban(promedios))


def ordenar_burbuja(nombres, notas1, notas2, promedios):
    """Ordena de mayor a menor"""
    cantidad = len(promedios)
    for pasada in range(cantidad - 1):
        for i in range(cantidad - 1 - pasada):
            if promedios[i] < promedios[i + 1]:
                # Intercambio con "auxiliar", lista por lista
                # Variable auxiliar para no perder el valor que se pisa
                auxiliar = promedios[i]
                promedios[i] = promedios[i + 1]
                promedios[i + 1] = auxiliar

                auxiliar = nombres[i]
                nombres[i] = nombres[i + 1]
                nombres[i + 1] = auxiliar

                auxiliar = notas1[i]
                notas1[i] = notas1[i + 1]
                notas1[i + 1] = auxiliar

                auxiliar = notas2[i]
                notas2[i] = notas2[i + 1]
                notas2[i + 1] = auxiliar


def mostrar_ranking(nombres, nota1, nota2, promedios):
    """Llama a burbuja para mostar completo los datos"""
    ordenar_burbuja(nombres, nota1, nota2, promedios)
    for i in range(len(nombres)):
        print(i + 1, "-", nombres[i], "| Promedio:", promedios[i])


def buscar_alumno(nombres, nombre_buscado):
    """Busca el nombre y devuelve la posicion"""
    for i in range(len(nombres)):
        if nombres[i] == nombre_buscado:
            return i
    return -1
    # -1 significa no encontrado


def pedir_posicion_alumno(nombres):
    """Pedir el nombre al usuario y avisar si no existe"""
    nombre = input("Ingrese el nombre del alumno: ")
    print()
    posicion = buscar_alumno(nombres, nombre)
    if posicion == -1:
        print("El alumno no existe.")
    return posicion


def mostrar_busqueda(nombres, nota1, nota2, promedios):
    """Mostrar los datos del alumno encontrado"""
    posicion = pedir_posicion_alumno(nombres)
    if posicion != -1:
        mostrar_alumno(nombres, nota1, nota2, promedios, posicion)


def es_vocal(caracter):
    """Devuelve True si el carácter es una vocal"""
    # Se compara la letra con cada vocal de la constante
    for i in range(len(VOCALES)):
        if caracter == VOCALES[i]:
            return True
    return False


def contar_vocales(nombre):
    """Cuenta cuántas vocales tiene el nombre"""
    contador = 0
    for i in range(len(nombre)):
        if es_vocal(nombre[i]):
            contador = contador + 1
    return contador


def invertir_nombre(nombre):
    """Devuelve el nombre ingresado invertido"""
    invertido = ""
    # Se recorre desde la última posición hasta la primera
    for i in range(len(nombre) - 1, -1, -1):
        # Cada letra se agrega al final del texto que se va armando
        invertido = invertido + nombre[i]
    return invertido


def jugar_con_nombre(nombres):
    """Muestra las vocales y el nombre invertido de un alumno"""
    posicion = pedir_posicion_alumno(nombres)
    # Solo funciona con alumnos ya cargados
    if posicion != -1:
        nombre = nombres[posicion]
        print("Cantidad de vocales:", contar_vocales(nombre))
        print("Nombre invertido:", invertir_nombre(nombre))
