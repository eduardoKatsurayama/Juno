from cyrodiil.api.interface import ApiRequester
from cyrodiil.utils.constants import ENDPOINTS, DEFAULT_PLATFORM

class Champion(ApiRequester):
    def __init__(self, region=DEFAULT_PLATFORM):
        super().__init__(region)
        self.endpoints = ENDPOINTS['CHAMPION-V3']

    def get_champion_rotations(self):
        uri = self.endpoints[0]
        return self._request(uri)
