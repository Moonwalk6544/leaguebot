import os
import requests
from dotenv import load_dotenv
import json
import time
import matplotlib.pyplot as plt
import MLE 
load_dotenv()
APIKEY=os.getenv("APIKEY")
TS=os.getenv("TESTSUMMONER")

NURL="https://na1.api.riotgames.com"
AURL="https://americas.api.riotgames.com"


matchData={}
def get_summoner_data(puuid):
    url = f"{NURL}/lol/summoner/v4/summoners/by-puuid/{puuid}"
    print(url)
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

def getCurrentMatch(puuid):
    url = f"{NURL}/lol/spectator/v5/active-games/by-summoner/{puuid}"
    headers = {
        "X-Riot-Token": APIKEY
    }
    response = requests.get(url, headers=headers)
    return response.json()
#print(get_summoner_data(TS))
#print (getMatchData(getCurrentMatch(TS)))
i=0
def puuidToName(puuid):
    url = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-puuid/{puuid}"

    headers = {
        "X-Riot-Token": APIKEY
    }
    response = requests.get(url, headers=headers)

    return response.json().get("gameName", "Unknown")
def getClientData():
    while True:
        data = {}
        response = requests.get("https://127.0.0.1:2999/liveclientdata/activeplayer", verify=False)
        if response.status_code == 200:
            data = response.json()
            json.dump(data, open(f"clientDataSample/liveclientdata{i}.json", "w"), indent=4)
            i+=1
            print('data retrieved')
        else:
            print("Error fetching data")
            return
        time.sleep(30)
def displayCorrelations():
    count = 0
    for entry in os.scandir("clientDataSample"):
        if entry.is_file() and entry.name.endswith(".json"):
            count += 1
    JArray=[{} for _ in range(count)]
    for i in range (2, count):
        
        with open(f"clientDataSample/liveclientdata{i}.json", "r") as f:
            JSE = json.load(f)
            JArray[i] = JSE
            #print(i) debugging
    damageNumbers = {}
    for i2 in range(2, count):
        damageNumbers[i2] = JArray[i2].get("championStats", {}).get("abilityPower", 0)
    plt.plot(damageNumbers.values())
    plt.xlabel('Time / 30 Seconds')
    plt.ylabel('Ability Power')
    plt.show()
    return
def getMatchTimeline(match_id):
    url = f"{AURL}/lol/match/v5/matches/{match_id}/timeline"
    headers = {
        "X-Riot-Token": APIKEY
    }
    response = requests.get(url, headers=headers)
    return response.json()
