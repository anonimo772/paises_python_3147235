#Importar, o usar
#una dependencia en python
from flask import Flask, render_template


#crear la aplicacion
#de flask 
app = Flask(__name__)

#utilzar app
#para crear una ruta
@app.route('/prueba')
def prueba():
    #defino la lista de paises
    paises = [
      {
        "nombre": "Colombia",
        "moneda": "peso colombiano",
        "capital": "bogota",
        "idioma": "español",
        "poblacion": "52.32 millones",
        "superficie": "1.142 millones km²",
        "ciudades_principales": "bogota, medellin, cali"
      },
      {
          "nombre": "brasil",
          "capital": "brasailia",
          "idioma": "portuges",
          "poblacion": "211.1 millones",
          "superficie": "8.51 millones km²",
          "ciudades_principales": "brasilia, sao paulo, rio de janeiro"
      },
      {
          "nombre": "argentina",
          "capital": "buenos aires",
          "idioma": "español",
          "poblacion": "45.54 millones",
          "superficie": "2.78 millones km²",
          "ciudades_principales": "ciudad de san luis, recistencia, rosario"
      },
      {
          "nombre": "potugal",
          "capital": "lisboa",
          "idioma": "portuges",
          "poblacion": "10.58 millones ",
          "superficie": "92,152 km²",
          "ciudades_principales": "lisboa, cintra, aveiro"
      },
      {
          "nombre": "francia",
          "capital": "paris",
          "idioma": "frances",
          "poblacion": "68.29 millones ",
          "superficie": "551,695 km²",
          "ciudades_principales": "paris, lyon, niza"
      }
    ]
    return render_template('paises.html', paises=paises, Usuario="cristian")