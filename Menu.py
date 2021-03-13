from Pir import sensorPir
from led import ledConf
from senDistancia import SensorDistancia
from saveCSV import saveCSV
from sensorTemperaturaHumedad import sensorTemperatura
import os
import time
from registroSensores import registro as Reg

class Menus:

    def __init__(self):
        print("Seleccione su tiempo a guardar datos")
        self.tiempo=int(input())
        self.limpiar()


    def limpiar(self):
        if os.name=="nt":
            os.system("cls")
        else:
            os.system("clear")

    def menuPR(self):
        try:

            while True:
                print("0.- Resgistrar sensor")
                print("1.- Leer Distancia (Sensor ultrasonico)")
                print("2.- Enceder y Apagar Led")
                print("3.- Detectar presencia con sensor PIR")
                print("4.- Temperatura y humedad")
                print("5.- Leer todos los sensores")

                print("10.- Configuracion")
                print("  ")
                print("  ")

                opc = input()

                if opc == "0":
                    Reg.registro()

                if opc == "1":
                    distancia=SensorDistancia()
                    distancia.leerDistancia(self.tiempo)
                    print("  ")
                    print("  ")

                if opc == "2":
                    self.limpiar()
                    led = ledConf()
                    print("1.-Encender Led")
                    print("2.-Apagar Led")
                    print("3.-Led Loop")
                    print("  ")
                    print("  ")

                    opc2 = input()
                    if opc2 == "1":
                        led.ledOn()
                    if opc2 == "2":
                        led.ledOff()
                    if opc2 == "3":
                        led.ledLoop()


                if opc == "3":
                    x=sensorPir()
                    x.leerMovimiento(self.tiempo)
                    print("  ")
                    print("  ")

                if opc == "4":
                    tempSens=sensorTemperatura()
                    tempSens.temperatura(self.tiempo)
                    print("  ")
                    print("  ")



                if opc == "5":
                    try:
                        while True:
                            distancia=SensorDistancia()
                            wardDist=distancia.distance()

                            pir=sensorPir()
                            wardPir=pir.leerMov()

                            senTempHumed=sensorTemperatura()
                            wardTemp,wardHumed=senTempHumed.sensorTemp()

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
