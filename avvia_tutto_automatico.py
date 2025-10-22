"""
🚀 AVVIA TUTTO - Sistema Automatico
====================================
Avvia Avatar + Dashboard + Mente senza blocchi.
"""

import subprocess
import sys
import time

print("\n" + "="*70)
print("  🚀 AVVIO SISTEMA COMPLETO")
print("="*70 + "\n")

# 1. Avatar
print("[1/3] Avvio Avatar 3D...")
if sys.platform == "win32":
    subprocess.Popen(["python", "avatar_3d.py"], 
                     creationflags=subprocess.CREATE_NEW_CONSOLE)
else:
    subprocess.Popen(["python", "avatar_3d.py"])
time.sleep(2)
print("      ✅ Avatar avviato\n")

# 2. Dashboard
print("[2/3] Avvio Dashboard Web...")
subprocess.Popen([sys.executable, "-m", "streamlit", "run", "dashboard.py"])
time.sleep(3)
print("      ✅ Dashboard: http://localhost:8501\n")

# 3. Demo
print("[3/3] Avvio Simulazione Demo...")
if sys.platform == "win32":
    subprocess.Popen(["python", "mente_ai_demo.py"],
                     creationflags=subprocess.CREATE_NEW_CONSOLE)
else:
    subprocess.Popen(["python", "mente_ai_demo.py"])
time.sleep(2)
print("      ✅ Demo avviata\n")

print("="*70)
print("  ✅ TUTTO AVVIATO!")
print("="*70)
print()
print("Componenti attivi:")
print("  🤖 Avatar 3D (finestra)")
print("  📊 Dashboard (http://localhost:8501)")
print("  🧠 Simulazione (console)")
print()
print("Apri browser su: http://localhost:8501")
print()
print("="*70)



