import os
import requests
from dotenv import load_dotenv
import json
import time
import matplotlib.pyplot as plt
load_dotenv()
APIKEY=os.getenv("APIKEY")
TS=os.getenv("TESTSUMMONER")

NURL="https://na1.api.riotgames.com"
AURL="https://americas.api.riotgames.com"
byPuuid="lol/summoner/v4/summoners/by-puuid/"


matchData={}
def getData(endpoint, arg1="", extraArgs="", base=NURL):
    #get data accepts a base as argument but also has backup implementation just in case.
    url = f"{base}/{endpoint}/{arg1}/{extraArgs}"
    if base==NURL:
        AltUrl = f"{AURL}/{endpoint}/{arg1}/{extraArgs}"
    else:
        AltUrl = f"{NURL}/{endpoint}/{arg1}/{extraArgs}"
    headers = {
        "X-Riot-Token": APIKEY

    }
    #print(APIKEY)
    #okay this function is awful. I know. im sorry. i couldnt figure out the try except thing so we're doing it 
    #old fashioned way haha
    r=requests.get(url, headers=headers)
    r1=requests.get(AltUrl, headers=headers)
    if r.status_code >300: #bad request 1
        if r1.status_code >300: #bad request 2
            print(f"Malformed request R: {r} R1: {r1}")
            return
        else:
            print(f"Request redirected to alternate server. R: {r} R1: {r1}")
            print(url)
            return r1.json()
    else:
        return r.json()

def getMatches(puuid,number):
    return getData("lol/match/v5/matches/by-puuid", puuid, f"ids?start=0&count={number}", base=AURL)
def getMatchData(match_id):
    return getData("lol/match/v5/matches", match_id, base=AURL)
def getCurrentMatch(puuid):
    return getData("lol/spectator/v5/active-games/by-summoner", puuid)
#print(get_summoner_data(TS))
#print (getMatchData(getCurrentMatch(TS)))
i=0
def puuidToName(puuid):
    url = f"{AURL}/riot/account/v1/accounts/by-puuid/{puuid}"

    headers = {
        "X-Riot-Token": APIKEY
    }
    response = requests.get(url, headers=headers)

    return response.json().get("gameName", "Unknown"), response.json().get("tagLine", "")
def nameToPuuid(gameName, tagLine):
    print(f"gamename: {gameName}, tagline: {tagLine}")
    data1=getData("riot/account/v1/accounts/by-riot-id", gameName, tagLine, AURL)
    if (data1 is not None):
        return data1
    else: 
        print("Please enter the riot ID or PUUID in the correct format. (GameName#Tagline)")

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
    return getData("lol/match/v5/matches", match_id, "/timeline")