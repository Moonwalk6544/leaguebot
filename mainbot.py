import os
import requests
from dotenv import load_dotenv
import json
import time
import matplotlib.pyplot as plt
import funcs as ff
import pandas as pd
import MLE 
load_dotenv()
APIKEY=os.getenv("APIKEY")
TS=os.getenv("TESTSUMMONER")
NURL="https://na1.api.riotgames.com"
AURL="https://americas.api.riotgames.com"

#riotID=ff.puuidToName(TS)
inns={}
inns=input("Enter riot ID and tagline, or riot PUUID: ")
inns=inns.replace(' ','')
innSplit=inns.split("#")
if len(innSplit) == 2:
    N2=ff.nameToPuuid(innSplit[0], innSplit[1])
    print(f"Now retrieving data for Player: {N2.get("gameName")}#{N2.get("tagLine")}")
else:
    N1=ff.puuidToName(innSplit)
    if N1[1] != "":
        print(f"Now retrieving data for Player: {N1[0]}#{N1[1]}")
    else:
        print('Incorrect Formatting. Please enter a valid PUUID or Riot Id.')
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
#debugging purposes
#getClientData()
#displayCorrelations()
'''
for i in getMatches(TS):
    json.dump(getMatchData(i), open(f"GameData/{i}.json", "w"), indent=4)
    json.dump(getMatchTimeline(i), open(f"GameTimelines/{i}_timeline.json", "w"), indent=4)
'''
#ok now its time to start getting serious. 
#MLE.analyze_match_data(getMatchData(getMatches(TS)[0]))

'''for match_id in getMatches(TS):
    matchData[match_id] = getMatchData(match_id)
    #print(matchData[match_id])
    json.dump(matchData[match_id], open(f"{match_id}.json", "w"), indent=4)
    ids = matchData[match_id].get("metadata", {}).get("participants", [])
    print(ids)
'''