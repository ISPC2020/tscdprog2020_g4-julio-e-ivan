class Cliente:
    def __init__(self, contacto):
        self.contactos = contacto
        self.cantidad = 0
    
    def crear(self):
        print("Indique los siguientes datos para crear su cuenta: ")
        nombre = input("Nombre: ")
        cantidad = float (input ("Con cuanto inicia la cuenta? "))
        self.contactos[nombre]=(cantidad)
    
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
    
