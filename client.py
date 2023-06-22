from handler import Handler
from objects.account import Account
from objects.character import Character
from objects.item import Item
from objects.spell import Spell
from objects.cache import Cache


class Client():
    def __init__(self, api_key, continent='ASIA', region='SG2'):
        self.api_key = api_key
        self.continent = continent
        self.region = region
        self.handler = Handler(self.api_key, self.continent, self.region)
        self.cache = Cache()
        self.__get_all_champions()
        self.__get_items()

    # data dragon api
    def __get_all_champions(self):
        response = self.handler('GET', 'all_champion_data', ddragon_route=True)
        data = response['data']

        for c in data.values():
            champ = Character(c['name'], c['title'], c['blurb'], \
                             c['partype'], c['tags'], c['info'], c['stats'])
            
            self.cache.champions[c['key']] = champ
        
        print('DDragon: Champions loaded.')
    
    def __get_items(self):
        response = self.handler('GET', 'items', ddragon_route=True)
        data = response['data']
        import json
        for iid, itm in data.items():
            item = Item(itm['name'], itm['plaintext'], itm['into'] if 'into' in itm else [], \
                        itm['gold']['total'], itm['gold']['sell'], itm['tags'], itm['stats'])
            self.cache.items[iid] = item

        print('DDragon: Items loaded.')

    def get_summoner_spells(self):
        response = self.handler('GET', 'summoner_spells', ddragon_route=True)

    # quality of life methods
    def get_champion(self, champion_id):    
        return self.cache.get_champion(champion_id)
    
    def get_item(self, item_id):
        pass

    def get_summoner_spell(self, spell_id):
        pass

    # riot api
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