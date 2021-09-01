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
            if opcion==1:
                self.añaCont()
            elif opcion==2:
                self.contactosAg()
            elif opcion==3:
                self.buscar()
            elif opcion==4:
                self.editar()
            elif opcion==5:
                self.cerrar()
            else:
                print("La opcion no es válida, vuelva a intentarlo")

    def añaCont(self):
        print("Indique los siguientes datos: ")
        nombre=input("Nombre: ")
        tel=input("Telefono: ")
        mail=input("E-Mail: ")
        self.contactos[nombre]=(tel, mail)
    def contactosAg(self):
        print("---"*4)
        print("Contactos agendados")
        for nombre in self.contactos:
            print("Nombre: ", nombre,"Telefono: ", self.contactos[nombre][0],"E-Mail: ", self.contactos[nombre][1])
    def buscar(self):
        nombre=input("Ingrese el nombre tal como esta escrito en la agenda: ")
        if nombre in self.contactos:
            print("Nombre buscado: ", nombre, "Telefono: ", self.contactos[nombre][0], "E-mail: ", self.contactos[nombre][1])
        else:
            print("uppss! El contacto no se encuenra en la lista o la busqueda esta mal ingresada :(")
    def editar(self):
        nombre=input("Ingrese el nombre del contacto a editar: ")
        if nombre in self.contactos:
            tel=input("Ingrese el nuevo nº de teléfono: ")
            mail=input("ingrese el nuevo correo electrónico: ")
            self.contactos[nombre]=[tel,mail]
            print("Los cambios han sido guardados.")
        else:
            print("uppss! El contacto no se encuenra en la lista o la busqueda esta mal ingresada :(")
    def cerrar(self):
        print("Adios!!!")




    
        
                
        

agenda1=agenda()
agenda1.menu()



