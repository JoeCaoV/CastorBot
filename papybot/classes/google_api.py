"""Requests module for Google Map Api and
Wikipedia module for Wiki Media API
"""
import json
import requests
import urllib

class GmApi():
    """Class for the differents Google Maps Api"""

    def __init__(self, key):
        """Setting the API key and the base URL for API requests"""
        self.url_static_map = "https://maps.googleapis.com/maps/api/staticmap"
        self.url_details = "https://maps.googleapis.com/maps/api/place/details/json"
        self.url_search = "https://maps.googleapis.com/maps/api/geocode/json"
        self.key = key

    def request_details(self, place_id):
        """Getting details of the specified place to get its address
        for Google Map Static requests and Photo Reference if there is
        for Google Map Photo requests
        """
        params = {"key" : self.key, "placeid" : place_id}
        api_get = requests.get(self.url_details, params=params).json()
        address = api_get['result']['formatted_address']
        routes = api_get['result']['address_components']
        for route in routes:
            if route['types'][0] == 'route':
                route_name = route['long_name']
                break
        return {'address' : address, 'route' : route_name}

    def request_map(self, center, zoom, size):
        """GET the Static Google Map Img from the API"""
        params = {"key"  : self.key, "center" : center, "zoom" : zoom,
                  "size" : size, "markers" : center}
        api_get = requests.get(self.url_static_map, params=params)
        return api_get

    def request_search(self, place):
        """Get the data of first place found according to the API result
        then return a dict containing 'place_id' for a Google_map details research
        and 'route' for Wiki Media Api requests
        """
        params = {"key" : self.key, "address" : place, "language" : 'fr',
                  "region" : "fr"}
        api_get = requests.get(self.url_search, params=params)
        if api_get.status_code == 200:
            return {'place_id' : api_get.json()['results'][0]['place_id']}
        return False
