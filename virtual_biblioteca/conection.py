import oracledb

class DataCon():
    def __init__(self) -> None:


        self.conexion = oracledb.connect(user='SYSTEM', password='Sopademani_223', dsn='localhost:1521/xe')
        self.cursor = self.conexion.cursor() 

    def closing(self):
        self.cursor.close()
        self.conexion.close()