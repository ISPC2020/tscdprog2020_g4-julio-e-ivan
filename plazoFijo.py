    
    def plazoFijo(self):
        interes = 3
        identificacion = int(input("Ingrese su numero de cliente: "))
        consulta = "SELECT * FROM 'employees' WHERE emp_no = {};".format(str(identificacion))
        resultado_consulta = Conexion().ejecutar_consulta(consulta)

        if (len(resultado_consulta) > 0):
            cuenta_corriente = float(resultado_consulta [0][6])
            plazo_fijo = int(input("Monto del Plazo Fijo a constituir $ "))
            dias = int(input("Ingrese el plazo a constituir: "))
            while plazo_fijo > cuenta_corriente:
                print("No dispone ese monto en su cuenta corriente")
                plazo_fijo = int(input("Ingrese un monto inferior a $ ", cuenta_corriente))
            cuenta_corriente -= plazo_fijo
            plazo_fijo = plazo_fijo * interes / 100 * dias
            print("Su saldo actual en Cuenta Corriente es de $ ", cuenta_corriente)
            print("Se constituyó el Plazo Fijo por $ ", plazo_fijo, "a ", dias, "dias, con un interés del ", interes, "%")
            consulta_plazo_fijo = "UPDATE employees SET plazo_fijo = {} WHERE emp_no = {};"format(str(cuenta_corriente), str(plazo_fijo), str(identificacion))
            Conexion().ejecutar_consulta(consulta_plazo_fijo)        
        else:
            print("Número de cliente inexistente")    