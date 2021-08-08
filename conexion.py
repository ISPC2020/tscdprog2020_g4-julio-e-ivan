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

