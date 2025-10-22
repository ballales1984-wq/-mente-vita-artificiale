#!/usr/bin/env python3
"""
🧪 TEST HARDWARE REALE - YOLOv8 + Whisper
"""

import cv2
import time
from datetime import datetime

print("\n" + "="*70)
print("  🧪 TEST HARDWARE REALE")
print("="*70)

# Test 1: YOLOv8
print("\n[1/2] 📷 TEST YOLOV8")
print("─"*70)

try:
    from ultralytics import YOLO
    print("✅ YOLOv8 importato")
    
    print("   Caricamento modello yolov8n.pt...")
    model = YOLO('yolov8n.pt')
    print("   ✅ Modello caricato")
    
    print("   Apertura camera...")
    camera = cv2.VideoCapture(0)
    time.sleep(1)
    
    ret, frame = camera.read()
    if ret:
        print("   ✅ Frame catturato")
        
        print("   Elaborazione con YOLOv8...")
        results = model(frame, verbose=False)
        
        detections = []
        for r in results:
            boxes = r.boxes
            for box in boxes:
                cls = int(box.cls[0])
                conf = float(box.conf[0])
                label = model.names[cls]
                detections.append((label, conf))
        
        if detections:
            print(f"   ✅ Rilevati {len(detections)} oggetti:")
            for label, conf in detections[:5]:  # Max 5
                print(f"      • {label}: {conf:.2%}")
        else:
            print("   ⚠️  Nessun oggetto rilevato (normale se stanza vuota)")
        
        # Salva frame annotato
        annotated = results[0].plot()
        filename = f"test_yolo_{datetime.now().strftime('%H%M%S')}.jpg"
        cv2.imwrite(filename, annotated)
        print(f"   💾 Frame salvato: {filename}")
    
    camera.release()
    cv2.destroyAllWindows()
    
except Exception as e:
    print(f"   ❌ ERRORE: {e}")

# Test 2: Whisper
print("\n[2/2] 🎤 TEST WHISPER")
print("─"*70)

try:
    import whisper
    print("✅ Whisper importato")
    
    print("   Caricamento modello 'base'...")
    model = whisper.load_model("base")
    print("   ✅ Modello caricato")
    
    print("\n   [INFO] Whisper è pronto per trascrivere audio")
    print("   [INFO] Per testarlo completamente, usa:")
    print("          python mente_buffer_temp.py → opzione 4")
    
except Exception as e:
    print(f"   ❌ ERRORE: {e}")

print("\n" + "="*70)
print("  ✅ TEST COMPLETATO!")
print("="*70)
print("\n[PROSSIMO PASSO]")
print("  Lancia: python mente_buffer_temp.py")
print("  Scegli: 4 (Camera + Microfono)")
print("  Vedrai: Riconoscimento oggetti REALE!")
print()

