file= open("EjemploArchivo.txt","w")
file.write("este es el contenido del archivo")
file.close()#liberar el recurso

lista =["fresa","mango", "papaya"]

with open("EjemploArchivo.txt","a") as file:
    for e in lista:
        file.write(e+"\n")

    print("Lista escrita en el archivo")
lista2=["honda","suzuki","BMV"]

with open("EjemploArchivo.txt","a") as file:
    file.writelines(lista2)
print("lista escrita con writelines")

print("imprimir todo el contenido del archivo")
with open("EjemploArchivo.txt","r") as file:
    print(file.read())
print("leer dos lineas y posteiormente 5 caracteres")
with open("EjemploArchivo.txt","r") as file:
    print(file.readline())
    print(file.readline())
    print(file.readline(5))

print("Almacenar el contenido en una lista y mostrar el ultimo elemento")
with open("EjemploArchivo.txt","r") as file:
    contenido= file.readlines()
    print(contenido[-1])


