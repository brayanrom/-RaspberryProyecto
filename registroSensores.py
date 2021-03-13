class registro:
    def registro():

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

        print(sensores)

   #
        SensorTipo = ("que tipo de sensor estas usando?")

        print("1.-Sensor de distancia: ")
        print("2.-Sensor pir: ")
        print("3.-Sensor de temperatura y humedad :")

        SensorTipo =  int(input("Elige una opcion: "))
        if SensorTipo == 1:

            nombre_sensor=input("Ingrese el nombre del sensor de distancia: ")
            puerto1=int(input("ingrese el puerto #1 "))
            puerto2=int(input("ingrese el puerto #2 "))

            sensores["sensor_Distancia"].update({nombre_sensor : {"Pin1":puerto1,"Pin2":puerto2}})

            print(sensores["sensor_Distancia"])
            print("todo")
            print(sensores)

        if SensorTipo == 2:
            
            nombre_sensor=input("Ingrese el nombre del sensor de distancia: ")
            puerto1=int(input("ingrese el puerto #1 "))
            puerto2=int(input("ingrese el puerto #2 "))
            sensores["sensor_Pir"].update({nombre_sensor : {"Pin1":puerto1,"Pin2":puerto2}})

        print(sensores["sensor_Pir"])
        print(sensores)

        if SensorTipo == 3  :
            #
            nombre_sensor=input("Ingrese el nombre del sensor de distancia: ")
            puerto1=int(input("ingrese el puerto #1 "))
            puerto2=int(input("ingrese el puerto #2 "))

        sensores["sensor_TempHum"].update({nombre_sensor : {"Pin1":puerto1,"Pin2":puerto2}})
        print(sensores["sensor_TempHum"])
        print(sensores)

