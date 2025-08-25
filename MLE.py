import json
import requests
import os
import funcso as ff
import random
import itemeval as ie
import seaborn as sns
import tensorflow as tf 
import pandas as pd
import matplotlib.pyplot as plt
valuableFields=['teamId','puuid', 'win', 'kills', 'deaths', 'assists', 'totalDamageDealtToChampions', 'goldEarned', 'totalMinionsKilled', 'visionScore','totalDamageDealt',
                'totalHeal', 'controlWardsPlaced', 'objectivesStolen', 'objectivesStolenAssists', 'totalTimeCCDealt', 'totalTimeSpentDead',]
def analyze_match_data(match_data, puuid):
    # Extract relevant information from the match data
    participants = match_data.get("info", {}).get("participants", [])
    for participant in participants:
        #maybe while we scan we keep the results for the network?
        puuid1 = participant.get("puuid")
        if puuid == puuid1:
            kills = participant.get("kills", 0)
            deaths = participant.get("deaths", 0)
            assists = participant.get("assists", 0)
            champion = participant.get("championName", "Unknown")
            # Perform analysis on the participant's data
            print(f"Player {ff.puuidToName(puuid)}: Champion={champion} Kills={kills}, Deaths={deaths}, Assists={assists}")
#changed to use higher elo game
#matchD=ff.getMatchData('NA1_5353780626')
#json.dump(matchD, open('GameData/matchD.json', 'w'), indent=4)

def extractInfo(participant):
    valuableInfo={}
    for field in valuableFields:
        valuableInfo[field]=participant.get(field, 0)

    return valuableInfo


def getParticipantData(matchD):
    Info={}
    for participant in matchD.get("info", {}).get("participants", []):
        #print(participant)
        Info[participant['championName']]=extractInfo(participant)
        PDData = pd.DataFrame.from_dict(Info, orient='index')
    print(Info.keys())
    return pd.DataFrame(PDData, index=Info.keys())

#for participant in PDData['championName'].unique():

#print(PDData.describe())
#print(Info)
def removeOutliers(dataFrame):
    Q1 = dataFrame.quantile(0.25)
    Q3 = dataFrame.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return pd.DataFrame((dataFrame < lower_bound) | (dataFrame > upper_bound))

def boxPlot():
    PDData={}
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
def heatMap(participantData):
    plt.figure(figsize=(30, 20))
    corr = participantData.corr().abs()
    print(corr)
    sns.heatmap(corr, annot=True)
    plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=5.0)
    plt.show()
def heatMapDiff(participantData, participantData2):
    plt.figure(figsize=(30, 20))
    for datum in participantData2:
        #work in progress
    corr = participantData.corr().abs()
    corr2= participantData2.corr().abs()
    diffy = corr - corr2
    print(diffy)
    sns.heatmap(diffy, annot=True)
    plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=5.0)
    plt.show()
#boxPlot()

#matchData=ff.getMatchData('NA1_5353780626')
#print(ie.getItemInfo(matchData))

#PData=getParticipantData(matchData)
#heatMap(PData.loc[["Irelia","Malzahar","Viktor"]])
def splitSet(pData):
    Set1={}
    for i in range(7):
        Set1[pData.iloc[i]['championName']] = pData.iloc[i]
    return Set1
#heatMap(PData)



def testScalars():
    scalar1=tf.constant(5)
    vector1=tf.constant([1, 2, 3])
    print(vector1)
    tensor=tf.constant([[[1,2],[3,4]],[[5,6],[7,8]]])
    rand_tensor=tf.random.Generator.from_seed(77)
    normalizedTensor=rand_tensor.normal(shape=[8,10], mean=50, stddev=7)
#lets check our normalized tensor's bell curve
def histogram(data):
    plt.figure(figsize=(30,30))
    sns.histplot(data, kde=True, stat='density')
    plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=5.0)
    plt.show()

def tensors():
    PDData={}
    tf_data = tf.convert_to_tensor(PDData.values, dtype=tf.float32)
    tf_labels = tf.convert_to_tensor(PDData['win'].values, dtype=tf.float32)
    #fig, axs=plt.subplots()
    # You can add more advanced analysis and visualization here
#going to make this its own thing so from here this will only run if testing the MLE engine.
