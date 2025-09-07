from tkinter import *
root = Tk()

texto = Text(root)
texto.insert("1.0", "ola")
texto.config(state="disabled")
texto.pack()

root.mainloop()