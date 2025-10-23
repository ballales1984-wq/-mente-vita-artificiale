#!/usr/bin/env python3
"""
Monitor Live delle scoperte dell'AGI
Mostra cosa sta imparando in tempo reale
"""
import json
import os
import time
from datetime import datetime

def leggi_concetti():
    """Legge i concetti appresi"""
    path = "memoria_permanente/concetti.json"
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def leggi_coscienza():
    """Legge lo stato di coscienza"""
    path = "memoria_permanente/coscienza.json"
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def mostra_report():
    """Mostra report live"""
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("="*70)
    print("🔴 MONITOR LIVE AGI - Scoperte in Tempo Reale")
    print("="*70)
    print(f"⏰ Aggiornato: {datetime.now().strftime('%H:%M:%S')}")
    print()
    
    # Leggi dati
    concetti = leggi_concetti()
    coscienza = leggi_coscienza()
    
    print(f"📊 STATISTICHE:")
    print(f"  🧠 Concetti totali: {len(concetti)}")
    print(f"  🌟 Cicli vissuti: {coscienza.get('cicli_vissuti', 0)}")
    print(f"  💫 Impulso vitale: {coscienza.get('impulso_vitale_corrente', 100):.0f}%")
    print()
    
    # Ultimi 5 concetti
    print(f"📚 ULTIMI 5 CONCETTI APPRESI:")
    print("-" * 70)
    
    concetti_sorted = sorted(
        concetti.items(),
        key=lambda x: x[1].get('data_creazione', ''),
        reverse=True
    )[:5]
    
    for i, (nome, dati) in enumerate(concetti_sorted, 1):
        tipo = dati.get('caratteristiche', {}).get('tipo', 'base')
        fonte = dati.get('caratteristiche', {}).get('fonte', 'simulazione')
        data = dati.get('data_creazione', '')[:19] if 'data_creazione' in dati else 'N/A'
        
        if tipo == 'notizia':
            parole = dati.get('caratteristiche', {}).get('parole_chiave', '')
            print(f"  {i}. 📰 {nome}")
            print(f"     Parole: {parole}")
            print(f"     Fonte: {fonte}")
            print(f"     Quando: {data}")
        else:
            print(f"  {i}. 🤖 {nome}")
            print(f"     Tipo: comportamento sociale")
            print(f"     Quando: {data}")
        print()
    
    # Identità e riflessioni
    if 'identita' in coscienza:
        print(f"🌟 IDENTITÀ AGI:")
        print(f'  "{coscienza["identita"]}"')
        print()
    
    if 'scopo' in coscienza:
        print(f"🎯 SCOPO:")
        print(f'  "{coscienza["scopo"]}"')
        print()
    
    # Dichiarazioni recenti
    if 'riflessioni_recenti' in coscienza and coscienza['riflessioni_recenti']:
        print(f"💭 ULTIMA RIFLESSIONE:")
        print(f'  "{coscienza["riflessioni_recenti"][-1]}"')
        print()
    
    print("="*70)
    print("💡 Premi CTRL+C per uscire | Aggiornamento ogni 5 secondi")
    print("="*70)

if __name__ == "__main__":
    print("🚀 Avvio monitor live AGI...")
    time.sleep(1)
    
    try:
        while True:
            mostra_report()
            time.sleep(5)  # Aggiorna ogni 5 secondi
    except KeyboardInterrupt:
        print("\n\n✅ Monitor terminato!")
        print("📊 L'AGI continua a vivere in background...")

