class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

class Coleccion_de_Objetos:
    lista_alumnos = []
    lista_alumnos.append(Persona('Hugo','Perez',2) )
    lista_alumnos.append(Persona('Paco','Perez',40) )
    lista_alumnos.append(Persona('Luis','Perez',44) )

    def mostrar_lista(self):
        for elemento in self.lista_alumnos:
            print(elemento.nombre, elemento.apellido, elemento.edad)

#Instancias de objetos
curso=Coleccion_de_Objetos()
curso.mostrar_lista()