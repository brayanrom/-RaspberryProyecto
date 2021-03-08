import RPi.GPIO as GPIO
import time
import os

class ledConf():
    def __init__(self,pinEntrada):
        self.led=pinEntrada.get("led")
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.led,GPIO.OUT)     #Configura el Pin 26 como salida
    
    def limpiar(self):
        if os.name=="nt":
            os.system("cls")
        else:
            os.system("clear")

    def ledOn(self):
        GPIO.output(self.led,1)   #Salida digital de 5V
        time.sleep(1)      #Delay en segundos
        print("Led encendido")
    def ledOff(self):
            GPIO.output(self.led,0)   #Apaga el led
            time.sleep(1)      #Delay en segundos
            print("Led apagado")
    def ledLoop(self):
        try:
            while True:
                GPIO.output(self.led,1)   #Salida digital de 5V
                time.sleep(1)      #Delay en segundos
                GPIO.output(self.led,0)   #Apaga el led
                time.sleep(1)      #Delay en segundos
        except KeyboardInterrupt:
            self.limpiar()
            print("Proceso detenido por el usuario")
            GPIO.cleanup()