
from datetime import datetime
import flask
from flask import Flask
from flask import jsonify
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail()
mail.init_app(app) 
   
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'santiago.quintero@correounivalle.edu.co'
app.config['MAIL_PASSWORD'] = 'Zasertyq123456'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


#definimos la funcion que usaremos para el metodo de fibunnaci
@app.route('/', methods=['GET'])
def fibonnaci():
    #inicializamos la hora actual,sacamos los minutos y los segundos
    now = datetime.now()
    minute = now.strftime("%M")
    second = now.second
    print("/////////",minute)
    #separamos los digitos de los minutos para tener las 2 semillas
    list_num = [int(a) for a in str(minute)]

    semilla_one = list_num[0]
    semilla_two = list_num[1]

    for i in range(second):
        sum = semilla_one + semilla_two
        semilla_one = semilla_two
        semilla_two = sum
        list_num.append(sum)

    date_time = now.strftime("%H:%M:%S")
    env_mail(date_time,str(list_num))
    return jsonify(list_num), 200

#Funcion para el envio de correo
def env_mail(hora, result): 
   msg = Message( 
                'Confirmacion de aplicacion', 
                sender ='santiago.quintero@correounivalle.edu.co', 
                recipients = ['juan.gomezh@proteccion.com.co','chamogomez@gmail.com'] 
               ) 
   msg.body = "Se corrio a las " + hora + " y este fue el resultado " + result
   mail.send(msg) 

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

    

