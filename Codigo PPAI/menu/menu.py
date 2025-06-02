import tkinter as tk
from interfaz.interfaz_inspecciones import InterfazInspecciones
from gestor.gestor_inspecciones import GestorInspecciones

class BarraMenu(tk.Menu):
    def __init__(self, app=None):
        super().__init__(app.app)
        self.app = app

        # Opciones del menu
        ordenes_menu = tk.Menu(self, tearoff=False)
        ordenes_menu.add_command(
            label="Cerrar orden de inspección", 
            command=lambda: self.app.selOpcCerrarOrdInspeccion(InterfazInspecciones, "Cerrar Orden de Inspección")
        )

        self.add_cascade(label="Ordenes", menu=ordenes_menu)