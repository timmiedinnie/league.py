import os
import json
import requests
from dotenv import load_dotenv
from client import Client

load_dotenv()

if __name__ == '__main__':
    api_key = os.getenv('RIOT_API_KEY')
    client = Client(api_key, continent='ASIA', region='SG2')

    puuid = client.get_puuid('thermostat', 'tom')
    # champion_masteries = client.get_champion_mastery(puuid)
    # champion_mastery = client.get_champion_mastery(puuid, championId=80)

    # print(json.dumps(champion_masteries, indent=4))
    # print(json.dumps(champion_mastery, indent=4))