# todo
import pytest

@pytest.mark.parametrize('continent, region', [
    ('ASIA', 'SG2'),
    ('AMERICAS', 'NA1'),
    ('EUROPE', 'EUW1'),
])

def test_client_init(api_key, client, continent, region):
    assert client.api_key == api_key
    assert client.continent == continent
    assert client.region == region

def test_get_summoner(client):
    summoner = client.get_summoner('timtamtom')
    
    assert summoner['id'] == 'NgcrA4udzPlTnWKWQmxcNYlZhFMfsUZSGMIIagDGCCCTYaN80t0HGx2XZw'
    assert summoner['name'] == 'timtamtom'
    assert summoner['puuid'] == 'N3UBD62V_MMh46MfiRo3TaMgD2xh5vprhF12IfAsAXzkUpBR-uL02rxgAsrDmOwzwbvBLWYadAeFQg'