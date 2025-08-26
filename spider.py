import requests
import funcso as ff
import json


'''we could use the call that gets multiple names from an elo. we would then have to make 2 calls, one for puuid and one for matches.
this method would be slower but possibly have higher fidelity. alternatively we could spider the old fashioned way. I think we'll go with the
latter.'''

#starting seed
silverPuuid = "Ad Infinitum#5659"
goldPuuid = "homietickler#NA1"
platPuuid = "inty500#NT500"
masterPuuid = "emerald lion#rank1"

seedPuuids = [silverPuuid, goldPuuid, platPuuid, masterPuuid]
ids=set()
def spiderElo(RiotId):
    puuid=ff.nameToPuuid(RiotId)
    matches = ff.getMatches(puuid, 5)
    for match in matches:
        matchData = ff.getMatchData(match)
        for participant in matchData.get("metadata", {}).get("participants", []):
            #handle unique check
            if participant not in ids:
                json.dump(matchData, open(f"GameData/{match}.json", "w"), indent=4)
                ids.add(participant)
        #ids.update(matchData.get("metadata", {}).get("participants", []))
spiderElo(goldPuuid)
