import RPi.GPIO as GPIO
from saveCSV import saveCSV
import dht11
import time
import datetime

class sensorTemperatura():
    def __init__(self):
        GPIO.cleanup()
        GPIO.setwarnings(True)
        GPIO.setmode(GPIO.BCM)

    def sensorTemp(self,individual=0):
        instance = dht11.DHT11(pin=23)

        result = instance.read()
        resultTemp= round(result.temperature,2)
        resultHumed= round(result.humidity,2)

        print("Temperatura: " +str(resultTemp))
        print("Humedad: " +str(resultHumed))
        
        if individual==1:
            dato = {"resultTemp": resultTemp, "resultHumed":resultHumed}

            x=saveCSV()
            x.insertSensorIndividual(dato,3)
            return 
        return resultTemp,resultHumed

    def temperatura(self,tiempo):
        individual=1
        try:
            while True:
                self.sensorTemp(individual)
                time.sleep(tiempo)

        except KeyboardInterrupt:
            print("Saliendo :)")
            GPIO.cleanup()