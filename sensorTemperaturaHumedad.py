import RPi.GPIO as GPIO
from saveCSV import saveCSV
import dht11
import time
import datetime

class sensorTemperatura():
    def __init__(self,pinEntrada):
        self.tempHumedadEntrada=pinEntrada.get("TemperaturaHumedad")
        self.Nombre=pinEntrada.get("Nombre")

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
                resultHumed= round(result.humidity,2)

                print("Temperatura: " +str(resultTemp))
                print("Humedad: " +str(resultHumed))

                return resultTemp,resultHumed
            else:
                nVeces+=1
                if nVeces==10:
                    break
        return 0,0


    def temperatura(self,tiempo):
        resultTemp,resultHumed=self.sensorTemp()
        dato = {"resultTemp": resultTemp, "resultHumed":resultHumed}
        x=saveCSV()
        x.insertSensorIndividual(dato,3,self.Nombre)
        time.sleep(tiempo)