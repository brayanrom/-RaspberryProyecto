import RPi.GPIO as GPIO
from saveCSV import saveCSV
import dht11
import time
import datetime

class sensorTemperatura():
    def __init__(self,pinEntrada):
        self.tempHumedadEntrada=pinEntrada.get("TemperaturaHumedad")
        self.Id_sensor=pinEntrada.get("Id_sensor")
        GPIO.setwarnings(False)
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)


    def sensorTemp(self):
        instance = dht11.DHT11(self.tempHumedadEntrada)
        result = instance.read()
        while True:
            if result.is_valid():
                resultTemp= round(result.temperature,2)
                print("Temperatura: " +str(resultTemp))

                return resultTemp
            else:
                print("Error en lectura")
                return 1


    def temperatura(self):
        resultTemp=self.sensorTemp()
        x=saveCSV()
        x.insertSensorIndividual(resultTemp,3,self.Id_sensor)
