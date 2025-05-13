import requests
import json
import urllib3

urllib3.disable_warnings(category=urllib3.exceptions.InsecureRequestWarning)

def values_kernenergie():
    timestamp = requests.get("https://smard.de/app/chart_data/1224/DE/index_quarterhour.json", verify=False).json()["timestamps"][-1]
    values = requests.get(f"https://www.smard.de/app/chart_data/1224/DE/1224_DE_quarterhour_{timestamp}.json", verify=False).json()
    
    return values

values = values_kernenergie()

with open("daten_kernenergie.json", "w") as file:
    json.dump(values, file, indent=4, ensure_ascii=False)
