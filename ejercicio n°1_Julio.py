#Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

#Se crea la clase alumno y la funcion de inicialización de atributos nombre y nota de la clase alumno
class student:
    def _init_ (self):
        self.name= input("introducir nombre de alumno:") 
        
        self.note=float(input("introducir nota:"))
    
 
 #Ahora se debe crear un modo de mostrar si el alumno aprobo o no
    def mostrar(self):
        print("name: ",self.name)
        if self.nota > 7:
            print("El alumno aprobo con: ",self.note)
        else:
            print("El alumno a desaprobado con", self.note)
 
# Bloque principal

student1 = student ()

student1= student1 . mostrar ()