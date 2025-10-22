"""
🎬 TEST COMANDI AVATAR - Demo Automatica
========================================
Mostra come la mente controlla automaticamente l'avatar.

Esegui: python test_avatar_comandi.py
(Assicurati che avatar_3d.py sia aperto!)
"""

import json
import time
import os

def invia_comando_avatar(emozione, azione, descrizione):
    """Invia comando all'avatar"""
    
    # Calcola parametri
    arousal = 0.7 if azione in ["cammina", "guarda"] else 0.4
    attenzione = 0.9 if azione == "guarda" else 0.6
    pattern = "░░░███████░░░" if arousal > 0.5 else "░░░░░█░░░░░"
    
    # Stato avatar
    stato = {
        'emozione': emozione,
        'azione': azione,
        'energia': 0.9,
        'attenzione': attenzione,
        'arousal': arousal,
        'pattern_neurale': pattern
    }
    
    # Salva
    os.makedirs("data", exist_ok=True)
    with open("data/avatar_stato.json", "w", encoding='utf-8') as f:
        json.dump(stato, f, indent=2)
    
    print(f"  📤 Comando inviato: {emozione.upper()} + {azione.upper()}")
    print(f"     {descrizione}")


def demo_scenario_1():
    """Scenario 1: Vede bottiglia, comando positivo"""
    print("\n" + "="*70)
    print("SCENARIO 1: 'Portami la bottiglia'")
    print("="*70)
    
    print("\n[CICLO COGNITIVO]")
    print("  👁️  Visione: bottle (87%)")
    print("  👂 Udito: 'Portami la bottiglia'")
    print("  ❤️  Emozione: POSITIVA (valenza +0.8)")
    print("  🧠 Decisione: cerca_oggetto")
    
    time.sleep(2)
    
    print("\n[AGGIORNA AVATAR]")
    invia_comando_avatar(
        emozione="felice",
        azione="guarda",
        descrizione="Omino felice che cerca la bottiglia"
    )
    
    print("\n[REAZIONE AVATAR]")
    print("  🤖 Espressione: FELICE (sorriso)")
    print("  🤖 Movimento: GUARDA (testa si muove)")
    print("  🤖 Attenzione: 90%")
    print("  🤖 Pattern: ░░░███████░░░")


def demo_scenario_2():
    """Scenario 2: Non trova oggetto, frustrazione"""
    print("\n" + "="*70)
    print("SCENARIO 2: Non trova l'oggetto")
    print("="*70)
    
    print("\n[CICLO COGNITIVO]")
    print("  👁️  Visione: nessun oggetto")
    print("  👂 Udito: 'Dov'è?'")
    print("  ❤️  Emozione: NEGATIVA (valenza -0.4)")
    print("  🧠 Decisione: mantieni_distanza")
    
    time.sleep(2)
    
    print("\n[AGGIORNA AVATAR]")
    invia_comando_avatar(
        emozione="triste",
        azione="pensa",
        descrizione="Omino confuso che pensa"
    )
    
    print("\n[REAZIONE AVATAR]")
    print("  🤖 Espressione: TRISTE (bocca giù)")
    print("  🤖 Movimento: PENSA (testa inclinata)")
    print("  🤖 Attenzione: 60%")
    print("  🤖 Pattern: ░░░░░█░░░░░")


def demo_scenario_3():
    """Scenario 3: Richiesta di avvicinarsi"""
    print("\n" + "="*70)
    print("SCENARIO 3: 'Vieni qui!'")
    print("="*70)
    
    print("\n[CICLO COGNITIVO]")
    print("  👁️  Visione: person (92%)")
    print("  👂 Udito: 'Vieni qui!'")
    print("  ❤️  Emozione: NEUTRALE (valenza +0.2)")
    print("  🧠 Decisione: avvicinati")
    
    time.sleep(2)
    
    print("\n[AGGIORNA AVATAR]")
    invia_comando_avatar(
        emozione="neutro",
        azione="cammina",
        descrizione="Omino che si avvicina"
    )
    
    print("\n[REAZIONE AVATAR]")
    print("  🤖 Espressione: NEUTRO (bocca dritta)")
    print("  🤖 Movimento: CAMMINA (braccia oscillano)")
    print("  🤖 Attenzione: 60%")
    print("  🤖 Pattern: ░░░███████░░░")


def demo_scenario_4():
    """Scenario 4: Riposo/Idle"""
    print("\n" + "="*70)
    print("SCENARIO 4: Nessun input, riposo")
    print("="*70)
    
    print("\n[CICLO COGNITIVO]")
    print("  👁️  Visione: nulla di rilevante")
    print("  👂 Udito: silenzio")
    print("  ❤️  Emozione: NEUTRALE (valenza 0.0)")
    print("  🧠 Decisione: monitora_ambiente")
    
    time.sleep(2)
    
    print("\n[AGGIORNA AVATAR]")
    invia_comando_avatar(
        emozione="neutro",
        azione="idle",
        descrizione="Omino in attesa tranquilla"
    )
    
    print("\n[REAZIONE AVATAR]")
    print("  🤖 Espressione: NEUTRO")
    print("  🤖 Movimento: IDLE (respiro lento)")
    print("  🤖 Attenzione: 50%")
    print("  🤖 Pattern: ░░░░░█░░░░░")


def main():
    print("\n" + "="*70)
    print("  🎬 DEMO COMANDI AVATAR - Sistema Automatico")
    print("="*70)
    print()
    print("[INFO] Questa demo mostra come la mente controlla l'avatar")
    print("[INFO] Assicurati che avatar_3d.py sia aperto!")
    print()
    
    risposta = input("Vuoi avviare l'avatar ora? (s/n): ").strip().lower()
    
    if risposta == 's':
        import subprocess
        import sys
        
        print("\n[AVVIO] Apertura avatar_3d.py...")
        
        if sys.platform == "win32":
            subprocess.Popen(
                ["python", "avatar_3d.py"],
                creationflags=subprocess.CREATE_NEW_CONSOLE
            )
        else:
            subprocess.Popen(["python", "avatar_3d.py"])
        
        print("[OK] Avatar avviato!")
        time.sleep(3)
    
    print("\n[START] Demo in 3 secondi...")
    time.sleep(3)
    
    # Esegui scenari
    demo_scenario_1()
    time.sleep(5)
    
    demo_scenario_2()
    time.sleep(5)
    
    demo_scenario_3()
    time.sleep(5)
    
    demo_scenario_4()
    time.sleep(3)
    
    print("\n" + "="*70)
    print("  ✅ DEMO COMPLETATA")
    print("="*70)
    print()
    print("[INFO] Hai visto come la mente controlla l'avatar!")
    print("[INFO] Nel sistema reale, questo avviene AUTOMATICAMENTE")
    print("[INFO] ad ogni ciclo cognitivo!")
    print()
    print("[NEXT] Prova il sistema completo:")
    print("  > python avvia_sistema_completo.py")
    print()


if __name__ == "__main__":
    main()



