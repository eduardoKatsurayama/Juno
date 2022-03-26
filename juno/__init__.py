version = '0.0.1'

import os # noqa : E402

from .api import (
    Account,
    ChampionMastery,
    Champion,
    LeagueExp,
    League,
    LolStatus,
    Match,
    Spectator,
    Summoner,
)


def authenticate(riot_token):
    os.environ['HEADERS'] = f'''
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
        'Accept-Language': 'en-AU,en;q=0.9,pt-BR;q=0.8,pt;q=0.7,en-GB;q=0.6,en-US;q=0.5',
        'Accept-Charset': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://developer.riotgames.com',
        'X-Riot-Token': '{riot_token}'
    ''' # noqa : E501


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
