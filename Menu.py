from sensorpir import sensorPir
from sensorled import ledConf
from sensordistancia import SensorDistancia
from saveCSV import saveCSV
from sensorTemperatura import sensorTemperatura
from sensorHumedad import sensorHumedad
from DBmongo import DatabaseMongoDB
import os
import time
from datetime import date
from DBsql import DatabaseSQLDB

class Menus:
    def __init__(self):
        self.sensores = {
            "sensor_Distancia" : {
                1 : {
                    "Pin1":3,
                    "Pin2":4
                },
                4 : {
                    "Pin1":24,
                    "Pin2":25
                }
            },
            "sensor_Pir" : {
                2 : {
                    "Pin1":27
                }
            },
            "sensor_TempHum" : {
                3 : {
                    "Pin1":23                
                }
            },
            "sensor_Led" : {
                5 : {
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
        db = DatabaseSQLDB()
        
        tabla = "sensores_registrados"
        valores = {"nombre":nombre_sensor, "tipo_id":SensorTipo}
        db.insert(tabla, valores)
        db.select(tabla)


    def pirMetodo(self):
        for x in self.sensores["sensor_Pir"]:
            print(" ")
            pin1=self.sensores["sensor_Pir"][x]["Pin1"]
            
            #aqui se imprime los pines de los sensores
            print("Sensor Registrado: "+str(x))#este imprime el id del sensor
            #aqui se imprime los pines de los sensores
            print("Puerto#1: "+str(pin1))
            
            pinEntrada={"id_sensor":x,"pir":pin1}
            #pinEntrada={"led":self.led, "pir":self.pir}
            x=sensorPir(pinEntrada)
            x.leerMovimiento(pinEntrada)
            print("  ")
            print("  ")

    def ledMetodo(self):
        for x in self.sensores["sensor_Led"]:
            print(" ")
            print("Sensor Registrado: "+str(x))#este imprime el id del sensor
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

            print("Sensor Registrado: "+str(x))#este imprime el id del sensor
            #aqui se imprime los pines de los sensores
            print("Puerto#1: "+str(pin1))
            print("Puerto#2: "+str(pin2))

            pinEntrada={"id_sensor":x,"GPIO_TRIGGER":pin1, "GPIO_ECHO":pin2}

            distancia=SensorDistancia(pinEntrada)
            distancia.leerDistancia()

            print("  ")
            print("  ")

    def tempHumedadMetodo(self):
        for x in self.sensores["sensor_TempHum"]:
            print(" ")

            pin1=self.sensores["sensor_TempHum"][x]["Pin1"]
            pinEntrada={"Id_sensor":x,"TemperaturaHumedad":pin1}

            #aqui se imprime los pines de los sensores
            print("Sensor Registrado: "+str(x))#este imprime el id del sensor
            #aqui se imprime los pines de los sensores
            print("Puerto#1: "+str(pin1))

            tempSens=sensorTemperatura(pinEntrada)
            tempSens.temperatura()

            humeSens=sensorHumedad(pinEntrada)
            humeSens.humedad()
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
                            time.sleep(self.tiempo)
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
                            time.sleep(self.tiempo)
                    # Reset by pressing CTRL + C
                    except KeyboardInterrupt:
                        self.limpiar()
                        print("Proceso detenido por el usuario")
                        print(" ")
                if opc == "4":
                    try:
                        while True:
                            #self.limpiar()
                            self.tempHumedadMetodo()
                            time.sleep(self.tiempo)
                    # Reset by pressing CTRL + C
                    except KeyboardInterrupt:
                        self.limpiar()
                        print("Proceso detenido por el usuario")
                        print(" ")

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
