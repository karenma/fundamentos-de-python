from tkinter import * #importacion de paquetes
from tkinter import ttk


raiz=Tk()
#boton con texto
boton= ttk.Button(raiz, text="Boton solo texto")
boton.grid()

imagen= PhotoImage (file="leon1.png")

#boton con imagen
btnImagen=ttk.Button(raiz)
btnImagen.grid()
btnImagen['image']=imagen

#boton con imagen y texto
btnCombinado=ttk.Button(raiz)
raiz.mainloop()