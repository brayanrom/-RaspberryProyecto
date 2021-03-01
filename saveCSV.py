from sqldb import DatabaseMysql
from mongodb import DatabaseMongoDB
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




        dbMysql = DatabaseMysql()
        dbMongo = DatabaseMongoDB()

        tabla = "historial"
        valores = {"temperatura": dato3, "humedad":dato4, "pir":dato2, "distancia":dato1}


        dbMysql.insert(tabla, valores)
        dbMysql.select(tabla)

        dbMongo.insert(tabla, valores)
        dbMongo.select(tabla)





    def insertSensorIndividual(self,dato,sensorTipo=0):
        datoNulo="NULL" 

        archivo = open("sensores.csv", "a")
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




        dbMysql = DatabaseMysql()
        dbMongo = DatabaseMongoDB()

        tabla = "historial"


        dbMysql.insert(tabla, valores)
        dbMysql.select(tabla)

        dbMongo.insert(tabla, valores)
        dbMongo.select(tabla)