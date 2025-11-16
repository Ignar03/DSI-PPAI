import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from gestor.gestor_inspecciones import GestorInspecciones

class InterfazInspecciones(tk.Frame):
    def __init__(self, app):
        super().__init__(app)
        
        self.habilitarVentana()
        
        self.gestor = GestorInspecciones(self)

    def habilitarVentana(self):

        label = tk.Label(self, text="Ordenes de Inspección", font=("Arial", 18))
        label.pack(pady=20)

        self.list_ordenesInspeccion = ttk.Treeview(self, columns=("ID", "Fecha", "Estacion", "Sismografo"), show="headings")
        self.list_ordenesInspeccion.heading("ID", text="ID Orden", anchor="center")
        self.list_ordenesInspeccion.heading("Fecha", text="Fecha Finalización", anchor="center")
        self.list_ordenesInspeccion.heading("Estacion", text="Estación Sismológica", anchor="center")
        self.list_ordenesInspeccion.heading("Sismografo", text="Sismógrafo", anchor="center")
        self.list_ordenesInspeccion.column("ID", anchor="center", width=70)
        self.list_ordenesInspeccion.column("Fecha", anchor="center", width=200)
        self.list_ordenesInspeccion.column("Estacion", anchor="center", width=200)
        self.list_ordenesInspeccion.column("Sismografo", anchor="center", width=90)
        self.list_ordenesInspeccion.pack(padx=10, pady=10, fill=tk.X)
        self.btn_seleccionarOrden = tk.Button(self, text="Cerrar orden seleccionada", command=self.tomarSeleccionOrdenInspeccion)
        self.btn_seleccionarOrden.pack(pady=10)

    def mostrarOrdCompRealizadas(self, ordenes):
        self.list_ordenesInspeccion.delete(*self.list_ordenesInspeccion.get_children())
        
        for orden in ordenes:
            self.list_ordenesInspeccion.insert("", "end", values=(orden["id"], orden["fechaFinalizacion"], orden["estacionSismologica"], orden["sismografoId"]))

    def pedirSeleccionOrdenInspeccion(self):
        label = tk.Label(self, text="*Por favor seleccione una orden*", font=("Arial", 9), fg="#FF0000")
        label.pack(pady=20)

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
        observacion = self.text_observacion.get("1.0", tk.END).strip()

        if observacion == "":
            messagebox.showwarning("Advertencia", "Debe ingresar una observación de cierre.")
            return
        
        self.gestor.tomarObservacion(observacion)
        self.win_observacion.destroy()

    def mostrarMotivosTipo(self, motivos):
        self.win_motivos = tk.Toplevel(self)
        self.win_motivos.title(f"Motivos de cierre para la orden")
        self.win_motivos.geometry("500x400")
        self.win_motivos.grab_set()
        tk.Label(self.win_motivos, text="Seleccione uno o varios motivos para poner fuera de servicio:").pack(pady=10)
        self.list_motivos = tk.Listbox(self.win_motivos, selectmode=tk.MULTIPLE, width=60, height=10)
        for motivo in motivos:
            self.list_motivos.insert(tk.END, motivo)

        self.list_motivos.pack(pady=10)
        btn_frame = tk.Frame(self.win_motivos)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Aceptar", command=lambda: self.gestor.solicitarSeleccionMotivoFueraDeServicio(motivos)).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Cancelar", command=self.cancelarCierre).pack(side=tk.LEFT)

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
        self.win_comentario.title(f"Comentario para motivo: {motivos[indiceMotivo]}")
        self.win_comentario.geometry("500x250")
        self.win_comentario.grab_set()
        tk.Label(self.win_comentario, text=f"Ingrese comentario para el motivo:'{motivos[indiceMotivo]}'").pack(pady=10)
        self.txt_comentarioMotivoDeCierre = tk.Text(self.win_comentario, width=60, height=6)
        self.txt_comentarioMotivoDeCierre.pack(pady=5)
        btn_frame = tk.Frame(self.win_comentario)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Guardar y siguiente", command=lambda: self.tomarComentario(motivos, indiceMotivo)).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Cancelar", command=self.cancelarCierre).pack(side=tk.LEFT)

    def tomarComentario(self, motivos, indiceMotivo):
        comentario = self.txt_comentarioMotivoDeCierre.get("1.0", tk.END).strip()
        
        # Validamos aca por una mejor UX 🙏🙏
        if comentario == "":
            messagebox.showwarning("Advertencia", "Debe seleccionar al menos un comentario.")
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
            messagebox.showinfo("Éxito", "Orden cerrada con éxito. \n\nMails y notificaciones enviadas a los monitores CCRS.")
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