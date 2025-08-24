import json
import requests
import os
import funcso as ff
import seaborn as sns
#import tensorflow as tf 
import pandas as pd
import matplotlib.pyplot as plt
valuableFields=['kills', 'deaths', 'assists', 'totalDamageDealtToChampions', 'goldEarned', 'totalMinionsKilled', 'visionScore','totalDamageDealt',
                'totalHeal', 'sightWardsBoughtInGame', 'objectivesStolen', 'objectivesStolenAssists', 'timeEnemySpentControlled', 'totalTimeCrowdControlDealt',]
def analyze_match_data(match_data):
    # Extract relevant information from the match data
    participants = match_data.get("info", {}).get("participants", [])
    for participant in participants:
        puuid = participant.get("puuid")
        kills = participant.get("kills", 0)
        deaths = participant.get("deaths", 0)
        assists = participant.get("assists", 0)
        # Perform analysis on the participant's data
        print(f"Player {ff.puuidToName(puuid)}: Kills={kills}, Deaths={deaths}, Assists={assists}")
matchD=ff.getMatchData('NA1_5352736503').get("info", {}).get("participants", [])
json.dump(matchD, open('GameData/matchD.json', 'w'), indent=4)

def extractInfo(participant):
    valuableInfo={}
    for field in valuableFields:
        valuableInfo[field]=participant.get(field, 0)

    return valuableInfo
Info={}
for participant in matchD:
    print(participant['championName'])
    Info[participant['championName']] = extractInfo(participant)

PDData = pd.DataFrame.from_dict(Info)
#for participant in PDData['championName'].unique():
fg, axs = plt.subplots(ncols=10, nrows=14, figsize=(30, 30))
print(PDData.describe())
index = 0
axs=axs.flatten()

for k, v in PDData["Volibear"].items():
    print(f"K: {k}, V: {v}")
    if isinstance(v, int):
        print('reached')
        sns.boxplot(y=k,data=PDData, ax=axs[index])
        #axs[index].boxplot(v)
        axs[index].set_title(k)
    index += 1
    if index >= axs.size:
        break
plt.tight_layout()
plt.show()

    #fig, axs=plt.subplots()
    # You can add more advanced analysis and visualization here
#going to make this its own thing so from here this will only run if testing the MLE engine.
