from prometheus_client import start_http_server, Summary
import random
import time

# criando métrica para saber o tempo gasto e as requisições feitas
REQUEST_TIME = Summary('request_processing_seconds_sum', 'Time spent processing request summary seconds')


# colocando uma funão decorate com métrica
@REQUEST_TIME.time()
def process_request(t):
    #uma função ficticia que leva um tempo
    time.sleep(t)

if __name__ == '__main__':
    # colocando o servidor para rodar na porta 8000 expondo as métricas
    start_http_server(8000)
    # gerando algumas requisições
    while True:
        process_request(random.random())
