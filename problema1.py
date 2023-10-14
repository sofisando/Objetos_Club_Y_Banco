# Plantear una clase "club" y otra clas "Socio"
# La clase Socio debe tener los siguientes atributos: nombre del soscio y  su antiguedad en el club (en años)
# En el método init de la clase Socio pedir la carga por teclado del nombre y su antiguedad.
# La clase Club debe tener como atributos 3 objetos de la clase Socio
# Definir un método que imprima el nombre del socio con mayor antiguedad en el club.

class Club:
    def __init__(self):
        self.lista_socios = []
    
    def mostrar_socios(self):
        for socio in self.lista_socios:
            print(f"Nombre: {socio.nombre_socio}")
            print(f"Edad: {socio.antiguedad}")

    def mostrar_socio_mayor_antiguedad(self):
        mayor_antiguedad = 0
        for socio in self.lista_socios:
            if socio.antiguedad > mayor_antiguedad:
                mayor_antiguedad = socio.antiguedad
        for socio in self.lista_socios:
            if socio.antiguedad == mayor_antiguedad:
                print(f"El socio con mayor antiguedad es {socio.nombre_socio} y su antiguedad es de {socio.antiguedad}" )
        

    # ESTO TIRÓ EL CHAT GPT
    # def socio_con_mayor_antiguedad(self):
    #     socio_mas_antiguo = max(self.socios, key=lambda x: x.antiguedad)
    #     print(f"El socio con mayor antigüedad en el club es: {socio_mas_antiguo.nombre} con {socio_mas_antiguo.antiguedad} años de antigüedad.")
        

class Socio:
    def __init__(self):
        self.nombre_socio = input("Ingrese el nombre: ")
        self.antiguedad = int(input("Ingrese antiguedad: "))
   

#funciones fuera de las clases
def cargar_socio(socio , club):
    club.lista_socios.append(socio)


my_club = Club()
for n in range(0,3):
    persona = Socio()
    cargar_socio(persona, my_club)
    
my_club.mostrar_socio_mayor_antiguedad()

