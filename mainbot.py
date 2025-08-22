import os
import requests
from dotenv import load_dotenv
import json
import time
import matplotlib.pyplot as plt
load_dotenv()
APIKEY=os.getenv("APIKEY")
TS=os.getenv("TESTSUMMONER")
print(APIKEY)
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
    url = f"{NURL}/lol/match/v5/matches/{match_id}"
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
print(get_summoner_data(TS))
#print (getMatchData(getCurrentMatch(TS)))
i=0

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
def getMatchTimeline(match_id):
    url = f"{AURL}/lol/match/v5/matches/{match_id}/timeline"
    headers = {
        "X-Riot-Token": APIKEY
    }
    response = requests.get(url, headers=headers)
    json.dump(response.json(), open(f"{match_id}_timeline.json", "w"), indent=4)
    return response.json()

    '''for index in range(2, count):
        jsonArray=[{} for _ in range(0,30)]
        #todo: change temp index range
        with open(f"clientDataSample/liveclientdata{index}.json", "r") as f:
            print(index)
            JSE=json.load(f)
            jsonArray[index % 30] = JSE
            #print(jsonArray[index].get("championStats", {}).get("abilityPower", 0))'''
    '''for data in jsonArray[2:]:
        damageNumbers = data.get("championStats", {}).get("abilityPower", 0)
        print(damageNumbers)'''
    return
#debugging purposes
#getClientData()
displayCorrelations()
for i in getMatches(TS):
    json.dump(getMatchTimeline(i), open(f"{i}_timeline.json", "w"), indent=4)

'''for match_id in getMatches(TS):
    matchData[match_id] = getMatchData(match_id)
    #print(matchData[match_id])
    json.dump(matchData[match_id], open(f"{match_id}.json", "w"), indent=4)
    ids = matchData[match_id].get("metadata", {}).get("participants", [])
    print(ids)
'''
