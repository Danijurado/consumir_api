from criptoexchange.models import *
from config import apikey

# creamos objetos
allcoin = AllcoinapiIO()
allcoin.getcoins(apikey)

print ('la cantidad de criptos son {}, \
    la cantidad de no criptos son {}'.format(len(allcoin.criptos),len(allcoin.no_criptos)))

crypto = input('ingrese moneda.').upper()

while crypto != '' and crypto.isalpha():
    if crypto in allcoin.criptos:
        exchange = Exchange(crypto)
        try:
            exchange.updateExchange(apikey)
            print('{:,.2f}€'.format(exchange.rate))
        
        except ModelError as error: 
            print(error)   
            
        
    crypto = input('ingrese moneda:').upper()
