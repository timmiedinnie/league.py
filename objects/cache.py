class Cache():
    def __init__(self):
        self.champions = {}
        self.items = {}
        self.summoner_spells = {}

    def get_champion(self, champion_id):
        return self.champions[champion_id]
    
    def get_item(self, item_id):
        return self.items[item_id]
