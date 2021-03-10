import os
class registro:
    
    def __init__(self):
        self.sensores = {
            "sensor_Distancia" : {
                "dist1" : {
                    "Pin1":3,
                    "Pin2":4
                }
            },
            "sensor_Pir" : {
                "pir1" : {
                    "Pin1":27
                }
            },
            "sensor_TempHum" : {
                "temhum1" : {
                    "Pin1":23                
                }
            },
            "sensor_Led" : {
                "led1" : {
                    "Pin1":2                
                }
            }
        }



    #imprimir nombres de sensores
    def getSensores(self,tipo_sensor):
        for x in self.sensores[tipo_sensor].keys():
            print(x)
            #   temhum1

    #imprimir pines
    def getPinesAll(self,tipo_sensor):
        for x in self.sensores[tipo_sensor]:
            for y in self.sensores[tipo_sensor][x]:
                print(self.sensores[tipo_sensor][x][y])
                #   3
                #   4

#imprime pines con su respectivo nombre de sensor
    def getPinesIndividual(self,tipo_sensor):
        for x in self.sensores[tipo_sensor]:
            print(" ")
            print(x)#este imprime el nombre del sensor
            #aqui se imprime los pines de los sensores
            if len(self.sensores[tipo_sensor][x]) == 1:
                pin1=self.sensores[tipo_sensor][x]["Pin1"]
                print(pin1)
                pinEntrada={"Nombre":x,"Pin1":pin1}
            if len(self.sensores[tipo_sensor][x]) == 2:
                pin1=self.sensores[tipo_sensor][x]["Pin1"]
                pin2=self.sensores[tipo_sensor][x]["Pin2"]
                print(pin1)
                print(pin2)
                pinEntrada={"Nombre":x,"Pin1":pin1, "Pin2":pin2}
            if len(self.sensores[tipo_sensor][x]) == 3:
                pin1=self.sensores[tipo_sensor][x]["Pin1"]
                pin2=self.sensores[tipo_sensor][x]["Pin2"]
                pin3=self.sensores[tipo_sensor][x]["Pin3"]
                print(pin1)
                print(pin2)
                print(pin3)
                pinEntrada={"Nombre":x,"Pin1":pin1, "Pin2":pin2, "Pin1":pin3}
            










    def menu(self):
        while True:
            print("Que desea hacer...")
            print(" ")
            print("1.- Agregar sensores")
            print("2.- Leer Sensores")

            opc=int(input("-> "))

            if opc==1:
                self.agregarSensor()
            if opc==2:
                print("ingrese el tipo de sensor que quiere leer")
                print("1.- distancia")
                print("2.- pir")
                print("3.- tempHum")
                valor=int(input("-> "))
                if valor==1:
                    tipo_sensor="sensor_Distancia"
                if valor==2:
                    tipo_sensor="sensor_Pir"
                if valor==3:
                    tipo_sensor="sensor_TempHum"

                print("1.- obtener sensores(solo nombre)")
                print("2.- obtener pines individual(pines y nombre)")
                print("3.- obtener pines all(solo pines)")

                hacer=int(input("Ingrese que desea hacer"))

                if hacer==1:
                    self.getSensores(tipo_sensor)
                if hacer==2:
                    self.getPinesIndividual(tipo_sensor)
                if hacer==3:
                    self.getPinesAll(tipo_sensor)
            












if __name__ == "__main__":
    x=registro()
    x.menu()
    print(" ")