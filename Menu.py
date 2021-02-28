from led import ledConf
from sensorDistancia import SensorDistancia
from Pir import sensorPir
import os

class Menus:
    def __init__(self):
        print("Seleccione su tiempo a guardar datos")
        self.tiempo=int(input())


    def limpiar(self):
        if os.name=="nt":
            os.system("cls")
        else:
            os.system("clear")

    def menuPR(self):
        while True:
            print("1.- Leer Distancia (Sensor ultrasonico)")
            print("2.- Enceder y Apagar Led")
            print("3.- Detectar presencia con sensor PIR")
            print("4.- Temperatura y humedad")
            print("5.- Configuracion")
            print("  ")
            print("  ")

            opc = input()

            if opc == "1":
                distancia=SensorDistancia()
                distancia.leerDistancia(self.tiempo)

            if opc == "2":
                self.limpiar()
                led = ledConf()
                print("1.-Encender Led")
                print("2.-Apagar Led")
                print("3.-Led Loop")
                print("  ")
                print("  ")

                opc2 = input()
                if opc2 == "1":
                    led.ledOn()
                if opc2 == "2":
                    led.ledOff()
                if opc2 == "3":
                    led.ledLoop()

            if opc == "3":
                x=sensorPir()
                x.leerMovimiento(self.tiempo)
                print("  ")
                print("  ")

            if opc == "5":
                self.limpiar()
                print("1.-Modificar tiempo de subida de datos (Sensores)")
                print("2.-Mostrar tiempo a guardar datos")
                print("3.-")
                print("  ")
                print("  ")

                opc3 = input()
                if opc3 == "1":
                    print("Ingrese los segundos a guardar los datos")
                    self.tiempo=int(input())
                    print("  ")

                if opc3 == "2":
                    print("El tiempo configurado a guardar datos es:")
                    print(str(self.tiempo) +" Segundos")
                    print("  ")
                    print("  ")

    def RegistrarArticulo(self,matricula,articulo,cantidad):
        tmp=Articulo()
        tmp.RegistroArticulo(matricula,articulo,cantidad)

        x=int(self.dbActual)
        if x==1:
            MysqlDatabase.insertarDatos(matricula,articulo,cantidad)
        elif x==2:
            MongoDatabase.insertarDatos(matricula,articulo,cantidad)