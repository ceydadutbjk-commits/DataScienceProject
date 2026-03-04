import requests
import json
import os

# Ordner erstellen, falls er noch nicht existiert
os.makedirs('raw_data', exist_ok=True)

# URL mit s_adj=NSA (Non-Seasonally Adjusted), um echte Daten zu erhalten
url = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/sts_inpp_m?format=JSON&lang=en&nace_r2=C105&s_adj=NSA&unit=I15&geo=DE"

print("Rufe Erzeugerpreise (PPI) Milchwirtschaft ab (NSA)...")

try:
    response = requests.get(url, timeout=15)
    if response.status_code == 200:
        data = response.json()
        
        # Speichern der Daten
        with open('raw_data/eurostat_ppi_dairy.json', 'w') as f:
            json.dump(data, f, indent=4)
            
        # Kleiner Test-Check für dich:
        if "value" in data and data["value"]:
            print("Erfolg! Daten wurden gefunden und gespeichert.")
        else:
            print("Achtung: Verbindung steht, aber das Feld 'value' ist noch leer.")
            
    else:
        print(f"Fehler: Status Code {response.status_code}")
except Exception as e:
    print(f"Verbindungsfehler: {e}")