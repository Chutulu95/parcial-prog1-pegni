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
