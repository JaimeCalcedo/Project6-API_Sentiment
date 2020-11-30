from config.configuration import db, collection 
from textblob import TextBlob

def mensajesusuario(usuario):
    "Función para obtener los mensajes de un usuario"
    query = {"user": {"$eq": f"{usuario}"}}
    mensajitos = list(collection.find(query, {"group": 1, "message": 1, "user": 1}))
    return mensajitos

def diferentesusuarios():
    "Función para obtener los diferentes usuarios"
    jugadores = list(collection.distinct("user"))
    return jugadores

def mensajesgrupo(grupo):
    "Función para obtener los mensajes de un grupo"
    query = {"group": {"$eq": f"{grupo}"}}
    contenido = list(collection.find(query, {"user": 1, "message": 1, "_id": 0}))
    return contenido

#Funciones para obtener la polaridad y la subjetividad de un texto
#SIN TERMINAR
def polarity(text):
    en_blob = TextBlob(u"{}".format(text))
    translated = en_blob.translate(to="en")
    return translated.sentiment[0]

def subjetivity(text):
    en_blob = TextBlob(u"{}".format(text))
    translated = en_blob.translate(to="en")
    return translated.sentiment[1]

def analisisdesensibilidad():
    "Función para obtener un análisis de sensibilidad de todos los users"
    mensajes4 = list(collection.find({}, {"user": 1, "message": 1, "_id": 0}))
