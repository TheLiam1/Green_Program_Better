#!Values für Photovoltaik
import values_gesamt, times_gesamt
#!
import values_biomasse, values_pumpspeicher, values_sonstige_erneuerbare, values_wasserkraft, values_wind_onshore

data_biomasse, data_pumpspeicher, data_sonstige_erneuerbare, data_wasserkraft, data_wind_onshore, daten_photovoltaik = values_biomasse.values_biomasse(), values_pumpspeicher.values_pumpspeicher(), values_sonstige_erneuerbare.values_sonstige_erneuerbare(), values_wasserkraft.values_wasserkraft(), values_wind_onshore.values_wind_onshore(), values_gesamt.get_data_out_of_r1_gesamt_json(times_gesamt.give_right_timestamp())

count_for_timestamps_wasserkraft = 0
count_overall_wasserkraft = 0
specific_count_right_timestamp_wasserkraft = None

MWh_for_specific_timestamp_wasserkraft = None
MWh_for_specific_timestamp_pumpspeicher = None
MWh_for_specific_timestamp_sonstige_erneuerbare = None
MWh_for_specific_timestamp_values_wind_onshore = None

search_timestamp = int(input("Searched timestamp: "))

#Hier wird geschaut, wo der gesuchte Timestamp zu finden ist
for i in data_wasserkraft["series"]:
    for k in i:
        count_overall_wasserkraft += 1
        if count_for_timestamps_wasserkraft % 2 == 0:
            if k == search_timestamp:
                print("Gesuchter Timestamp:  ", k)
                specific_count_right_timestamp_wasserkraft = count_overall_wasserkraft
        count_for_timestamps_wasserkraft += 1

count_overall_wasserkraft = 0

#Hier wird dann zur richtigen Position(abhängig vom gesuchten Timestamp) die MWh Menge herausgefunden
for i in data_wasserkraft["series"]:
    for k in i:
        count_overall_wasserkraft += 1
        if count_overall_wasserkraft == specific_count_right_timestamp_wasserkraft + 1:
            MWh_for_specific_timestamp_wasserkraft = k

#Das Ganze wiederhole ich dann für die anderen Energiearten
#Hier für Pumpspeicher Energie
count_for_timestamps_pumpspeicher = 0
count_overall_pumpspeicher = 0
specific_count_right_timestamp_pumpspeicher = None

for i in data_pumpspeicher["series"]:
    for k in i:
        count_overall_pumpspeicher += 1
        if count_for_timestamps_pumpspeicher % 2 == 0:
            if k == search_timestamp:
                print("Gesuchter Timestamp:  ", k)
                specific_count_right_timestamp_pumpspeicher = count_overall_pumpspeicher
        count_for_timestamps_pumpspeicher += 1

count_overall_pumpspeicher = 0

for i in data_pumpspeicher["series"]:
    for k in i:
        count_overall_pumpspeicher += 1
        if count_overall_pumpspeicher == specific_count_right_timestamp_pumpspeicher + 1:
            MWh_for_specific_timestamp_pumpspeicher = k

#Hier für sonstige Erneuerbare
count_for_timestamps_sonstige_erneuerbare = 0
count_overall_sonstige_erneuerbare = 0
specific_count_right_timestamp_sonstige_erneuerbare = None

for i in data_sonstige_erneuerbare["series"]:
    for k in i:
        count_overall_sonstige_erneuerbare += 1
        if count_for_timestamps_sonstige_erneuerbare % 2 == 0:
            if k == search_timestamp:
                print("Gesuchter Timestamp:  ", k)
                specific_count_right_timestamp_sonstige_erneuerbare = count_overall_sonstige_erneuerbare
        count_for_timestamps_sonstige_erneuerbare += 1

count_overall_sonstige_erneuerbare = 0

for i in data_sonstige_erneuerbare["series"]:
    for k in i:
        count_overall_sonstige_erneuerbare += 1
        if count_overall_sonstige_erneuerbare == specific_count_right_timestamp_sonstige_erneuerbare + 1:
            MWh_for_specific_timestamp_sonstige_erneuerbare = k

count_for_timestamps_wind_onshore = 0
count_overall_wind_onshore = 0
specific_count_right_timestamp_wind_onshore = None

for i in data_wind_onshore["series"]:
    for k in i:
        count_overall_wind_onshore += 1
        if count_for_timestamps_wind_onshore % 2 == 0:
            if k == search_timestamp:
                print("Gesuchter Timestamp:  ", k)
                specific_count_right_timestamp_wind_onshore = count_overall_wind_onshore
        count_for_timestamps_wind_onshore += 1

count_overall_wind_onshore = 0

for i in data_wind_onshore["series"]:
    for k in i:
        count_overall_wind_onshore += 1
        if count_overall_wind_onshore == specific_count_right_timestamp_wind_onshore+ 1:
            MWh_for_specific_timestamp_values_wind_onshore = k
