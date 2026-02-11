# Импорт данных запроса из модуля data
import data

# Импорт функций для создания заказа и получения заказа по трек-номеру
import sender_stand_request

# Проверка, что код ответа равен 200
def test_status_code_for_order_200():
    order_response = sender_stand_request.create_order(data.order_body)
    track = order_response.json()["track"]
    get_response = sender_stand_request.get_order_by_track(track)
    assert get_response.status_code == 200

test_status_code_for_order_200()