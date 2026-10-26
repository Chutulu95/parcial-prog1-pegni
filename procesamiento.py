from validaciones import pedir_nombre, validar_nota


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
