
from BaseDeDatos import BaseDatos
from Animal import Animal

def main():
    bd = BaseDatos()

    while True:
        print("\n=== MENÚ GRANJA AVÍCOLA ===")
        print("1. Agregar animal")
        print("2. Consultar animal")
        print("3. Registrar producción semanal")
        print("4. Mostrar todos los animales")
        print("5. Actualizar animal")
        print("6. Eliminar animal")
        print("7. Producción total de la granja")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            codigo = input("Código: ")
            raza = input("Raza: ")
            edad = int(input("Edad (meses): "))
            a = Animal(codigo, raza, edad)
            bd.crear(a)

        elif opcion == "2":
            codigo = input("Ingrese código del animal: ")
            bd.leer(codigo)

        elif opcion == "3":
            codigo = input("Código del animal: ")
            if codigo in bd.animales:
                semana = input("Semana (ej: 'semana1'): ")
                cantidad = int(input("Cantidad de huevos: "))
                bd.animales[codigo].registrar_produccion(semana, cantidad)
            else:
                print("No existe un animal con ese código.")

        elif opcion == "4":
            bd.mostrar_todos()

        elif opcion == "5":
            codigo = input("Código a actualizar: ")
            raza = input("Nueva raza (dejar vacío si no cambia): ")
            edad = input("Nueva edad (dejar vacío si no cambia): ")

            nuevos_datos = {}
            if raza:
                nuevos_datos["raza"] = raza
            if edad:
                nuevos_datos["edad"] = int(edad)

            bd.actualizar(codigo, nuevos_datos)

        elif opcion == "6":
            codigo = input("Código a eliminar: ")
            bd.eliminar(codigo)

        elif opcion == "7":
            bd.produccion_total_granja()

        elif opcion == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()
