    #Método extraer, controlamos que la extracción sea menor al saldo de la cuenta
    def extraer(self):
        identificacion = int(input("Ingrese su numero de cliente: "))
        consulta = "SELECT * FROM 'employees' WHERE emp_no = {};".format(str(identificacion))
        resultado_consulta = Conexion().ejecutar_consulta(consulta)
        
        if (len(resultado_consulta) > 0):
            cuenta_corriente = float(resultado_consulta [0][6])
            importe = int(input("Ingrese el importe a extraer $"))
            #el monto a extraer debe ser menor al saldo xq no puede quedar la cuenta en $0
            while importe >= cuenta_corriente:
                print("Debe ingresar un monto menor a $ ",cuenta_corriente)
                importe = int(input("Ingrese el nuevo importe a extraer $ "))
            #ingresado el monto correcto, se descuenta del saldo de la cuenta del cliente
            cuenta_corriente -= importe
            print("****Retire su dinero****")
            print("Su saldo actual en cuenta corriente es de $ ", cuenta_corriente)
            #se actualiza la base de datos
            consulta_extraer = "UPDASTE employees SET cuenta_corriente = {} WHERE emp_no = {};".format(str(cuenta_corriente), str(identificacion))
            Conexion().ejecutar_consulta(consulta_extraer)
        else:
            print("Número de cliente inexistente")
