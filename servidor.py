from flask import Flask, render_template

servidorWeb = Flask(__name__)


@servidorWeb.route("/holamundo",methods=['GET'])
def formulario():
    return render_template('pagina1.html')

if __name__ == '__main__':
    servidorWeb.run(debug=False,host='0.0.0.0',port='8080')

