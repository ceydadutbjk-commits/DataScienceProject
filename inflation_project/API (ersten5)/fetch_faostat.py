import requests
import json
import os

os.makedirs('raw_data', exist_ok=True)

# Wir versuchen einen leicht anderen API-Pfad für Deutschland (Area 79), Milch (Item 882)
url = "https://fenixservices.fao.org/faostat/api/v1/en/data/PP?area=79&item=882&element=5530"

print("Versuche Verbindung zu FAOSTAT (Rohmilch-Preise)...")

try:
    # timeout=20 bedeutet: Wenn nach 20 Sek. keine Antwort kommt, bricht er ab statt zu hängen
    response = requests.get(url, timeout=20)
    
    if response.status_code == 200:
        data = response.json()
        with open('raw_data/faostat_raw_milk.json', 'w') as f:
            json.dump(data, f)
        print("Erfolg! 'raw_data/faostat_raw_milk.json' wurde erstellt.")
    else:
        print(f"Server antwortete mit Fehlercode: {response.status_code}")

except requests.exceptions.Timeout:
    print("Fehler: Die FAOSTAT-API ist gerade zu langsam (Timeout). Versuch es gleich noch einmal.")
except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")

# Wir haben den API-Zugriff programmiert (Code vorhanden), 
# aber aufgrund von Server-Instabilitäten bei FAOSTAT haben wir 
# den Test-Datensatz für heute manuell als CSV/JSON von der Website geladen.