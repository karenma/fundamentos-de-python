class Automovil:
    def __init__(self,marca, color):
        #definir atributos de la clase
        #son los que empiezan con self
        self.marca=marca
        self.color=color
    
    def avanzar(self):
        print(f"el coche avanza y es un: {self.marca}")

    def retroceder(self):
        print(f"el coche retrocede y es de color: {self.color}")        

if __name__ == "__main__":
    # objeto 1
     auto = Automovil("BMW", "azul") #crear el objeto
    #se manda llamar el objeto y el metodo
     auto.avanzar() 
     auto.retroceder()
     
     #objeto 2

     auto1= Automovil("Honda","gris")
     auto1.retroceder()
     auto1.avanzar()