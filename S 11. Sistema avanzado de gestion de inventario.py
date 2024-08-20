mport os

def mostrar_titulo():
    print("========================================")
    print("        UNIVERSIDAD ESTATAL AMAZÓNICA    ")
    print("========================================")
    print("Nombre: Fernando Corrales")
    print("========================================\n")

import pickle

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.__id_producto = id_producto  # Atributo privado
        self.__nombre = nombre            # Atributo privado
        self.__cantidad = cantidad        # Atributo privado
        self.__precio = precio            # Atributo privado

    # Métodos getters
    def obtener_id(self):
        return self.__id_producto

    def obtener_nombre(self):
        return self.__nombre

    def obtener_cantidad(self):
        return self.__cantidad

    def obtener_precio(self):
        return self.__precio

    # Métodos setters
    def establecer_nombre(self, nombre):
        self.__nombre = nombre

    def establecer_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def establecer_precio(self, precio):
        self.__precio = precio

    def __str__(self):
        return f"ID: {self.__id_producto}, Nombre: {self.__nombre}, Cantidad: {self.__cantidad}, Precio: {self.__precio}"

class Inventario:
    def __init__(self):
        self.productos = {}  # Usaremos un diccionario para almacenar los productos

    def agregar_producto(self, producto):
        self.productos[producto.obtener_id()] = producto

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].establecer_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].establecer_precio(precio)
        else:
            print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        for producto in self.productos.values():
            if producto.obtener_nombre().lower() == nombre.lower():
                print(producto)
                return producto
        print("Producto no encontrado.")
        return None

    def mostrar_todos_los_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
        for producto in self.productos.values():
            print(producto)

    def guardar_en_archivo(self, nombre_archivo):
        with open(nombre_archivo, 'wb') as archivo:
            pickle.dump(self.productos, archivo)

    def cargar_desde_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'rb') as archivo:
                self.productos = pickle.load(archivo)
        except FileNotFoundError:
            print("Archivo no encontrado. Iniciando con inventario vacío.")

def menu():
    inventario = Inventario()
    inventario.cargar_desde_archivo('inventario.dat')

    while True:
        print("\n--- Sistema de Gestión de Inventarios ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos los productos")
        print("6. Guardar y salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad del producto: "))
            precio = float(input("Precio del producto: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == '2':
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == '3':
            id_producto = input("ID del producto a actualizar: ")
            cantidad = int(input("Nueva cantidad (dejar en blanco si no se quiere cambiar): ") or -1)
            precio = float(input("Nuevo precio (dejar en blanco si no se quiere cambiar): ") or -1)
            if cantidad == -1: cantidad = None
            if precio == -1: precio = None
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == '4':
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == '5':
            inventario.mostrar_todos_los_productos()

        elif opcion == '6':
            inventario.guardar_en_archivo('inventario.dat')
            print("Inventario guardado. Saliendo del sistema.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
