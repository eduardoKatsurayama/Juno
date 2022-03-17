from src.api.interface import ApiRequester
from src.utils.constants import ENDPOINTS

class Summoner(ApiRequester):
    def __init__(self, url):
        super().__init__(url, uri=ENDPOINTS['SUMMONER-V4'][1])
    
    def get_by_summoner_name(self, summoner_name):
        return self.request(summoner_name=summoner_name)
