import tkinter as tk
from tkinter import messagebox


class AplicacionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Datos")

        # TÍTULO PRINCIPAL
        self.titulo = tk.Label(root, text="UNIVERSIDAD ESTATAL AMAZÓNICA", font=("Helvetica", 16, "bold"))
        self.titulo.pack(pady=10)

        # SUBTÍTULO 1
        self.subtitulo1 = tk.Label(root, text="Programación Orientada a Objetos", font=("Helvetica", 12))
        self.subtitulo1.pack(pady=5)

        # SUBTÍTULO 2
        self.subtitulo2 = tk.Label(root, text="Fernando Corrales Tarira", font=("Helvetica", 12))
        self.subtitulo2.pack(pady=5)

        # Etiqueta
        self.label = tk.Label(root, text="Ingrese Información:")
        self.label.pack(pady=10)

        # Campo de texto
        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=5)

        # Botón "Agregar"
        self.btn_agregar = tk.Button(root, text="Agregar", command=self.agregar_dato)
        self.btn_agregar.pack(pady=5)

        # Lista para mostrar los datos
        self.lista_datos = tk.Listbox(root, height=10, width=50)
        self.lista_datos.pack(pady=10)

        # Botón "Limpiar"
        self.btn_limpiar = tk.Button(root, text="Limpiar", command=self.limpiar_datos)
        self.btn_limpiar.pack(pady=5)

    def agregar_dato(self):
        dato = self.entry.get()
        if dato:
            self.lista_datos.insert(tk.END, dato)
            self.entry.delete(0, tk.END)  # Limpiar campo de texto
        else:
            messagebox.showwarning("Entrada vacía", "Por favor, ingrese algún dato.")

    def limpiar_datos(self):
        self.lista_datos.delete(0, tk.END)  # Limpiar la lista


# Crear ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionGUI(root)
    root.mainloop()
