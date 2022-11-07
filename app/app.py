#Importando  flask y algunos paquetes del mismo
from flask import Flask, render_template, request, redirect, url_for, jsonify
import random
import datetime
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
    totalPreguntas = len(dataPreguntas) #Total de preguntas
    mycursor.close() #cerrando conexion SQL
    conexion_MySQLdb.close() #cerrando conexion de la BD
    #Creando un diccionario de posibles respuestas
    arrayRespuestas = {
        'SI': 'SI',
        'NO': 'NO',
        'Tal_vez': 'T'        
    }
    codigo = (random.randrange(100, 1000))
    #print(codigo)
    return render_template('public/index.html', Preguntas = dataPreguntas, dataRespuesta = arrayRespuestas, dataTotalPreguntas = totalPreguntas, codigoBD = codigo)
   
  
@app.route('/guardar-encuesta', methods=['GET', 'POST'])
def  savedEncuesta():
    if request.method == 'POST':
        data         = request.form
        #print(data)
        
        observacion         = request.form['observacion']
        codigo              = request.form['codigo']
        created             = datetime.datetime.now()
        position = 0
        for  clave, valor in data.items():
           
            position = position + 1
            if(position <=10):
                #print(f'clave {position}, valor {valor}')

                conexion_MySQLdb = connectionBD()
                mycursor = conexion_MySQLdb.cursor(dictionary=True)
                
                sql = "INSERT INTO respuestas_encuesta (id_pregunta, respuesta, codigo, observacion, created) VALUES (%s, %s, %s, %s, %s)"
                val = (position, valor, codigo, observacion, created)
                mycursor.execute(sql, val)
                conexion_MySQLdb.commit()
                resultadoInsert = mycursor.rowcount #si la operacion fue un exito devuelve 1
                
                mycursor.close() #Cerrando conexion SQL
                conexion_MySQLdb.close() #cerrando conexion de la BD
                
                #print(mycursor.rowcount, "registro insertado correctamente")
                #print("Id ultimo registro insertado: ", mycursor.lastrowid) #Inserte una fila y devuelva el ID
                 
        return jsonify(res=["respuesta", resultadoInsert])
        
    return render_template('public/index.html')
    

#Informacion de encuesta por codigo
@app.route('/<codigo>', methods=['GET','POST'])
def encuesta(codigo):
    print(codigo)
    
    conexion_MySQLdb = connectionBD() #Hago instancia a mi conexión desde la función
    mycursor         = conexion_MySQLdb.cursor(dictionary=True)
    mycursor.execute("SELECT p.id, p.pregunta, r.respuesta,r.codigo, r.observacion, r.created FROM preguntas as p INNER JOIN respuestas_encuesta AS r ON  p.id = r.id_pregunta AND p.estatus='1' AND r.codigo='%s'" % (codigo,))
    inforEncuesta = mycursor.fetchall() 
    conexion_MySQLdb.close() #cerrando conexion de la BD
    
    return render_template('public/listaEncuesta.html', data = inforEncuesta)
    
       
       
#Redireccionando cuando la página no existe
@app.errorhandler(404)
def not_found(error):
        return redirect(url_for('inicio'))
    


if __name__ == "__main__":
    app.run(debug=True, port=8005)

