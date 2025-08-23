import requests
import os
import funcs as ff
#import tensorflow as tf 
import pandas as pd
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
    # You can add more advanced analysis and visualization here
