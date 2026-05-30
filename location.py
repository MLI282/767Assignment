# location.py

import geocoder


def get_current_location():

    g = geocoder.ip("me")

    lat, lng = g.latlng

    return lat, lng