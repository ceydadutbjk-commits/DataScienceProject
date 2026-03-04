import os
import json
from dotenv import load_dotenv
from fredapi import Fred

# 1. Geheimschlüssel aus der .env Datei laden
load_dotenv()
api_key = os.getenv('FRED_API_KEY')

# 2. Verbindung zur FRED API herstellen
fred = Fred(api_key=api_key)

# 3. Daten abrufen: Verbraucherpreisindex (CPI) für Deutschland
# Wir nehmen den Zeitraum 2020 bis heute
print("Rufe Daten von FRED ab...")
data = fred.get_series('DEUCPIALLMINMEI', observation_start='2020-01-01')

# 4. Daten für JSON vorbereiten
# JSON mag keine speziellen Datums-Objekte, daher machen wir Text daraus
json_data = {str(date).split()[0]: value for date, value in data.items()}

# 5. Ordner 'raw_data' erstellen, falls er noch nicht da ist
if not os.path.exists('raw_data'):
    os.makedirs('raw_data')

# 6. Als JSON-Datei speichern
with open('raw_data/fred_cpi_germany.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=4)

print("Check! Die Daten liegen jetzt in raw_data/fred_cpi_germany.json")