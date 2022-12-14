import requests
from config import apikey

moneda_cripto = input('Ingrese una criptomoneda:').upper()

while moneda_cripto != '' and moneda_cripto.isalpha():

    r = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{moneda_cripto}/EUR?apikey={apikey}')

    #print(r.status_code)

    #print(r.text)

    #ejercicio 1 capturar resultado correcto
    #ejercicio 2 capturar error 
    #ejercicio 3 formatear el valor de rate en €
    #ejercicio 4 como controlo input vacio
    
    resultado = r.json()
    if r.status_code == 200:
        print('{:,.2f}€'.format(resultado['rate'])) 
     

    else:
        print(resultado['error'])  
    
    moneda_cripto = input('Ingrese una criptomoneda:').upper()




  