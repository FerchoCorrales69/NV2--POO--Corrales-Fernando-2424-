import os

def mostrar_titulo():
    print("========================================")
    print("        UNIVERSIDAD ESTATAL AMAZÓNICA    ")
    print("========================================")
    print("Nombre: Fernando Corrales")
    print("========================================\n")

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f'ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}'

class Inventario:
    def __init__(self):
        self.productos = []
        self.cargar_datos()

    def añadir_producto(self, producto):
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: El ID del producto ya existe.")
        else:
            self.productos.append(producto)
            self.guardar_datos()
            print("Producto añadido exitosamente.")

    def eliminar_producto(self, id_producto):
        for producto in self.productos:
            if producto.get_id() == id_producto:
                confirmacion = input(f"¿Está seguro de que desea eliminar el producto '{producto.get_nombre()}'? (s/n): ")
                if confirmacion.lower() == 's':
                    self.productos.remove(producto)
                    self.guardar_datos()
                    print("Producto eliminado exitosamente.")
                else:
                    print("Operación cancelada.")
                return
        print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for producto in self.productos:
            if producto.get_id() == id_producto:
                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)
                self.guardar_datos()
                print("Producto actualizado exitosamente.")
                return
        print("Producto no encontrado.")

    def buscar_producto_por_id(self, id_producto):
        for producto in self.productos:
            if producto.get_id() == id_producto:
                print(producto)
                return
        print("Producto no encontrado.")

    def mostrar_todos_los_productos(self):
        if self.productos:
            for producto in self.productos:
                print(producto)
        else:
            print("No hay productos en el inventario.")

    def guardar_datos(self):
        try:
            with open("inventario.txt", "w") as f:
                for producto in self.productos:
                    f.write(f'{producto.get_id()},{producto.get_nombre()},{producto.get_cantidad()},{producto.get_precio()}\n')
            print("Datos guardados exitosamente.")
        except (PermissionError, IOError) as e:
            print(f"Error al guardar los datos: {e}")

    def cargar_datos(self):
        if not os.path.exists("inventario.txt"):
            print("Archivo de inventario no encontrado. Se creará uno nuevo al agregar productos.")
            return

        try:
            with open("inventario.txt", "r") as f:
                for linea in f:
                    id_producto, nombre, cantidad, precio = linea.strip().split(',')
                    producto = Producto(id_producto, nombre, int(cantidad), float(precio))
                    self.productos.append(producto)
            print("Datos cargados exitosamente.")
        except (FileNotFoundError, IOError) as e:
            print(f"Error al cargar los datos: {e}")
        except ValueError as e:
            print(f"Error en los datos del archivo: {e}")

def mostrar_menu():
    print("\n--- Menú de Gestión de Inventario ---")
    print("1. Añadir nuevo producto")
    print("2. Eliminar producto por ID")
    print("3. Actualizar cantidad o precio de un producto por ID")
    print("4. Buscar producto por ID")
    print("5. Mostrar todos los productos")
    print("6. Salir")

def obtener_numero_valido(prompt, tipo):
    while True:
        try:
            valor = tipo(input(prompt))
            return valor
        except ValueError:
            print(f"Error: Ingrese un valor válido de tipo {tipo.__name__}.")

def main():
    mostrar_titulo()
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = obtener_numero_valido("Ingrese cantidad del producto: ", int)
            precio = obtener_numero_valido("Ingrese precio del producto: ", float)
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese ID del producto a actualizar: ")
            nueva_cantidad = input("Ingrese nueva cantidad (deje en blanco si no desea cambiarla): ")
            nuevo_precio = input("Ingrese nuevo precio (deje en blanco si no desea cambiarlo): ")
            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
            nuevo_precio = float(nuevo_precio) if nuevo_precio else None
            inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

        elif opcion == "4":
            id_producto = input("Ingrese ID del producto a buscar: ")
            inventario.buscar_producto_por_id(id_producto)

        elif opcion == "5":
            inventario.mostrar_todos_los_productos()

        elif opcion == "6":
            confirmacion = input("¿Está seguro de que desea salir? (s/n): ")
            if confirmacion.lower() == 's':
                print("Saliendo del programa...")
                break
            else:
                print("Operación cancelada.")

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()

