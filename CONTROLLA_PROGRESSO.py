#!/usr/bin/env python3
"""Controlla progresso AUTO-LEARNING"""
import json
from pathlib import Path
from datetime import datetime

checkpoint_path = Path("checkpoints/auto_learning_checkpoint.json")

print("\n" + "="*70)
print("📊 MONITOR PROGRESSO AUTO-LEARNING")
print("="*70)

if not checkpoint_path.exists():
    print("\n⚠️  Nessun checkpoint trovato!")
    print("   Il sistema deve ancora salvare il primo checkpoint (100 cicli)\n")
else:
    try:
        with open(checkpoint_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        ciclo = data.get('ciclo_corrente', 0)
        timestamp = data.get('timestamp', '')
        stats = data.get('stats', {})
        impulsi = data.get('impulsi_vitali', {})
        obiettivi = data.get('obiettivi_attivi', 0)
        concetti = data.get('concetti_appresi', 0)
        ram = data.get('memoria_ram_percent', 0)
        
        print(f"\n🔢 CICLI:")
        print(f"   Completati: {ciclo:,}")
        print(f"   Ultimo salvataggio: {timestamp[:19]}")
        
        print(f"\n💫 IMPULSO VITALE:")
        if impulsi:
            for nome, valore in impulsi.items():
                print(f"   • {nome:15s}: {valore:.0%}")
            impulso_medio = sum(impulsi.values()) / len(impulsi)
            print(f"   ━━━━━━━━━━━━━━━━━━━")
            print(f"   MEDIO: {impulso_medio:.0%}")
        
        print(f"\n🎯 APPRENDIMENTO:")
        print(f"   • Obiettivi attivi: {obiettivi}")
        print(f"   • Concetti appresi: {concetti}")
        
        print(f"\n🧠 SISTEMA:")
        print(f"   • RAM: {ram:.0f}%")
        
        # Stats impulso vitale
        impulsi_storia = stats.get('impulso_vitale', [])
        if impulsi_storia and len(impulsi_storia) > 1:
            impulso_iniziale = impulsi_storia[0]
            impulso_finale = impulsi_storia[-1]
            delta = impulso_finale - impulso_iniziale
            
            print(f"\n📈 EVOLUZIONE IMPULSO:")
            print(f"   Iniziale: {impulso_iniziale:.0%}")
            print(f"   Attuale:  {impulso_finale:.0%}")
            print(f"   Delta:    {delta:+.1%}")
        
        # Azioni
        azioni = stats.get('azioni', {})
        if azioni:
            print(f"\n🦾 AZIONI PIÙ FREQUENTI:")
            top_azioni = sorted(azioni.items(), key=lambda x: x[1], reverse=True)[:3]
            for azione, count in top_azioni:
                percent = count / ciclo * 100 if ciclo > 0 else 0
                print(f"   • {azione:20s}: {count:5,} ({percent:5.1f}%)")
        
        print("\n" + "="*70)
        print("✅ Checkpoint caricato con successo!")
        print("="*70 + "\n")
        
    except Exception as e:
        print(f"\n❌ Errore lettura checkpoint: {e}\n")

print("💡 Esegui di nuovo per aggiornare i dati!\n")

