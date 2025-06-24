from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def agregar_datos(nombre_archivo,datos):
    try:
        with open(nombre_archivo, 'a') as archivo:
            archivo.write(f"<!--{datos['nombre']}-->\n")
            archivo.write(f"<!--{datos['apaterno']}-->\n")
            archivo.write(f"<!--{datos['amaterno']}-->\n")
            archivo.write(f"<!--{datos['correo']}-->\n")
            archivo.write(f"<!--{datos['tmovil']}-->\n")
            archivo.write(f"<!--{datos['Estudiante']}-->\n")
            archivo.write(f"<!--{datos['Empleado']}-->\n")
            archivo.write(f"<!--{datos['Desempleado']}-->\n")
            archivo.write(f"<!--{datos['Leer']}-->\n")
            archivo.write(f"<!--{datos['Musica']}-->\n")
            archivo.write(f"<!--{datos['Videoj']}-->\n")
            archivo.write(f"<!--{datos['Estados']}-->\n")
        messagebox.showinfo("Exito","informacion agregada correctamente al archivo")
    except Exception as e:
        messagebox.showerror("error",f"error al agregar la informacion al archivo: {e}")

def enviar_datos():
    datos={
        'nombre': txtnombre.get(),
        'apaterno':txtapaterno.get(),
        'amaterno':txtamaterno.get(),
        'correo':txtcorreo.get(),
        'movil':txtmovil.get(),
        'Estudiante':rbEstudiante.get(),
        'Empleado':rbEmpleado.get(),
        'Desempleado':rbDesempleado.get(),
        'Leer':cbLeer.get(),
        'Musica':cbMusica.get(),
        'Videoj':cbVideoj.get(),
        'Estados':comboEstados.get()
    }
    agregar_datos("servicio.svc",datos)





raiz =Tk()
raiz.title("Muestra widgets")
raiz.geometry("500x400")

# Frame de Datos Personales
frame_datos = ttk.Frame(raiz)
frame_datos.place(x=10, y=10, width=300)

ttk.Label(frame_datos, text="Nombre:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
txtnombre=ttk.Entry(frame_datos).grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_datos, text="Apellido Paterno:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
txtapaterno=ttk.Entry(frame_datos).grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame_datos, text="Apellido Materno:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
txtamaterno=ttk.Entry(frame_datos).grid(row=2, column=1, padx=5, pady=5)

ttk.Label(frame_datos,text="Correo").grid(row=3, column=0, padx=5, pady=5, sticky="e")
txtcorreo=ttk.Entry(frame_datos).grid(row=3, column=1, padx=5, pady=5)

ttk.Label(frame_datos,text="Movil").grid(row=4, column=0, padx=5, pady=5, sticky="e")
txtmovil=ttk.Entry(frame_datos).grid(row=4, column=1, padx=5, pady=5)
# RadioButtons en una fila (fuera del frame, a la derecha)
estado_var = StringVar()
estado_var.set("Estudiante")
fradio = ttk.Frame(raiz)
fradio.place(x=320, y=25)

rbEstudiante=ttk.Radiobutton(fradio, text="Estudiante", variable=estado_var, value="Estudiante").grid(row=0, column=2, sticky="w")
rbEmpleado=ttk.Radiobutton(fradio, text="Empleado", variable=estado_var, value="Empleado").grid(row=1, column=2, sticky="w")
rbDesempleado=ttk.Radiobutton(fradio, text="Desempleado", variable=estado_var, value="Desempleado").grid(row=2, column=2, sticky="w")



# Frame de Aficiones
faficiones = ttk.LabelFrame(raiz, text="Aficiones")
faficiones.place(x=10, y=170, width=300)

leer_var =BooleanVar()
musica_var = BooleanVar()
videojuegos_var = BooleanVar()

cbLeer=ttk.Checkbutton(faficiones, text="Leer", variable=leer_var).grid(row=0, column=0, sticky="w")
cbMusica=ttk.Checkbutton(faficiones, text="Música", variable=musica_var).grid(row=0, column=2, sticky="w")
cbVideoj=ttk.Checkbutton(faficiones, text="Videojuegos", variable=videojuegos_var).grid(row=0, column=3, sticky="w")

# ComboBox para estados (fuera de los frames, debajo de Datos Personales)
# Lista de los 32 estados de México

estado=StringVar()  
comboEstados = ttk.Combobox(raiz, textvariable=estado)
comboEstados.place(x=350,y=190)

comboEstados['value'] = ("Aguascalientes", "Baja California", "Baja California Sur", "Campeche",
    "Chiapas", "Chihuahua", "Ciudad de México", "Coahuila", "Colima",
    "Durango", "Estado de México", "Guanajuato", "Guerrero", "Hidalgo",
    "Jalisco", "Michoacán", "Morelos", "Nayarit", "Nuevo León", "Oaxaca",
    "Puebla", "Querétaro", "Quintana Roo", "San Luis Potosí", "Sinaloa",
    "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala", "Veracruz", "Yucatán", "Zacatecas"
)
# Botones 
fbotones = ttk.Frame(raiz)
fbotones.place(x=10, y=300)

ttk.Button(fbotones, text="Aceptar", command=enviar_datos).pack(side="left", padx=10)
ttk.Button(fbotones, text="Cancelar").pack(side="left", padx=10)
ttk.Button(fbotones, text="Consultar").pack(side="left", padx=10)

raiz.mainloop()