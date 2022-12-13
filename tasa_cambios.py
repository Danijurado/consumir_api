import requests

r = requests.get('https://rest.coinapi.io/v1/exchangerate/ETH/EUR?apikey=C47BA907-D782-4D42-9B19-3AEE81E069D1')

print(r.status_code)

print(r.text)