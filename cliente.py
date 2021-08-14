class Cliente:
    def __init__(self, contacto):
        self.contactos = contacto

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
            conexion.commit() #probar si hay un auto commit
            #INSERT INTO employees (emp_no, first_name, last_name) VALUES (1, 'Demian', 'Torres');

            print('Se agrego el usuario: ', nombre)
        else:
            print('Ya existe un usuario con numero de cliente')


    # TODO: Analizar el caso en el que no exista un usuario en la base.
    def depositar(self):
        identificacion = int(input("Ingrese su numero de cliente: "))
        #nombre = input("Ingrese el usuario: ")
        for cliente in range(len(self.clientes)):
            if identificacion == self.cliente['numero_de_cliente']:
                platitaUsuario = self.cliente['cuenta_corriente']
                valor = int(input("Ingrese monto a depositar $ "))
                platitaUsuario += valor
                self.cliente['cuenta_corriente'] = platitaUsuario
                conexion = Conexion().conectar()
                cursor = conexion.cursor()        
                sql= "UPDATE employees SET cuenta_corriente = platitaUsuario WHERE emp_no = identificacion;"
                cursor.execute(sql)
                conexion.commit() #probar si hay un auto commit
                print("Su saldo actual es de $ ", platitaUsuario)
            else:
                print("Número de cliente inexistente")

    # TODO: Tiene que ser float
    def extraer(self):
        identificacion = int(input("Ingrese su numero de cliente: "))
        #nombre = input("Ingrese el usuario: ")
        for cliente in range(len(self.clientes)):
            if identificacion == self.cliente['numero_de_cliente']:
                platitaUsuario = self.cliente['cuenta_corriente']
                valor = int(input("Ingrese importe a extraer $ "))
                platitaUsuario -= valor
                self.cliente['cuenta_corriente'] = platitaUsuario
                conexion = Conexion().conectar()
                cursor = conexion.cursor()        
                sql= "UPDATE employees SET cuenta_corriente = platitaUsuario WHERE emp_no = identificacion;"
                cursor.execute(sql)
                conexion.commit() #probar si hay un auto commit
                print("Su saldo actual es de $ ", platitaUsuario)
            else:
                print("Número de cliente inexistente")