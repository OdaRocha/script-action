import json
from consumer import Consumer
from access_control import AccessControl
from throttling import Throttling

def json_to_class(json_file):
    with open(json_file) as f:
        dadoJson = json.load(f)
        return dadoJson    
    
def map_to_consumer(file_path): 
    consumer_json = json_to_class(file_path)
    consumer_list_json = consumer_json['consumers']

    consumer_list = []
    for consumer in consumer_list_json:
        accress_control_list = []
        for access_control in consumer['controle_acesso']:
            throttling_list = []
            for throttling in access_control['throttling']:
                throttling_list.append(
                    Throttling(
                    method = throttling['method'],
                    tps = throttling['tps']
                    )
                )
            accress_control_list.append(
                AccessControl(
                    api_key = access_control['api_key'],
                    name = access_control['nome'],
                    throttling = throttling_list
                )
            )
        consumer_list.append(
            Consumer(
                path = consumer['path'], 
                access_control = accress_control_list
            )
        )
    
    return consumer_list