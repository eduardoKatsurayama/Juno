from cyrodiil.api.interface import ApiRequester
from cyrodiil.utils.constants import DEFAULT_REGION, ENDPOINTS


class Match(ApiRequester):
    def __init__(self, region=DEFAULT_REGION):
        super().__init__(region, by_platform=False)
        self.endpoints = ENDPOINTS['MATCH-V5']

    def get_matches_ids_by_puuid(self, puuid):
        uri = self.endpoints[0]
        return self._request(uri, puuid=puuid)

    def get_matches_by_match_id(self, match_id):
        uri = self.endpoints[1]
        return self._request(uri, match_id=match_id)

    def get_matches_timeline_by_match_id(self, match_id):
        uri = self.endpoints[2]
        return self._request(uri, match_id=match_id)
