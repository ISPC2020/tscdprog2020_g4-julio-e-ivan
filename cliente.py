from conexion import Conexion

class Cliente:
    def __init__(self):
        objetoConexion = Conexion().conectar()
        colectorDeDatos = objetoConexion.cursor() #metodo cursor esta retornado desde la libreria pymysql

        colectorDeDatos.execute("SELECT * FROM employees limit 10") #por cursor puedo usar execute y hago la consulta a la BD

        resultado = colectorDeDatos.fetchall() #fetchall es un metodo de pymysql que es para traer todos los datos del cursor

        clientes = []
        for row in resultado:
            cliente= {"numero_de_cliente":row[0], "nombre_cliente":row[2], "apellido_cliente":row[3], "cuenta_corriente":row[6]}   
            clientes.append(cliente)

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
        #nombre = input("Ingrese el usuario: ")
        identificacion = int(input("Ingrese su numero de cliente: ")) #Lo agrego para buscar al cliente
        conexion = Conexion().conectar()
        cursor = conexion.cursor()
        #sql= "SELECT * FROM `employees` WHERE emp_no = "
        cursor.execute("SELECT * FROM `employees` WHERE emp_no = %s",  (str(identificacion)))
        resultado = cursor.fetchall()
        cuenta_corriente_act = float(resultado[0][6])
        
        if (len(resultado) > 0):
            ingreso = float(input("Cuanto desea depositar: "))
            cuenta_corriente_nva = ingreso + cuenta_corriente_act
            print("Su cuenta dispone de ", cuenta_corriente_nva)
            cursor_update = conexion.cursor()
            cursor_update.execute("UPDATE employees SET cuenta_corriente = %s WHERE emp_no = %s;", (str(cuenta_corriente_nva), str(identificacion)))
            #UPDATE employees SET cuenta_corriente = 1 WHERE emp_no = 12;
            conexion.commit() 
            
        

        #SELECT * FROM `employees` WHERE emp_no = 06

        #for contacto in range(len(self.contactos)):
            #if nombre == self.contactos[contacto]['nombre']:
                #platitaUsuario = self.contactos[contacto]['cantidad']
                #valor = int(input("Ingrese cuanto desea depositar: "))
                #platitaUsuario += valor
                #self.contactos[contacto]['cantidad'] = platitaUsuario
               # print(platitaUsuario)


    def extraer(self):
        nombre = input("Ingrese el nombre del usuario: ")
        for contacto in range(len(self.contactos)):
            if nombre == self.contactos[contacto]['nombre']:
                platitaUsuario = self.contactos[contacto]['cantidad']
                valor = int(input("Ingrese cuanto desea extraer: "))
                if valor < platitaUsuario:
                    platitaUsuario -= valor
                    self.contactos[contacto]['cantidad'] = platitaUsuario
                    print(platitaUsuario)




#agregar plazo fijo
