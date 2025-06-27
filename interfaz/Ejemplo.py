from tkinter import * #importar 
from tkinter import ttk

def calcular (*args):
   
        pass

raiz=Tk() #creacion de ventana 
raiz.title("Inicio de sesion") #el titulo principal

marcoPrincipal= ttk.Frame(raiz, padding="4 4 12 12") #marco de trabajo
marcoPrincipal.grid(column=0, row=0, sticky=(N, W, E, S)) #sticky a donde se carga la orienzation del componente
marcoPrincipal.columnconfigure(0, weight=1) #distribucion 
marcoPrincipal.rowconfigure(0, weight=1)

usuarios = StringVar()
contrasena = StringVar()

txtusuario=ttk.Entry(marcoPrincipal, width=20, textvariable=usuarios)
txtusuario.grid(column=2,row=1, sticky=(W))

txtcontrasena=ttk.Entry(marcoPrincipal, width=20, textvariable=contrasena)
txtcontrasena.grid(column=2,row=2, sticky=(W,E))

ttk.Label(marcoPrincipal, textvariable=contrasena).grid(column=2,row=1, sticky=(E))
ttk.Button(marcoPrincipal, text="Ingresar",command=calcular).grid(column=3, row=3, sticky=W)


ttk.Label(marcoPrincipal, text="usuarios").grid(column=1,row=1, sticky=E)
ttk.Label(marcoPrincipal, text="contraseña").grid(column=1,row=2,sticky=W)

for child in marcoPrincipal.winfo_children(): #foco
    child.grid_configure(padx=5, pady=5)

txtusuario.focus()
txtcontrasena.focus()

raiz.mainloop()