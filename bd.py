import mysql.connector
import pymongo

class MysqlDatabase():
    def crearBD(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
        )
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS iot")

    def crearTabla(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  
        database="iot"
        )
        mycursor = mydb.cursor()
        mycursor.execute("CREATE TABLE IF NOT EXISTS historial (matricula INT , articulo VARCHAR(100) , cantidad INT)")

    def insertarDatos(matricula,articulo,cantidad): #solo para pruebas
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  
        database="iot"
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO historial (matricula, articulo, cantidad) VALUES (%s, %s, %s)"
        val = (matricula,articulo,cantidad)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "datos insertado.")
        print("")
        print("")

    def insertarDatosPrueba(): #solo para pruebas
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  
        database="iot"
        )
        print("Insercion de datos:")
        x=int(input("Matricula->"))
        y=input("Articulo->")
        z=int(input("Cantidad->"))
        mycursor = mydb.cursor()
        sql = "INSERT INTO historial (matricula, articulo, cantidad) VALUES (%s, %s, %s)"
        val = (x,y,z)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "datos insertado.")
        print("")
        print("")


class MongoDatabase():
    def crearBD(self):
        True
    def crearTabla(self):
        print("Se supone que realizo todo")

    def insertarDatos(matricula,articulo,cantidad): 
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["mydatabase"]
        mycol = mydb["historial"]
        mydict = { "matricula": matricula, "articulo": articulo, "cantidad":cantidad}
        x = mycol.insert_one(mydict)

    def insertarDatosPrueba(self): 
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["mydatabase"]
        mycol = mydb["historial"]
        print("Insercion de datos:")
        Matricula=int(input("Matricula->"))
        Articulo=input("Articulo->")
        Cantidad=int(input("Cantidad->"))
        mydict = { "Matricula": Matricula, "Articulo": Articulo, "Cantidad":Cantidad}
        x = mycol.insert_one(mydict)
