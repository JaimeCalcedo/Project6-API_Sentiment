# Creación de una API básica con Flask

La API tendrá un método POST para añadir los diferentes datos a la base de datos, y 
un método GET para extraer los datos deseados por el usuario de la base de datos. 

## ¿Cómo funciona?

### POST
Endpoint:
    - /nuevomensaje : con este endpoint, a través de un diccionario podemos añadir un mensaje, especificando el grupo de whatsapp, el usuario que lo envía y el contenido del mensaje.

### GET 
Endpoints:
    - /mensajes/<"usuario"> : con este endpoint podemos especificar un usuario, y nos devolverá todos los mensajes enviados por el. 

    - /usuarios : con este endppoint podemos obtener todos los miembros de los diferentes grupos de whatsapp.

    -/mensajes2/<grupo> : con este endpoint podemos especificar un grupo, y nos devolverá todos los mensajes enviados en ese grupo.  