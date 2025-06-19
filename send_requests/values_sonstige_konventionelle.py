import requests
import json
import certifi

def values_sonstige_konventionelle():
    timestamp = requests.get("https://smard.de/app/chart_data/1227/DE/index_quarterhour.json", verify=certifi.where()).json()["timestamps"][-1]
    values = requests.get(f"https://www.smard.de/app/chart_data/1227/DE/1227_DE_quarterhour_{timestamp}.json", verify=certifi.where()).json()
    
    return values

values = values_sonstige_konventionelle()

with open("daten_sonstige_konventionelle.json", "w") as file:
    json.dump(values, file, indent=4, ensure_ascii=False)
