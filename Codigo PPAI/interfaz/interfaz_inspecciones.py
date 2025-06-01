import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from gestor.gestor_inspecciones import GestorInspecciones

class InterfazInspecciones(tk.Frame):
    def __init__(self, app):
        super().__init__(app)
        
        label = tk.Label(self, text="Ordenes de Inspección", font=("Arial", 18))
        label.pack(pady=20)

        self.tree = ttk.Treeview(self, columns=("ID", "Fecha", "Estacion", "Sismografo"), show="headings")
        self.tree.heading("ID", text="ID Orden", anchor="center")
        self.tree.heading("Fecha", text="Fecha Finalización", anchor="center")
        self.tree.heading("Estacion", text="Estación Sismológica", anchor="center")
        self.tree.heading("Sismografo", text="Sismógrafo", anchor="center")
        self.tree.column("ID", anchor="center", width=70)
        self.tree.column("Fecha", anchor="center", width=200)
        self.tree.column("Estacion", anchor="center", width=200)
        self.tree.column("Sismografo", anchor="center", width=90)
        self.tree.pack(padx=10, pady=10, fill=tk.X)
        self.btn_seleccionar = tk.Button(self, text="Cerrar orden seleccionada", command=self.tomarSeleccionOrdenInspeccion)
        self.btn_seleccionar.pack(pady=10)
        
        self.gestor = GestorInspecciones(self)

    def mostrarOrdCompRealizadas(self, ordenes):
        self.tree.delete(*self.tree.get_children())
        
        for orden in ordenes:
            self.tree.insert("", "end", values=(orden.id, orden.obtenerFechaFinalizacion(), orden.obtenerEstacionSismologica(), orden.obtenerIdentificadorSismografo()))

    # Este método refresca la tabla cuando termina el CU ¿Será necesario?
    # Si fuera necesario, hay que implementarlo bien
    def refrescarTabla(self):
        # self.mostrarOrdCompRealizadas()
        return

    def tomarSeleccionOrdenInspeccion(self):
        seleccion = self.tree.selection()
        
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione una orden.")
            return
        
        self.tree_item_id = seleccion[0]
        item = self.tree.item(seleccion)
        id_orden = int(item["values"][0])

        orden = self.gestor.tomarOrdenDeInspeccionSeleccionada(id_orden)
        
        if not orden:
            messagebox.showerror("Error", "Orden no encontrada.")
            return
        
        self.gestor.pedirObservacion()

    def pedirObservacion(self):
        self.win_observacion = tk.Toplevel(self)
        self.win_observacion.title("Observación de cierre")
        self.win_observacion.geometry("500x250")
        self.win_observacion.grab_set()
        tk.Label(self.win_observacion, text="Ingrese observación de cierre:").pack(pady=10)
        self.text_observacion = tk.Text(self.win_observacion, width=60, height=6)
        self.text_observacion.pack(pady=5)
        btn_frame = tk.Frame(self.win_observacion)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Aceptar", command=self.tomarObservacion).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Cancelar", command=self.cancelarCierre).pack(side=tk.LEFT)

    def tomarObservacion(self):
        texto = self.text_observacion.get("1.0", tk.END).strip()

        if texto == "":
            messagebox.showwarning("Advertencia", "Debe ingresar una observación de cierre.")
            return
        
        self.gestor.tomarObservacion(texto)
        self.win_observacion.destroy()

    def mostrarMotivosTipo(self, motivos):
        self.win_motivos = tk.Toplevel(self)
        self.win_motivos.title(f"Motivos de cierre para la orden")
        self.win_motivos.geometry("500x400")
        self.win_motivos.grab_set()
        tk.Label(self.win_motivos, text="Seleccione uno o varios motivos para poner fuera de servicio:").pack(pady=10)
        self.listbox = tk.Listbox(self.win_motivos, selectmode=tk.MULTIPLE, width=60, height=10)
        for motivo in motivos:
            self.listbox.insert(tk.END, motivo)

        self.listbox.pack(pady=10)
        btn_frame = tk.Frame(self.win_motivos)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Aceptar", command=lambda: self.gestor.solicitarSeleccionMotivoFueraDeServicio(motivos)).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Cancelar", command=self.cancelarCierre).pack(side=tk.LEFT)

    # def solicitarSeleccionMotivoFueraDeServicio(self, motivos):
    #     seleccion_indices = self.listbox.curselection()
    #     if not seleccion_indices:
    #         messagebox.showwarning("Advertencia", "Debe seleccionar al menos un motivo.")
    #         return
        
    #     motivosPreseleccionados = [motivos[i] for i in seleccion_indices]
    #     self.win_motivos.destroy()

    #     indiceMotivo = 0
    #     self.tomarMotivoFueraDeServicio(motivosPreseleccionados, indiceMotivo)

    # def tomarMotivoFueraDeServicio(self, motivos, indiceMotivo):        
    #     self.gestor.tomarMotivosFueraServicio(motivos, indiceMotivo)
        
    # def pedirComentario(self, motivos, indiceMotivo):
    #     win_comentario = tk.Toplevel(self)
    #     win_comentario.title(f"Comentario para motivo: '{motivos[indiceMotivo]}'")
    #     win_comentario.geometry("500x250")
    #     win_comentario.grab_set()

    #     tk.Label(win_comentario, text=f"Ingrese comentario para el motivo: '{motivos[indiceMotivo]}'").pack(pady=10)

    #     txt_comentario = tk.Text(win_comentario, width=60, height=6)
    #     txt_comentario.pack(pady=5)

    #     btn_frame = tk.Frame(win_comentario)
    #     btn_frame.pack(pady=10)

    #     tk.Button(btn_frame, text="Guardar y siguiente", command=lambda: self.tomarComentario(motivos, indiceMotivo, txt_comentario, win_comentario)).pack(side=tk.LEFT, padx=10)
    #     tk.Button(btn_frame, text="Cancelar", command=self.cancelarCierre).pack(side=tk.LEFT)

    # def tomarComentario(self, motivos, indiceMotivo, text_widget, win_comentario):
    #     comentario = text_widget.get("1.0", tk.END).strip()
    #     win_comentario.destroy()


    #     if indiceMotivo < len(motivos):
    #         self.gestor.tomarComentario(indiceMotivo, comentario)
    #         indiceMotivo += 1
    #         self.pedirComentario(motivos, indiceMotivo)
    #     else:
    #         self.pedirConfirmacionCierreOrden()  

    def solicitarSeleccionMotivoFueraDeServicio(self, motivos):
        seleccion_indices = self.listbox.curselection()
        if not seleccion_indices:
            messagebox.showwarning("Advertencia", "Debe seleccionar al menos un motivo.")
            return
        
        motivosPreseleccionados = [motivos[i] for i in seleccion_indices]

        self.win_motivos.destroy()

        indiceMotivo = 0

        self.tomarMotivoFueraDeServicio(motivosPreseleccionados, indiceMotivo)

    def tomarMotivoFueraDeServicio(self, motivosPreseleccionados, indiceMotivo):

        print(indiceMotivo)

        if indiceMotivo >= len(motivosPreseleccionados):
            self.pedirConfirmacionCierreOrden()
            return

        self.gestor.tomarMotivosFueraServicio(motivosPreseleccionados, indiceMotivo)
        
    def pedirComentario(self, motivos, indiceMotivo):
        win_comentario = tk.Toplevel(self)
        win_comentario.title(f"Comentario para motivo: {motivos[indiceMotivo]}")
        win_comentario.geometry("500x250")
        win_comentario.grab_set()
        tk.Label(win_comentario, text=f"Ingrese comentario para el motivo:'{motivos[indiceMotivo]}'").pack(pady=10)
        self.txt_comentarioMotivoDeCierre = tk.Text(win_comentario, width=60, height=6)
        self.txt_comentarioMotivoDeCierre.pack(pady=5)
        btn_frame = tk.Frame(win_comentario)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Guardar y siguiente", command=lambda: self.tomarComentario(motivos, indiceMotivo, win_comentario)).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Cancelar", command=self.cancelarCierre).pack(side=tk.LEFT)

    def tomarComentario(self, motivos, indiceMotivo, win_comentario):
        comentario = self.txt_comentarioMotivoDeCierre.get("1.0", tk.END).strip()

        self.gestor.tomarComentario(indiceMotivo, comentario)
        win_comentario.destroy()
        indiceMotivo += 1
        self.tomarMotivoFueraDeServicio(motivos, indiceMotivo)

    def pedirConfirmacionCierreOrden(self):
        respuesta = messagebox.askyesno("Confirmar cierre", "¿Desea confirmar el cierre de la orden?")
        if respuesta:
            self.tomarConfirmacionCierre(True)
        else:
            self.tomarConfirmacionCierre(False)

    def tomarConfirmacionCierre(self, confirmado):
        if confirmado:
            for motivo, comentario in self.comentarios_motivos.items():
                self.gestor.tomarMotivoCierre(motivo, comentario)

            if not self.gestor.validarCierreOrden():
                messagebox.showwarning("Atención", "Faltan observación o motivos para cerrar.")
                return

            canal = self.seleccionarCanalNotificacion()
            if canal is None:
                messagebox.showinfo("Cancelado", "Cierre de orden cancelado.")
                return
            notificar_mail, notificar_monitor = canal

            exito = self.gestor.cerrarOrden(notificar_mail=notificar_mail, notificar_monitor=notificar_monitor)
            if exito:
                self.refrescarTabla()
                messagebox.showinfo("Éxito", "Orden cerrada con éxito.")
                if len(self.gestor.buscarOrdenesInspeccion()) == 0:
                    messagebox.showinfo("Información",
                                        "No hay más órdenes de inspección finalizadas asignadas a usted.")
                self.orden_actual = None
                self.tree_item_id = None
            else:
                messagebox.showerror("Error", "Error al cerrar la orden.")
        else:
            messagebox.showinfo("Cancelado", "Cierre de orden cancelado.")

    def seleccionarCanalNotificacion(self):
        ventana = tk.Toplevel(self)
        ventana.title("Canal de notificación")
        ventana.geometry("400x200")
        ventana.grab_set()

        var_mail = tk.BooleanVar(value=True)
        var_monitor = tk.BooleanVar(value=True)

        resultado = {'valor': None}

        tk.Label(ventana, text="¿Cómo desea notificar el cierre de la orden?").pack(pady=10)

        chk_mail = tk.Checkbutton(ventana, text="Notificar por mail", variable=var_mail)
        chk_mail.pack()
        chk_monitor = tk.Checkbutton(ventana, text="Notificar en monitor CCRS", variable=var_monitor)
        chk_monitor.pack()

        def confirmar():
            if not var_mail.get() and not var_monitor.get():
                messagebox.showwarning("Atención", "Seleccione al menos un canal de notificación.")
                return
            resultado['valor'] = (var_mail.get(), var_monitor.get())
            ventana.destroy()

        def cancelar():
            resultado['valor'] = None
            ventana.destroy()

        btn_frame = tk.Frame(ventana)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Confirmar", command=confirmar).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Cancelar", command=cancelar).pack(side=tk.LEFT)

        ventana.wait_window()
        return resultado['valor']

    def cancelarCierre(self):
        if messagebox.askyesno("Cancelar", "¿Está seguro que desea cancelar el cierre de la orden?"):
            self.orden_actual = None
            for ventana in ["win_observacion", "win_motivos", "win_comentario"]:
                if hasattr(self, ventana):
                    w = getattr(self, ventana)
                    if w and w.winfo_exists():
                        w.destroy()
