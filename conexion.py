import mysql.connector
import pymysql

try:
    conexion=mysql.connector.connect(host='localhost',
                                 user='root',
                                 password='administrador',
                                 database='asistencia')

except Exception as err:
        print('ERROR CONECTANDO A LA BASE')
else:
    print('CONECTADO A MYSQL')
conexion.close()