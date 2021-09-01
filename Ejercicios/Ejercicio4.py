#Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método init. Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.

class calculadora:
    def __init__(self):
        print("Te pediré que ingreses dos valores")
        print("ATENCION!!!primero ingresa el valor mayor")
        self.valor1=float(input("Por favor ingresá un valor: "))
        self.valor2=float(input("Por favor ingresá un valor más: "))
    def suma(self):
        print()
        print()
        self.suma=self.valor1+self.valor2
        print("La suma de los valores es igual a: ",self.suma)
    def resta(self):
        self.resta=self.valor1-self.valor2
        print("La resta del primer valor menos el segundo es de: ",self.resta)
    def multiplicacion(self):
        self.multiplicacion=self.valor1*self.valor2
        print("Los valores multiplicados son igual a: ",self.multiplicacion)
    def divicion(self):
        if self.valor2!=0:
            self.divicion=self.valor1/self.valor2
            print("El valor1 dividido el valor2 es igual a: ",self.divicion)
        else:
            print("No es posible dividir por 0")


    

    

cal=calculadora()
cal.suma()
cal.resta()
cal.multiplicacion()
cal.divicion()
cal.multiplicacion()
