import tkinter as tk
from tkinter import messagebox
from modelo.gimnasio import Gimnasio
from modelo.excepciones import UsuarioExistenteError, UsuarioNoEncontradoError

class InterfazGrafica:
    def __init__(self, master):
        self.master = master
        self.master.title("Gimnasio")
        self.gimnasio = Gimnasio()

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.label = tk.Label(self.frame, text="Gimnasio - Registro de Usuarios")
        self.label.pack()

        self.boton_registrar = tk.Button(self.frame, text="Registrar Usuario", command=self.registrar_usuario)
        self.boton_registrar.pack(pady=10)

        self.boton_consultar = tk.Button(self.frame, text="Consultar Usuario", command=self.consultar_usuario)
        self.boton_consultar.pack(pady=10)

    def registrar_usuario(self):
        self.popup_registrar = tk.Toplevel(self.master)
        self.popup_registrar.title("Registrar Usuario")

        tk.Label(self.popup_registrar, text="Nombre:").pack()
        self.nombre_entry = tk.Entry(self.popup_registrar)
        self.nombre_entry.pack()

        tk.Label(self.popup_registrar, text="Correo:").pack()
        self.correo_entry = tk.Entry(self.popup_registrar)
        self.correo_entry.pack()

        tk.Label(self.popup_registrar, text="Tipo de Membresía:").pack()
        self.membresia_entry = tk.Entry(self.popup_registrar)
        self.membresia_entry.pack()

        tk.Label(self.popup_registrar, text="Tipo de Documento:").pack()
        self.t_documento_entry = tk.Entry(self.popup_registrar)
        self.t_documento_entry.pack()

        tk.Label(self.popup_registrar, text="Número de Documento:").pack()
        self.n_documento_entry = tk.Entry(self.popup_registrar)
        self.n_documento_entry.pack()

        tk.Button(self.popup_registrar, text="Registrar", command=self.confirmar_registro).pack()

    def confirmar_registro(self):
        nombre = self.nombre_entry.get()
        correo = self.correo_entry.get()
        membresia = self.membresia_entry.get()
        t_documento = self.t_documento_entry.get()
        n_documento = self.n_documento_entry.get()

        try:
            self.gimnasio.registrar_usuario(nombre, correo, membresia, t_documento, n_documento)
            messagebox.showinfo("Éxito", "Usuario registrado con éxito.")
            self.popup_registrar.destroy()
        except UsuarioExistenteError as e:
            messagebox.showerror("Error", e.mensaje)

    def consultar_usuario(self):
        self.popup_consultar = tk.Toplevel(self.master)
        self.popup_consultar.title("Consultar Usuario")

        tk.Label(self.popup_consultar, text="Número de Documento:").pack()
        self.n_documento_entry = tk.Entry(self.popup_consultar)
        self.n_documento_entry.pack()

        tk.Button(self.popup_consultar, text="Consultar", command=self.mostrar_usuario).pack()

    def mostrar_usuario(self):
        n_documento = self.n_documento_entry.get()
        try:
            usuario = self.gimnasio.consultar_usuario(n_documento)
            messagebox.showinfo("Usuario Encontrado", f"Nombre: {usuario.nombre}\nCorreo: {usuario.correo}")
            self.popup_consultar.destroy()
        except UsuarioNoEncontradoError as e:
            messagebox.showerror("Error", e.mensaje)
