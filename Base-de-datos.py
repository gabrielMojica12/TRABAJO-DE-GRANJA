from Interface import Interface
class BaseDatos(Interface):
    def __init__(self):
        # Diccionario principal: clave = código del animal, valor = objeto Animal
        self.animales = {}

    def crear(self, animal):
        if animal.codigo in self.animales:
            print("Ya existe un animal con ese código.")
        else:
            self.animales[animal.codigo] = animal
            print("Animal agregado correctamente.")

    def leer(self, codigo):
        if codigo in self.animales:
            animal = self.animales[codigo]
            print(animal)
            animal.mostrar_produccion()
        else:
            print("No se encontró el animal con ese código.")

    def actualizar(self, codigo, nuevos_datos):
        if codigo in self.animales:
            animal = self.animales[codigo]
            if "raza" in nuevos_datos:
                animal.raza = nuevos_datos["raza"]
            if "edad" in nuevos_datos:
                animal.edad = nuevos_datos["edad"]
            print("Animal actualizado correctamente.")
        else:
            print("No se encontró el animal para actualizar.")

    def eliminar(self, codigo):
        if codigo in self.animales:
            del self.animales[codigo]
            print("Animal eliminado correctamente.")
        else:
            print("No se encontró el animal para eliminar.")

    def mostrar_todos(self):
        if not self.animales:
            print("No hay animales registrados.")
        else:
            print("\n=== Lista de animales registrados ===")
            for a in self.animales.values():
                print(a)

    def produccion_total_granja(self):
        total = sum(a.produccion_total() for a in self.animales.values())
        print(f"Producción total de la granja: {total} huevos")
