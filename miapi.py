from flask import Flask, request
import markdown.extensions.fenced_code
import tools.postdata as pos
import tools.getdata as get
import json



app = Flask(__name__) #Para cuando más tarde iniciaremos la aplicación.


#PARA EL README
@app.route("/")
def index():
    readme_file = open("README.MD", "r")
    md_template_string = markdown.markdown(readme_file.read(), extensions = ["fenced_code"])
    return md_template_string

#ENDPOINT DE POST
@app.route("/nuevomensaje", methods = ["POST"]) #Esto es algo propio de flask, que es un decorador que ya está hecho, le estamos indicando como va a ser el formato de la ruta para ejecutar los endpoints.
def inserta_mensaje():
    grupo = request.form.get("group")
    usuario = request.form.get("user")
    mensaje = request.form.get("message")
    pos.insertamensaje(grupo, usuario, mensaje)
    return "Mensaje introducido en base de datos"

#ENDPOINTS DE GET
@app.route("/mensajes/<usuario>")
def usuario_mensajes(usuario):
    mensajes = get.mensajesusuario(usuario)
    return json.dumps(mensajes)

@app.route("/usuarios")
def usuarios_whatsapp():
    usuarios = get.diferentesusuarios()
    return json.dumps(usuarios)

@app.route("/mensajes2/<grupo>")
def grupo_mensajes(grupo):
    mensajes2 = get.mensajesgrupo(grupo)
    return json.dumps(mensajes2)

#ENDPOINT DE LA SENSIBILITY






















app.run(debug = True)
#Ella sola cuando hacemos cambios en el código la app se runea sola, pero cuando este acabada esto lo cambiaremos a False.
#Mientras desarrollas True, cuando la vamos a deployerar la ponemos en False



