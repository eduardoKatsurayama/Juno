from __future__ import annotations
from abc import ABC, abstractmethod

import requests

from src.utils.constants import HEADERS


class ApiRequester(ABC):
    def __init__(self, url, uri):
        self.url = f'https://{url}'
        self.uri = uri

    def get_endpoint(self, kwargs):
        for key, value in kwargs.items():
            self.uri = self.uri.replace('{'+key+'}', value)

        return self.url + self.uri

    def request(self, **kwargs):
        endpoint = self.get_endpoint(kwargs)
        response = requests.get(endpoint, headers=HEADERS)
        
        return response.text
