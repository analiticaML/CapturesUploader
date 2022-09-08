#Se importan librerías
import pika
import json
from image_uploader_service import ImageUploaderService

#Clase encargada de la recpeción del mensaje de confirmación de envío
#del servicio de mensajería Rabbitmq 
class Consumer:
    
    #Constructor
    def __init__(self, mq_host, queue, url):
        self.mq_host = mq_host
        self.queue = queue
        self.image_uploader_service = ImageUploaderService(url)

    #Método con Json con imagen para enviar al APIgateway
    def callback(self, ch, method, properties, body):
        json_body = json.loads(body.decode('utf-8'))
        path = json_body.get('path')
        print(' [x] Loading image from', path)
        #Se obtiene la imagen del directorio local
        image = self.image_uploader_service.get_image(path)
        print(' [x] Send image')

        try:
            #Se envía la imagen al endpoint preestablecido
            self.image_uploader_service.send_image(image, path)
        except Exception as err:
            print(' [x] Exception sending image', err)
            pass
        
    #Método que recibe mensaje de confirmación y envía la imagen al endpoint
    def consume(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(self.mq_host))

        channel = connection.channel()

        channel.queue_declare(queue=self.queue)

        channel.basic_consume(queue=self.queue,
                        auto_ack=True,
                        on_message_callback=self.callback)

        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()