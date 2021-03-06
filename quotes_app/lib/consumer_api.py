#!/usr/bin/env python
import requests


def get_request(url):
    """Request method

    Method used to access the API.
    Return response
    """
    response = requests.get(url)
    return response


class ConsumerAPI:

    def __init__(self):
        self.url = 'https://1c22eh3aj8.execute-api.us-east-1.amazonaws.com/challenge/quotes'
        self.resp = None

    def get_quotes(self):
        self.resp = get_request(self.url).json()
        return self.resp

    def get_quote(self, number):
        quote_url = self.url + '/' + '{}' .format(number)
        self.resp = get_request(quote_url).json()
        return self.resp
