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

    def plazoFijo(self):
        identificacion = int(input("Ingrese su numero de cliente: "))
        #nombre = input("Ingrese el usuario: ")
        for cliente in range(len(self.clientes)):
            if identificacion == self.cliente['numero_de_cliente']:
                platitaUsuario = self.cliente['cuenta_corriente']
                inversion = int(input("Ingrese monto a generar plazo fijo $ "))
                platitaUsuario -= inversion
                plazo = int(input("Ingrese plazo a constituir el Plazo Fijo"))
                interes = float(input("Ingreses tasa de interés convenida"))
                totalInteres = inversion * interes / 100
                self.cliente['cuenta_corriente'] = platitaUsuario
                self.cliente['plazo_fijo'] = inversion
                self.cliente['total_int'] = totalInteres
                conexion = Conexion().conectar()
                cursor = conexion.cursor()        
                sql= "UPDATE employees SET plazo_fijo = inversion, total_int = totalInteres WHERE emp_no = identificacion;"
                cursor.execute(sql)
                conexion.commit() #probar si hay un auto commit
                print("Su saldo actual en Caja de Ahorro es de $ ", platitaUsuario)
                print("Su Plazo Fijo constituido es de $", inversion, "a ", plazo, "días")
                print("Con un interés del ", interes, "%", "y un monto total de intereses de $", totalInteres)

            else:
                print("Número de cliente inexistente")    