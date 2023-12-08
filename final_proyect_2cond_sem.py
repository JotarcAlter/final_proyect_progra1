import oracledb

conexion = oracledb.connect(user='SYSTEM', password='Sopademani_223', dsn='localhost:1521/xe')
cursor = conexion.cursor() 


cursor.execute("SELECT * FROM PRESTAMOS WHERE ID_PRESTAMOS = 321")
filas_data = cursor.fetchall()

for fila in filas_data:
    print(fila)

cursor.close()
conexion.close()





