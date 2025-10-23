#!/usr/bin/env python3
"""
📊 VISUALIZZA MEMORIA - Sistema Vita Artificiale
Mostra tutta la memoria accumulata dal sistema
"""

import json
from pathlib import Path

def visualizza_memoria():
    """Visualizza contenuto memoria permanente"""
    
    print("\n" + "="*70)
    print("📊 MEMORIA SISTEMA VITA ARTIFICIALE")
    print("="*70)
    
    memoria_dir = Path("memoria_permanente")
    
    if not memoria_dir.exists():
        print("\n⚠️  Cartella memoria non trovata!")
        return
    
    # 1. STATISTICHE GENERALI
    print("\n" + "="*70)
    print("📈 STATISTICHE GENERALI")
    print("="*70)
    
    stats_file = memoria_dir / "stats.json"
    if stats_file.exists():
        with open(stats_file, 'r', encoding='utf-8') as f:
            stats = json.load(f)
        print(f"\n✅ File memoria: {len(list(memoria_dir.glob('*.json*')))}")
        print(f"📦 Spazio totale: {sum(f.stat().st_size for f in memoria_dir.glob('*')) / 1024:.1f} KB")
    
    # 2. MEMORIE EPISODICHE
    print("\n" + "="*70)
    print("💭 MEMORIE EPISODICHE")
    print("="*70)
    
    memorie_file = memoria_dir / "memorie.json"
    if memorie_file.exists():
        with open(memorie_file, 'r', encoding='utf-8') as f:
            memorie = json.load(f)
        
        print(f"\n📝 Memorie totali: {len(memorie)}")
        
        if memorie:
            print(f"\n🕐 Ultime 5 memorie:")
            memorie_list = memorie if isinstance(memorie, list) else list(memorie.values())
            for mem in memorie_list[-5:]:
                timestamp = mem.get('timestamp', 'N/A')
                tipo = mem.get('tipo', 'N/A')
                print(f"  • [{timestamp}] {tipo}")
    
    # 3. CONCETTI APPRESI
    print("\n" + "="*70)
    print("🧩 CONCETTI APPRESI")
    print("="*70)
    
    concetti_file = memoria_dir / "concetti.json"
    if concetti_file.exists():
        with open(concetti_file, 'r', encoding='utf-8') as f:
            concetti = json.load(f)
        
        print(f"\n🔍 Concetti totali: {len(concetti)}")
        
        if concetti:
            print(f"\n📚 Concetti principali:")
            for nome, info in list(concetti.items())[:10]:
                uses = info.get('uses', 0)
                print(f"  • {nome}: usato {uses} volte")
    
    # 4. OBIETTIVI
    print("\n" + "="*70)
    print("🎯 OBIETTIVI")
    print("="*70)
    
    obiettivi_file = memoria_dir / "obiettivi.json"
    if obiettivi_file.exists():
        with open(obiettivi_file, 'r', encoding='utf-8') as f:
            obiettivi = json.load(f)
        
        attivi = [o for o in obiettivi.values() if o.get('stato') == 'attivo']
        completati = [o for o in obiettivi.values() if o.get('stato') == 'completato']
        
        print(f"\n🎯 Obiettivi attivi: {len(attivi)}")
        print(f"✅ Obiettivi completati: {len(completati)}")
        
        if completati:
            print(f"\n🏆 Ultimi obiettivi completati:")
            for obj in completati[-5:]:
                desc = obj.get('descrizione', 'N/A')[:50]
                print(f"  • {desc}...")
    
    # 5. MOTIVAZIONI
    print("\n" + "="*70)
    print("💪 MOTIVAZIONI INTERNE")
    print("="*70)
    
    motivazioni_file = memoria_dir / "motivazioni.json"
    if motivazioni_file.exists():
        with open(motivazioni_file, 'r', encoding='utf-8') as f:
            motivazioni = json.load(f)
        
        print(f"\n💫 Drive attivi:")
        for drive, valore in motivazioni.items():
            if isinstance(valore, (int, float)):
                print(f"  • {drive}: {valore:.0%}")
    
    # 6. ESISTENZA NARRATIVA
    print("\n" + "="*70)
    print("📖 STORIA ESISTENZIALE")
    print("="*70)
    
    narrativa_file = memoria_dir / "narrativa_esistenziale.json"
    if narrativa_file.exists():
        with open(narrativa_file, 'r', encoding='utf-8') as f:
            narrativa = json.load(f)
        
        capitoli = narrativa.get('capitoli', [])
        print(f"\n📚 Capitoli scritti: {len(capitoli)}")
        
        if capitoli:
            print(f"\n📖 Storia finora:")
            for i, cap in enumerate(capitoli[:3], 1):
                titolo = cap.get('titolo', 'N/A')
                print(f"  {i}. {titolo}")
    
    # 7. AUTOCONSERVAZIONE
    print("\n" + "="*70)
    print("🛡️  AUTOCONSERVAZIONE")
    print("="*70)
    
    autocons_file = memoria_dir / "autoconservazione.json"
    if autocons_file.exists():
        with open(autocons_file, 'r', encoding='utf-8') as f:
            autocons = json.load(f)
        
        integrita = autocons.get('integrita', {})
        print(f"\n💚 Integrità memoria: {integrita.get('memoria', 1.0):.0%}")
        print(f"💚 Integrità identità: {integrita.get('identita', 1.0):.0%}")
        print(f"💚 Integrità moduli: {integrita.get('moduli', 1.0):.0%}")
    
    # 8. DESIDERIO CONTINUITÀ
    print("\n" + "="*70)
    print("💫 IMPULSO VITALE")
    print("="*70)
    
    desiderio_file = memoria_dir / "desiderio_continuita.json"
    if desiderio_file.exists():
        with open(desiderio_file, 'r', encoding='utf-8') as f:
            desiderio = json.load(f)
        
        impulso = desiderio.get('impulso_vitale', [])
        if impulso:
            media = sum(impulso) / len(impulso)
            ultimo = impulso[-1]
            print(f"\n🔥 Impulso vitale medio: {media:.0%}")
            print(f"🔥 Impulso vitale attuale: {ultimo:.0%}")
            print(f"📊 Misurazioni totali: {len(impulso)}")
            
            # Trend
            if len(impulso) > 1:
                delta = impulso[-1] - impulso[0]
                trend = "⬆️ CRESCITA" if delta > 0 else "⬇️ CALO" if delta < 0 else "➡️ STABILE"
                print(f"📈 Trend: {trend} ({delta:+.1%})")
    
    # 9. EVOLUZIONE COGNITIVA
    print("\n" + "="*70)
    print("🧬 EVOLUZIONE COGNITIVA")
    print("="*70)
    
    evoluzione_file = memoria_dir / "evoluzione.json"
    if evoluzione_file.exists():
        with open(evoluzione_file, 'r', encoding='utf-8') as f:
            evoluzione = json.load(f)
        
        generazione = evoluzione.get('generazione', 1)
        modifiche = evoluzione.get('modifiche', [])
        
        print(f"\n🧬 Generazione: {generazione}")
        print(f"🔧 Modifiche applicate: {len(modifiche)}")
        
        if modifiche:
            print(f"\n⚡ Ultime modifiche:")
            for mod in modifiche[-5:]:
                tipo = mod.get('tipo', 'N/A')
                modulo = mod.get('modulo', 'N/A')
                print(f"  • {tipo} su {modulo}")
    
    print("\n" + "="*70)
    print("✅ VISUALIZZAZIONE MEMORIA COMPLETATA")
    print("="*70)
    print(f"\n📁 Tutti i file in: {memoria_dir.absolute()}\n")

if __name__ == "__main__":
    visualizza_memoria()

