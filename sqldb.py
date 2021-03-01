import mysql.connector as mysql
class DatabaseMysql:
    def __init__(self):
        self.mydb = mysql.connect(
            host="localhost",
            user="root",
            password="1234",
            database="IoT"
            )
        print(self.mydb)
        self.mycursor = self.mydb.cursor()

    def all(self):
        self.mycursor.execute("SHOW DATABASES")
        for x in self.mycursor:
            print(x)
    
    def insert(self, tabla, valores):
        t = valores.get('temperatura')
        h = valores.get('humedad')
        p = valores.get('pir')
        d = valores.get('distancia')
        self.mycursor.execute('INSERT INTO %s (sensTemp, sensHumed, sensPir, sensDistancia) values ("%s", "%s", "%s", "%s")' % (tabla, t, h, p, d))
        self.mydb.commit()   
  
    def select(self, tabla):
        self.mycursor.execute('SELECT * FROM %s' % (tabla))
        myresult = self.mycursor.fetchall()
        for x in myresult:
            print(x)
        
    def delete(self, tabla, valores):
        for clave, x in valores.items():  
            columna = clave
        valor = valores.get(col)
        self.mycursor.execute('DELETE FROM %s where %s = "%s"' % (tabla, columna , valor))
        self.mydb.commit()     
        


# EJEMPLO DE INSERTAR
# db = Database()
# tabla = "historial"
# valores = {"temperatura": 20, "distancia":30}
# db.insert(tabla, valores )
# db.select(tabla)


# EJEMPLO DE ELIMINAR
# db = Database()
# tabla = "historial"
# valores = {"temperatura":20}
# db.delete(tabla, valores)
# db.select(tabla)  
