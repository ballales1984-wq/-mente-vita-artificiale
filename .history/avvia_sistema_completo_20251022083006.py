"""
🚀 LAUNCHER SISTEMA COMPLETO
============================
Avvia TUTTO insieme:
- Mente Artificiale
- Avatar 3D
- Dashboard Streamlit

Autore: Alessio + Cursor AI
"""

import subprocess
import sys
import time
import os

def banner():
    """Mostra banner"""
    print("\n" + "="*70)
    print("  🧠⚡🤖 SISTEMA COMPLETO - Mente Artificiale + Avatar")
    print("="*70 + "\n")

def controlla_dipendenze():
    """Controlla dipendenze necessarie"""
    print("[1/4] Controllo dipendenze...")
    
    dipendenze_ok = True
    
    # Pygame
    try:
        import pygame
        print("  ✅ pygame")
    except:
        print("  ❌ pygame - installa con: pip install pygame")
        dipendenze_ok = False
    
    # Streamlit
    try:
        import streamlit
        print("  ✅ streamlit")
    except:
        print("  ❌ streamlit - installa con: pip install streamlit")
        dipendenze_ok = False
    
    # OpenCV
    try:
        import cv2
        print("  ✅ opencv")
    except:
        print("  ⚠️  opencv - opzionale ma consigliato")
    
    print()
    
    if not dipendenze_ok:
        print("[!] Alcune dipendenze mancano!")
        print("[!] Installa con: pip install pygame streamlit")
        risposta = input("\nContinuo comunque? (s/n): ")
        if risposta.lower() != 's':
            return False
    
    return True

def prepara_ambiente():
    """Prepara ambiente"""
    print("[2/4] Preparazione ambiente...")
    
    # Crea directory data
    os.makedirs("data", exist_ok=True)
    print("  ✅ Directory data/ pronta")
    
    # Crea file stato avatar iniziale
    import json
    stato_iniziale = {
        'emozione': 'neutro',
        'azione': 'idle',
        'energia': 1.0,
        'attenzione': 0.5,
        'arousal': 0.5,
        'pattern_neurale': '0000000000'
    }
    
    with open("data/avatar_stato.json", "w", encoding='utf-8') as f:
        json.dump(stato_iniziale, f, indent=2)
    
    print("  ✅ File avatar_stato.json creato")
    print()

def avvia_avatar():
    """Avvia avatar 3D"""
    print("[3/4] Avvio Avatar 3D...")
    
    try:
        if sys.platform == "win32":
            # Windows
            processo = subprocess.Popen(
                ["python", "avatar_3d.py"],
                creationflags=subprocess.CREATE_NEW_CONSOLE
            )
        else:
            # Linux/Mac
            processo = subprocess.Popen(
                ["python", "avatar_3d.py"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
        
        print("  ✅ Avatar avviato (finestra separata)")
        time.sleep(2)
        return processo
    
    except Exception as e:
        print(f"  ❌ Errore: {e}")
        return None

def avvia_dashboard():
    """Avvia dashboard Streamlit"""
    print("[4/4] Avvio Dashboard...")
    
    try:
        if sys.platform == "win32":
            # Windows
            processo = subprocess.Popen(
                [sys.executable, "-m", "streamlit", "run", "dashboard.py"],
                creationflags=subprocess.CREATE_NEW_CONSOLE
            )
        else:
            # Linux/Mac
            processo = subprocess.Popen(
                [sys.executable, "-m", "streamlit", "run", "dashboard.py"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
        
        print("  ✅ Dashboard avviata")
        print("  📊 Apri browser su: http://localhost:8501")
        time.sleep(2)
        return processo
    
    except Exception as e:
        print(f"  ❌ Errore: {e}")
        return None

def avvia_mente():
    """Avvia mente artificiale"""
    print("\n" + "="*70)
    print("  🧠 AVVIO MENTE ARTIFICIALE")
    print("="*70 + "\n")
    
    print("[INFO] La mente controlla l'avatar e aggiorna la dashboard")
    print("[INFO] Ogni ciclo cognitivo:")
    print("  → Percepisce (camera + microfono)")
    print("  → Ricorda (memoria intelligente)")
    print("  → Decide (ragionamento)")
    print("  → Agisce (motoria)")
    print("  → Impara (rete neurale)")
    print("  → AGGIORNA AVATAR (espressione + movimento)")
    print()
    
    # Importa e avvia
    try:
        from mente_artificiale_completa import MenteArtificialeCompleta, ConfigurazioneCompleta
        
        config = ConfigurazioneCompleta()
        config.usa_camera_reale = True
        config.usa_microfono_reale = True
        
        mente = MenteArtificialeCompleta(config)
        
        # Menu veloce
        print("\n[MENU] Modalità:")
        print("  1. Ciclo singolo")
        print("  2. Sessione 5 cicli (automatica)")
        print("  3. Sessione continua (CTRL+C per fermare)")
        
        scelta = input("\n>> Scelta (1-3): ").strip()
        
        if scelta == "1":
            mente.ciclo_cognitivo()
        elif scelta == "2":
            mente.esegui_sessione(num_cicli=5, interattivo=False)
        elif scelta == "3":
            mente.esegui_sessione(num_cicli=999, interattivo=False)
        else:
            print("[!] Scelta non valida")
        
        mente.chiudi()
    
    except KeyboardInterrupt:
        print("\n\n[!] Interruzione manuale")
    
    except Exception as e:
        print(f"\n[ERROR] {e}")
        import traceback
        traceback.print_exc()

def main():
    """Main"""
    banner()
    
    # Controlli
    if not controlla_dipendenze():
        return
    
    prepara_ambiente()
    
    # Avvia componenti
    processo_avatar = avvia_avatar()
    processo_dashboard = avvia_dashboard()
    
    # Pausa per dare tempo di aprire
    print("\n[INFO] Componenti in avvio...")
    print("[INFO] Attendi apertura finestre...")
    time.sleep(3)
    
    # Avvia mente (blocca finché non finisce)
    try:
        avvia_mente()
    finally:
        # Cleanup
        print("\n[INFO] Chiusura componenti...")
        
        if processo_avatar:
            try:
                processo_avatar.terminate()
                print("  ✅ Avatar chiuso")
            except:
                pass
        
        if processo_dashboard:
            try:
                processo_dashboard.terminate()
                print("  ✅ Dashboard chiusa")
            except:
                pass
        
        print("\n[OK] Sistema spento\n")

if __name__ == "__main__":
    main()

