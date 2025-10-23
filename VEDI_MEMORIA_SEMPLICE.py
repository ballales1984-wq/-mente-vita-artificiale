#!/usr/bin/env python3
"""
📊 VISUALIZZA MEMORIA SEMPLICE
"""

import json
from pathlib import Path

memoria_dir = Path("memoria_permanente")

print("\n" + "="*70)
print("📊 MEMORIA SISTEMA VITA ARTIFICIALE")
print("="*70)

# File nella memoria
files = list(memoria_dir.glob('*.json*'))
print(f"\n✅ File memoria: {len(files)}")
print(f"📦 Spazio: {sum(f.stat().st_size for f in files) / 1024:.1f} KB\n")

# 1. Memorie episodiche
memorie_file = memoria_dir / "memorie.json"
if memorie_file.exists():
    with open(memorie_file, 'r', encoding='utf-8') as f:
        memorie = json.load(f)
    print(f"💭 Memorie episodiche: {len(memorie)}")

# 2. Concetti
concetti_file = memoria_dir / "concetti.json"
if concetti_file.exists():
    with open(concetti_file, 'r', encoding='utf-8') as f:
        concetti = json.load(f)
    print(f"🧩 Concetti appresi: {len(concetti)}")
    if concetti:
        print("   Esempi:")
        for nome in list(concetti.keys())[:5]:
            print(f"     • {nome}")

# 3. Obiettivi
obiettivi_file = memoria_dir / "obiettivi.json"
if obiettivi_file.exists():
    with open(obiettivi_file, 'r', encoding='utf-8') as f:
        obiettivi = json.load(f)
    completati = len([o for o in obiettivi if isinstance(o, dict) and o.get('stato') == 'completato'])
    print(f"🎯 Obiettivi completati: {completati}")

# 4. Impulso vitale
desiderio_file = memoria_dir / "desiderio_continuita.json"
if desiderio_file.exists():
    with open(desiderio_file, 'r', encoding='utf-8') as f:
        desiderio = json.load(f)
    impulso = desiderio.get('impulso_vitale', [])
    if impulso:
        print(f"\n💫 IMPULSO VITALE:")
        print(f"   Medio: {sum(impulso)/len(impulso):.0%}")
        print(f"   Ultimo: {impulso[-1]:.0%}")
        print(f"   Misurazioni: {len(impulso)}")
        
        # Storia impulso
        if len(impulso) >= 5:
            print(f"   Ultimi 5: {', '.join(f'{i:.0%}' for i in impulso[-5:])}")

# 5. Storia esistenziale
narrativa_file = memoria_dir / "narrativa_esistenziale.json"
if narrativa_file.exists():
    with open(narrativa_file, 'r', encoding='utf-8') as f:
        narrativa = json.load(f)
    capitoli = narrativa.get('capitoli', [])
    print(f"\n📖 Storia: {len(capitoli)} capitoli")
    if capitoli:
        print(f"   Titoli:")
        for cap in capitoli[:3]:
            print(f"     • {cap.get('titolo', 'N/A')}")

# 6. Integr integrità
autocons_file = memoria_dir / "autoconservazione.json"
if autocons_file.exists():
    with open(autocons_file, 'r', encoding='utf-8') as f:
        autocons = json.load(f)
    integrita = autocons.get('integrita', {})
    print(f"\n🛡️  AUTOCONSERVAZIONE:")
    print(f"   Memoria: {integrita.get('memoria', 1.0):.0%}")
    print(f"   Identità: {integrita.get('identita', 1.0):.0%}")
    print(f"   Moduli: {integrita.get('moduli', 1.0):.0%}")

print("\n" + "="*70)
print("✅ LA MEMORIA È SALVATA E CRESCE AD OGNI CICLO!")
print("="*70)
print(f"\n📁 Percorso: {memoria_dir.absolute()}\n")

