# Импорт данных запроса из модуля data
import data

# Импорт настроек из модуля configuration
import configuration 

# Импорт библиотеки requests для выполнения HTTP-запросов
import requests

# Функция для отправки POST-запроса на создание нового заказа
def create_order(order_body):  
    return requests.post(configuration.URL_SERVICE_PATH + configuration.CREATE_ORDER_PATH,
				json=order_body,
				headers=data.headers)

# Функция, которая отправляет GET-запрос к серверу для получения заказа по трек-номеру
def get_order_by_track(track_number): 
    return requests.get(configuration.URL_SERVICE_PATH + configuration.TRACK_ORDERS_PATH + str(track_number))