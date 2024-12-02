# Игорь Суханов, 24 когорта, Финальный проект. Инженер по тестированию плюс
import sender_stand_request

# не совсем понял зачем разделять функции по разным файлам, проект мизерный можно все в одном файле сделать.
# Но раз ревьюер хочет...
def test_create_and_track_order():
    track_number = sender_stand_request.get_track_number()
    get_response = sender_stand_request.get_order_info(track_number)
    assert get_response.status_code == 200