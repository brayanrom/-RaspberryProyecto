import mysql.connector as mysql
from CheckTypeValues import CheckTypeValues
from datetime import date
import time

ctv = CheckTypeValues()

class DatabaseSQLDB:

    def __init__(self):
        self.mydb = mysql.connect(
            host="localhost",
            user="root",
            password="",
            database="IoT"
            )
        print(self.mydb)
        self.mycursor = self.mydb.cursor()

    def all(self):
        self.mycursor.execute("SHOW DATABASES")
        for x in self.mycursor:
            print(x)
    
    def insert(self, tabla, valores):
        if tabla == "sensores_tipos":
            t = valores.get('tipo')
            self.mycursor.execute('INSERT INTO %s (tipo) values ("%s")' % (tabla, t))
            self.mydb.commit()
        elif tabla == "sensores_registrados":
            n = valores.get('nombre')
            tipo_sensor = valores.get('tipo_id')
            self.mycursor.execute('INSERT INTO %s (nombre, tipo_id) values ("%s", "%s")' % (tabla, n, tipo_sensor))
            self.mydb.commit()
        elif tabla == "historial":
            s = valores.get('sensor_id')
            val = valores.get('valor')
            fecha_tiempo = valores.get('fecha_tiempo')
            if ctv.isInt(val):
                self.mycursor.execute('INSERT INTO %s (sensor_id, valor_int, fecha_tiempo) VALUES ("%s", "%s", "%s")'% (tabla, s, val, fecha_tiempo))
                self.mydb.commit()
            elif ctv.isFloat(val):
                self.mycursor.execute('INSERT INTO %s (sensor_id, valor_dec, fecha_tiempo) VALUES ("%s", "%s", "%s")'% (tabla, s, val, fecha_tiempo))
                self.mydb.commit()
            elif ctv.isString(val):
                self.mycursor.execute('INSERT INTO %s (sensor_id, valor_str, fecha_tiempo) VALUES ("%s", "%s", "%s")'% (tabla, s, val, fecha_tiempo))
                self.mydb.commit()
            elif ctv.isNumericBool(val):
                self.mycursor.execute('INSERT INTO %s (sensor_id, valor_bool, fecha_tiempo) VALUES ("%s", "%s", "%s")'% (tabla, s, val, fecha_tiempo))
                self.mydb.commit()
            else:
                print("El valor recibido no es valido")
        
    def select(self, tabla):
        self.mycursor.execute('SELECT * FROM %s' % (tabla))
        myresult = self.mycursor.fetchall()
        for x in myresult:
            print(x)
        
    def delete(self, tabla, valores):
        for clave, x in valores.items():  
            columna = clave
        valor = valores.get(columna)
        self. mycursor.execute('DELETE FROM %s where %s = "%s"' % (tabla, columna , valor))
        self.mydb.commit()     
        




''' EJEMPLO DE INSERCION
db = DatabaseSQLDB()

db.all()


today = date.today()
time = time.strftime("%H:%M:%S")
fecha = str(today) + ' ' + str(time)
print(fecha)

tabla = "historial"
valores = {"sensor_id":1, "valor":1, "fecha_tiempo":fecha}

db.insert(tabla, valores)
db.select(tabla) '''




# ASI FUNCIONA PARA SACAR LA FECHA ACTUAL
# today = date.today()
# time = time.strftime("%H:%M:%S")
# fecha = str(today) + ' ' + str(time)
# print(fecha)


# EJEMPLO DE INSERTAR EN TABLA SENSORES_TIPOS
# db = Database()
# tabla = "sensores_tipos"
# valores = {"tipo":"pir"}
# db.insert(tabla, valores )
# db.select(tabla)


# EJEMPLO DE INSERTAR EN TABLA SENSORES_REGISTRADOS
# tabla = "sensores_registrados"
# valores = {"nombre":"pir_sala", "tipo_id":1}
# db.insert(tabla, valores )
# db.select(tabla)


# EJEMPLO DE INSERTAR EN TABLA HISTORIAL
# tabla = "historial"
# valores = {"sensor_id": 1, "valor_bool":1, "fecha_tiempo":fecha}
# db.insert(tabla, valores )
# db.select(tabla)



# EJEMPLO DE ELIMINAR
# tabla = "historial"
# valores = {"sensor_id":1}
# db.delete(tabla, valores)
# db.select(tabla)  


