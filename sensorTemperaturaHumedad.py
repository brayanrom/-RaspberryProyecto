import RPi.GPIO as GPIO
from saveCSV import saveCSV
import dht11
import time
import datetime

class sensorTemperatura():
    def __init__(self,pinEntrada):
        self.tempHumedadEntrada=pinEntrada.get("TemperaturaHumedad")
        self.Id_sensor=pinEntrada.get("Id_sensor")

        GPIO.cleanup()
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)


    def sensorTemp(self):
        instance = dht11.DHT11(self.tempHumedadEntrada)
        result = instance.read()
        nVeces=0
        while True:
            if result.is_valid():
                resultTemp= round(result.temperature,2)

                print("Temperatura: " +str(resultTemp))

                return resultTemp
            else:
                nVeces+=1
                if nVeces==10:
                    break
        return 0


    def sensorHumedad(self):
        instance = dht11.DHT11(self.tempHumedadEntrada)
        result = instance.read()
        nVeces=0
        while True:
            if result.is_valid():
                resultHumed= round(result.humidity,2)

                print("Humedad: " +str(resultHumed))

                return resultHumed
            else:
                nVeces+=1
                if nVeces==10:
                    break
        return 0

    def temperatura(self,tiempo):
        resultTemp=self.sensorTemp()
        resultHumed=self.sensorHumedad()

        x=saveCSV()
        x.insertSensorIndividual(resultTemp,8,self.Id_sensor)
        y=saveCSV()
        y.insertSensorIndividual(resultHumed,9,self.Id_sensor)

        time.sleep(tiempo)