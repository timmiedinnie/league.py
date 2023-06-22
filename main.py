import os
import json
import requests
from dotenv import load_dotenv
from client import Client

load_dotenv()

if __name__ == '__main__':
    api_key = os.getenv('RIOT_API_KEY')
    client = Client(api_key, continent='ASIA', region='SG2')

    # summoner = client.get_summoner('timtamtom')

    # champion_masteries = client.get_champion_mastery(summoner['puuid'])
    # champion_mastery = client.get_champion_mastery(summoner['puuid'], championId=80)
    # top_2_champions = client.get_champion_mastery(summoner['puuid'], limit=2)
    # mastery_score = client.get_mastery_score(summoner['puuid'])
    # champion_rotation = client.get_champion_rotation()
    # pantheon = client.get_champion('80')
    # boots = client.cache.get_item('1001')
    # ignite = client.cache.get_summoner_spell('14')

    # print(json.dumps(summoner, indent=4))
    # print(json.dumps(champion_masteries, indent=4))
    # print(json.dumps(champion_mastery, indent=4))
    # print(json.dumps(top_2_champions, indent=4))
    # print(json.dumps(mastery_score, indent=4))
    # print(json.dumps(champion_rotation, indent=4))
    # print(pantheon)
    # print(boots)
    # print(ignite)