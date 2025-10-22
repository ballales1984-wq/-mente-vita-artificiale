"""
🔊 TEST VOCE SINTETICA
======================
Testa il sistema Text-to-Speech.

Esegui: python test_voce.py
"""

import pyttsx3

print("="*70)
print("  🔊 TEST VOCE SINTETICA")
print("="*70)
print()

# Inizializza engine
print("[1/3] Inizializzazione motore TTS...")
engine = pyttsx3.init()

# Configura
engine.setProperty('rate', 150)    # Velocità (default: 200)
engine.setProperty('volume', 0.9)  # Volume (0-1)

print("      ✅ Motore inizializzato")
print()

# Lista voci disponibili
print("[2/3] Voci disponibili:")
voices = engine.getProperty('voices')

for i, voice in enumerate(voices[:5]):  # Prime 5
    print(f"  [{i}] {voice.name}")
    if 'italian' in voice.name.lower():
        print(f"      ← Italiana!")

print()

# Test voce
print("[3/3] Test voce...")
print()

frasi_test = [
    "Ciao! Sono la mente artificiale modulare.",
    "Sto percependo l'ambiente con la mia camera.",
    "Ho rilevato una persona.",
    "Sto cercando la bottiglia come richiesto.",
    "Sistema operativo al cento percento."
]

for i, frase in enumerate(frasi_test, 1):
    print(f"  [{i}] '{frase}'")
    engine.say(frase)
    engine.runAndWait()
    
    if i < len(frasi_test):
        import time
        time.sleep(0.5)

print()
print("="*70)
print("  ✅ TEST COMPLETATO")
print("="*70)
print()
print("[INFO] La voce funziona!")
print("[INFO] Ora la mente può parlare!")
print()
print("[NEXT] Usa il sistema completo con voce:")
print("  > python mente_artificiale_completa.py")
print()



