import os

from cyrodiil.api.concrete.account import Account
from cyrodiil.api.concrete.champion_mastery import ChampionMastery
from cyrodiil.api.concrete.champion import Champion
from cyrodiil.api.concrete.league_exp import LeagueExp
from cyrodiil.api.concrete.league import League
from cyrodiil.api.concrete.lol_status import LolStatus
from cyrodiil.api.concrete.match import Match
from cyrodiil.api.concrete.spectator import Spectator
from cyrodiil.api.concrete.summoner import Summoner


def authenticate(riot_token):
    os.environ['HEADERS'] = f'''
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
        'Accept-Language': 'en-AU,en;q=0.9,pt-BR;q=0.8,pt;q=0.7,en-GB;q=0.6,en-US;q=0.5',
        'Accept-Charset': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://developer.riotgames.com',
        'X-Riot-Token': '{riot_token}'
    ''' # noqa


__all__ = [
    'Account',
    'ChampionMastery',
    'Champion',
    'LeagueExp',
    'League',
    'LolStatus',
    'Match',
    'Spectator',
    'Summoner',
]
