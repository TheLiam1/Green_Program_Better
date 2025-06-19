#!Values für Photovoltaik
import values_gesamt, times_gesamt
#!
import values_biomasse, values_pumpspeicher, values_sonstige_erneuerbare, values_wasserkraft, values_wind_onshore, values_wind_offshore

data_biomasse, data_pumpspeicher, data_sonstige_erneuerbare, data_wasserkraft, data_wind_onshore, data_photovoltaik, data_wind_offshore = values_biomasse.values_biomasse(), values_pumpspeicher.values_pumpspeicher(), values_sonstige_erneuerbare.values_sonstige_erneuerbare(), values_wasserkraft.values_wasserkraft(), values_wind_onshore.values_wind_onshore(), values_gesamt.get_data_out_of_r1_gesamt_json(times_gesamt.give_right_timestamp()), values_wind_offshore.values_wind_offshore()

#Jetzt die nicht grünen Energiedaten importieren
#benutzen tu ich die unten
import values_braunkohle, values_erdgas, values_kernenergie, values_sonstige_konventionelle, values_steinkohle

data_braunkohle, data_erdgas, data_kernenergie, data_sonstige_konventionelle, data_steinkohle = values_braunkohle.values_braunkohle(), values_erdgas.values_erdgas(), values_kernenergie.values_kernenergie(), values_sonstige_konventionelle.values_sonstige_konventionelle(), values_steinkohle.values_steinkohle()

# !! Hier fängt der arbeitende Code an !!

count_for_timestamps_wasserkraft = 0
count_overall_wasserkraft = 0
specific_count_right_timestamp_wasserkraft = None

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

print("Richtige MWh für Wasserkraft:", MWh_for_specific_timestamp_wasserkraft)
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

print("Richtige MWh für Pumpspeicher:", MWh_for_specific_timestamp_pumpspeicher)
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

print("Richtige MWh für sonstige Erneuerbare:", MWh_for_specific_timestamp_sonstige_erneuerbare)

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

print("Richtige MWh für wind onshore:", MWh_for_specific_timestamp_values_wind_onshore)

count_for_timestamps_biomasse = 0
count_overall_biomasse = 0
specific_count_right_timestamp_biomasse = None

for i in data_biomasse["series"]:
    for k in i:
        count_overall_biomasse += 1
        if count_for_timestamps_biomasse % 2 == 0:
            if k == search_timestamp:
                print("Gesuchter Timestamp:  ", k)
                specific_count_right_timestamp_biomasse = count_overall_biomasse
        count_for_timestamps_biomasse += 1

count_overall_biomasse = 0

for i in data_biomasse["series"]:
    for k in i:
        count_overall_biomasse += 1
        if count_overall_biomasse == specific_count_right_timestamp_biomasse+ 1:
            MWh_for_specific_timestamp_values_biomasse = k

print("Richtige MWh für biomasse:", MWh_for_specific_timestamp_values_biomasse)

count_for_timestamps_photovoltaik = 0
count_overall_photovoltaik = 0
specific_count_right_timestamp_photovoltaik = None

for i in data_photovoltaik["series"]:
    for k in i:
        count_overall_photovoltaik += 1
        if count_for_timestamps_photovoltaik % 2 == 0:
            if k == search_timestamp:
                print("Gesuchter Timestamp:  ", k)
                specific_count_right_timestamp_photovoltaik = count_overall_photovoltaik
        count_for_timestamps_photovoltaik += 1

count_overall_photovoltaik = 0

for i in data_photovoltaik["series"]:
    for k in i:
        count_overall_photovoltaik += 1
        if count_overall_photovoltaik == specific_count_right_timestamp_photovoltaik + 1:
            MWh_for_specific_timestamp_photovoltaik = k

print("Richtige MWh für photovoltaik:", MWh_for_specific_timestamp_photovoltaik)

count_for_timestamps_wind_offshore = 0
count_overall_wind_offshore = 0
specific_count_right_timestamp_wind_offshore = None

for i in data_wind_offshore["series"]:
    for k in i:
        count_overall_wind_offshore += 1
        if count_for_timestamps_wind_offshore % 2 == 0:
            if k == search_timestamp:
                print("Gesuchter Timestamp:  ", k)
                specific_count_right_timestamp_wind_offshore = count_overall_wind_offshore
        count_for_timestamps_wind_offshore += 1

count_overall_wind_offshore = 0

for i in data_wind_offshore["series"]:
    for k in i:
        count_overall_wind_offshore += 1
        if count_overall_wind_offshore == specific_count_right_timestamp_wind_offshore + 1:
            MWh_for_specific_timestamp_wind_offshore = k

print("Richtige MWh für wind offshore:", MWh_for_specific_timestamp_wind_offshore)

#Jezt möchte ich die gesamte Erzeugung von grüner Energie zu einem bestimmten Timestamp herausfinden

gesamt_grüne_energie = MWh_for_specific_timestamp_wasserkraft + MWh_for_specific_timestamp_photovoltaik + MWh_for_specific_timestamp_pumpspeicher + MWh_for_specific_timestamp_sonstige_erneuerbare + MWh_for_specific_timestamp_values_wind_onshore + MWh_for_specific_timestamp_values_biomasse + MWh_for_specific_timestamp_wind_offshore

print("Dies ist die gesamte Erzeugung grüner Energie zu dem gesuchten Timestamp: ", gesamt_grüne_energie)

#Jetzt noch die genauen Daten für nicht grüne Energie herausfinden, um den Anteil an grünem Strom im Bundesstromnetz berechnen zu können

count_for_timestamps_braunkohle = 0
count_overall_braunkohle = 0
specific_count_right_timestamp_braunkohle = None

#Hier wird geschaut, wo der gesuchte Timestamp zu finden ist
for i in data_braunkohle["series"]:
    for k in i:
        count_overall_braunkohle += 1
        if count_for_timestamps_braunkohle % 2 == 0:
            if k == search_timestamp:
                print("Gesuchter Timestamp:  ", k)
                specific_count_right_timestamp_braunkohle = count_overall_braunkohle
        count_for_timestamps_braunkohle += 1

count_overall_braunkohle = 0

#Hier wird dann zur richtigen Position(abhängig vom gesuchten Timestamp) die MWh Menge herausgefunden
for i in data_braunkohle["series"]:
    for k in i:
        count_overall_braunkohle += 1
        if count_overall_braunkohle == specific_count_right_timestamp_braunkohle + 1:
            MWh_for_specific_timestamp_braunkohle = k

print("Richtige MWh für Braunkohle:", MWh_for_specific_timestamp_braunkohle)
