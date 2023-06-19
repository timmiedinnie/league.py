import requests
from lexicon import Lexicon


def validate_args(*args):
    valid_args = Lexicon.CONTINENTS + Lexicon.REGIONS
    for arg in args:
        if arg in valid_args:
            continue
        else:
            raise ValueError(f'Invalid argument: {arg}')
        
    return True


class Handler():
    def __init__(self, api_key, continent, region, ddragon_route=False):
        self.endpoints = Lexicon.ENDPOINTS
        self.ddragon_route = ddragon_route
        self.base = 'https://{}.api.riotgames.com/' if not ddragon_route \
            else Lexicon._DATA_DRAGON['root']
        self.sess = requests.Session()
        self.sess.headers.update(
            {
                "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
                "User-Agent": "Mozilla/5.0",
                "X-Riot-Token": api_key,
            }
        )

        if validate_args(continent, region):
            self.continent = continent
            self.region = region

    def __call__(self, method, route, switch_locale=True, **params):
        if self.ddragon_route:
            url = self.base.format(**params) + self.endpoints[route]
        else:
            url = self.base.format(self.region if switch_locale else self.continent) + \
                self.endpoints[route].format(**params)
        
        res = self.sess.request(method, url)
        
        if res.status_code == 200:
            return res.json()
        else:
            # res.raise_for_status()
            raise Exception(f'Error {res.status_code} {res.reason}')