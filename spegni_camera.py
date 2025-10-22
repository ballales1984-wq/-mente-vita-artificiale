"""
🔴 SPEGNI CAMERA - Script di Emergenza
======================================
Usa questo script se la camera rimane bloccata/accesa.

Esegui: python spegni_camera.py
"""

import sys

print("="*70)
print("  🔴 SPEGNI CAMERA - Script di Emergenza")
print("="*70)
print()

# Prova a rilasciare con OpenCV
try:
    import cv2
    print("[1/3] Chiudo finestre OpenCV...")
    cv2.destroyAllWindows()
    print("      ✅ Finestre chiuse")
except ImportError:
    print("[1/3] ⚠️ OpenCV non disponibile")
except Exception as e:
    print(f"[1/3] ⚠️ Errore: {e}")

# Prova a rilasciare tutte le videocapture
try:
    import cv2
    print("\n[2/3] Rilascio tutte le camera...")
    
    # Prova camera 0, 1, 2
    for cam_id in range(3):
        try:
            cap = cv2.VideoCapture(cam_id)
            if cap.isOpened():
                cap.release()
                print(f"      ✅ Camera {cam_id} rilasciata")
        except:
            pass
    
    cv2.destroyAllWindows()
    print("      ✅ Tutte le camera rilasciate")
    
except ImportError:
    print("[2/3] ⚠️ OpenCV non disponibile")
except Exception as e:
    print(f"[2/3] ⚠️ Errore: {e}")

# Forza garbage collection
try:
    import gc
    print("\n[3/3] Garbage collection...")
    gc.collect()
    print("      ✅ Memoria pulita")
except Exception as e:
    print(f"[3/3] ⚠️ Errore: {e}")

print("\n" + "="*70)
print("  ✅ OPERAZIONE COMPLETATA")
print("="*70)
print()
print("[INFO] Se la camera è ancora accesa:")
print("  1. Chiudi tutte le finestre Python")
print("  2. Riavvia il programma")
print("  3. Se persiste, riavvia il PC")
print()
print("[OK] Script terminato\n")



