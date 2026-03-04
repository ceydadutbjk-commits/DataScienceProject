import requests
import json
import os

# Ordner erstellen
os.makedirs('raw_data', exist_ok=True)

# URL für Verbraucherpreise (HICP) - Milch, Käse, Eier (CP0114) in Deutschland
url = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/prc_hicp_midx?format=JSON&lang=en&coicop=CP0114&geo=DE&unit=I15"

print("Rufe Verbraucherpreise (CPI) für Milchprodukte ab...")

try:
    response = requests.get(url, timeout=15)
    if response.status_code == 200:
        data = response.json()
        
        # Speichern als neue Datei
        with open('raw_data/eurostat_cpi_dairy.json', 'w') as f:
            json.dump(data, f, indent=4)
            
        if "value" in data and data["value"]:
            print("Erfolg! Verbraucherdaten (CPI) gespeichert.")
            # Kleiner Check der Datenpunkte
            count = len(data["value"])
            print(f"Anzahl der Datenpunkte: {count}")
        else:
            print("Verbindung okay, aber keine Datenwerte gefunden.")
    else:
        print(f"Fehler: Status Code {response.status_code}")
except Exception as e:
    print(f"Verbindungsfehler: {e}")

    # Anzahl der Datenpunkte: 360