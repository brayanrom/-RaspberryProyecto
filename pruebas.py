sensores = {
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
                },
                "led2" : {
                    "Pin1":3,
                    "pin2":4                
                }
            }
        }

for x in sensores["sensor_Led"]:
    print(len(sensores["sensor_Led"][x]))
                #   3
                #   4