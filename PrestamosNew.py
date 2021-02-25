import json
from os import system

class Articulo:
    ListaArticulos = []
    data = {}
    data['ListaPrestamos'] = []

    def __init__(self,matricula=None, articulo=None, cantidad=None):
        self.matricula      = matricula
        self.articulo       = articulo
        self.cantidad       = cantidad
        
    def limpiar():
        system("cls")

    def RegistroArticulo(self,matricula, articulo, cantidad):
        newArticulo = Articulo(matricula,articulo, cantidad)
        self.ListaArticulos.append(newArticulo)
        self.data['ListaPrestamos'].append(encoderArticulo(newArticulo))
        with open('Registro.json', 'w') as file:
            json.dump(self.data, file, indent=4)
        print('Registrado :)\n')
        return newArticulo

    def VerArticulos(self):
        return self.ListaArticulos

    def CargarArticulos(self):
        with open('Registro.json') as f:
            listillaJSON = json.load(f)
        for li in listillaJSON['ListaPrestamos']:
            newArticulo = Articulo(li['matricula'],li['articulo'],li['cantidad'])
            self.ListaArticulos.append(newArticulo)
            self.data['ListaPrestamos'].append(encoderArticulo(newArticulo))
        print('Datos cargados\n')
        return self.ListaArticulos

    def CargarArticulosReemplazado(self):  #reemplaza el jason por los diccionar
        with open('Registro.json', 'w') as file:
            json.dump(self.data, file, indent=4)
        print("Cargado....")
        Articulo.limpiar()

def encoderArticulo(articulo):
        if isinstance(articulo,Articulo):
            return {
            'matricula'  : articulo.matricula,
            'articulo'   : articulo.articulo,
            'cantidad' : articulo.cantidad
            }
        raise TypeError(f'El objeto {articulo} es incorrecto')