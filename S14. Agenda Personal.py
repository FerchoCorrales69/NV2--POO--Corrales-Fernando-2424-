import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("500x400")

        # Frame para los campos de entrada
        self.entry_frame = tk.Frame(self.root)
        self.entry_frame.pack(pady=10)

        # Campos de entrada
        tk.Label(self.entry_frame, text="Fecha (DD/MM/AAAA):").grid(row=0, column=0, padx=10, pady=5)
        self.date_entry = tk.Entry(self.entry_frame)
        self.date_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.entry_frame, text="Hora (HH:MM):").grid(row=1, column=0, padx=10, pady=5)
        self.time_entry = tk.Entry(self.entry_frame)
        self.time_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.entry_frame, text="Descripción:").grid(row=2, column=0, padx=10, pady=5)
        self.desc_entry = tk.Entry(self.entry_frame)
        self.desc_entry.grid(row=2, column=1, padx=10, pady=5)

        # Botones de acciones
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.add_button = tk.Button(self.button_frame, text="Agregar Evento", command=self.agregar_evento)
        self.add_button.grid(row=0, column=0, padx=10)

        self.delete_button = tk.Button(self.button_frame, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        self.delete_button.grid(row=0, column=1, padx=10)

        self.quit_button = tk.Button(self.button_frame, text="Salir", command=self.root.quit)
        self.quit_button.grid(row=0, column=2, padx=10)

        # Treeview para mostrar los eventos
        self.event_tree = ttk.Treeview(self.root, columns=("Fecha", "Hora", "Descripción"), show='headings', height=10)
        self.event_tree.heading("Fecha", text="Fecha")
        self.event_tree.heading("Hora", text="Hora")
        self.event_tree.heading("Descripción", text="Descripción")
        self.event_tree.pack(pady=10)

        # Estilo para Treeview
        style = ttk.Style()
        style.configure("Treeview", rowheight=25)

    def agregar_evento(self):
        fecha = self.date_entry.get()
        hora = self.time_entry.get()
        descripcion = self.desc_entry.get()

        if not fecha or not hora or not descripcion:
            messagebox.showwarning("Campos Vacíos", "Por favor, complete todos los campos.")
        else:
            self.event_tree.insert("", "end", values=(fecha, hora, descripcion))
            self.date_entry.delete(0, tk.END)
            self.time_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)

    def eliminar_evento(self):
        selected_item = self.event_tree.selection()
        if not selected_item:
            messagebox.showwarning("Seleccionar Evento", "Por favor, seleccione un evento para eliminar.")
        else:
            confirm = messagebox.askyesno("Confirmar Eliminación", "¿Está seguro de eliminar el evento seleccionado?")
            if confirm:
                self.event_tree.delete(selected_item)

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = AgendaApp(root)
        root.mainloop()
    except Exception as e:
        print(f"Ocurrió un error: {e}")
