from fundamentos import nuevo_tema #esta funcion manda llamar una funcion de otro archivo .py
import calc.operaciones  # se importa con el paquete el archivo completo y se le agrega un alias con as
if __name__=="__main__": #funcion principal main
    nuevo_tema("modulos y paquetes")
    print(cal.operaciones.resta(4, 1))