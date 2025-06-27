from tkinter import *
from tkinter import ttk, messagebox
import csv
import os

archivocsv = 'archivo_datos.csv'

# Crear archivo CSV con encabezados si no existe
#if not os.path.exists(archivocsv):
 #   with open(archivocsv, 'w', newline='') as f:
  #      writer = csv.writer(f)
   #     writer.writerow(['Nombre', 'Apellido Paterno', 'Apellido Materno', 'Correo', 'Móvil', 'Estado Laboral', 'Leer', 'Música', 'Videojuegos', 'Estado'])
#funcion para agregar los datos al archivo
def agregar_datos(datos):
    try:
        with open(archivocsv, 'a', newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerow([
                datos['nombre'], datos['apaterno'], datos['amaterno'],
                datos['correo'], datos['movil'], datos['estado'],
                datos['leer'], datos['musica'], datos['videoj'], datos['estado_combo']
            ])
        messagebox.showinfo("Éxito", "Información agregada correctamente al archivo")
        limpiar_campos()
    except Exception as e:
        messagebox.showerror("Error", f"Error al agregar la información al archivo: {e}")

#funcion para enviar datos 
def enviar_datos():
    datos = {
        'nombre': txtnombre.get(),
        'apaterno': txtapaterno.get(),
        'amaterno': txtamaterno.get(),
        'correo': txtcorreo.get(),
        'movil': txtmovil.get(),
        'estado': estado_var.get(),
        'leer': leer_var.get(),
        'musica': musica_var.get(),
        'videoj': videojuegos_var.get(),
        'estado_combo': comboEstados.get()
    }
    agregar_datos(datos)

#funcion para limpiar los campos
def limpiar_campos():
    txtnombre.delete(0, END)
    txtapaterno.delete(0, END)
    txtamaterno.delete(0, END)
    txtcorreo.delete(0, END)
    txtmovil.delete(0, END)
    estado_var.set("Estudiante")
    leer_var.set(False)
    musica_var.set(False)
    videojuegos_var.set(False)
    comboEstados.set("")

#funcion  para consultar datos del archivo
def consultar_datos():
    if not os.path.exists(archivocsv):
        messagebox.showwarning("Sin datos", "No se encontró el archivo de datos.")
        return

    ventana_consulta = Toplevel(raiz)
    ventana_consulta.title("Muestra Widgets")
    ventana_consulta.geometry("850x300")

    with open(archivocsv, newline='') as archivo:
        lector = csv.reader(archivo)
        for i, fila in enumerate(lector):
            for j, valor in enumerate(fila):
                celda = Label(ventana_consulta, text=valor, borderwidth=1, relief="solid", width=15)
                celda.grid(row=i, column=j, padx=1, pady=1)

#Interfaz
raiz = Tk()
raiz.title("Formulario")
raiz.geometry("500x400")

# Frame de Datos Personales
frame_datos = ttk.Frame(raiz)
frame_datos.place(x=10, y=10, width=300)

ttk.Label(frame_datos, text="Nombre:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
txtnombre = ttk.Entry(frame_datos)
txtnombre.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_datos, text="Apellido Paterno:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
txtapaterno = ttk.Entry(frame_datos)
txtapaterno.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame_datos, text="Apellido Materno:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
txtamaterno = ttk.Entry(frame_datos)
txtamaterno.grid(row=2, column=1, padx=5, pady=5)

ttk.Label(frame_datos, text="Correo:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
txtcorreo = ttk.Entry(frame_datos)
txtcorreo.grid(row=3, column=1, padx=5, pady=5)

ttk.Label(frame_datos, text="Móvil:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
txtmovil = ttk.Entry(frame_datos)
txtmovil.grid(row=4, column=1, padx=5, pady=5)

# estado laboral
estado_var = StringVar()
estado_var.set("Estudiante")
fradio = ttk.Frame(raiz)
fradio.place(x=320, y=25)

ttk.Radiobutton(fradio, text="Estudiante", variable=estado_var, value="Estudiante").grid(row=0, column=2, sticky="w")
ttk.Radiobutton(fradio, text="Empleado", variable=estado_var, value="Empleado").grid(row=1, column=2, sticky="w")
ttk.Radiobutton(fradio, text="Desempleado", variable=estado_var, value="Desempleado").grid(row=2, column=2, sticky="w")

# Frame de Aficiones
faficiones = ttk.LabelFrame(raiz, text="Aficiones")
faficiones.place(x=10, y=170, width=300)

#activacion de los valores en boleano
leer_var = BooleanVar()
musica_var = BooleanVar()
videojuegos_var = BooleanVar()

ttk.Checkbutton(faficiones, text="Leer", variable=leer_var).grid(row=0, column=0, sticky="w")
ttk.Checkbutton(faficiones, text="Música", variable=musica_var).grid(row=0, column=2, sticky="w")
ttk.Checkbutton(faficiones, text="Videojuegos", variable=videojuegos_var).grid(row=0, column=3, sticky="w")

# ComboBox de estados
estado = StringVar()
comboEstados = ttk.Combobox(raiz, textvariable=estado)
comboEstados.place(x=350, y=190)
comboEstados['value'] = (
    "Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Chiapas", "Chihuahua", "Ciudad de México", 
    "Coahuila", "Colima", "Durango", "Estado de México", "Guanajuato", "Guerrero", "Hidalgo", "Jalisco", "Michoacán", 
    "Morelos", "Nayarit", "Nuevo León", "Oaxaca", "Puebla", "Querétaro", "Quintana Roo", "San Luis Potosí", "Sinaloa", 
    "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala", "Veracruz", "Yucatán", "Zacatecas"
)

# Botones
fbotones = ttk.Frame(raiz)
fbotones.place(x=10, y=300)

ttk.Button(fbotones, text="Aceptar", command=enviar_datos).pack(side="left", padx=10)
ttk.Button(fbotones, text="Cancelar", command=limpiar_campos).pack(side="left", padx=10)
ttk.Button(fbotones, text="Consultar", command=consultar_datos).pack(side="left", padx=10)

raiz.mainloop()
