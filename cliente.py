from conexion import Conexion

class Cliente:
    def __init__(self):
        clientes = []
        self.clientes = clientes

    def crear(self):
        identificacion = input("Ingrese un numero que será su numero de cliente: ")#Lo agrego para buscar al cliente
        consulta = "SELECT * FROM `employees` WHERE emp_no = {};".format(identificacion)
        resultado_verificacion = Conexion().ejecutar_consulta(consulta)
        if (len(resultado_verificacion) < 1): 
            apellido = input("Indique su apellido: ")
            nombre = input("Indique su nombre: ")
            sql = (f"insert into employees (emp_no, first_name, last_name) values ({identificacion}, '{nombre}', '{apellido}')")
            prueba = Conexion().ejecutar_consulta(sql)
        else:
            print("El usuario ya se encuentra registrado, elija otro numero de identificacion")



    def depositar(self):
        identificacion = int(input("Ingrese su numero de cliente: ")) #Lo agrego para buscar al cliente
        consulta = "SELECT * FROM `employees` WHERE emp_no = {};".format(str(identificacion))
        resultado_consulta = Conexion().ejecutar_consulta(consulta)
        
        if (len(resultado_consulta) > 0): #Con Len cuento los resultados y le digo que si es mas de 0 que vaya con el if
            cuenta_corriente_act = float(resultado_consulta[0][6]) #guardo en cuenta corriente el dato del resultado 1 y el valor de la posición 6 que es la de cuenta corriente
            ingreso = float(input("Cuanto desea depositar: "))
            cuenta_corriente_nva = ingreso + cuenta_corriente_act
            print("Su cuenta dispone de ", cuenta_corriente_nva)
            consultaupdate = "UPDATE employees SET cuenta_corriente = {} WHERE emp_no = {};".format(str(cuenta_corriente_nva), str(identificacion))
            Conexion().ejecutar_consulta(consultaupdate)
        else:
            print("El usuarion no se encuentra registrado. Verifique el numero o cree un usuario nuevo")

    def extraer(self):
        identificacion = int(input("Ingrese su numero de cliente: ")) #Lo agrego para buscar al cliente
        consulta = "SELECT * FROM `employees` WHERE emp_no = {};".format(str(identificacion))
        resultado_consulta = Conexion().ejecutar_consulta(consulta)
        
        if (len(resultado_consulta) > 0): #Con Len cuento los resultados y le digo que si es mas de 0 que vaya con el if
            cuenta_corriente_act = float(resultado_consulta[0][6]) #guardo en cuenta corriente el dato del resultado 1 y el valor de la posición 6 que es la de cuenta corriente
            egreso = float(input("Cuanto desea extraer?: "))
            cuenta_corriente_nva = cuenta_corriente_act - egreso
            print("Su cuenta dispone de ", cuenta_corriente_nva)
            consulta_extraer = "UPDATE employees SET cuenta_corriente = {} WHERE emp_no = {};".format(str(cuenta_corriente_nva), str(identificacion))
            Conexion().ejecutar_consulta(consulta_extraer)
        else:
            print("El usuarion no se encuentra registrado. Verifique el numero o cree un usuario nuevo")


