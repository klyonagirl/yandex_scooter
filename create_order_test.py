# Клёна Дик, 40-я когорта — Финальный проект. Инженер по тестированию плюс
import data
import sender_stand_request

def test_status_code_for_order_200():
    order_response = sender_stand_request.create_order(data.order_body)
    track = order_response.json()["track"]
    get_response = sender_stand_request.get_order_by_track(track)
    assert get_response.status_code == 200

test_status_code_for_order_200()