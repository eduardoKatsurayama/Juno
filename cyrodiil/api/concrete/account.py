from cyrodiil.api.interface import ApiRequester
from cyrodiil.utils.constants import ENDPOINTS, DEFAULT_REGION

class Account(ApiRequester):
    def __init__(self, region=DEFAULT_REGION):
        super().__init__(region, by_platform=False)
        self.endpoints = ENDPOINTS['ACCOUNT-V1']

    def get_accounts_by_puuid(self, puuid):
        uri = self.endpoints[0]
        return self._request(uri, puuid=puuid)

    def get_accounts_by_game_name_tag_line(self, game_name, tag_line):
        uri = self.endpoints[1]
        return self._request(uri, game_name=game_name, tag_line=tag_line)

    def get_active_shards_by_game_puuid(self, game, puuid):
        uri = self.endpoints[3]
        return self._request(uri, game=game, puuid=puuid)
