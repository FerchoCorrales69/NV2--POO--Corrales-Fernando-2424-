import tkinter as tk
from tkinter import messagebox

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")

        # Crear interfaz gráfica
        self.create_widgets()

    def create_widgets(self):
        # Título y subtítulo
        title_label = tk.Label(self.root, text="UNIVERSIDAD ESTATAL AMAZÓNICA", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)

        subtitle_label = tk.Label(self.root, text="Fernando Corrales", font=("Arial", 12))
        subtitle_label.grid(row=1, column=0, columnspan=2, pady=5)

        # Campo de entrada de nuevas tareas
        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.grid(row=2, column=0, padx=10, pady=10)
        self.task_entry.bind("<Return>", self.add_task_event)

        # Botón para añadir tarea
        add_button = tk.Button(self.root, text="Añadir Tarea", command=self.add_task)
        add_button.grid(row=2, column=1, padx=10, pady=10)

        # Lista para mostrar tareas
        self.task_listbox = tk.Listbox(self.root, width=50, height=10, selectmode=tk.SINGLE)
        self.task_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Botón para marcar como completada
        complete_button = tk.Button(self.root, text="Marcar como Completada", command=self.mark_task_complete)
        complete_button.grid(row=4, column=0, padx=10, pady=10)

        # Botón para eliminar tarea
        delete_button = tk.Button(self.root, text="Eliminar Tarea", command=self.delete_task)
        delete_button.grid(row=4, column=1, padx=10, pady=10)

    def add_task_event(self, event):
        self.add_task()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Escriba una tarea antes de añadirla.")

    def mark_task_complete(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            task = self.task_listbox.get(task_index)
            self.task_listbox.delete(task_index)
            self.task_listbox.insert(task_index, f"{task} (Completada)")
        else:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para marcar como completada.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            self.task_listbox.delete(task_index)
        else:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar.")

# Inicializar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
