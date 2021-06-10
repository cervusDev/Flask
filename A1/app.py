# Import padrão do flask
from flask import Flask
# Inicializador padrão do Flask
app = Flask(__name__)
#Criação da rota,   metodo de requisã via postman
@app.route("/<number>", methods = ['GET','POST'])
def Hellow(number):
    return 'Hellow Flask. {}'.format(number)

if __name__ == "__main__":
    app.run(debug = True)