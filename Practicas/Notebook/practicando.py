import tkinter as tk
from tkinter import filedialog, messagebox

def guardar_archivo():
    archivo = filedialog.asksaveasfilename(defaultextension=".txt",
                                           filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if archivo:
        with open(archivo, "w") as f:
            f.write(texto.get("1.0", tk.END))
        messagebox.showinfo("Guardar", "Archivo guardado exitosamente")

def abrir_archivo():
    archivo = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if archivo:
        with open(archivo, "r") as f:
            contenido = f.read()
        texto.delete("1.0", tk.END)
        texto.insert(tk.END, contenido)
        messagebox.showinfo("Abrir", "Archivo cargado exitosamente")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Bloc de Notas")

# Crear un widget de texto
texto = tk.Text(ventana, wrap=tk.WORD)
texto.pack(expand=True, fill=tk.BOTH)

# Crear un menú
menu_bar = tk.Menu(ventana)
ventana.config(menu=menu_bar)

# Añadir opciones al menú
menu_archivo = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Abrir", command=abrir_archivo)
menu_archivo.add_command(label="Guardar", command=guardar_archivo)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=ventana.quit)

# Iniciar el bucle de la aplicación
ventana.mainloop()
