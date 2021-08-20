import pymysql

class Conexion:
    
    def __init__(self):
        self.host='127.0.0.1'
        self.user='root'
        self.password=''
        self.db='employees'
        
        
    def conectar(self):
        try:
            conexion = pymysql.connect(host=self.host,
                                    user=self.user,
                                    password=self.password,
                                    db=self.db)
            return conexion   

        except (pymysql.err.OperationalError, pymysql.err.InternalError) as error:
            print("Ocurrió un error al conectar: ", error)

    def ejecutar_consulta(self, consulta):
        coneccion = self.conectar()
        cursor = coneccion.cursor()        
        cursor.execute(consulta)
        coneccion.commit()
        resultado = cursor.fetchall()
        cursor.close() #Cerrar el cursor                
        coneccion.close() 
        return resultado

