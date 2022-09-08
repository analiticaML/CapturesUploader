'''
Programa de envío de imagen a través de APIgateway a AWS.
Se recibe mensaje de software de detección de movimiento confirmando la captura de una imagen.
Al recibir el mensaje se realiza un post al endpoint del APIGateway que 
dispara función lambda en AWS.
'''

#Se importan librerías
import os
import asyncio
import concurrent.futures

from consumer import Consumer

#Función de inicialización
async def main():
    #Se crea objeto tipo Consumer
    consumer = Consumer(mq_host, mq_queue, url)
    #Loop para ejecutar el método consumer infinitamente
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, consumer.consume)


if __name__ == "__main__":
    #Se definen variables obteniendo valores de las variables de entorno del sistema
    mq_host = os.environ.get('MQ_HOST')
    mq_queue = os.environ.get('MQ_QUEUE')
    url = os.environ.get('ARGUS_UPLOAD_URL')
    captures_folder = os.environ.get('CAPTURES_FOLDER')

    asyncio.run(main())