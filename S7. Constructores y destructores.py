class Archivo:
    def __init__(self, nombre_archivo, modo):
        """
        Constructor de la clase Archivo.
        Inicializa los atributos y abre el archivo.

        Args:
            nombre_archivo (str): El nombre del archivo a abrir.
            modo (str): El modo en el que se abrirá el archivo (e.g., 'r', 'w', 'a').
        """
        self.nombre_archivo = nombre_archivo
        self.modo = modo
        try:
            self.archivo = open(nombre_archivo, modo)
            print(f"Archivo '{nombre_archivo}' abierto en modo '{modo}'.")
        except IOError as e:
            print(f"No se pudo abrir el archivo: {e}")
            self.archivo = None

    def escribir(self, texto):
        """
        Escribe texto en el archivo si está abierto en modo escritura.

        Args:
            texto (str): El texto a escribir en el archivo.
        """
        if self.archivo and 'w' in self.modo:
            self.archivo.write(texto)
            print(f"Texto escrito en el archivo '{self.nombre_archivo}'.")
        else:
            print(f"El archivo '{self.nombre_archivo}' no está abierto en modo escritura.")

    def leer(self):
        """
        Lee el contenido del archivo si está abierto en modo lectura.

        Returns:
            str: El contenido del archivo.
        """
        if self.archivo and 'r' in self.modo:
            contenido = self.archivo.read()
            print(f"Contenido leído del archivo '{self.nombre_archivo}':\n{contenido}")
            return contenido
        else:
            print(f"El archivo '{self.nombre_archivo}' no está abierto en modo lectura.")
            return None

    def __del__(self):
        """
        Destructor de la clase Archivo.
        Se asegura de que el archivo se cierre correctamente.
        """
        if self.archivo:
            self.archivo.close()
            print(f"Archivo '{self.nombre_archivo}' cerrado.")

# Demostración del uso de la clase Archivo

# Crear un objeto de la clase Archivo y abrirlo en modo escritura
archivo_escritura = Archivo("ejemplo.txt", "w")
archivo_escritura.escribir("Este es un ejemplo de uso del constructor y destructor en Python.\n")

# Crear un objeto de la clase Archivo y abrirlo en modo lectura
archivo_lectura = Archivo("ejemplo.txt", "r")
contenido = archivo_lectura.leer()

# Al final del programa, los objetos serán destruidos automáticamente y los archivos se cerrarán
