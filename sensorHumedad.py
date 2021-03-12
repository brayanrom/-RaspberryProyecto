import RPi.GPIO as GPIO
from saveCSV import saveCSV
import dht11
import time
import datetime

class sensorHumedad():
    def __init__(self,pinEntrada):
        self.tempHumedadEntrada=pinEntrada.get("TemperaturaHumedad")
        self.Id_sensor=pinEntrada.get("Id_sensor")
        GPIO.setwarnings(False)
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)


    def sensorhumedad(self):
        instance = dht11.DHT11(self.tempHumedadEntrada)
        result = instance.read()
        while True:
            if result.is_valid():
                resultHumed= round(result.humidity,2)
                print("Humedad: " +str(resultHumed))

                return resultHumed
            else:
                print("Error en lectura")
                return 2


    def humedad(self):
        resultHumed=self.sensorhumedad()
        x=saveCSV()
        x.insertSensorIndividual(resultHumed,4,self.Id_sensor)

