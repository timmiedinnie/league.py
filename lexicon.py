class Lexicon():
    def __init__(self):
        raise NotImplementedError("Vocab is an abstract class and cannot be instantiated.")
    
    CONTINENTS = [
        'AMERICAS',
        'ASIA',
        'EUROPE'
    ]

    REGIONS = [
        'BR1',   # Brazil
        'EUN1',  # Europe Nordic & East
        'EUW1',  # Europe West
        'JP1',   # Japan
        'KR',    # Korea
        'LA1',   # Latin America North
        'LA2',   # Latin America South
        'NA1',   # North America
        'OC1',   # Oceania
        'PH2',   # Phillipines
        'RU',    # Russia
        'SG2',   # Singapore
        'TH2',   # Thailand
        'TR1',   # Turkey
        'TW2',   # Taiwan
        'VN2',   # Vietnam
    ]

    _CHAMPION_MASTERY_V4 = {
        'champion_masteries': 'lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}',  # get all champion mastery entries sorted by number of champion points descending
        'champion_mastery': 'lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}/by-champion/{championId}', # get a champion mastery by puuid and championId
        'top_n_champion_masteries': 'lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}/top?count={limit}',  #  get specified number of top champion mastery entries sorted by number of champion points descending
        'mastery_score': 'lol/champion-mastery/v4/scores/by-puuid/{puuid}',  # get a player's total champion mastery score, which is the sum of individual champion mastery levels
    }

    _CHAMPION_V3 = {}

    _CLASH_V1 = {}

    _LEAGUE_EXP_V4 = {}

    _LEAGUE_V4 = {}

    _LOL_CHALLENGES_V1 = {}

    _LOL_STATUS_V4 = {}

    _LEAGUE_V4 = {}

    _LEAGUE_EXP_V4 = {}

    _MATCH_V5 = {}

    _SPECTATOR_V4 = {}

    _DATA_DRAGON = {
        # 'data_dragon': 'https://ddragon.leagueoflegends.com/cdn/dragontail-13.11.1.tgz'
    }

    ENDPOINTS = {
        'account': 'riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}',
        **_CHAMPION_MASTERY_V4
    }