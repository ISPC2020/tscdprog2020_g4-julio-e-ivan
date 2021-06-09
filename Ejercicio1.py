#Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.´

class alumno:
    def __init__(self):
        self.nombre=input("Indique el nombre del alumno: ")
        self.nota=float(input("Indique la calificacion del alumno: "))
        
    def mostrar(self):
        print("Nombre: ", self.nombre)
        if self.nota > 6:
            print("El alumno aprobó con ", self.nota)
        else:
            print("El alumno esta desaprobado y su nota es: ", self.nota)

# bloque principal
alumno1=alumno()
alumno1=alumno1.mostrar()




    
