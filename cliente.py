from conexion import Conexion

class Cliente:
    def __init__(self):
        clientes = []
        self.clientes = clientes

    def crear(self):
                # pedir el ID de empleado para identificarlo
        identificacion = int(input("Ingrese su numero de cliente: "))
        # recorrer el listado de los clientes actuales y buscar de que no exista en la base.
        if not any(cliente['numero_de_cliente'] == identificacion for cliente in self.clientes):
            nombre = input("Ingrese su nombre: ")
            apellido = input("Ingrese su apellido: ")
            #nuevo_cliente = {'numero_de_cliente': identificacion, "nombre_cliente": nombre, "apellido_cliente":apellido, "cuenta_corriente":0}
           # self.contactos.append(nuevo_cliente)
            conexion = Conexion().conectar()
            cursor = conexion.cursor()        
            cursor.execute("insert into employees (emp_no, first_name, last_name) values (%s, %s, %s);", (str(identificacion), nombre, apellido))
            conexion.commit() #probar si hay un auto commit

            print('Se agrego el usuario: ', nombre)
        else:
            print('Ya existe un usuario con numero de cliente')


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


