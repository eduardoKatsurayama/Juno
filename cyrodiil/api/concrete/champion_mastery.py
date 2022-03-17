from cyrodiil.api.interface import ApiRequester
from cyrodiil.utils.constants import ENDPOINTS, DEFAULT_PLATFORM

class ChampionMastery(ApiRequester):
    def __init__(self, region=DEFAULT_PLATFORM):
        super().__init__(region)
        self.endpoints = ENDPOINTS['CHAMPION-MASTERY-V4']

    def get_champion_masteries_by_encrypted_summoner_id(self, encrypted_summoner_id):
        uri = self.endpoints[0]
        return self._request(uri, encrypted_summoner_id=encrypted_summoner_id)

    def get_champion_masteries_by_encrypted_summoner_id_champion_id(
        self, encrypted_summoner_id, champion_id
    ):
        uri = self.endpoints[1]
        return self._request(
            uri,
            encrypted_summoner_id=encrypted_summoner_id,
            champion_id=champion_id
        )

    def get_scores_by_encrypted_summoner_id(self, encrypted_summoner_id):
        uri = self.endpoints[2]
        return self._request(uri, encrypted_summoner_id=encrypted_summoner_id)
