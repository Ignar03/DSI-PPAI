import tkinter as tk
from menu.menu import BarraMenu

class App:
    def __init__(self, titulo):
        self.app = tk.Tk()
        self.titulo = titulo
        self.ancho = self.app.winfo_screenwidth()
        self.alto = self.app.winfo_screenheight()
        self.frame_contenido = tk.Frame(self.app, width=self.ancho, height=self.alto)
        self.menu = BarraMenu(self)

        self.app.state('zoomed')
        self.app.title(titulo)
        self.frame_contenido.pack(fill=tk.BOTH, expand=True)

        self.app.config(menu=self.menu)

        self.app.mainloop()
    
    def mostrarInterfaz(self, interfaz, gestor, titulo):
        for widget in self.frame_contenido.winfo_children():
            widget.destroy()

        nueva_interfaz = interfaz(self.frame_contenido, gestor)
        nueva_interfaz.pack(fill=tk.BOTH, expand=True)

        self.cambiarTitulo(titulo)

    def cambiarTitulo(self, titulo):
        self.app.title(titulo)
        return

if __name__ == "__main__":
    app = App("Redes Sísmicas")