import RPi.GPIO as GPIO
import time
from saveCSV import saveCSV

#este sensor usa 5V
class sensorPir():
    def __init__(self,pinEntrada):        
        self.pir=pinEntrada.get("pir")
        self.id_sensor=pinEntrada.get("id_sensor")
        GPIO.setwarnings(False)
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pir, GPIO.IN)     


    def leerMov(self):
        deteccionPir=GPIO.input(self.pir)
        if deteccionPir==0:                
            print ("Movimiento No detectado")
        elif deteccionPir==1:               
            print ("Movimiento detectado")
        return deteccionPir


    def leerMovimiento(self,pinEntrada):
        mov=sensorPir(pinEntrada)
        wardPir=mov.leerMov()
        x=saveCSV()
        x.insertSensorIndividual(wardPir,2,self.id_sensor)