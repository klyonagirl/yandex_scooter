import data
import configuration
import requests

def create_order(order_body):
    return requests.post(configuration.URL_SERVICE_PATH + configuration.CREATE_ORDER_PATH,
                         json=order_body,
                         headers=data.headers)
def get_order_by_track(track_number):
    return requests.get(configuration.URL_SERVICE_PATH + configuration.TRACK_ORDERS_PATH + str(track_number))