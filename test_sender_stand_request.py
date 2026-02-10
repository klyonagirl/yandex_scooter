# Клёна Дик, 40-я когорта — Финальный проект. Инженер по тестированию плюс
import data
import create_order

def test_status_code_for_order_200():
    order_response = create_order.create_order(data.order_body)
    track = order_response.json()["track"]
    get_response = create_order.get_order_by_track(track)
    print(get_response)
    assert get_response.status_code == 200

test_status_code_for_order_200()