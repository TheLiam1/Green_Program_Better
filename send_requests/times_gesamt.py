import requests
#!für Photovoltaik
import urllib3

urllib3.disable_warnings(category=urllib3.exceptions.InsecureRequestWarning)

def give_right_timestamp():
    R1_TIMES_GESAMT = requests.get("https://smard.de/app/chart_data/4068/DE/index_quarterhour.json", verify=False)
    data6 = R1_TIMES_GESAMT.json()
    current_timestamp6 = data6["timestamps"][-1]
    return current_timestamp6