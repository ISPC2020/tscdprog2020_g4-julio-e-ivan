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
                # pedir el nombre / cambiar por ID de empleado
        identificacion = int(input("Ingrese su numero de cliente: "))
        # recorrer el listado de los clientes actuales y buscar de que no exista en la base.
        if not any(cliente['numero_de_cliente'] == identificacion for cliente in self.clientes):
            nombre = input("Ingrese su nombre: ")
            apellido = input("Ingrese su apellido: ")
            #nuevo_cliente = {'numero_de_cliente': identificacion, "nombre_cliente": nombre, "apellido_cliente":apellido, "cuenta_corriente":0}
           # self.contactos.append(nuevo_cliente)
            conexion = Conexion().conectar()
            cursor = conexion.cursor()        
            sql= "insert into employees (emp_no, first_name, last_name) values ("+str(identificacion)+",'"+nombre+"','"+apellido+"');"
            cursor.execute(sql)
            conexion.commit()
            #INSERT INTO employees (emp_no, first_name, last_name) VALUES (1, 'Demian', 'Torres');

            print('Se agrego el usuario: ', nombre)
        else:
            print('Ya existe un usuario con numero de cliente')

    # TODO: Analizar el caso en el que no exista un usuario en la base.
    def depositar(self):
        nombre = input("Ingrese el usuario: ")
        for contacto in range(len(self.contactos)):
            if nombre == self.contactos[contacto]['nombre']:
                platitaUsuario = self.contactos[contacto]['cantidad']
                valor = int(input("Ingrese cuanto desea depositar: "))
                platitaUsuario += valor
                self.contactos[contacto]['cantidad'] = platitaUsuario
                print(platitaUsuario)

    # TODO: Tiene que ser float
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
