from src.utils.constants import PLATFORM
from src.api.concrete.summoner import Summoner

summoner_name='Panka'

url = PLATFORM["BR1"]
summoner = Summoner(url)
response = summoner.get_by_summoner_name(summoner_name=summoner_name)
print(response)
