from tkinter import *   
from tkinter import ttk

#variables
datos = ""
evaluado = False

#funcion para agregar los datos
def agregar(valor):
    global datos, evaluado
    if evaluado:
        datos = ""
        datos = False
    datos += str(valor)
    entrada_texto.set(datos)
    actualizar_resultado()

#funcion borrar
def borrar():
    global datos
    datos = datos[:-1]
    entrada_texto.set(datos)
    actualizar_resultado()

#funcion limpiar
def limpiar():
    global datos, evaluado
    datos = ""
    evaluado = False
    entrada_texto.set("")
    resultado_texto.set("")

#funcion de actualizar los datos
def actualizar_resultado():
    global evaluado
    if not evaluado:
        try:
            resultado = eval(datos)
            resultado_texto.set(f"= {resultado}")
        except:
            resultado_texto.set("")

#funcion que muestra el resultado
def mostrar_resultado_final():
    global evaluado
    try:
        resultado = eval(datos)
        resultado_texto.set(f"= {resultado}")
        evaluado = True
    except:
        resultado_texto.set("Error")
        evaluado = True

# creacion de interfaz grafica
raiz = Tk()
raiz.title("Calculadora Básica")
raiz.geometry("400x600")

#Activaciond de los textos
entrada_texto = StringVar()
resultado_texto = StringVar()

pantalla = Entry(raiz, textvariable=entrada_texto, justify="right",fg="gray", font=("Ventana",18))
pantalla.pack(fill="both", padx=10, pady=5)

resultado = Label(raiz, textvariable=resultado_texto, anchor="e", height=2, font=("Ventana",20))
resultado.pack(fill="both", padx=10, pady=5)

botones = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', 'CE', '+']
]
#ciclo para crear los botones
for fila in botones:
    frame = Frame(raiz)#creacion del frame para los botones
    frame.pack(expand=True, fill="both")
    for btn in fila:
        b = Button(frame, text=btn,
                   command=lambda x=btn: borrar() if x == 'CE' else agregar(x),font=("Ventana",18), bg="lightblue",fg="black", width=5, height=2,highlightbackground="gray",highlightthickness=1)
        b.pack(side="left", expand=True, fill="both",padx=2, pady=2)

# Botón igual 
igual_btn = Button(raiz, text="=",bg="lightblue",fg="black", width=5, height=2,highlightbackground="gray",highlightthickness=1, command=mostrar_resultado_final)
igual_btn.pack(fill="both", padx=10, pady=5, ipady=10)

# Botón limpiar
limpiar_btn = Button(raiz, text="C", command=limpiar,font=("Ventana",18),bg="lightblue",fg="black", width=5, height=2,highlightbackground="gray",highlightthickness=1)
limpiar_btn.pack(fill="both", padx=10, pady=5)

raiz.mainloop()