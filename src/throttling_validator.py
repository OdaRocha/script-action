import collections

from access_control import AccessControl
from consumer import Consumer
from throttling import Throttling

def validate_duplicate(consumerList):
    duplicate_list = [item for item, count in collections.Counter(consumerList.access_control).items() if count > 1]
    if len(duplicate_list) > 0 :
        print('duplicados', duplicate_list)
        raise Exception('file contains duplicate api-keys')


def teste():
    list = [
            Consumer(
                path ='path_1',
                access_control = [
                    AccessControl(
                        api_key = 'api_key_1',
                        name = 'name_1',
                        throttling=[
                            Throttling(method = 'get', tps = 100),
                            Throttling(method = 'post', tps = 100)
                            ]
                        )
                    ]
                ),
            Consumer(
                path ='path_1',
                access_control = [
                    AccessControl(
                        api_key = 'api_key_2',
                        name = 'name_2',
                        throttling=[
                            Throttling(method = 'get', tps = 100),
                            Throttling(method = 'post', tps = 100)
                            ]
                        )
                    ]
                )
            ]
    print(list)
    validate_duplicate(list)
