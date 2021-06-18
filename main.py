from cliente import Cliente

def main():
    cliente1 = Cliente([{'nombre' : 'Carlos', 'cantidad' : 1000}, {'nombre' : 'Demian', 'cantidad' : 100000}])
    opcion=0

    while opcion !=3:
        print("1 - Depositar")
        print("2 - Extraer")
        print("3 - Salir")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            cliente1.depositar()
        if opcion == 2:
            cliente1.extraer()
        if opcion == 3:
            print("Gracias por su visita")
        else:
            print("La opcion no es válida, vuelva a intentarlo")


if __name__ == '__main__':
    main()