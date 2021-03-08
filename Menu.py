from Pir import sensorPir
from led import ledConf
from senDistancia import SensorDistancia
from saveCSV import saveCSV
from sensorTemperaturaHumedad import sensorTemperatura
import os
import time

class Menus:
    def __init__(self):
        print("Seleccione su tiempo a guardar datos")
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

                if opc == "1":
                    pinEntrada={"GPIO_TRIGGER":self.GPIO_TRIGGER, "GPIO_ECHO":self.GPIO_ECHO}
                    distancia=SensorDistancia(pinEntrada)
                    distancia.leerDistancia(self.tiempo,pinEntrada)
                    print("  ")
                    print("  ")


                if opc == "2":
                    self.limpiar()
                    pinEntrada={"led":self.led}
                    led = ledConf(pinEntrada)
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
                    pinEntrada={"led":self.led, "pir":self.pir}

                    x=sensorPir(pinEntrada)
                    x.leerMovimiento(self.tiempo,pinEntrada)
                    print("  ")
                    print("  ")

                if opc == "4":
                    pinEntrada={"TemperaturaHumedad":self.temperatura}
                    
                    tempSens=sensorTemperatura(pinEntrada)
                    tempSens.temperatura(self.tiempo,pinEntrada)
                    print("  ")
                    print("  ")



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
