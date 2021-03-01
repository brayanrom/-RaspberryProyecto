import RPi.GPIO as GPIO
import time
import os
from saveCSV import saveCSV

#este sensor usa 5V
class sensorPir():
    def __init__(self):
        GPIO.cleanup()


    def limpiar(self):
        if os.name=="nt":
            os.system("cls")
        else:
            os.system("clear")


    def leerMov(self):
        led=2
        pir=27
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pir, GPIO.IN)     
        GPIO.setup(led, GPIO.OUT)         
        i=GPIO.input(pir)
        if i==0:                 #When output from motion sensor is LOW
            print ("Movimiento No detectado")
            GPIO.output(led, 0)  #Turn OFF LED
        elif i==1:               #When output from motion sensor is HIGH
            print ("Movimiento detectado")
            GPIO.output(led, 1)  #Turn ON LED
        return i


    def leerMovimiento(self,tiempo):
        try:
            while True:
                mov=sensorPir()
                wardPir=mov.leerMov()

                x=saveCSV()
                x.insertSensorIndividual(str(wardPir),2)

                time.sleep(tiempo)

                # Reset by pressing CTRL + C
        except KeyboardInterrupt:
            self.limpiar()
            print("Proceso detenido por el usuario")
            GPIO.cleanup()