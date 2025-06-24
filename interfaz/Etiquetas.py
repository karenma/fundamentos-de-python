from tkinter import *  # importación de paquetes
from tkinter import ttk

raiz = Tk()  # creación del elemento raíz
etqTexto = ttk.Label(raiz, text="etiquetas solo texto")
etqTexto.grid()

imagen = PhotoImage(file = "leon.png")

etqImagen = ttk.Label(raiz)
etqImagen.grid()
etqImagen['image'] = imagen

etqCombinada = ttk.Label(raiz, text="etiqueta combinada", compound="center",image=imagen)
etqCombinada.grid()


raiz.mainloop()
