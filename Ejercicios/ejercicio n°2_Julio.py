#Realizar un programa con una clase persona con las siguientes características:
#a-La clase tendrá como atributos el nombre y la edad de una persona. 
#b-Implementar los métodos necesarios para inicializar los atributos.
#c- mostrar los datos e indicar si la persona es mayor de edad o no.

# Se crea la clase Persona
class Persona:
    # Se crean las funciones para inicializar atributo nombre y edad 
    def _init_ (self, Nombre):
        self.Nombre= input("ingrese nombre:")
        self.edad= int(input("ingrese edad:"))
 
    # Se crea el método para mostrar nombre 
    def mostrar(self):
        print("Nombre: ", self.Nombre)
        
    # Se pregunta y selecciona por  la mayoria de edad
        if self.edad > 17:
             print (self.Nombre, "eres mayor de edad")
        else:
             print (self.Nombre, "eres menor de edad")
 
Persona = Persona ()
Persona = Persona . mostrar () 

