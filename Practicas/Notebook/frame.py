import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Dividir ventana con LabelFrame")

# Crear un LabelFrame
lf = tk.LabelFrame(root, text="Sección 1", padx=20, pady=20)
lf.pack(padx=10, pady=10, fill="both", expand=True)

# Añadir widgets dentro del LabelFrame
label1 = tk.Label(lf, text="Este es un Label dentro de LabelFrame")
label1.pack(pady=20)

# Iniciar el loop principal
root.mainloop()
