#Importando  flask y algunos paquetes del mismo
from flask import Flask, render_template, request, redirect, url_for, jsonify
from confiDB import *  #Importando conexión BD


#Declarando el nombre de la aplicación e inicializando - crear la aplicación Flask
app = Flask(__name__)
application = app


#Creando mi Decorador para el Home 
@app.route('/', methods=['GET','POST'])
def inicio():
    conexion_MySQLdb = connectionBD() #Hago instancia a mi conexión desde la función
    mycursor         = conexion_MySQLdb.cursor(dictionary=True)
    querySQL  = ("SELECT * FROM preguntas ORDER BY id ASC")
    mycursor.execute(querySQL)
    dataPreguntas = mycursor.fetchall() #fetchall () Obtener todos los registros
    mycursor.close() #cerrando conexion SQL
    conexion_MySQLdb.close() #cerrando conexion de la BD
    return render_template('public/index.html', Preguntas = dataPreguntas)
   
   
#Redireccionando cuando la página no existe
@app.errorhandler(404)
def not_found(error):
        return redirect(url_for('inicio'))
    


if __name__ == "__main__":
    app.run(debug=True, port=8000)

