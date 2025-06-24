from fundamentos import nuevo_tema #esta funcion manda llamar una funcion de otro archivo .py
import calc.operaciones as c # se importa con el paquete el archivo completo y se le agrega un alias con as
if __name__=="__main__": #funcion principal main
    nuevo_tema("modulos y paquetes")
    print(c.resta(4, 1))
    print(c.suma(2, 3, 4))
    print(c.mult(5, 6))
    print(c.div(11, 2.5))