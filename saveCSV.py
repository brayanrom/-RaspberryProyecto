from sqldb import DatabaseSQLDB
from mongodb import DatabaseMongoDB

import time
from datetime import date
from sqldb import DatabaseSQLDB

class saveCSV():        
        #insercion de los datos en bucle
    def postPersona(self,dato1="NULL",dato2="NULL",dato3="NULL",dato4="NULL"):

        archivo = open("sensores.csv", "a")

        archivo.write(dato1)
        archivo.write(",")   

        archivo.write(dato2)
        archivo.write(",")  

        archivo.write(dato3)
        archivo.write(",")  

        archivo.write(dato4)

        archivo.write("\n")
        archivo.close()

        valores = {"temperatura": dato3, "humedad":dato4, "pir":dato2, "distancia":dato1}



    def insertSensorIndividual(self,dato , Id_sensor, dato2 = None):
        '''archivo = open("sensores.csv", "a")

        #imprime el tipo de sensor
        archivo.write(str(sensorTipo))
        archivo.write(",")'''
        

        if dato and dato2:
            valores = {"sensor_id":Id_sensor, "valor":dato}
            valores2 = {"sensor_id":Id_sensor, "valor":dato2}
            self.guardarDatos(valores, valores2)
        else:
            valores = {"sensor_id":Id_sensor, "valor":dato}
            self.guardarDatos(valores)
        
        
        '''
        # distancia
        if Id_sensor==4:
            archivo.write(dato)
            archivo.write(", NULL,NULL, NULL") 
            valores = {"sensor_id":Id_sensor, "valor":float(dato)}
            self.guardarDatos(valores)

        # pir
        if Id_sensor==6:
            archivo.write("NULL,")
            archivo.write(dato)
            archivo.write(",NULL,NULL")
            valores = {"sensor_id":Id_sensor, "valor":int(dato)}
            self.guardarDatos(valores)

        #3 temperatura
        if Id_sensor == 3:
            archivo.write("NULL,NULL,") 
            archivo.write(str(dato))
            archivo.write(",NULL") 
            valores = {"sensor_id":Id_sensor, "valor":float(dato)}
            valores2 = {"sensor_id":Id_sensor, "valor":float(dato2)}
            self.guardarDatos(valores, valores2)

        #4 humedad
        if Id_sensor == 7:
            archivo.write("NULL,NULL,NULL") 
            archivo.write(str(dato))
            valores = {"sensor_id":Id_sensor, "valor":dato}
            self.guardarDatos(valores)


        archivo.write("\n")
        archivo.close()'''


    
#donde se guardaran los datos en las BD's
    def guardarDatos(self,valores, valores2 = None):
            sensorTipo=valores.get("sensor_id")
            dato=valores.get("valor")

            db = DatabaseSQLDB()
            today = date.today()
            ti = time.strftime("%H:%M:%S")
            fecha = str(today) + ' ' + str(ti)
            tabla = "historial"

            valores = {"sensor_id":sensorTipo, "valor":dato, "fecha_tiempo":fecha}
        
            db.insert(tabla, valores )
            db.select(tabla)

            if valores2:
                sensorTipo_2 = valores2.get("sensor_id")
                dato_2 = valores2.get("valor")
                today = date.today()
                ti = time.strftime("%H:%M:%S")
                fecha = str(today) + ' ' + str(ti)
                tabla = "historial"
                valores_2 = {"sensor_id":sensorTipo_2, "valor":dato_2, "fecha_tiempo":fecha}
        
                db.insert(tabla, valores_2)
                db.select(tabla)
