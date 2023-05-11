import json
import hcl

from consumer_service import map_to_consumer
from throttling_validator import validate_duplicate



def tfvar_to_class(terraform_file):
    with open(terraform_file, 'r') as fp:
        obj = hcl.load(fp)
    return obj

def start():
    filePath = '../consumers.json'
    consumerList = map_to_consumer(filePath)
    validate_duplicate(consumerList[0])

start()
