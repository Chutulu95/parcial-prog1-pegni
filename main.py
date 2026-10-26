"""Bienvenido a NotaFacil. En este modulo solo nos encontramos con el flujo del programa y su menu principal"""


from validaciones import validar_cantidad
from procesamiento import (jugar_con_nombre, mostrar_busqueda, crear_lista, cargar_datos, hay_alumnos, calcular_promedios, mostrar_listado, mostrar_estadisticas, mostrar_ranking) 


def main():
    """Muestra el menu y sus opciones"""
    cantidad = 0
    nombres = []
    nota1 = []
    nota2 = []
    promedios = []
    opcion = ""
    # Mientras la opcion sea distinta 0 el programa sigue abierto
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
        # Cada match_case corresponde a una funcion que esta documentada en su respectivo modulo
        match opcion:
            case "1":
                cantidad = validar_cantidad()
                nombres = crear_lista(cantidad, "")
                nota1 = crear_lista(cantidad, 0)
                nota2 = crear_lista(cantidad, 0)
                cargar_datos(nombres, nota1, nota2, cantidad)
                promedios = calcular_promedios(nota1, nota2)
        # Obviamente no van a funcionar si primero no hay dato que usar, no me hagas hacer laburo doble
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
                print("¡Hasta luego, gracias por la oportunidad!")
            case _:
                print("Opcion inexistente, volve a intentarlo.")


main()