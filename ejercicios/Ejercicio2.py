#Realizar un programa que tenga una clase Persona con las siguientes características. La clase tendrá como atributos el nombre y la edad de una persona. Implementar los métodos necesarios para inicializar los atributos, mostrar los datos e indicar si la persona es mayor de edad o no.

class persona:
    def __init__(self):
        self.nombre=input("Indica tu nombre por favor: ")
        self.edad=float(input("Cuantos años tienes?: "))
    def mostrar(self):
        if self.edad > 17:
            print("Hola ", self.nombre, "eres mayor de edad y puedes continuar")
        else:
            print("Lo siento ", self.nombre, "no puedes continuar ya que eres menor de edad")

persona1=persona()
persona1=persona1.mostrar()


