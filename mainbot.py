import os
import requests
from dotenv import load_dotenv
import json
import time
load_dotenv()
APIKEY=os.getenv("APIKEY")
TS=os.getenv("TESTSUMMONER")
print(APIKEY)
AURL="https://na1.api.riotgames.com"
matchData={}
def get_summoner_data(puuid):
    url = f"{AURL}/lol/summoner/v4/summoners/by-puuid/{puuid}"
    print(url)
    headers = {
        "X-Riot-Token": APIKEY
    }
    response = requests.get(url, headers=headers)
    return response.json()
def getMatches(puuid):
    url = f"{AURL}/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=1"
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
def getCurrentMatch(puuid):
    url = f"{AURL}/lol/spectator/v5/active-games/by-summoner/{puuid}"
    headers = {
        "X-Riot-Token": APIKEY
    }
    response = requests.get(url, headers=headers)
    return response.json()
print(get_summoner_data(TS))
#print (getMatchData(getCurrentMatch(TS)))
i=1
while True:
    data = {}
    response = requests.get("https://127.0.0.1:2999/liveclientdata/activeplayer", verify=False)
    if response.status_code == 200:
        data = response.json()
        i+=1
        print('data retrieved')
    else:
        print("Error fetching data")

    json.dump(data, open(f"clientDataSample/liveclientdata{i}.json", "w"), indent=4)
    time.sleep(30)
#debugging purposes
'''for match_id in getMatches(TS):
    matchData[match_id] = getMatchData(match_id)
    #print(matchData[match_id])
    json.dump(matchData[match_id], open(f"{match_id}.json", "w"), indent=4)
    ids = matchData[match_id].get("metadata", {}).get("participants", [])
    print(ids)
'''
