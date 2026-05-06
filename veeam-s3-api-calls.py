import pandas as pd
import matplotlib.pyplot as plt
import json
import glob
import os

# Folder mit den Log Files
log_directory = '/Users/fbanaszak/Downloads/veeamapi' 
# Suche nach .log, .json and .jsonl files
file_patterns = ["*.log", "*.jsonl", "*.json"]

all_events = []

print("--- Starting Analysis ---")

# Alle Files im angegebenen Directory durchsuchen
files_to_process = []
for pattern in file_patterns:
    files_to_process.extend(glob.glob(os.path.join(log_directory, pattern)))

if not files_to_process:
    print(f"Keine Files mit {file_patterns} in '{log_directory}' gefunden.")
else:
    print(f"{len(files_to_process)} Files gefunden - jetzt lese Ich die mal ein....")
    
    for file_path in files_to_process:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line: continue
                try:
                    obj = json.loads(line)
                    if 'eventName' in obj:
                        all_events.append(obj['eventName'])
                except json.JSONDecodeError:
                    # Falls JSON falsch formatiert ist wird hier ignoriert
                    continue

# Ergebnisse und alles was eingelesen wird, wird jetzt verarbeitet in nen Chart
if not all_events:
    print("No valid 'eventName' entries foud.")
else:
    # Panda Series Konvertierung, braucht Python anscheinend um besser zu zählen, keine Ahnung wieviele Stunden ich hier verschwendet habe...
    series = pd.Series(all_events)
    counts = series.value_counts()

    print(f"\nErgebnis der Zählung:")
    print(counts)

    # Bar Chart generieren 
    plt.figure(figsize=(12, 8))
    
    # Bar Chart
    counts.plot(kind='bar', color='steelblue', edgecolor='black')
    
    plt.title(f'Verteilung aller API-Calls ({len(all_events)} Events insgesamt)', fontsize=14)
    plt.xlabel('API Call (eventName)', fontsize=12)
    plt.ylabel('Häufigkeit', fontsize=12)
    
    # Damit die Namen der API Calls nicht überlappen
    plt.xticks(rotation=45, ha='right')
    
    # Gitter für bessere Lesbarkeit
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    
    # Speichern oder Anzeigen
    # plt.savefig('api_calls_chart.png') # Optional: als Bild speichern
    plt.show()