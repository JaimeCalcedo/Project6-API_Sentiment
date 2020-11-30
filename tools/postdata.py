from config.configuration import db,collection
#import tools.grupos_whatsapp as grpw

def insertamensaje(grupo, usuario, mensaje):
    """
    función que inserta los datos en la base de datos vacía
    Aqui debemos checkear que el mensaje no es repetido, que la persona
    que lo envía esta en el grupo, etc
    """

    dict_insert = {"group" : f"{grupo}",
    "user" : f"{usuario}",
    "message": f"{mensaje}"}

    #for items in dict_insert:
    #    if grupo == "españa_RMCF":
    #        if usuario in grpw.españa_RMCF:
    #            collection.insert_one(dict_insert)

    collection.insert_one(dict_insert)