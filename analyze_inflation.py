import json
import pandas as pd

# 1. Daten laden
with open('raw_data/eurostat_ppi_dairy.json', 'r') as f:
    ppi_data = json.load(f)
with open('raw_data/eurostat_cpi_dairy.json', 'r') as f:
    cpi_data = json.load(f)

# 2. Hilfsfunktion zum Extrahieren der Zeitreihen
def extract_series(data):
    indices = data['dimension']['time']['category']['index']
    values = data['value']
    # Wir mappen den Index auf das Datum und den Wert
    series = {date: values.get(str(idx)) for date, idx in indices.items()}
    return series

ppi_series = extract_series(ppi_data)
cpi_series = extract_series(cpi_data)

# 3. In ein Pandas DataFrame umwandeln
df_ppi = pd.DataFrame.from_dict(ppi_series, orient='index', columns=['PPI_Industry'])
df_cpi = pd.DataFrame.from_dict(cpi_series, orient='index', columns=['CPI_Consumer'])

# 4. Zusammenführen (nur Monate, die in beiden vorkommen)
df_combined = df_ppi.join(df_cpi, how='inner').dropna()

# 5. Speichern und Anzeigen
df_combined.to_csv('processed_data_comparison.csv')
print("Kombinierte Daten (Vorschau der letzten 12 Monate):")
print(df_combined.tail(12))

# Berechnung der Differenz (Gap)
df_combined['Price_Gap'] = df_combined['CPI_Consumer'] - df_combined['PPI_Industry']
print("\nDurchschnittlicher Price Gap in den letzten Monaten:")
print(df_combined['Price_Gap'].tail(5))