from handler import Handler


class Client():
    def __init__(self, api_key, continent='ASIA', region='SG2'):
        self.api_key = api_key
        self.continent = continent
        self.region = region
        self.handler = Handler(self.api_key, self.continent, self.region)

    def get_puuid(self, gameName, tagLine):
        response = self.handler('GET', 'account', \
                            gameName=gameName, tagLine=tagLine)['puuid']
        return response
        
    def get_champion_mastery(self, puuid, championId=None, limit=None):
        if championId is None and limit is None:
            response = self.handler('GET', 'champion_masteries', puuid=puuid, switch_locale=True)
        elif championId is not None and limit is None:
            response = self.handler('GET', 'champion_mastery', \
                                puuid=puuid, championId=championId, switch_locale=True)
        elif championId is None and limit is not None:
            response = self.handler('GET', 'top_n_champion_masteries', \
                                puuid=puuid, limit=limit, switch_locale=True)
        else:
            raise KeyError('championId and limit cannot be specified at the same time.')
        
        return response