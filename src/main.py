from consumer_service import map_to_consumer
from throttling_validator import validate_duplicate

def start():
    filePath = './consumers.json'
    consumerList = map_to_consumer(filePath)
    validate_duplicate(consumerList[0])

start()
