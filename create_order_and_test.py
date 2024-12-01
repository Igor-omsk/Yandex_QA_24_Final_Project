import requests
import configuration
import data

def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
           json=data.order_body)


def get_order_info(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_INFO,
           params={"t": track_number})

def get_track_number():
    track_number = post_new_order()
    return track_number.json()["track"]

def test_create_and_track_order():
    track_number = get_track_number()
    get_response = get_order_info(track_number)
    assert get_response.status_code == 200