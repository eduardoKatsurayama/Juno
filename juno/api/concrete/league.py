from ..interface import ApiRequester
from juno.utils.constants import DEFAULT_PLATFORM, ENDPOINTS


class League(ApiRequester):
    def __init__(self, region=DEFAULT_PLATFORM):
        super().__init__(region)
        self.endpoints = ENDPOINTS['LEAGUE-V4']

    def get_challenger_leagues_by_queue(self, queue):
        uri = self.endpoints[0]
        return self._request(uri, queue=queue)

    def get_entries_by_encrypted_summoner_id(self, encrypted_summoner_id):
        uri = self.endpoints[1]
        return self._request(uri, encrypted_summoner_id=encrypted_summoner_id)

    def get_entries_by_queue_tier_division(self, queue, tier, division):
        uri = self.endpoints[2]
        return self._request(uri, queue=queue, tier=tier, division=division)

    def get_grandmaster_leagues_by_queue(self, queue):
        uri = self.endpoints[3]
        return self._request(uri, queue=queue)

    def get_leagues_by_league_id(self, queue):
        uri = self.endpoints[4]
        return self._request(uri, queue=queue)

    def get_master_leagues_by_queue(self, queue):
        uri = self.endpoints[5]
        return self._request(uri, queue=queue)
