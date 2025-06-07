def nuevo_tema(tema):
    print("\n-----",tema,"-------\n")


if __name__=="__main__":
    nuevo_tema("operadores aritmeticos")
    print ("Operador suma 3+5=", 3 + 5)
    print ("Operador resta 9-8=", 9 + 8)
    print ("Operador multiplicacion  3*5=", 3 * 5)
    print ("Operador division 3/5=", 3 / 5)
    print ("Operador division entera 3//5=", 3 // 5)
    print ("Operador residuo 10%3", 10%3)
    print ("Operador Exponente 3^5=", 3 ^5)
    #este comentario de una sola linea
    '''este es un comenrario 
    de varias lineas?'''
    nuevo_tema("operadores Logicos")
    #tablas de verdad de and
    nuevo_tema("tabla de verdad and")
    print("True and Tue:",True and True)
    print("True and False:",True and False)
    print("False and True:",False and True)
    print("False and False:",False and False)
    #tablas de verdad de or
    nuevo_tema("tabla de verdad de or")
    print("True or Tue:",True or True)
    print("True or False:",True or False)
    print("False or True:",False or True)
    print("False or False:",False or False)
    #tablas de verdad de not
    nuevo_tema("tabla de verdad de negacion")
    print("not False:",not False)
    print("not True:",not True)
   #operadores de comparación
    nuevo_tema("operadores de comparacion")
    print("operador de igualdad 5==5",5==5)
    print("operador de desigual 5!=3",5!=3)
    print("operador de menor que 2<10",2<10)
    print("operador de menor o igual que 1<=3",1<=3)
    print("operador de mayor que 5>3",5>3)
    print("operador de igualdad 6>=5",6>=5)

    nuevo_tema("variables")
    variable1 = 10
    variable2 =6.25
    variable3 ="Pepe"
    nombreVariable=8
    nombre_variable=34.2
    print(variable1,variable2,variable3,nombreVariable,nombre_variable)
    a,b,c= 5,10.8,"hola"
    print(a)
    print(b)
    print(c)
#ejemplo de variable dinamica
    nombre_variable= "Adios"
    print(nombre_variable)
    nuevo_tema("enteros")
    w = 105
    x = 1234567890998887666
    y = -58
    z = 0b000110011
    h = 0xFF

    print(w,type(w))
    print(x,type(x))
    print(y,type(y))
    print(z,type(z))
    print(h,type(h))
    
    nuevo_tema("Flotantes")
    x =1234.56
    print(x,type(x))
    y =-0.3444
    print(y,type(y))

    nuevo_tema("Complejos")
    x =-46j
    y=12+45j
    z=2j
    c =y+z
    print(x,type(x))
    print(y,type(y))
    print(z,type(z))
    print(c,type(c))
    nuevo_tema("boleanos")
    x = True
    print(x,type(x))
    nuevo_tema("listas")
    lista= [10,20.5,"lista de Python"]
    print(lista)
    print(lista[1])
    lista[0] ="hola"
    lista.append(34)
    print(lista)
    lista.insert(0,1.1)
    print(lista)
    lista.append([3,4,5,6,7,8])
    print(lista)
    print(lista[5])
    print(lista[5][4])
    print(lista[3][4])
    nuevo_tema("tuplas")
    tupla=(25,"tupla",1+10j)
    print(tupla)
    print(tupla[1])
    tupla=(25,"tupla",1+10j,"otro")
    #tupla[1]=0 operacion no valida en tuplas
    print(tupla)
    nuevo_tema("conjuntos")
    conjunto={10,20,30,40,50}
    print(conjunto)

    print(50 in conjunto)
    nuevo_tema("diccionarios")
    diccionario={"nombre":"Conrado",
                 "edad":43,
                 "telefono":123456788,
                 90 :4+3j}
    print(diccionario)
    print(diccionario["nombre"])
    print(diccionario[90])
    nuevo_tema("cadenas")
    cadena1="esto es una cadena"
    cadena2='esto es otra cadena'
    cadena_multilinea='''esto es una cadena de varias lineas
    con varios tabuladores
    salits
    de 
    linea'''
    print(cadena1,type(cadena1))
    print(cadena2,type(cadena2))
    print(cadena_multilinea,type(cadena2))
    cadena3="hola "*5
    print(cadena3)
    print(cadena1[2])#posicion 
    print(cadena1[2:10]) #un unicio y un fin
    print(cadena1[:5])#del inicio de la cadena a un punto
    print(cadena1[5:])#de un punto de la cadena hasta el fina
    print(cadena1[5:-5])# de un inicio al final
    print(cadena1[::-1])#escribir al reves la cadena