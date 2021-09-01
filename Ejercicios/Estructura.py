class Cliente:
    nombre = ""
    cantidad = 0

    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad
    
    def depositar(self, valor):
        self.cantidad += valor
    
    def extraer(self, valor):
        self.cantidad -= valor
    
    def mostrar_total(self):
        return f"{self.nombre}: {self.cantidad}"

#....................................................................

class Banco:
    clientes = {}
    def __init__(self):
        ...
    def operar(self, cliente):
        self.clientes[cliente.name] = cliente

    def deposito_total(self):
        total = 0
        for cliente in self.clientes:
            total += cliente.cantidad
        
        return total


def main():
    print("Introduzca un nombre")
    nombre = input()
    print("Introduzca una cantidad")
    cantidad = input()
    instancia = Cliente(nombre, cantidad)
    print("El Total es:", instancia.mostrar_total())

if __name__ == '__main__':
    main()

 
