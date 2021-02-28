import RPi.GPIO as GPIO
import time
import os

#este sensor usa 5V
class SensorDistancia():
    def limpiar(self):
        if os.name=="nt":
            os.system("cls")
        else:
            os.system("clear")

    def __init__(self):
        GPIO.cleanup()
        self.limpiar()
        GPIO.setmode(GPIO.BCM)
        GPIO_TRIGGER = 3
        GPIO_ECHO = 4
        GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(GPIO_ECHO, GPIO.IN)

    def distance(self,tiempo):
        self.limpiar()
        GPIO.output(GPIO_TRIGGER, True)
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)

        StartTime = time.time()
        StopTime = time.time()

        # save StartTime
        while GPIO.input(GPIO_ECHO) == 0:
            StartTime = time.time()

        # save time of arrival
        while GPIO.input(GPIO_ECHO) == 1:
            StopTime = time.time()

        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2

        dist =  distance
        print ("Distancia detectada = %.1f cm" % dist)
        time.sleep(tiempo)

    def leerDistancia(self,tiempo):
        try:
            while True:
                x=SensorDistancia()
                x.distance(tiempo)
        # Reset by pressing CTRL + C
        except KeyboardInterrupt:
            self.limpiar()
            print("Proceso detenido por el usuario")
            GPIO.cleanup()