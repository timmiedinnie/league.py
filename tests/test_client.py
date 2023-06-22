# todo
import pytest

@pytest.mark.parametrize('continent, region', [
    ('AMERICAS', 'NA1'),
    ('AMERICAS', 'BR1'),
    ('AMERICAS', 'LA1'),
    ('AMERICAS', 'LA2'),
    ('ASIA', 'KR'),
    ('ASIA', 'JP1'),
    ('ASIA', 'OC1'),
    ('ASIA', 'PH2'),
    ('ASIA', 'SG2'),
    ('ASIA', 'TH2'),
    ('ASIA', 'VN2'),
    ('EUROPE', 'EUN1'),
    ('EUROPE', 'EUW1'),
    ('EUROPE', 'RU'),
    ('EUROPE', 'TR1'),
    ('EUROPE', 'TW2')
])

def test_client_init(api_key, client, continent, region):
    client.continent = continent
    client.region = region

    assert client.api_key == api_key
    assert client.continent == continent
    assert client.region == region

def test_get_summoner(client):
    summoner = client.get_summoner('timtamtom')
    
    assert summoner['id'] == 'NgcrA4udzPlTnWKWQmxcNYlZhFMfsUZSGMIIagDGCCCTYaN80t0HGx2XZw'
    assert summoner['name'] == 'timtamtom'
    assert summoner['puuid'] == 'N3UBD62V_MMh46MfiRo3TaMgD2xh5vprhF12IfAsAXzkUpBR-uL02rxgAsrDmOwzwbvBLWYadAeFQg'