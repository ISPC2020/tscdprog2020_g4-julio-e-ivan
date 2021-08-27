    def plazoFijo(self):
        interes = 1.03
        identificacion = int(input("Ingrese su numero de cliente: "))
        conexion = Conexion().conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM 'employees' WHERE emp_no = &s", (str(identificacion)))
        resultado = cursor.fetchall()
        cuenta_corriente = float(resultado[0][6])
        consulta = "SELECT * FROM 'employees' WHERE emp_no = {};".format(str(identificacion))
        resultado_consulta = Conexion().ejecutar_consulta(consulta)

        if (len(resultado_consulta) > 0):
            cuenta_corriente = float(resultado_consulta [0][6])
            plazo_fijo = int(input("Monto del Plazo Fijo a constituir $ "))
            if (plazo_fijo < cuenta_corriente):
                cuenta_corriente -= plazo_fijo
                plazo_fijo = plazo_fijo * interes
                print("Su saldo actual en Cuenta Corriente es de $ ", cuenta_corriente)
                print("Su Plazo Fijo constituido con intereses es de $ ", plazo_fijo)
                cursor_update = conexion.cursor()
                cursor_update.execute("UPDATE employees SET plazo_fijo = %s WHERE emp_no = %s;", (str(cuenta_corriente), str(plazo_fijo), str(identificacion)))
                conexion.commit()
            else:
                print("No dispone ese monto en su cuenta corriente")    
        else:
            print("Número de cliente inexistente")    