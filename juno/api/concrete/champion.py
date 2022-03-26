from juno.api.interface import ApiRequester
from juno.utils.constants import DEFAULT_PLATFORM, ENDPOINTS


class Champion(ApiRequester):
    def __init__(self, region=DEFAULT_PLATFORM):
        super().__init__(region)
        self.endpoints = ENDPOINTS['CHAMPION-V3']

    def get_champion_rotations(self):
        uri = self.endpoints[0]
        return self._request(uri)
