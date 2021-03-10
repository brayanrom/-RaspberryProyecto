from Pir import sensorPir
from led import ledConf
from senDistancia import SensorDistancia
from saveCSV import saveCSV
from sensorTemperaturaHumedad import sensorTemperatura
import os
import time

class Menus:
    def __init__(self):
        self.sensores = {
            "sensor_Distancia" : {
                "dist1" : {
                    "Pin1":3,
                    "Pin2":4
                }
            },
            "sensor_Pir" : {
                "pir1" : {
                    "Pin1":27
                }
            },
            "sensor_TempHum" : {
                "temhum1" : {
                    "Pin1":23                
                }
            },
            "sensor_Led" : {
                "led1" : {
                    "Pin1":2                
                }
            }
        }
#dist2  24 y 25
#led2 22
#pir2 8
        print("Seleccione su tiempo de espera")
        self.tiempo=int(input())
        self.limpiar()

        self.led=2
        self.pir=27
        self.temperatura=23
        self.GPIO_TRIGGER=3
        self.GPIO_ECHO=4

    def limpiar(self):
        if os.name=="nt":
            os.system("cls")
        else:
            os.system("clear")




#nuevo
    def agregarSensor(self):
        print("1.-Sensor de distancia: ")
        print("2.-Sensor pir: ")
        print("3.-Sensor de temperatura y humedad :")
        print("4.-Sensor Led :")
        SensorTipo =  int(input("Elige una opcion: "))

        if SensorTipo == 1:
            tipSen="sensor_Distancia"
            print("Para TRIGGER es Pin1, y Echo es Pin2")
        if SensorTipo == 2:
            tipSen="sensor_Pir"
        if SensorTipo == 3  :
            tipSen="sensor_TempHum"
        if SensorTipo == 4  :
            tipSen="sensor_Led"

        nombre_sensor=input("Ahora ingrese el nombre del sensor: ")

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
        self.sensores[tipSen].update(sentencia)
        print(self.sensores[tipSen])
        print("")
        print("")
        print("")



    def pirMetodo(self):
        for x in self.sensores["sensor_Pir"]:
            print(" ")
            pin1=self.sensores["sensor_Pir"][x]["Pin1"]
            
            #aqui se imprime los pines de los sensores
            print("Nombre del sensor: "+str(x))#este imprime el nombre del sensor
            #aqui se imprime los pines de los sensores
            print("Puerto#1: "+str(pin1))
            
            pinEntrada={"Nombre":x,"pir":pin1}
            #pinEntrada={"led":self.led, "pir":self.pir}
            x=sensorPir(pinEntrada)
            x.leerMovimiento(self.tiempo,pinEntrada)
            print("  ")
            print("  ")

    def ledMetodo(self):
        for x in self.sensores["sensor_Led"]:
            print(" ")
            print("Nombre del sensor: "+str(x))#este imprime el nombre del sensor
            #aqui se imprime los pines de los sensores
            pin1=self.sensores["sensor_Led"][x]["Pin1"]
            print("Puerto#1: "+str(pin1))
            pinEntrada={"Nombre":x,"led":pin1}
            print(" ")
            print("1.-Encender Led")
            print("2.-Apagar Led")
            print("3.-Led Loop")
            print("  ")
            print("  ")
            led = ledConf(pinEntrada)
            opc2 = input("-> ")
            if opc2 == "1":
                led.ledOn()
            if opc2 == "2":
                led.ledOff()
            if opc2 == "3":
                led.ledLoop()

    def distanciaMetodo(self):
        for x in self.sensores["sensor_Distancia"]:
            print(" ")
            #aqui se imprime los pines de los sensores
            pin1=self.sensores["sensor_Distancia"][x]["Pin1"]
            pin2=self.sensores["sensor_Distancia"][x]["Pin2"]

            #aqui se imprime los pines de los sensores
            print("Nombre del sensor: "+str(x))#este imprime el nombre del sensor
            #aqui se imprime los pines de los sensores
            print("Puerto#1: "+str(pin1))
            print("Puerto#2: "+str(pin2))

            pinEntrada={"Nombre":x,"GPIO_TRIGGER":pin1, "GPIO_ECHO":pin2}
            distancia=SensorDistancia(pinEntrada)
            distancia.leerDistancia(self.tiempo)
            print("  ")
            print("  ")
            self.limpiar()

    def tempHumedadMetodo(self):
        for x in self.sensores["sensor_TempHum"]:
            print(" ")
            pin1=self.sensores["sensor_TempHum"][x]["Pin1"]
            pinEntrada={"Nombre":x,"TemperaturaHumedad":pin1}

            #aqui se imprime los pines de los sensores
            print("Nombre del sensor: "+str(x))#este imprime el nombre del sensor
            #aqui se imprime los pines de los sensores
            print("Puerto#1: "+str(pin1))

            tempSens=sensorTemperatura(pinEntrada)
            tempSens.temperatura(self.tiempo)
            print("  ")
            print("  ")


    def menuPR(self):
        try:
            while True:
                print("0.- Resgistrar sensor")
                print("1.- Leer Distancia (Sensor ultrasonico)")
                print("2.- Enceder y Apagar Led's")
                print("3.- Detectar presencia con sensor PIR")
                print("4.- Temperatura y humedad")
                print("5.- Leer todos los sensores")
                print("10.- Configuracion")
                print("  ")
                print("  ")
                opc = input()
                if opc == "0":
                    self.limpiar()
                    self.agregarSensor()

                if opc == "1":
                    try:
                        while True:
                            self.limpiar()
                            self.distanciaMetodo()
                    # Reset by pressing CTRL + C
                    except KeyboardInterrupt:
                        self.limpiar()
                        print("Proceso detenido por el usuario")
                        print(" ")

                if opc == "2":
                    self.limpiar()
                    self.ledMetodo()

                if opc == "3":
                    try:
                        while True:
                            self.limpiar()
                            self.pirMetodo()
                    # Reset by pressing CTRL + C
                    except KeyboardInterrupt:
                        self.limpiar()
                        print("Proceso detenido por el usuario")
                        print(" ")
                if opc == "4":
                    try:
                        while True:
                            self.limpiar()
                            self.tempHumedadMetodo()
                    # Reset by pressing CTRL + C
                    except KeyboardInterrupt:
                        self.limpiar()
                        print("Proceso detenido por el usuario")
                        print(" ")
                if opc == "5":
                    try:
                        while True:

                            pinEntrada={"GPIO_TRIGGER":self.GPIO_TRIGGER, 
                            "GPIO_ECHO":self.GPIO_ECHO,
                            "led":self.led, 
                            "pir":self.pir,
                            "TemperaturaHumedad":self.temperatura}
                            

                            distancia=SensorDistancia(pinEntrada)
                            wardDist=distancia.distance()

                            pir=sensorPir(pinEntrada)
                            wardPir=pir.leerMov()

                            temp=sensorTemperatura(pinEntrada)
                            wardTemp,wardHumed=temp.sensorTemp()


                            x=saveCSV()
                            x.postPersona(str(wardDist),str(wardPir),str(wardTemp),str(wardHumed))


                            time.sleep(self.tiempo)
                            self.limpiar()

                    # Reset by pressing CTRL + C
                    except KeyboardInterrupt:
                        self.limpiar()
                        print("Proceso detenido por el usuario")
                        print("  ")
                        print("  ")


                if opc == "10":
                    self.limpiar()
                    print("1.-Modificar tiempo de subida de datos (Sensores)")
                    print("2.-Mostrar tiempo a guardar datos")
                    print("3.-")
                    print("  ")
                    print("  ")

                    opc3 = input()
                    if opc3 == "1":
                        print("Ingrese los segundos a guardar los datos")
                        self.tiempo=int(input())
                        print("  ")

                    if opc3 == "2":
                        print("El tiempo configurado a guardar datos es:")
                        print(str(self.tiempo) +" Segundos")
                        print("  ")
                        print("  ")

        except KeyboardInterrupt:
            self.limpiar()
            print("Proceso detenido por el usuario")
            print("Nos vemos :)")
