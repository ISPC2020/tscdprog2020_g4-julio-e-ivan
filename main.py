from cliente import Cliente

def main():
    cliente1 = Cliente([{'nombre' : 'Carlos', 'cantidad' : 1000}, {'nombre' : 'Demian', 'cantidad' : 100000}])
    opcion=0

    while opcion !=9:
        print("=================")
        print("1 - Depositar")
        print("2 - Extraer")
        print("3 - Crear")
        print("9 - Salir")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            cliente1.depositar()
        elif opcion == 2:
            cliente1.extraer()
        elif opcion == 3:
            cliente1.crear()
        elif opcion == 9:
            print("Gracias por su visita")
        else:
            print("La opcion no es válida, vuelva a intentarlo")

if __name__ == '__main__':
    main()