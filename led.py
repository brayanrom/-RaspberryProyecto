import RPi.GPIO as GPIO
import time

class ledConf():
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(3,GPIO.OUT)     #Configura el Pin 3 como salida

    def ledOn():
        GPIO.output(3,1)   #Salida digital de 5V

    def ledOf():
        GPIO.output(3,0)   #Apaga el led

    def ledLoop():
        while True:
        GPIO.output(3,1)   #Salida digital de 5V
        time.sleep(1)      #Delay en segundos
        GPIO.output(3,0)   #Apaga el led
        time.sleep(1)      #Delay en segundos

