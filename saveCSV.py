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



    def insertSensorIndividual(self,dato,sensorTipo,Id_sensor):
        archivo = open("sensores.csv", "a")

        #imprime el tipo de sensor
        archivo.write(str(sensorTipo))
        archivo.write(",")

        
        
        # distancia
        if sensorTipo==6:
            archivo.write(dato)
            archivo.write(", NULL,NULL, NULL")   
            valores = {"sensor_id":Id_sensor, "valor":float(dato)}

        # pir
        if sensorTipo==7:
            archivo.write("NULL,")
            archivo.write(dato)
            archivo.write(",NULL,NULL")
            valores = {"sensor_id":Id_sensor, "valor":int(dato)}

        #3 temperatura
        if sensorTipo==8:
            archivo.write("NULL,NULL,") 
            archivo.write(str(dato))
            archivo.write(",NULL") 
            valores = {"sensor_id":Id_sensor, "valor":dato}

        #4 humedad
        if sensorTipo==9:
            archivo.write("NULL,NULL,NULL") 
            archivo.write(str(dato))
            valores = {"sensor_id":Id_sensor, "valor":dato}


        archivo.write("\n")
        archivo.close()


        self.guardarDatos(valores)





#donde se guardaran los datos en las BD's
    def guardarDatos(self,pinEntrada):
            sensorTipo=pinEntrada.get("sensor_id")
            dato=pinEntrada.get("valor")

            db = DatabaseSQLDB()
            today = date.today()
            ti = time.strftime("%H:%M:%S")
            fecha = str(today) + ' ' + str(ti)
            tabla = "historial"

            valores = {"sensor_id":sensorTipo, "valor":dato, "fecha_tiempo":fecha}

            db.insert(tabla, valores )
            db.select(tabla)