from sqldb import DatabaseSQLDB
from mongodb import DatabaseMongoDB
class saveCSV():
    def __init__(self):
        #cambiar este valor a True cuando se realicen pruebas
        #esto hara que no se envien datos a las BD's
        self.modoPrueba=True

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

        if self.modoPrueba==False:
            self.guardarDatos(valores)


    def insertSensorIndividual(self,dato,sensorTipo=0,nombreSensor="NULL"):
        datoNulo="NULL" 

        archivo = open("sensores.csv", "a")
        archivo.write(nombreSensor)

        
        
        #1 es distancia
        if sensorTipo==1:
            archivo.write(dato)
            archivo.write(", NULL,NULL, NULL")   
            valores = {"temperatura": datoNulo, "humedad":datoNulo, "pir":datoNulo, "distancia":dato}

        #2 es pir
        if sensorTipo==2:
            archivo.write("NULL,")
            archivo.write(dato)
            archivo.write(",NULL,NULL")
            valores = {"temperatura": datoNulo, "humedad":datoNulo, "pir":dato, "distancia":datoNulo}

        #3 es temperatura y humedad
        if sensorTipo==3:
            archivo.write("NULL,NULL,") 

            t = dato.get('resultTemp')
            h = dato.get('resultHumed')

        
            archivo.write(str(t))
            archivo.write(",")
            archivo.write(str(h))

            valores = {"temperatura": t, "humedad":h, "pir":datoNulo, "distancia":datoNulo}

        archivo.write("\n")
        archivo.close()


        if self.modoPrueba==False:
            self.guardarDatos(valores)





#donde se guardaran los datos en las BD's
    def guardarDatos(self,pinEntrada):
            dbMysql = DatabaseSQLDB()
            dbMongo = DatabaseMongoDB()
            tabla = "historial"

            dato3=pinEntrada.get("temperatura")
            dato4=pinEntrada.get("humedad")
            dato2=pinEntrada.get("pir")
            dato1=pinEntrada.get("distancia")

            valoresBD = {"temperatura": dato3, "humedad":dato4, "pir":dato2, "distancia":dato1}


            dbMysql.insert(tabla, valoresBD)
            dbMysql.select(tabla)

            dbMongo.insert(tabla, valoresBD)
            dbMongo.select(tabla)