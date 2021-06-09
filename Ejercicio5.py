#Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email. 
#Además deberá mostrar un menú con las siguientes opciones
#Añadir contacto
#Lista de contactos
#Buscar contacto
#Editar contacto
#Cerrar agenda

class agenda:
    def __init__(self):
        self.contactos={}
    def menu(self):
        opcion=0

        while opcion !=5:
            print("1 - Añadir contacto")
            print("2 - Desplegar lista de contactos")
            print("3 - Buscar contacto")
            print("4 - Editar contacto")
            print("5 - Cerrar agenda")
            opcion=int(input("Seleccione una opción: "))

agenda1=agenda()
agenda1.menu()



