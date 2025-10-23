#!/usr/bin/env python3
"""
🧠 AVVIA SISTEMA REALE AUTOMATICO
Con Camera e Microfono - Senza blocchi
"""

import subprocess
import sys
import time

def main():
    print("\n" + "="*70)
    print("  🧠 SISTEMA REALE CON HARDWARE - MODALITÀ AUTO")
    print("="*70)
    
    processi = []
    
    try:
        # 1. Avvia Avatar 3D
        print("\n[1/3] 🎭 Avvio Avatar 3D...")
        if sys.platform == "win32":
            p_avatar = subprocess.Popen(
                ["python", "avatar_3d.py"],
                creationflags=subprocess.CREATE_NEW_CONSOLE
            )
        else:
            p_avatar = subprocess.Popen(["python", "avatar_3d.py"])
        processi.append(("Avatar", p_avatar))
        print("      ✅ Avatar avviato")
        time.sleep(2)
        
        # 2. Avvia Dashboard
        print("\n[2/3] 📊 Avvio Dashboard...")
        if sys.platform == "win32":
            p_dashboard = subprocess.Popen(
                ["streamlit", "run", "dashboard.py"],
                creationflags=subprocess.CREATE_NEW_CONSOLE
            )
        else:
            p_dashboard = subprocess.Popen(["streamlit", "run", "dashboard.py"])
        processi.append(("Dashboard", p_dashboard))
        print("      ✅ Dashboard avviato")
        time.sleep(3)
        
        # 3. Avvia Mente AI REALE con modalità automatica
        print("\n[3/3] 🧠 Avvio Mente AI (HARDWARE REALE)...")
        print("      📷 Camera attiva")
        print("      🎤 Microfono attivo")
        if sys.platform == "win32":
            p_mente = subprocess.Popen(
                ["python", "mente_artificiale_completa.py", "--auto"],
                creationflags=subprocess.CREATE_NEW_CONSOLE
            )
        else:
            p_mente = subprocess.Popen(["python", "mente_artificiale_completa.py", "--auto"])
        processi.append(("Mente AI", p_mente))
        print("      ✅ Mente AI avviato")
        
        print("\n" + "="*70)
        print("  ✅ SISTEMA COMPLETO CON HARDWARE ATTIVO!")
        print("="*70)
        print("\n[INFO] Componenti attivi:")
        print("  • Avatar 3D → Finestra separata")
        print("  • Dashboard → http://localhost:8501")
        print("  • Mente AI → 5 cicli automatici con camera+microfono")
        print("\n[⚠️] HARDWARE ATTIVO:")
        print("  📷 Webcam accesa")
        print("  🎤 Microfono in ascolto")
        print("\n[!] Premi CTRL+C per fermare tutto\n")
        
        # Attendi
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n\n[STOP] Interruzione utente...")
        print("[SHUTDOWN] Chiusura processi...")
        for nome, processo in processi:
            try:
                processo.terminate()
                print(f"  ✅ {nome} terminato")
            except:
                pass
        
        # Spegni camera
        print("\n[CLEANUP] Rilascio camera...")
        try:
            subprocess.run(["python", "spegni_camera.py"], timeout=5)
        except:
            pass
        
        print("\n[OK] Sistema spento\n")

if __name__ == "__main__":
    main()

