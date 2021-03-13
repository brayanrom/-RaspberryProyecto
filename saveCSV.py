from DBsql import DatabaseSQLDB
from DBmongo import DatabaseMongoDB
import time
from datetime import date

class saveCSV():        
        #insercion de los datos en bucle
    def postPersona(self,dato1="NULL",dato2="NULL",dato3="NULL",dato4="NULL"):

        #archivo = open("sensores.csv", "a")

       ''' archivo.write(dato1)
        archivo.write(",")   

        archivo.write(dato2)
        archivo.write(",")  

        archivo.write(dato3)
        archivo.write(",")  

        archivo.write(dato4)

        archivo.write("\n")
        archivo.close()

        valores = {"temperatura": dato3, "humedad":dato4, "pir":dato2, "distancia":dato1}
'''


    def insertSensorIndividual(self,dato,sensor_tipo,id_sensor):

        #se configura la fecha para despues enviarla
        today = date.today()
        ti = time.strftime("%H:%M:%S")
        fecha = str(today) + ' ' + str(ti)
            

        #imprime la id del sensor
        archivo = open("sensores.csv", "a")
        archivo.write(str(id_sensor))
        archivo.write(",")

        #1 distancia
        if sensor_tipo==1:
            archivo.write(str(dato))
            archivo.write(", NULL, NULL, NULL") 
            valores = {"sensor_id":id_sensor, "distancia":dato, "fecha_tiempo":fecha}

        #2 pir
        if sensor_tipo==2:
            archivo.write("NULL, ")
            archivo.write(str(dato))
            archivo.write(", NULL, NULL")
            valores = {"sensor_id":id_sensor, "pir":dato, "fecha_tiempo":fecha}

        #3 temperatura
        if sensor_tipo==3:
            archivo.write("NULL, NULL, ") 
            archivo.write(str(dato))
            archivo.write(", NULL") 
            valores = {"sensor_id":id_sensor, "temperatura":dato, "fecha_tiempo":fecha}

        #4 humedad
        if sensor_tipo == 4:
            archivo.write("NULL, NULL, NULL, ") 
            archivo.write(str(dato))
            valores = {"sensor_id":id_sensor, "humedad":dato, "fecha_tiempo":fecha}

        self.guardarDatos(valores)
        archivo.write("\n")
        archivo.close()


#donde se guardaran los datos en las BD's
    def guardarDatos(self,valores):
            db = DatabaseSQLDB()

            tabla = "historial"

            db.insert(tabla, valores )

