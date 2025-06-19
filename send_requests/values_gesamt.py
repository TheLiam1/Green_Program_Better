import times_gesamt as mtg
import requests
import json
import certifi
#!für Photovoltaik

current_timestamp7 = mtg.give_right_timestamp()


def get_data_out_of_r1_gesamt_json(time):
    R2_GESAMT = requests.get(f"https://www.smard.de/app/chart_data/4068/DE/4068_DE_quarterhour_{time}.json", verify=certifi.where())
    data8 = R2_GESAMT.json()
    return data8

test = get_data_out_of_r1_gesamt_json(current_timestamp7)
with open("daten_photovoltaik.json", "w") as file:
    json.dump(test, file, indent=4, ensure_ascii=False)