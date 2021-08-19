
"""
Created on Tue Jun 15 16:38:14 2021

@author: Sil
"""
        

#Banco tiene una relación de Agregación con Clientes y Empleados        
class Banco:
    
    #Creamos el constructor de la clase Banco
    def __init__(self, clientes, empleados):
        self.clientes = clientes
        self.empleados = empleados
        totalDepositado = 0

#clase Padre que será heredada por Clientes y Empleados
class Persona:
    
    def __init__(self):
        self.dni = 0
        self.nombre = ""
        self.telefono = 0
        self.email = ""
        #self.datosClientes = {Clientes()}
        #self.datosEmpleados = {Empleados()} 
    
    def cargarDatos(self):
        self.dni = int(input("Ingrese el DNI de la persona: "))
        self.nombre = input("Ingrese el nombre de la persona ")
        self.telefono = int(input("Ingrese el teléfono de la persona: "))
        self.email = input("Ingrese el email de la persona: ")
      
    """def modificarDatos(self):
        dni = input("Ingrese el DNI de la persona que quiere modificar")
        for c in :
            self.nombre
       """ 
        
        
#clase Empleados hereda de clase Persona  
class Empleados(Persona): 
    def __init__(self):
        super().__init__()
        self.datosEmpleados = {}
        
    
    def cargarDatos(self):
        super().cargarDatos() 
        self.datosEmpleados.append(self.dni, self.nombre, self.telfono, self.email)

        
#clase Clientes hereda de clase Persona
class Clientes(Persona):
    
    #Contructor de la clase Clientes
    def __init__(self):
        super().__init__()
        self.datosClientes = {}
        self.CajaAhorro = CajaAhorro(self.nombre, 0)
        self.PlazoFijo = PlazoFijo(self.nombre, 0,0,0.0)
        
        
    def cargarDatos(self):
        super().cargarDatos()
        self.datosClientes.append(self.dni, self.nombre, self.telfono, self.email)

        
    #Método depositar
    def depositar(self):
        monto = int(input("Ingrese el monto a depositar $ "))
        #acumula los montos depositados por el cliente
        self.cantidad += monto
        #se actualiza el diccionario
        self.datosClientes[self.dni] = [self.nombre, self.cantidad]
    
    #Método extraer, controlamos que la extracción sea menor al saldo de la cuenta
    def extraer(self):
        importe = int(input("Ingrese el importe a extraer $"))
        #el monto a extraer debe ser menor al saldo xq no puede quedar la cuenta en $0
        while importe >= self.cantidad:
            print("Debe ingresar un monto menor a $",self.cantidad)
            importe = int(input("Ingrese el nuevo importe a extraer $"))
        #ingresado el monto correcto, se descuenta del saldo de la cuenta del cliente
        self.cantidad -= importe
        print("****Retire su dinero****")
        #se actualiza el diccionario
        self.datosClientes[self.dni] = [self.nombre, self.cantidad]
        
    #Método mostrar Total
    def imprimirTotal(self):
        total = self.cantidad
        print("Su saldo actual es de $", total)
        
#clase Padre, que será heredada de Caja de Ahorro y Plazo Fijo   
class Cuentas:
    
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad
        
    def imprimir(self):
        print("Titular de la Cuenta ", self.titular)
        print("Saldo de la Cuenta ", self.cantidad)
        
#clase hija de Cuentas
class CajaAhorro(Cuentas):
    
    #constructor de la clase, hereda el constructor de Cuentas
    def __init__(self, titular, cantidad):
        super().__init__(titular, cantidad)
    
    #Método para impirmir los datos de la Caja de Ahorro
    def imprimir(self):
        print("***Caja de Ahorro***")
        super().imprimir()

#clase hija de Cuentas        
class PlazoFijo(Cuentas):
    #constructor de la clase, hereda el constructor de Cuentas
    def __init__(self, titular, cantidad, plazo, interes):
        super().__init__(titular, cantidad)
        self.plazo = plazo
        self.interes = interes
        
    def importeInteres(self):
        interesTotal = self.cantidad * self.interes/100
        return interesTotal
    
    #Método para impirmir los datos del Plazo Fijo
    def imprimir(self):
        print("***Plazo Fijo***")
        super().imprimir()
        print("El plazo fijo es a ", self.plazo, "días, con tasa de interés de ", self.interes, "%")
        print("El interés total es de ", self.importeInteres())
        
