import funcso as ff
import requests
import json

def getItemInfo(matchd):
    with open(f"item.json") as f:
        item_data = json.load(f)
    item_info = {}
    item_names = {}
    for participant in matchd['info']['participants']:
        item_info[participant['championName']] = {}
        item_names[participant['championName']] = {}
        for item in range(7):
            itemNumber = participant[f'item{item}']
            item_info[participant['championName']][item] = itemNumber
            item_names[participant['championName']][item] = item_data.get('data', {}).get(str(itemNumber), {}).get('name', 'Unknown Item')

    return item_info, item_names
def Main():
    itemInf, itemName=getItemInfo(ff.getMatchData('NA1_5353780626'))
    print(itemName)
