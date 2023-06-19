from handler import Handler
from objects.account import Account
from objects.character import Character
from objects.spell import Spell


class Client():
    def __init__(self, api_key, continent='ASIA', region='SG2'):
        self.api_key = api_key
        self.continent = continent
        self.region = region
        self.handler = Handler(self.api_key, self.continent, self.region)

        # self.cache = { 'champions': {}, 'items': {}, 'summoner_spells': {} }
        self.champion_cache = {}
        self.item_cache = {}
        self.summoner_spell_cache = {}

        self.__get_all_champions()

        
    def get_summoner(self, summoner_name):
        response = self.handler('GET', 'summoner', summonerName=summoner_name)

        return response
        
    def get_champion_mastery(self, puuid, championId=None, limit=None):
        if championId is None and limit is None:
            response = self.handler('GET', 'champion_masteries', puuid=puuid)
        elif championId is not None and limit is None:
            response = self.handler('GET', 'champion_mastery', \
                                puuid=puuid, championId=championId)
        elif championId is None and limit is not None:
            response = self.handler('GET', 'top_n_champion_masteries', \
                                puuid=puuid, limit=limit)
        else:
            raise KeyError('championId and limit cannot be specified at the same time.')
        
        return response
    
    def get_mastery_score(self, puuid):
        response = self.handler('GET', 'mastery_score', puuid=puuid)
        
        return response
    
    def get_champion_rotation(self):
        response = self.handler('GET', 'champion_rotation')
        
        return response
    
    # data dragon api
    def __get_all_champions(self):
        response = self.handler('GET', 'all_champion_data', ddragon_route=True)
        data = response['data']

        for c in data.values():
            test = Character(c['key'], c['name'], c['title'], c['blurb'], \
                             c['partype'], c['tags'], c['info'], c['stats'])
            
            self.champion_cache[c['key']] = test
            break

    
    
    
    def get_items(self):
        response = self.handler('GET', 'items', ddragon_route=True)
        
        
    
    def get_summoner_spells(self):
        response = self.handler('GET', 'summoner_spells', ddragon_route=True)
        
        