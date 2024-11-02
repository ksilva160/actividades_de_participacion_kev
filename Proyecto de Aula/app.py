from modelo.excepciones import UsuarioExistenteError, UsuarioNoEncontradoError, MembresiaInactivaError
from view.interfaz_grafica import InterfazGrafica

if __name__ == "__main__":
    # Inicializa la interfaz gráfica
    import tkinter as tk
    
    root = tk.Tk()
    interfaz = InterfazGrafica(root)
    root.mainloop()


