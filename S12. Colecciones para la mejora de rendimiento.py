# UNIVERSIDAD ESTATAL AMAZÓNICA
# Programación Orientada a Objetos
# Estudiante: Fernando Corrales

# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo_autor = (titulo, autor)  # Tupla inmutable con título y autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"'{self.titulo_autor[0]}' de {self.titulo_autor[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"

# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista para gestionar libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}"

    def listar_libros_prestados(self):
        if self.libros_prestados:
            print(f"Libros prestados por {self.nombre}:")
            for libro in self.libros_prestados:
                print(libro)
        else:
            print(f"{self.nombre} no tiene libros prestados.")

# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario para gestionar libros por ISBN
        self.usuarios_registrados = set()  # Conjunto para asegurar IDs únicos de usuarios

    def agregar_libro(self, libro):
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro '{libro.titulo_autor[0]}' agregado a la biblioteca.")
        else:
            print(f"El libro con ISBN {libro.isbn} ya existe en la biblioteca.")

    def eliminar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            libro = self.libros_disponibles.pop(isbn)
            print(f"Libro '{libro.titulo_autor[0]}' eliminado de la biblioteca.")
        else:
            print(f"No se encontró el libro con ISBN {isbn}.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios_registrados:
            self.usuarios_registrados.add(usuario.id_usuario)
            print(f"Usuario '{usuario.nombre}' registrado con éxito.")
        else:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")

    def dar_baja_usuario(self, usuario):
        if usuario.id_usuario in self.usuarios_registrados:
            self.usuarios_registrados.remove(usuario.id_usuario)
            print(f"Usuario '{usuario.nombre}' dado de baja.")
        else:
            print(f"El usuario con ID {usuario.id_usuario} no está registrado.")

    def prestar_libro(self, isbn, usuario):
        if isbn in self.libros_disponibles:
            libro = self.libros_disponibles.pop(isbn)
            usuario.libros_prestados.append(libro)
            print(f"Libro '{libro.titulo_autor[0]}' prestado a {usuario.nombre}.")
        else:
            print(f"El libro con ISBN {isbn} no está disponible para préstamo.")

    def devolver_libro(self, isbn, usuario):
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.libros_prestados.remove(libro)
                self.libros_disponibles[isbn] = libro
                print(f"Libro '{libro.titulo_autor[0]}' devuelto por {usuario.nombre}.")
                return
        print(f"El usuario {usuario.nombre} no tiene el libro con ISBN {isbn}.")

    def buscar_libro(self, titulo=None, autor=None, categoria=None):
        resultados = []
        for libro in self.libros_disponibles.values():
            if titulo and titulo.lower() in libro.titulo_autor[0].lower():
                resultados.append(libro)
            elif autor and autor.lower() in libro.titulo_autor[1].lower():
                resultados.append(libro)
            elif categoria and categoria.lower() == libro.categoria.lower():
                resultados.append(libro)
        return resultados

# Ejemplo de uso del sistema de biblioteca
if __name__ == "__main__":
    print("UNIVERSIDAD ESTATAL AMAZÓNICA")
    print("Programación Orientada a Objetos")
    print("Estudiante: Fernando Corrales")
    print()

    # Crear algunos libros
    libro1 = Libro("El Quijote", "Miguel de Cervantes", "Novela", "123456")
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Ficción", "789101")
    libro3 = Libro("El principito", "Antoine de Saint-Exupéry", "Fábula", "112131")

    # Crear un usuario
    usuario1 = Usuario("Fernando Corrales", "001")

    # Crear la biblioteca y registrar libros y usuarios
    biblioteca = Biblioteca()
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)

    biblioteca.registrar_usuario(usuario1)

    # Prestar un libro
    biblioteca.prestar_libro("123456", usuario1)

    # Listar libros prestados
    usuario1.listar_libros_prestados()

    # Devolver un libro
    biblioteca.devolver_libro("123456", usuario1)

    # Buscar libros por título, autor o categoría
    resultados = biblioteca.buscar_libro(titulo="El Quijote")
    for libro in resultados:
        print(libro)


