import os
import tarfile
import requests


CURRENT_VERSION = '13.11.1'  # as of 11/06/2023

url = f'https://ddragon.leagueoflegends.com/cdn/dragontail-{CURRENT_VERSION}.tgz'
target_path = f'dragontail-{CURRENT_VERSION}.tgz'

response = requests.get(url, stream=True)

if response.status_code == 200:
    with open(target_path, 'wb') as f:
        f.write(response.raw.read())

file = tarfile.open(target_path)  # open file

if not os.path.exists('./data_dragon'):
    os.mkdir('./data_dragon')

file.extractall('./data_dragon')
file.close()
os.remove(target_path)