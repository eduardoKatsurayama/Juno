from cyrodiil.api.interface import ApiRequester
from cyrodiil.utils.constants import ENDPOINTS, DEFAULT_PLATFORM

class LolStatus(ApiRequester):
    def __init__(self, region=DEFAULT_PLATFORM):
        super().__init__(region)
        self.endpoints = ENDPOINTS['LOL-STATUS-V4']

    def get_platform_data(self):
        uri = self.endpoints[0]
        return self._request(uri)
