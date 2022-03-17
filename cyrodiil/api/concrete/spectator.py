from cyrodiil.api.interface import ApiRequester
from cyrodiil.utils.constants import ENDPOINTS, DEFAULT_PLATFORM

class Spectator(ApiRequester):
    def __init__(self, region=DEFAULT_PLATFORM):
        super().__init__(region)
        self.endpoints = ENDPOINTS['SPECTATOR-V4']

    def get_active_games_by_encrypted_summoner_id(self, encrypted_summoner_id):
        uri = self.endpoints[0]
        return self._request(uri, encrypted_summoner_id=encrypted_summoner_id)

    def get_featured_games(self):
        uri = self.endpoints[1]
        return self._request(uri)
