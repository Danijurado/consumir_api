from criptoexchange.models import AllcoinapiIO, Exchange, ModelError
from config import apikey
#16156 de 16378 (222)

def test_todocoin():
    todo = AllcoinapiIO()
    assert isinstance(todo, AllcoinapiIO)
    todo.getcoins(apikey)
    assert len(todo.criptos) == 16156
    assert len(todo.no_criptos) == 222
    
    
def test_cambio_ok():
    cambio = Exchange ('ETC')
    assert cambio.rate is None
    assert cambio.time is None
    cambio.updateExchange(apikey)
    assert cambio.rate > 0
    assert isinstance(cambio.time, str)
    
    
def test_cambio_fail():
    fail = Exchange('NADA')
    respuesta = fail.updateExchange(apikey)
    
    
    