
def imprimircuestionario():
    with open("pregunta1", "r") as archivo:
        print(archivo.read())

imprimircuestionario()