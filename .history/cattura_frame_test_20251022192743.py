#!/usr/bin/env python3
"""
📷 Test Cattura Frame - Salva permanentemente
"""

import cv2
import time
from datetime import datetime

print("\n" + "="*70)
print("  📷 TEST CATTURA FRAME")
print("="*70)

# Apri camera
print("\n[1/3] Apertura camera...")
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("❌ Camera non disponibile!")
    exit(1)

print("✅ Camera aperta")

# Attendi stabilizzazione
print("\n[2/3] Stabilizzazione (2 secondi)...")
time.sleep(2)

# Cattura frame
ret, frame = camera.read()

if not ret:
    print("❌ Errore cattura frame!")
    camera.release()
    exit(1)

# Info frame
h, w = frame.shape[:2]
print(f"✅ Frame catturato: {w}x{h}")

# Salva con timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"frame_catturato_{timestamp}.jpg"
cv2.imwrite(filename, frame)

print(f"\n[3/3] ✅ Frame salvato: {filename}")
print(f"     Dimensione: {w}x{h} pixel")

# Mostra anche anteprima piccola
print("\n[ANTEPRIMA] Apertura finestra...")
cv2.imshow("Frame Catturato - Premi un tasto per chiudere", frame)
print("     → Premi un TASTO qualsiasi sulla finestra per chiudere")
cv2.waitKey(0)

# Chiudi
camera.release()
cv2.destroyAllWindows()

print("\n" + "="*70)
print(f"  ✅ FATTO! Guarda il file: {filename}")
print("="*70)
print()

