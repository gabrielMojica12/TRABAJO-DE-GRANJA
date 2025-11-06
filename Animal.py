class Animal:
    def __init__(self, codigo, raza, edad):
        self.codigo = codigo
        self.raza = raza
        self.edad = edad
        self.produccion = {}  # Ejemplo: {"semana1": 20, "semana2": 18}

    def registrar_produccion(self, semana, cantidad):
        """Registra la cantidad de huevos en una semana."""
        self.produccion[semana] = cantidad
        print(f"Registrados {cantidad} huevos en {semana} para el animal {self.codigo}")

    def produccion_total(self):
        """Retorna la cantidad total de huevos producidos."""
        return sum(self.produccion.values())

    def mostrar_produccion(self):
        """Muestra la producción de cada semana."""
        if not self.produccion:
            print("No hay producción registrada.")
        else:
            for semana, cantidad in self.produccion.items():
                print(f"  {semana}: {cantidad} huevos")

    def __str__(self):
        return (f"Código: {self.codigo}, Raza: {self.raza}, "
                f"Edad: {self.edad} meses, Total huevos: {self.produccion_total()}")
