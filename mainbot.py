import os
import requests
from dotenv import load_dotenv
load_dotenv()
APIKEY=os.getenv("APIKEY")
TS=os.getenv("TESTSUMMONER")
print(APIKEY)
AURL="https://americas.api.riotgames.com"

def get_summoner_data(puuid):
    url = f"{AURL}/riot/account/v1/accounts/by-puuid/{puuid}"
    headers = {
        "X-Riot-Token": APIKEY
    }
    response = requests.get(url, headers=headers)
    return response.json()
def getMatches(puuid):
    url = f"{AURL}/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=10"
    headers = {
        "X-Riot-Token": APIKEY
    }
    response = requests.get(url, headers=headers)
    return response.json()
def getMatchData(match_id):
    url = f"{AURL}/lol/match/v5/matches/{match_id}"
    headers = {
        "X-Riot-Token": APIKEY
    }
    response = requests.get(url, headers=headers)
    return response.json()
print(get_summoner_data(TS))
for match_id in getMatches(TS):
    print(getMatchData(match_id))