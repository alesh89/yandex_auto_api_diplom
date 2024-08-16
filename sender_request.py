import configuration
import requests
import data

def post_new_order(body):
    response_order=requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=body)
    track_number = response_order.json()['track']
    return track_number


def get_order(track_number):    
    return requests.get(configuration.URL_SERVICE + configuration.TRACK_STATUS , params={"t":track_number})