import json
import requests
import os
import funcso as ff
import seaborn as sns
#import tensorflow as tf 
import pandas as pd
import matplotlib.pyplot as plt
valuableFields=['kills', 'deaths', 'assists', 'totalDamageDealtToChampions', 'goldEarned', 'totalMinionsKilled', 'visionScore','totalDamageDealt',
                'totalHeal', 'controlWardsPlaced', 'objectivesStolen', 'objectivesStolenAssists', 'totalTimeCCDealt', 'totalTimeSpentDead',]
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
PDData={}
for participant in matchD:
    print(participant['championName'])
    Info[participant['championName']]=extractInfo(participant)
    PDData = pd.DataFrame.from_dict(Info, orient='index')

#for participant in PDData['championName'].unique():

print(PDData.describe())
#print(Info)

def boxPlot():
    index = 0
    fg, axs = plt.subplots(ncols=5, nrows=4, figsize=(10, 20))
    axs=axs.flatten()
    for k, v in PDData.items():
        print(f"K: {k}, V: {v}")

        #sns.boxplot(y=k,data=PDData, ax=axs[index])
        #sns.histplot(v, kde=True, ax=axs[index],stat='density')
        
        #axs[index].boxplot(v)
        #axs[index].set_title(k)
        index += 1
        if index >= axs.size:
            break
    plt.figure(figsize=(30, 20))
    sns.heatmap(PDData.corr().abs(), annot=True)
    plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=5.0)
    plt.show()
boxPlot()
    #fig, axs=plt.subplots()
    # You can add more advanced analysis and visualization here
#going to make this its own thing so from here this will only run if testing the MLE engine.
