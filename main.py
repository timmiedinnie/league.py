import os
import json
import requests
from dotenv import load_dotenv
from client import Client


if __name__ == '__main__':
    load_dotenv()
    
    api_key = os.getenv('RIOT_API_KEY')
    client = Client(api_key, continent='ASIA', region='SG2')
    puuid = client.get_puuid('thermostat', 'tom')
    
    champion_mastery = client.get_champion_mastery(puuid)

    for champ in champion_mastery:
        print(f'Character: {champ["championId"]}, Level: {champ["championLevel"]}')
