from ..interface import ApiRequester
from juno.constants import DEFAULT_PLATFORM, ENDPOINTS


class Summoner(ApiRequester):
    def __init__(self, region=DEFAULT_PLATFORM):
        super().__init__(region)
        self.endpoints = ENDPOINTS['SUMMONER-V4']

    def get_summoners_by_encrypted_account_id(self, encrypted_account_id):
        uri = self.endpoints[0]
        return self._request(uri, encrypted_account_id=encrypted_account_id)

    def get_summoners_by_summoner_name(self, summoner_name):
        uri = self.endpoints[1]
        return self._request(uri, summoner_name=summoner_name)

    def get_summoners_by_encrypted_puuid(self, encrypted_puuid):
        uri = self.endpoints[2]
        return self._request(uri, encrypted_puuid=encrypted_puuid)

    def get_summoners_by_encrypted_summoner_id(self, encrypted_summoner_id):
        uri = self.endpoints[3]
        return self._request(uri, encrypted_summoner_id=encrypted_summoner_id)
