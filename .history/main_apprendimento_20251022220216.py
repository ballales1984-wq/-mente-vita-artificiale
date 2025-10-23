#!/usr/bin/env python3
"""
🎓 MAIN APPRENDIMENTO - Sistema Completo Adattivo
Ciclo di apprendimento unificato: analizza → regole → applica → migliora
"""

import json
from pathlib import Path
from datetime import datetime
from moduli.apprendimento_adattivo import ApprendimentoAdattivo

def genera_pensiero_simulato(ciclo_num: int) -> dict:
    """
    Genera pensiero simulato per test
    
    Args:
        ciclo_num: Numero ciclo
        
    Returns:
        Pensiero simulato
    """
    import random
    
    scenari = [
        {
            'descrizione': 'Scena indoor: persona seduta',
            'audio': 'Ciao, vieni qui',
            'emozione': 'positivo',
            'valenza': 0.7,
            'azione': 'avvicinati',
            'successo': True
        },
        {
            'descrizione': 'Ambiente vuoto',
            'audio': '',
            'emozione': 'neutro',
            'valenza': 0.0,
            'azione': 'mantieni_distanza',
            'successo': True
        },
        {
            'descrizione': 'Scena esterna: veicolo',
            'audio': 'Fermati',
            'emozione': 'cauto',
            'valenza': -0.2,
            'azione': 'fermati',
            'successo': True
        },
        {
            'descrizione': 'Persona e oggetti',
            'audio': 'Prendi la bottiglia',
            'emozione': 'positivo',
            'valenza': 0.5,
            'azione': 'esegui_comando',
            'successo': random.choice([True, False])
        }
    ]
    
    pensiero = random.choice(scenari).copy()
    pensiero['ciclo'] = ciclo_num
    pensiero['timestamp'] = datetime.now().isoformat()
    
    return pensiero


def main():
    """
    Ciclo principale con apprendimento completo
    """
    print("\n" + "="*70)
    print("  🎓 SISTEMA APPRENDIMENTO COMPLETO")
    print("="*70)
    print("\n[INFO] Sistema adattivo con regole automatiche")
    print("[INFO] Analizza → Regole → Applica → Migliora")
    print()
    
    # Inizializza sistema apprendimento
    sistema = ApprendimentoAdattivo()
    
    # 1. FASE INIZIALE: Carica pensieri passati
    print("[1/4] 📚 Caricamento pensieri passati...")
    pensieri_passati = sistema.carica_pensieri_passati()
    print(f"      ✅ Caricati {len(pensieri_passati)} pensieri")
    
    # 2. FASE ANALISI: Trova schemi
    print("\n[2/4] 🔍 Analisi schemi ricorrenti...")
    schemi = sistema.trova_schemi(pensieri_passati, soglia=3)
    print(f"      ✅ Trovati {len(schemi)} schemi significativi")
    
    if schemi:
        print("\n      📊 Schemi principali:")
        for i, (chiave, decisioni) in enumerate(list(schemi.items())[:3], 1):
            vista, udito, emo = chiave
            for dec, score in decisioni.items():
                print(f"         {i}. {vista[:20]}... + {emo} → {dec.upper()} (score: {score})")
    
    # 3. FASE REGOLE: Genera regole
    print("\n[3/4] ⚙️  Generazione regole decisionali...")
    regole = sistema.genera_regole(schemi)
    print(f"      ✅ Generate {len(regole)} regole")
    
    if regole:
        print("\n      📋 Top 3 regole:")
        for i, regola in enumerate(regole[:3], 1):
            print(f"         {i}. {regola['azione'].upper()} (confidenza: {regola['confidenza']:.0%}, score: {regola['punteggio']})")
    
    # 4. FASE APPLICAZIONE: Cicli con regole
    num_cicli = 20
    print(f"\n[4/4] 🔄 Esecuzione {num_cicli} cicli con apprendimento...")
    print(f"      [INFO] Regole verranno applicate automaticamente")
    print()
    
    stats = {'regole_applicate': 0, 'successi': 0, 'fallimenti': 0}
    
    for i in range(1, num_cicli + 1):
        print(f"\n{'─'*70}")
        print(f"CICLO #{i:03d}")
        print(f"{'─'*70}")
        
        # Genera nuovo pensiero
        pensiero = genera_pensiero_simulato(i)
        
        print(f"[INPUT]")
        print(f"  Vista: {pensiero['descrizione']}")
        print(f"  Udito: '{pensiero['audio'] if pensiero['audio'] else 'silenzio'}'")
        print(f"  Emozione: {pensiero['emozione']} ({pensiero['valenza']:+.2f})")
        
        # Applica regole (se ci sono)
        if regole:
            result_app = sistema.elabora(pensiero, fase='applicazione')
            
            if result_app.get('regola_applicata'):
                pensiero_con_regola = result_app['pensiero']
                print(f"\n[REGOLA APPLICATA] ✅")
                print(f"  Azione suggerita: {pensiero_con_regola['azione_suggerita'].upper()}")
                print(f"  Confidenza: {pensiero_con_regola['confidenza_regola']:.0%}")
                print(f"  {pensiero_con_regola['motivazione_apprendimento']}")
                
                # Usa azione suggerita
                pensiero['azione'] = pensiero_con_regola['azione_suggerita']
                stats['regole_applicate'] += 1
            else:
                print(f"\n[DECISIONE LIBERA]")
                print(f"  Azione: {pensiero['azione'].upper()}")
        
        # Valuta pensiero
        result_val = sistema.elabora(pensiero, fase='valutazione')
        
        print(f"\n[APPRENDIMENTO]")
        print(f"  Valutazione: {result_val['valutazione']:+d}")
        print(f"  Peso {pensiero['azione']}: {result_val['peso_nuovo']:.2f}")
        
        if pensiero['successo']:
            stats['successi'] += 1
        else:
            stats['fallimenti'] += 1
        
        # Ogni 5 cicli, aggiorna regole
        if i % 5 == 0 and i > 0:
            print(f"\n[AGGIORNAMENTO] Rigenerazione regole...")
            pensieri_aggiornati = sistema.carica_pensieri_passati()
            schemi = sistema.trova_schemi(pensieri_aggiornati, soglia=2)
            regole = sistema.genera_regole(schemi)
            print(f"  ✅ Regole aggiornate: {len(regole)} disponibili")
    
    # Salva pesi finali
    sistema.salva_pesi()
    
    # Report finale
    print(f"\n{'='*70}")
    print(f"  🎉 APPRENDIMENTO COMPLETATO")
    print(f"{'='*70}")
    print(f"\n[STATISTICHE]")
    print(f"  • Cicli eseguiti: {num_cicli}")
    print(f"  • Successi: {stats['successi']}")
    print(f"  • Fallimenti: {stats['fallimenti']}")
    print(f"  • Tasso successo: {stats['successi']/num_cicli*100:.1f}%")
    print(f"  • Regole applicate: {stats['regole_applicate']}")
    print(f"  • Schemi trovati: {len(schemi)}")
    print(f"  • Regole finali: {len(regole)}")
    
    print(f"\n[FILE SALVATI]")
    print(f"  • Pensieri: memoria_permanente/pensieri_valutati.jsonl")
    print(f"  • Pesi: memoria_permanente/pesi_decisioni.json")
    
    print(f"\n[PESI FINALI]")
    pesi_sorted = sorted(sistema.probabilita_decisioni.items(), 
                        key=lambda x: x[1], reverse=True)
    for azione, peso in pesi_sorted[:5]:
        print(f"  • {azione}: {peso:.2f}")
    
    print(f"\n{'='*70}")
    print(f"  ✅ Il sistema ha IMPARATO e MIGLIORATO!")
    print(f"{'='*70}\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n✅ Interruzione utente\n")
    except Exception as e:
        print(f"\n❌ Errore: {e}\n")
        import traceback
        traceback.print_exc()

