import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from gestor.gestor_inspecciones import GestorInspecciones

class InterfazInspecciones(tk.Frame):
    def __init__(self, app):
        super().__init__(app, bg="#f5f5f5")
        
        self.habilitarVentana()
        
        self.gestor = GestorInspecciones(self)

    def habilitarVentana(self):
        # Configurar peso de filas y columnas para responsive
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # === ENCABEZADO NARANJA CON IMAGEN ===
        header_frame = tk.Frame(self, bg="#FF8C42", height=100)
        header_frame.grid(row=0, column=0, sticky="ew")
        header_frame.grid_propagate(False)
        
        # Cargar logo en ambos lados
        try:
            logo = tk.PhotoImage(file="assets/img/Logo.png")
            logo = logo.subsample(3, 3)
            
            logo_label_left = tk.Label(header_frame, image=logo, bg="#FF8C42")
            logo_label_left.image = logo
            logo_label_left.pack(side=tk.LEFT, padx=20)
            
            logo_label_right = tk.Label(header_frame, image=logo, bg="#FF8C42")
            logo_label_right.image = logo
            logo_label_right.pack(side=tk.RIGHT, padx=20)
        except:
            pass
        
        label = tk.Label(header_frame, text="📋 Órdenes de Inspección", 
                        font=("Arial", 22, "bold"), bg="#FF8C42", fg="white")
        label.pack(expand=True)

        # === CONTENEDOR PRINCIPAL ===
        main_frame = tk.Frame(self, bg="#f5f5f5")
        main_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)

        # === ESTILO PERSONALIZADO PARA TREEVIEW ===
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Custom.Treeview",
                       background="#ffffff",
                       foreground="#333333",
                       rowheight=30,
                       fieldbackground="#ffffff",
                       borderwidth=0)
        style.configure("Custom.Treeview.Heading",
                       background="#FF8C42",
                       foreground="white",
                       font=("Arial", 10, "bold"),
                       borderwidth=0)
        style.map("Custom.Treeview",
                 background=[("selected", "#FFB380")])

        # === FRAME PARA TABLA Y SCROLLBAR ===
        table_frame = tk.Frame(main_frame, bg="#f5f5f5")
        table_frame.grid(row=0, column=0, sticky="nsew", pady=(0, 20))
        table_frame.grid_rowconfigure(0, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)

        # === TABLA DE ÓRDENES ===
        self.list_ordenesInspeccion = ttk.Treeview(
            table_frame, 
            columns=("ID", "Fecha", "Estacion", "Sismografo"), 
            show="headings",
            style="Custom.Treeview"
        )
        self.list_ordenesInspeccion.heading("ID", text="ID Orden", anchor="center")
        self.list_ordenesInspeccion.heading("Fecha", text="Fecha Finalización", anchor="center")
        self.list_ordenesInspeccion.heading("Estacion", text="Estación Sismológica", anchor="center")
        self.list_ordenesInspeccion.heading("Sismografo", text="Sismógrafo", anchor="center")
        self.list_ordenesInspeccion.column("ID", anchor="center", width=80, minwidth=60)
        self.list_ordenesInspeccion.column("Fecha", anchor="center", width=180, minwidth=120)
        self.list_ordenesInspeccion.column("Estacion", anchor="center", width=250, minwidth=150)
        self.list_ordenesInspeccion.column("Sismografo", anchor="center", width=100, minwidth=80)
        self.list_ordenesInspeccion.grid(row=0, column=0, sticky="nsew")

        # === SCROLLBAR ===
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.list_ordenesInspeccion.yview)
        self.list_ordenesInspeccion.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns")

        # === BOTÓN MEJORADO (Con respecto al anterior) ===
        self.btn_seleccionarOrden = tk.Button(
            main_frame, 
            text="✓ Cerrar Orden Seleccionada", 
            command=self.tomarSeleccionOrdenInspeccion,
            bg="#FF8C42",
            fg="white",
            font=("Arial", 12, "bold"),
            relief=tk.FLAT,
            padx=30,
            pady=12,
            cursor="hand2",
            activebackground="#FF7526",
            activeforeground="white"
        )
        self.btn_seleccionarOrden.grid(row=1, column=0, pady=10)

    def mostrarOrdCompRealizadas(self, ordenes):
        self.list_ordenesInspeccion.delete(*self.list_ordenesInspeccion.get_children())
        
        for orden in ordenes:
            self.list_ordenesInspeccion.insert("", "end", values=(orden["id"], orden["fechaFinalizacion"], orden["estacionSismologica"], orden["sismografoId"]))

    def pedirSeleccionOrdenInspeccion(self):
        label = tk.Label(self, text="⚠ Por favor seleccione una orden", font=("Arial", 10), fg="#FF0000", bg="#f5f5f5")
        label.grid(row=2, column=0, pady=20)

    def tomarSeleccionOrdenInspeccion(self):
        seleccion = self.list_ordenesInspeccion.selection()
        
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione una orden.")
            return
        
        self.list_ordenesInspeccion_item_id = seleccion[0]
        item = self.list_ordenesInspeccion.item(seleccion)
        idOrden = int(item["values"][0])

        orden = self.gestor.tomarOrdenDeInspeccionSeleccionada(idOrden)
        
        if not orden:
            messagebox.showerror("Error", "Orden no encontrada.")
            return
        
        self.gestor.pedirObservacion()

    def pedirObservacion(self):
        self.win_observacion = tk.Toplevel(self)
        self.win_observacion.title("Observación de cierre")
        self.win_observacion.geometry("550x300")
        self.win_observacion.configure(bg="#f5f5f5")
        self.win_observacion.grab_set()
        
        # Header de la ventana
        header = tk.Frame(self.win_observacion, bg="#FF8C42", height=60)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        tk.Label(header, text="📝 Observación de Cierre", font=("Arial", 14, "bold"), 
                bg="#FF8C42", fg="white").pack(pady=15)
        
        content = tk.Frame(self.win_observacion, bg="#f5f5f5")
        content.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        tk.Label(content, text="Ingrese observación de cierre:", 
                font=("Arial", 10), bg="#f5f5f5").pack(pady=(0, 10), anchor="w")
        
        self.text_observacion = tk.Text(content, width=60, height=6, font=("Arial", 10),
                                       relief=tk.SOLID, borderwidth=1)
        self.text_observacion.pack(pady=5)
        
        btn_frame = tk.Frame(content, bg="#f5f5f5")
        btn_frame.pack(pady=20)
        
        tk.Button(btn_frame, text="✓ Aceptar", command=self.tomarObservacion,
                 bg="#4CAF50", fg="white", font=("Arial", 10, "bold"),
                 padx=20, pady=8, relief=tk.FLAT, cursor="hand2").pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="✕ Cancelar", command=self.cancelarCierre,
                 bg="#f44336", fg="white", font=("Arial", 10, "bold"),
                 padx=20, pady=8, relief=tk.FLAT, cursor="hand2").pack(side=tk.LEFT)

    def tomarObservacion(self):
        observacion = self.text_observacion.get("1.0", tk.END).strip()

        if observacion == "":
            messagebox.showwarning("Advertencia", "Debe ingresar una observación de cierre.")
            return
        
        self.gestor.tomarObservacion(observacion)
        self.win_observacion.destroy()

    def mostrarMotivosTipo(self, motivos):
        self.win_motivos = tk.Toplevel(self)
        self.win_motivos.title(f"Motivos de cierre")
        self.win_motivos.geometry("600x450")
        self.win_motivos.configure(bg="#f5f5f5")
        self.win_motivos.grab_set()
        
        # Header
        header = tk.Frame(self.win_motivos, bg="#FF8C42", height=60)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        tk.Label(header, text="🔧 Motivos de Cierre", font=("Arial", 14, "bold"), 
                bg="#FF8C42", fg="white").pack(pady=15)
        
        content = tk.Frame(self.win_motivos, bg="#f5f5f5")
        content.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        tk.Label(content, text="Seleccione uno o varios motivos para poner fuera de servicio:",
                font=("Arial", 10), bg="#f5f5f5").pack(pady=(0, 10), anchor="w")
        
        self.list_motivos = tk.Listbox(content, selectmode=tk.MULTIPLE, width=70, height=12,
                                       font=("Arial", 10), relief=tk.SOLID, borderwidth=1)
        for motivo in motivos:
            self.list_motivos.insert(tk.END, motivo)

        self.list_motivos.pack(pady=10, fill=tk.BOTH, expand=True)
        
        btn_frame = tk.Frame(content, bg="#f5f5f5")
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="✓ Aceptar", 
                 command=lambda: self.gestor.solicitarSeleccionMotivoFueraDeServicio(motivos),
                 bg="#4CAF50", fg="white", font=("Arial", 10, "bold"),
                 padx=20, pady=8, relief=tk.FLAT, cursor="hand2").pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="✕ Cancelar", command=self.cancelarCierre,
                 bg="#f44336", fg="white", font=("Arial", 10, "bold"),
                 padx=20, pady=8, relief=tk.FLAT, cursor="hand2").pack(side=tk.LEFT)

    def solicitarSeleccionMotivoFueraDeServicio(self, motivos, indiceMotivo):
        seleccion_indices = self.list_motivos.curselection()
        if not seleccion_indices:
            messagebox.showwarning("Advertencia", "Debe seleccionar al menos un motivo.")
            return
        
        motivosPreseleccionados = [motivos[i] for i in seleccion_indices]

        self.win_motivos.destroy()

        self.tomarMotivoFueraDeServicio(motivosPreseleccionados, indiceMotivo)

    def tomarMotivoFueraDeServicio(self, motivosPreseleccionados, indiceMotivo):
        self.gestor.tomarMotivosFueraServicio(motivosPreseleccionados, indiceMotivo)
        
    def pedirComentario(self, motivos, indiceMotivo):
        self.win_comentario = tk.Toplevel(self)
        self.win_comentario.title(f"Comentario para motivo")
        self.win_comentario.geometry("550x300")
        self.win_comentario.configure(bg="#f5f5f5")
        self.win_comentario.grab_set()
        
        # Header
        header = tk.Frame(self.win_comentario, bg="#FF8C42", height=60)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        tk.Label(header, text="💬 Comentario del Motivo", font=("Arial", 14, "bold"), 
                bg="#FF8C42", fg="white").pack(pady=15)
        
        content = tk.Frame(self.win_comentario, bg="#f5f5f5")
        content.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        tk.Label(content, text=f"Ingrese comentario para: '{motivos[indiceMotivo]}'",
                font=("Arial", 10), bg="#f5f5f5", wraplength=500).pack(pady=(0, 10), anchor="w")
        
        self.txt_comentarioMotivoDeCierre = tk.Text(content, width=60, height=6, 
                                                    font=("Arial", 10), relief=tk.SOLID, borderwidth=1)
        self.txt_comentarioMotivoDeCierre.pack(pady=5)
        
        btn_frame = tk.Frame(content, bg="#f5f5f5")
        btn_frame.pack(pady=20)
        
        tk.Button(btn_frame, text="→ Guardar y Siguiente", 
                 command=lambda: self.tomarComentario(motivos, indiceMotivo),
                 bg="#2196F3", fg="white", font=("Arial", 10, "bold"),
                 padx=20, pady=8, relief=tk.FLAT, cursor="hand2").pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="✕ Cancelar", command=self.cancelarCierre,
                 bg="#f44336", fg="white", font=("Arial", 10, "bold"),
                 padx=20, pady=8, relief=tk.FLAT, cursor="hand2").pack(side=tk.LEFT)

    def tomarComentario(self, motivos, indiceMotivo):
        comentario = self.txt_comentarioMotivoDeCierre.get("1.0", tk.END).strip()
        
        if comentario == "":
            messagebox.showwarning("Advertencia", "Debe ingresar un comentario.")
            self.win_comentario.destroy()
            
            self.pedirComentario(motivos, indiceMotivo)
            return

        self.gestor.tomarComentario(comentario, indiceMotivo)
        self.win_comentario.destroy()
        indiceMotivo += 1
        self.tomarMotivoFueraDeServicio(motivos, indiceMotivo)

    def pedirConfirmacionCierreOrden(self):
        respuesta = messagebox.askyesno("Confirmar cierre", "¿Desea confirmar el cierre de la orden?")
        if respuesta:
            self.tomarConfirmacionCierreOrden(True)
        else:
            self.tomarConfirmacionCierreOrden(False)

    def tomarConfirmacionCierreOrden(self, confirmado):
        
        if not confirmado:
            messagebox.showinfo("Cancelado", "Cierre de orden cancelado.")
            return

        cerrada = self.gestor.tomarConfirmacionCierreOrden()

        if cerrada:
            messagebox.showinfo("Éxito", "Orden cerrada con éxito.\n\n✉ Mails y notificaciones enviadas a los monitores CCRS.")
        else:
            messagebox.showerror("Error", "Error al cerrar la orden.")

    def cancelarCierre(self):
        if messagebox.askyesno("Cancelar", "¿Está seguro que desea cancelar el cierre de la orden?"):
            self.orden_actual = None
            for ventana in ["win_observacion", "win_motivos", "win_comentario"]:
                if hasattr(self, ventana):
                    w = getattr(self, ventana)
                    if w and w.winfo_exists():
                        w.destroy()