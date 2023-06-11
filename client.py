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
        
    def get_champion_mastery(self, puuid):
        response = self.handler('GET', 'champion_mastery', \
                            puuid=puuid, region=self.region)
        return response