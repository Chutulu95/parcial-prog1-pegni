from validaciones import validar_cantidad
from procesamiento import (jugar_con_nombre, mostrar_busqueda, crear_lista, cargar_datos, hay_alumnos, calcular_promedios, mostrar_listado, mostrar_estadisticas, mostrar_ranking) 


def main():
    cantidad = 0
    nombres = []
    nota1 = []
    nota2 = []
    promedios = []
    opcion = ""
    while opcion != "0":
        print()
        print("===== NOTA FÁCIL =====")
        print("1. Cargar alumnos")
        print("2. Mostrar listado")
        print("3. Mostrar estadísticas")
        print("4. Ver ranking")
        print("5. Buscar alumno")
        print("6. Juegos con un nombre")
        print("0. Salir")
        opcion = input("Elegí una opción: ")
        print()
        match opcion:
            case "1":
                cantidad = validar_cantidad()
                nombres = crear_lista(cantidad, "")
                nota1 = crear_lista(cantidad, 0)
                nota2 = crear_lista(cantidad, 0)
                cargar_datos(nombres, nota1, nota2, cantidad)
                promedios = calcular_promedios(nota1, nota2)
            case "2":
                if hay_alumnos(cantidad):
                    mostrar_listado(nombres, nota1, nota2, promedios)
            case "3":
                if hay_alumnos(cantidad):
                    mostrar_estadisticas(nombres, promedios)
            case "4":
                if hay_alumnos(cantidad):
                    mostrar_ranking(nombres, nota1, nota2, promedios)
            case "5":
                if hay_alumnos(cantidad):
                    mostrar_busqueda(nombres, nota1, nota2, promedios)
            case "6":
                if hay_alumnos(cantidad):
                    jugar_con_nombre(nombres)
            case "0":
                print("¡Hasta luego!")
            case _:
                print("Esa opción no existe. Probá de nuevo.")


main()