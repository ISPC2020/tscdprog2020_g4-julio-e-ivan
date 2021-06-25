class Cliente:
    def __init__(self, contacto):
        self.contactos = contacto

    def crear(self):
        # pedir el nombre
        nombre = input("Ingrese el usuario: ")
        # recorrer el listado de los clientes actuales y buscar de que no exista en la base.
        if not any(contacto['nombre'] == nombre for contacto in self.contactos):
            nuevoContacto = {'nombre': nombre, 'cantidad': 0}
            self.contactos.append(nuevoContacto)
            print('Se agrego el usuario: ', nombre)
        else:
            print('Ya existe un usuario con ese nombre')

    # TODO: Analizar el caso en el que no exista un usuario en la base.
    def depositar(self):
        nombre = input("Ingrese el usuario: ")
        for contacto in range(len(self.contactos)):
            if nombre == self.contactos[contacto]['nombre']:
                platitaUsuario = self.contactos[contacto]['cantidad']
                valor = int(input("Ingrese cuanto desea depositar: "))
                platitaUsuario += valor
                self.contactos[contacto]['cantidad'] = platitaUsuario
                print(platitaUsuario)

    # TODO: Tiene que ser float
    def extraer(self):
        nombre = input("Ingrese el nombre del usuario: ")
        for contacto in range(len(self.contactos)):
            if nombre == self.contactos[contacto]['nombre']:
                platitaUsuario = self.contactos[contacto]['cantidad']
                valor = int(input("Ingrese cuanto desea extraer: "))
                if valor < platitaUsuario:
                    platitaUsuario -= valor
                    self.contactos[contacto]['cantidad'] = platitaUsuario
                    print(platitaUsuario)
