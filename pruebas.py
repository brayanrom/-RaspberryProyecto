class ledConf():
    def __init__(self,ledEntrada):
        self.led=ledEntrada
    
    def show(self):
        print(self.led)

if __name__ == "__main__":
    x=ledConf(5)
    x.show()
    