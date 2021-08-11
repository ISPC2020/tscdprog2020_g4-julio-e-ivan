from cliente import Cliente
from banco import Banco

def main():



    #datosIniciales = [{'dni': 111, 'nombre': 'Carlos', 'cantidad': 1000}, {'dni': 222, 'nombre': 'Demian', 'cantidad': 10000}, {
    #   'dni': 333, 'nombre': 'Emi', 'cantidad': 10000}, {'dni': 444, 'nombre': 'Mono', 'cantidad': 10000}]
   # baseDeDatos = [{'dni': 111, 'nombre': 'Carlos', 'cantidad': 1000}, {'dni': 222, 'nombre': 'Demian', 'cantidad': 10000}, {
    #    'dni': 333, 'nombre': 'Emi', 'cantidad': 10000}, {'dni': 444, 'nombre': 'Mono', 'cantidad': 10000}]
    opcion = 0
    cliente = Cliente()
    while opcion != 3:
        print("=================")
        print("Ingrese como desea operar")
        print("1 - Cliente")
        print("2 - Banco")
        print("3 - Salir")
        print("=================")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            opcionCliente = 0
            while opcionCliente != 9:
                print("=================")
                print("1 - Depositar")
                print("2 - Extraer")
                print("3 - Crear")
                print("9 - Salir")
                opcionCliente = int(input("Seleccione una opción: "))
                if opcionCliente == 1:
                    cliente.depositar()
                elif opcionCliente == 2:
                    cliente.extraer()
                elif opcionCliente == 3:
                    cliente.crear()
                elif opcionCliente == 9:
                    print("Gracias por su visita")
                else:
                    print("La opcion no es válida, vuelva a intentarlo")
        elif opcion == 2:
            banco = Banco(datosIniciales, cliente.contactos)
            opcionBanco = 0
            while opcionBanco != 3:
                print("=================")
                print("1 - Arqueo inicial")
                print("2 - Arqueo final")
                print("3 - Salir")
                opcionBanco = int(input("Seleccione una opción: "))
                if opcionBanco == 1:
                    print("==============")
                    print("Arqueo inicial: ")
                    print(banco.arqueoInicial())
                    print("==============")
                elif opcionBanco == 2:
                    print("==============")
                    print("Arqueo final: ")
                    print(banco.arqueoFinal())
                    print("==============")
                    print("Balance: ")
                    banco.balance()
                    print("==============")
                elif opcionBanco == 3:
                    print("Gracias por su visita")
                else:
                    print("La opcion no es válida, vuelva a intentarlo")
        elif opcion == 3:
            print("Gracias por su visita")
        else:
            print("La opcion no es válida, vuelva a intentarlo")


if __name__ == '__main__':
    main()
