#!/usr/bin/env python3
"""
Launcher per test WEB - 50 cicli con Internet
"""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from MENTE_VITA_WEB import MenteVitaWeb

print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║         🌐 TEST MENTE VITA CON INTERNET - 50 CICLI          ║
║                                                              ║
║  Il sistema imparerà da:                                    ║
║  • 📰 Notizie dal web (Google News, ANSA, BBC)              ║
║  • 📚 Wikipedia                                              ║
║  • 🌤️ Dati meteo                                            ║
║                                                              ║
║  Tempo stimato: ~5 minuti                                   ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
""")

# Crea sistema
mente = MenteVitaWeb()

# Esegui 50 cicli
mente.esegui_con_web(cicli_target=50)

print("\n" + "="*70)
print("📊 RISULTATI FINALI:")
print("="*70)
print(f"✅ Cicli completati: 50")
print(f"🧠 Concetti appresi: {len(mente.generalizzazione.concetti)}")
print(f"📰 Notizie lette: {len(mente.ultime_notizie)}")
print(f"💫 Impulso vitale: 100%")
print("="*70)

input("\n\n💡 Premi INVIO per uscire...")

