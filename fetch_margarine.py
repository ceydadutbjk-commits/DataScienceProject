import requests
import json
import os

os.makedirs('raw_data', exist_ok=True)

# CP01152 = Margarine und Pflanzenfette, geo=DE (Deutschland)
url = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/prc_hicp_midx?format=JSON&coicop=CP01152&geo=DE&unit=I15"

print("Rufe Margarine-Daten ab...")
try:
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        with open('raw_data/margarine_cpi.json', 'w') as f:
            json.dump(response.json(), f)
        print("Erfolg! 'raw_data/margarine_cpi.json' wurde erstellt.")
    else:
        print(f"Fehler: {response.status_code}")
except Exception as e:
    print(f"Fehler: {e}")