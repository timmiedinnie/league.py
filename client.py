from handler import Handler


class Client():
    def __init__(self, api_key, continent='ASIA', region='SG2', ddragon_version='13.12.1'):
        self.api_key = api_key
        self.continent = continent
        self.region = region
        self.ddragon_version = ddragon_version
        self.handler = Handler(self.api_key, self.continent, self.region)
        

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
    def get_champions(self):
        response = self.handler('GET', 'all_champion_data', version=self.ddragon_version)
        
        return response
    
    def get_items(self):
        response = self.handler('GET', 'items', version=self.ddragon_version)
        
        return response
    
    def get_summoner_spells(self):
        response = self.handler('GET', 'summoner_spells', version=self.ddragon_version)
        
        return response