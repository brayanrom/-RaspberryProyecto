import RPi.GPIO as GPIO
from saveCSV import saveCSV
import dht11
import time
import datetime

class sensorTemperatura():
    def __init__(self,pinEntrada):
        tempHumedadEntrada=pinEntrada.get("TemperaturaHumedad")
        GPIO.cleanup()
        GPIO.setwarnings(True)
        GPIO.setmode(GPIO.BCM)
        self.instance = dht11.DHT11(tempHumedadEntrada)


    def sensorTemp(self,individual=0):

        result = self.instance.read()

        nVerifica=1
        while nVerifica<10:
            if result.is_valid()
            resultTemp= round(result.temperature,2)
            resultHumed= round(result.humidity,2)
            break
        nVerifica+=1



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