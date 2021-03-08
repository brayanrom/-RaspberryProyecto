class registro:
    def registroSensor(self):
        sensores = {
            "sensor_Distancia" : {
                "dist1" : {
                    "Pin1":23,
                    "Pin2":24
                },
                
                "dist2" : {
                    "Pin1":25,
                    "Pin2":26
                }
            },
            "sensor_Pir" : {
                "pir1" : {
                    "Pin1":27,
                    "Pin2":28
                },
                
                "pir2" : {
                    "Pin1":29,
                    "Pin2":30
                }
            },

            "sensor_TempHum" : {
                "temhum1" : {
                    "Pin1":31,
                    "Pin2":32
                },
                
                "temhum2" : {
                    "Pin1":33,
                    "Pin2":34
                }
            }
        }

        print("")
        print(sensores)
        print("")
        print("")

        print("1.-Sensor de distancia: ")
        print("2.-Sensor pir: ")
        print("3.-Sensor de temperatura y humedad :")
        
        SensorTipo =  int(input("Elige una opcion: "))

        if SensorTipo == 1:
            nombre_sensor=input("Ingrese el nombre del sensor de distancia: ")
            tipSen="sensor_Distancia"

        if SensorTipo == 2:
            nombre_sensor=input("Ingrese el nombre del sensor Pir: ")
            tipSen="sensor_Pir"

        if SensorTipo == 3  :
            nombre_sensor=input("Ingrese el nombre del sensor de Temperatura y Humedad: ")
            tipSen="sensor_TempHum"



        puertosNum = int(input("Cuantos puertos tiene? (Maximo 3) "))
        if puertosNum==1:
            puerto1=int(input("ingrese el puerto #1 "))
            puertos={"Pin1":puerto1}
        if puertosNum==2:
            puerto1=int(input("ingrese el puerto #1 "))
            puerto2=int(input("ingrese el puerto #2 "))
            puertos={"Pin1":puerto1,"Pin2":puerto2}
        if puertosNum==3:
            puerto1=int(input("ingrese el puerto #1 "))
            puerto2=int(input("ingrese el puerto #2 "))
            puerto3=int(input("ingrese el puerto #3 "))
            puertos={"Pin1":puerto1,"Pin2":puerto2,"Pin3":puerto3}


        sentencia={nombre_sensor : puertos}
        sensores[tipSen].update(sentencia)
        
        print("")
        print("")
        print(sensores[tipSen])
        print("")
        print("")
        print(sensores)

        
if __name__ == "__main__":
    x=registro()
    x.registroSensor()