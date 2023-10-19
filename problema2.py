# un banco tiene 3 clientes que pueden hacer depositos y extracciones (metodos creo)
# se requiere que el banco calcule al finalizar el dia la cantidad del dinero que hay depositado y tambien el saldo que posee cada cliente.

# creo que seria una plantilla para que los clientes puedan tener los metodos, y como atributos los saldos de cada uno

class Banco:
    def __init__(self):
        self.lista_clientes = []
        self.dinero = int(input('¿Cual es el saldo del banco?: '))

    def saldo_depositado(self):
        for cliente in self.lista_clientes:
            total_banco = 0
            total_banco += cliente.saldo
        return print('El total depositado en el banco es:', total_banco)

    def dinero_clientes(self):
        for cliente in self.lista_clientes:
            print(f'El saldo del cliente: {cliente.nombre_cliente} es: {cliente.saldo}')


class Clientes:
    def __init__(self):
        self.nombre_cliente = input("Ingrese el nombre: ")
        self.saldo = int(input("Ingrese su saldo: "))

    def depositar(self, banco):
        cant = int(input('¿Cual es el monto a depositar?: '))
        self.saldo -= cant #restar del saldo
        banco.dinero += cant #sumar al banco
        
    def extraer(self, banco):
        cant = int(input('¿Cual es el monto a depositar?: '))
        
        banco.dinero -= cant  #restar del banco



#funciones fuera de las clases
def cargar_cliente(cliente , banco):
    banco.lista_clientes.append(cliente)


# instancias
print('Se instanciará un nuevo banco\n')
my_banco = Banco()
print('\nSe crearán 3 clientes de ese banco\n')
persona1 = Clientes()
cargar_cliente(persona1, my_banco)
# persona2 = Clientes()
# cargar_cliente(persona2, my_banco)
# persona3 = Clientes()
# cargar_cliente(persona3, my_banco)

print('Saldo del banco actual:')
print(my_banco.dinero)

print('persona2 quiere depositar')
persona1.depositar(my_banco)        #cambiar a persona2

print('Se vuelve a mostrar el saldo del banco sumando el deposito del cliente')
print(my_banco.dinero)

print('Se muestra el saldo de persona2')
print(persona1.saldo)


    

