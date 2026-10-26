from validaciones import pedir_nombre, validar_nota

VOCALES = "aeiouAEIOU"
PROMEDIO_PROMOCION = 6
PROMEDIO_APROBACION = 4


def crear_lista(cantidad, valor_inicial):
    lista = []
    for i in range(cantidad):
        lista = lista + [valor_inicial]
    return lista


def cargar_datos(nombres, nota1, nota2, cantidad):
    for i in range(cantidad):
        print()
        print("Alumno", i + 1)
        nombres[i] = pedir_nombre()
        nota1[i] = validar_nota("primer")
        nota2[i] = validar_nota("segundo")


def hay_alumnos(cantidad):
    if cantidad == 0:
        print("Primero tenés que cargar alumnos (opción 1).")
        return False
    return True


def calcular_promedios(notas1, notas2):
    promedios = []
    for i in range(len(notas1)):
        promedio = (notas1[i] + notas2[i]) / 2
        promedios = promedios + [promedio]
    return promedios


def calcular_promedio_general(promedios):
    acumulador = 0
    for i in range(len(promedios)):
        acumulador = acumulador + promedios[i]
    return acumulador / len(promedios)


def buscar_indice_mejor(promedios):
    indice_mejor = 0
    for i in range(1, len(promedios)):
        if promedios[i] > promedios[indice_mejor]:
            indice_mejor = i
    return indice_mejor


def buscar_indice_peor(promedios):
    indice_peor = 0
    for i in range(1, len(promedios)):
        if promedios[i] < promedios[indice_peor]:
            indice_peor = i
    return indice_peor


def contar_promocionan(promedios):
    contador = 0
    for i in range(len(promedios)):
        if promedios[i] >= PROMEDIO_PROMOCION:
            contador = contador + 1
    return contador


def contar_aprueban(promedios):
    contador = 0
    for i in range(len(promedios)):
        if PROMEDIO_APROBACION <= promedios[i] < PROMEDIO_PROMOCION:
            contador = contador + 1
    return contador


def contar_desaprueban(promedios):
    contador = 0
    for i in range(len(promedios)):
        if promedios[i] < PROMEDIO_APROBACION:
            contador = contador + 1
    return contador


def mostrar_alumno(nombres, nota1, nota2, promedios, posicion):
    print("Alumno:", nombres[posicion])
    print("Parcial 1:", nota1[posicion])
    print("Parcial 2:", nota2[posicion])
    print("Promedio:", promedios[posicion])


def mostrar_listado(nombres, nota1, nota2, promedios):
    for i in range(len(nombres)):
        if i > 0:
            print()
        mostrar_alumno(nombres, nota1, nota2, promedios, i)


def mostrar_estadisticas(nombres, promedios):
    indice_mejor = buscar_indice_mejor(promedios)
    indice_peor = buscar_indice_peor(promedios)
    print("Promedio general:", calcular_promedio_general(promedios))
    print("Mejor promedio:", nombres[indice_mejor],
          "con", promedios[indice_mejor])
    print("Peor promedio:", nombres[indice_peor],
          "con", promedios[indice_peor])
    print("Promocionan:", contar_promocionan(promedios))
    print("Aprueban:", contar_aprueban(promedios))
    print("Desaprueban:", contar_desaprueban(promedios))


def ordenar_burbuja(nombres, notas1, notas2, promedios):
    cantidad = len(promedios)
    for pasada in range(cantidad - 1):
        for i in range(cantidad - 1 - pasada):
            if promedios[i] < promedios[i + 1]:
                # Intercambio con variable auxiliar, lista por lista
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
    ordenar_burbuja(nombres, nota1, nota2, promedios)
    for i in range(len(nombres)):
        print(i + 1, "-", nombres[i], "| Promedio:", promedios[i])


def buscar_alumno(nombres, nombre_buscado):
    for i in range(len(nombres)):
        if nombres[i] == nombre_buscado:
            return i
    return -1


def pedir_posicion_alumno(nombres):
    nombre = input("Ingrese el nombre del alumno: ")
    print()
    posicion = buscar_alumno(nombres, nombre)
    if posicion == -1:
        print("El alumno no existe.")
    return posicion


def mostrar_busqueda(nombres, nota1, nota2, promedios):
    posicion = pedir_posicion_alumno(nombres)
    if posicion != -1:
        mostrar_alumno(nombres, nota1, nota2, promedios, posicion)


def es_vocal(caracter):
    for i in range(len(VOCALES)):
        if caracter == VOCALES[i]:
            return True
    return False


def contar_vocales(nombre):
    contador = 0
    for i in range(len(nombre)):
        if es_vocal(nombre[i]):
            contador = contador + 1
    return contador


def invertir_nombre(nombre):
    invertido = ""
    for i in range(len(nombre) - 1, -1, -1):
        invertido = invertido + nombre[i]
    return invertido


def jugar_con_nombre(nombres):
    posicion = pedir_posicion_alumno(nombres)
    if posicion != -1:
        nombre = nombres[posicion]
        print("Cantidad de vocales:", contar_vocales(nombre))
        print("Nombre invertido:", invertir_nombre(nombre))
