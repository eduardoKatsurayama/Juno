from cyrodiil.api.interface import ApiRequester
from cyrodiil.utils.constants import ENDPOINTS, DEFAULT_PLATFORM

class LeagueExp(ApiRequester):
    def __init__(self, region=DEFAULT_PLATFORM):
        super().__init__(region)
        self.endpoints = ENDPOINTS['LEAGUE-EXP-V4']

    def get_entries_by_queue_tier_division(self, queue, tier, division):
        uri = self.endpoints[0]
        return self._request(uri, queue=queue, tier=tier, division=division)
