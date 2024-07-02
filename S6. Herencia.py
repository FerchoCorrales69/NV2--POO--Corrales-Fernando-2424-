# clase base
class Animal:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # atributo encapsulado
        self.edad = edad

    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser sobrescrito por la clase derivada")

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

# clase derivada
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def hacer_sonido(self):
        return "Guau"

    def descripcion(self):
        return f"Nombre: {self.get_nombre()}, Edad: {self.edad}, Raza: {self.raza}"

def main():
    mi_perro = Perro("Rex", 5, "Labrador")
    print(mi_perro.descripcion())  # uso de método específico de la clase derivada
    print(mi_perro.hacer_sonido())  # ejemplo de polimorfismo

if __name__ == "__main__":
    main()
