from flask import Flask, render_template, request
from funciones import carga_csv

app = Flask(__name__)
#Metio toda la instrucción a chatgpt
@app.route('/')
def index():
    global cartelera
    return render_template('index.html')

@app.route('/generos')
def generos():
    return render_template('generos.html')

@app.route('/anio')
def anio():
    return render_template('anio.html')

@app.route('/alfabetico')
def alfabetico():
    return render_template('alfabetico.html')
@app.route('/pelicula')
def pelicula():
    return render_template('pelicula.html')