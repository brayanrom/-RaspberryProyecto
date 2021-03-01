import RPi.GPIO as GPIO
from saveCSV import saveCSV
import dht11
import time
import datetime

class sensorTemperatura():
    def __init__(self):
        GPIO.cleanup()

    def sensorTemp(self,individual=0):
        GPIO.setwarnings(True)
        GPIO.setmode(GPIO.BCM)

        instance = dht11.DHT11(pin=23)

        result = instance.read()
        if result.is_valid():
            resultTemp= round(result.temperature,2)
            resultHumed= round(result.humidity,2)

            print("Temperatura: " +str(resultTemp))
            print("Humedad: " +str(resultHumed))
        
            retornarDatos = str(resultTemp)+","+str(resultHumed)
            
            if individual==1:
                x=saveCSV()
                x.insertSensorIndividual(retornarDatos,3)

            return (retornarDatos)



    def temperatura(self,tiempo):
        individual=1
        try:
            while True:
                self.sensorTemp(individual)
                time.sleep(tiempo)

        except KeyboardInterrupt:
            print("Saliendo :)")
            GPIO.cleanup()