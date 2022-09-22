#Se importan librerías
import requests
import os
import json

#Clase para realizar post al endpoint
class RequestManager:

    #método para realizar post
    def post(self, url, bytes_image, path, timeout):
        body = {
            'account': os.environ.get('ACCOUNT'),
            'capture': bytes_image,
            'date': path.split('/')[5][:-4],
            'producer': os.environ.get('PRODUCER_NAME'),
            'secret': os.environ.get('PRODUCER_SECRET')
        }
        response = requests.post(url, data=json.dumps(body), timeout=timeout)
        print(' [x] Request respose', response.status_code)