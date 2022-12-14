import requests
from config import apikey

class ModelError():
    pass

class AllcoinapiIO:
    def __init__(self):
        self.criptos = []
        self.no_criptos = []
        
    def getcoins(self, apikey):
        r = requests.get(f'https://rest.coinapi.io/v1/assets/?apikey={apikey}')
        if r.status_code != 200:
            raise Exception('Error en consulta de assets:{}'.format(r.status_code))
        lista_general = r.json()


        for item in lista_general:
            if item["type_is_crypto"] == 1:
                self.criptos.append(item['asset_id'])
            else:
                self.no_criptos.append(item['asset_id'])
                
class Exchange:
    def __init__(self, cripto):
        self.cripto = cripto
        self.rate = None
        self.time = None
        
    def updateExchange(self,apikey):
            r = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{self.cripto}/EUR?apikey={apikey}')
            resultado = r.json()
            if r.status_code == 200:
                self.rate = resultado['rate']
                self.time = resultado['time']
            else:
                raise ModelError ('status:{}, Error:{}'.format(r.status_code, resultado['error']))
                