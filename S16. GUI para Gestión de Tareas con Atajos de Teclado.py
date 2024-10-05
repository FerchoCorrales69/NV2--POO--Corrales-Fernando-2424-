import tkinter as tk
from tkinter import messagebox

# Funciones para gestionar las tareas
def agregar_tarea(event=None):
    tarea = entrada_tarea.get()
    if tarea != "":
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")

def marcar_completada(event=None):
    try:
        index = lista_tareas.curselection()[0]
        tarea = lista_tareas.get(index)
        lista_tareas.delete(index)
        lista_tareas.insert(index, f"[Completada] {tarea}")
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

def eliminar_tarea(event=None):
    try:
        index = lista_tareas.curselection()[0]
        lista_tareas.delete(index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

def cerrar_aplicacion(event=None):
    ventana.quit()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Tareas Pendientes")
ventana.geometry("400x400")

# Crear el título y subtítulo
titulo = tk.Label(ventana, text="Universidad Estatal Amazónica", font=("Arial", 16, "bold"))
titulo.pack(pady=10)

subtitulo = tk.Label(ventana, text="FERNANDO CORRALES TARIRA", font=("Arial", 12))
subtitulo.pack(pady=5)

# Crear campo de entrada para nuevas tareas
entrada_tarea = tk.Entry(ventana, font=("Arial", 12))
entrada_tarea.pack(pady=10)

# Crear lista para mostrar las tareas
lista_tareas = tk.Listbox(ventana, font=("Arial", 12), height=10, selectmode=tk.SINGLE)
lista_tareas.pack(pady=10)

# Crear botones
boton_agregar = tk.Button(ventana, text="Agregar Tarea", command=agregar_tarea)
boton_agregar.pack(pady=5)

boton_completar = tk.Button(ventana, text="Marcar como Completada", command=marcar_completada)
boton_completar.pack(pady=5)

boton_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea)
boton_eliminar.pack(pady=5)

# Manejo de atajos de teclado
ventana.bind("<Return>", agregar_tarea)  # Enter para agregar tarea
ventana.bind("<c>", marcar_completada)   # 'C' para marcar como completada
ventana.bind("<d>", eliminar_tarea)      # 'D' para eliminar tarea
ventana.bind("<Delete>", eliminar_tarea) # Suprimir para eliminar tarea
ventana.bind("<Escape>", cerrar_aplicacion) # Escape para cerrar la aplicación

# Iniciar la aplicación
ventana.mainloop()
