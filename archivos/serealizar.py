import pickle
info=[35,88,3.14,16]

with open("./archivos/ArchivoSerial","wb") as binFile:
    pickle.dump(info,binFile)

print("archivo binario escrito")