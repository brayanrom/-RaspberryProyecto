import RPi.GPIO as GPIO
from saveCSV import saveCSV
import time
import os

#este sensor usa 5V
class SensorDistancia():
    def __init__(self,pinEntrada):

        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)

        self.GPIO_TRIGGER=pinEntrada.get("GPIO_TRIGGER")
        self.GPIO_ECHO=pinEntrada.get("GPIO_ECHO")
        self.Nombre=pinEntrada.get("Nombre")

        GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(self.GPIO_ECHO, GPIO.IN)

    def distance(self):
        GPIO.output(self.GPIO_TRIGGER, True)
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(self.GPIO_TRIGGER, False)

        StartTime = time.time()
        StopTime = time.time()

        # save StartTime
        while GPIO.input(self.GPIO_ECHO) == 0:
            StartTime = time.time()

        # save time of arrival
        while GPIO.input(self.GPIO_ECHO) == 1:
            StopTime = time.time()

        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2

        ditsFinal= str(round(distance,2))
        print ("Distancia detectada = "+ditsFinal+ " cm")
        
        return ditsFinal


    def leerDistancia(self,tiempo):
        wardDist=self.distance()
        x=saveCSV()
        x.insertSensorIndividual(wardDist,6,self.Nombre)

        time.sleep(tiempo)
