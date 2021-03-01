class saveCSV():

    def postPersona(self,dato1="NULL",dato2="NULL",dato3="NULL"):

        archivo = open("sensores.csv", "a")

        archivo.write(dato1)
        archivo.write(",")   

        archivo.write(dato2)
        archivo.write(",")  
        
        if str(dato3)=="None":
            archivo.write("NULL,NULL") 
        else:
            archivo.write(str(dato3))


        archivo.write("\n")
        archivo.close()

    def insertSensorIndividual(self,dato,sensorTipo=0):

        archivo = open("sensores.csv", "a")
        #1 es distancia

        if sensorTipo==1:
            archivo.write(dato)
            archivo.write(", NULL,NULL, NULL")    

        #2 es pir
        if sensorTipo==2:
            archivo.write("NULL,")
            archivo.write(dato)
            archivo.write(",NULL,NULL")
            
        #3 es temperatura y humedad
        if sensorTipo==3:
            archivo.write("NULL,NULL,") 
            archivo.write(str(dato))

        archivo.write("\n")
        archivo.close()
