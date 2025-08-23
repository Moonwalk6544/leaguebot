import os
import requests
from dotenv import load_dotenv
import json
import time
import matplotlib.pyplot as plt
import funcs as ff
import MLE 
load_dotenv()
APIKEY=os.getenv("APIKEY")
TS=os.getenv("TESTSUMMONER")
NURL="https://na1.api.riotgames.com"
AURL="https://americas.api.riotgames.com"


print('Now retrieving data for player: ', ff.puuidToName(TS))



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
