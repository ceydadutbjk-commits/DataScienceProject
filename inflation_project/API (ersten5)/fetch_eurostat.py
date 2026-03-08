import requests
import json
import os

# Die URL für Butterpreise in Deutschland (HICP Index)
# geo=DE steht für Deutschland, coicop=CP01115 ist der Code für Butter
url = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/prc_hicp_midx?geo=DE&coicop=CP01151&format=JSON"

print("Rufe Butter-Daten von Eurostat ab...")
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    # Sicherstellen, dass der Ordner 'raw_data' existiert
    if not os.path.exists('raw_data'):
        os.makedirs('raw_data')
    
    # Speichern als JSON-Datei
    with open('raw_data/eurostat_butter_cpi.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    print("Erfolg! 'raw_data/eurostat_butter_cpi.json' wurde erstellt.")
else:
    print(f"Fehler: Status Code {response.status_code}")