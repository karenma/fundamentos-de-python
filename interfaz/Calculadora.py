from tkinter import *   
from tkinter import ttk

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

def actualizar_resultado():
    global evaluado
    if not evaluado:
        try:
            resultado = eval(datos)
            resultado_texto.set(f"= {resultado}")
        except:
            resultado_texto.set("")

def mostrar_resultado_final():
    global evaluado
    try:
        resultado = eval(datos)
        resultado_texto.set(f"= {resultado}")
        evaluado = True
    except:
        resultado_texto.set("Error")
        evaluado = True

# Interfaz gráfica
raiz = Tk()
raiz.title("Calculadora Básica")
raiz.geometry("400x600")
raiz.resizable(False, False)

entrada_texto = StringVar()
resultado_texto = StringVar()

entrada = Entry(raiz, textvariable=entrada_texto, justify="right")
entrada.pack(fill="both", padx=10, pady=5)

resultado = Label(raiz, textvariable=resultado_texto, anchor="e", height=2)
resultado.pack(fill="both", padx=10, pady=5)

botones = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '←', '+']
]

for fila in botones:
    frame = Frame(raiz)
    frame.pack(expand=True, fill="both")
    for btn in fila:
        b = Button(frame, text=btn,
                   command=lambda x=btn: borrar() if x == '←' else agregar(x))
        b.pack(side="left", expand=True, fill="both")

# Botón igual 
igual_btn = ttk.Button(raiz, text="=", command=mostrar_resultado_final)
igual_btn.pack(fill="both", padx=10, pady=5, ipady=10)

# Botón limpiar (rojo)
limpiar_btn = Button(raiz, text="C", command=limpiar)
limpiar_btn.pack(fill="both", padx=10, pady=5)

raiz.mainloop()