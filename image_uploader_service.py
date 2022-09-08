#Se importan las liberías
import base64
from request_manager import RequestManager

#Clase para obtener la captura del directorio local y enviar captura
class ImageUploaderService:
    
    #Constructor
    def __init__(self, url):
        self.url = url
        self.request_manager = RequestManager()

    #Método para realizar post con la imagen al endpoint 
    def send_image(self, image, path):
        self.request_manager.post(self.url, image, path, 1)
        
    #método para obetener imagen del directorio local    
    def get_image(self, path):
        with open(path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode('utf-8')