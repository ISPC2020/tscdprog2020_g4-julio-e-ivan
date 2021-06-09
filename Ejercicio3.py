#Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los métodos para inicializar los atributos, imprimir el valor del lado con un tamaño mayor y el tipo de triángulo que es (equilátero, isósceles o escaleno).

class triangulo:
    def __init__(self):
        self.lado1=float(input("Indica uno de los lados por favor: "))
        self.lado2=float(input("Indica el proximo lado por favor: "))
        self.lado3=float(input("Indica ultimo lado por favor: "))
    def ladomayor(self):
        #aca identifica si se trata de tres lados iguales
        if self.lado1==self.lado2 and self.lado1==self.lado3:
            print("Todos lados son iguales y miden: ", self.lado1)
        #a partir de este punto se enfoca a encontrar el lado mayor en triangulos escalenos
        elif self.lado1>self.lado2 and self.lado1>self.lado3:
            print("el lado mayor es el primero y mide: ", self.lado1)
        elif self.lado2>self.lado1 and self.lado2>self.lado3:
            print("el lado mayor es el segundo y mide: ", self.lado2)
        elif self.lado3>self.lado1 and self.lado3>self.lado2:
            print("el lado mayor es el tercero y mide: ", self.lado3)
        #aquí busca los lados mayores en triangulos isoseles 
        elif self.lado1==self.lado2 and self.lado1>self.lado3:
            print("el primer lado y el segundo son iguales y los mayores. Miden: ", self.lado1)
        elif self.lado2==self.lado3 and self.lado2>self.lado1:
            print("el segundo lado y el tercer son iguales y los mayores. Miden: ", self.lado2)
        elif self.lado3==self.lado1 and self.lado3>self.lado2:
            print("el primer lado y el tercero son iguales y los mayores. Miden: ", self.lado3)
    

tri=triangulo()
tri.ladomayor()



