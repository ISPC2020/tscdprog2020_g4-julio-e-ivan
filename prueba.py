#class Persona:
#    def inicializar(self,nom):
#        self.nombre=nom
#    def mostrar(self):
#        print("Nombre: ",self.nombre)

#persona1=Persona()
#persona1.inicializar("Ivano")
#persona1.mostrar()

#----------------------------------------------------------

class Persona:
    def __init__(self):
        self.nombre=input("Indica tu nombre por favor:  ")
        self.edad=int(input("indica tu edad por favor: "))

    def mostrar(self):
        print("Nombre: ", self.nombre)
        print("Edad: ",self.edad)

class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.horas=float(input("cuantas horas trabajas?: "))
        self.sueldo=float(input("Cuanto cobras?: "))

    def mostrar(self):
        super().mostrar()
        print("horas: ",self.horas)
        print("Sueldo: ",self.sueldo)


# bloque principal
persona1=Persona()
persona1.mostrar()
empleado1=Empleado() 
empleado1.mostrar()