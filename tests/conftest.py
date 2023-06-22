import os
import pytest
from dotenv import load_dotenv
from league import Client

load_dotenv()

@pytest.fixture
def api_key():
    return os.getenv('RIOT_API_KEY')

@pytest.fixture
def client(api_key):
    return Client(api_key, continent='ASIA', region='SG2')