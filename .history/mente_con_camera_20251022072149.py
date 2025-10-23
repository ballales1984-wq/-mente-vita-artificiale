"""
📷🧠 MENTE ARTIFICIALE CON CAMERA REALE
========================================
Sistema che usa la telecamera/webcam per input visivo reale.

Funzionalità:
- Cattura video dalla camera
- Elaborazione real-time con YOLOv8
- Ciclo cognitivo con input reale
- Visualizzazione annotazioni
"""

import cv2
import time
import sys
from moduli import visione, udito, prefrontale, motoria, emozione, memoria

def test_camera():
    """Testa se la camera è disponibile"""
    print("="*70)
    print("[TEST CAMERA] Verifica disponibilita...")
    print("="*70)
    
    # Prova camera index 0
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("\n[ERROR] Camera non disponibile!")
        print("\nSoluzioni:")
        print("  1. Verifica che la webcam sia collegata")
        print("  2. Chiudi altre app che usano la camera")
        print("  3. Prova index diverso (1, 2, ecc.)")
        print("\nUsa modalita simulata: python esempio_semplice.py")
        cap.release()
        return False
    
    # Cattura frame di test
    ret, frame = cap.read()
    
    if not ret:
        print("\n[ERROR] Impossibile catturare frame!")
        cap.release()
        return False
    
    h, w, c = frame.shape
    print(f"\n[OK] Camera disponibile!")
    print(f"  Risoluzione: {w}x{h}")
    print(f"  Canali: {c}")
    print(f"  Frame rate: {cap.get(cv2.CAP_PROP_FPS):.1f} fps")
    
    # Salva frame test
    cv2.imwrite("camera_test.jpg", frame)
    print(f"  Frame test salvato: camera_test.jpg")
    
    cap.release()
    return True


def ciclo_con_camera_singolo():
    """Esegue un ciclo cognitivo con frame dalla camera"""
    print("\n" + "="*70)
    print("[CICLO COGNITIVO CON CAMERA REALE]")
    print("="*70)
    
    # Inizializza moduli
    ippocampo = memoria.get_instance()
    amigdala = emozione.get_instance()
    
    # Apri camera
    print("\n[CAMERA] Apertura...")
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("[ERROR] Camera non disponibile!")
        return False
    
    print("[OK] Camera attiva\n")
    
    # Cattura frame
    print("[1/6] CATTURA FRAME...")
    ret, frame = cap.read()
    cap.release()
    
    if not ret:
        print("[ERROR] Cattura fallita!")
        return False
    
    print(f"  [OK] Frame catturato ({frame.shape[1]}x{frame.shape[0]})")
    
    # Elabora con YOLO
    print("\n[2/6] VISIONE: Elaborazione con YOLOv8...")
    risultato_visivo = visione.elabora(frame)
    
    print(f"  Risultato: {risultato_visivo['descrizione']}")
    print(f"  Oggetti rilevati: {risultato_visivo['num_oggetti']}")
    
    if risultato_visivo['num_oggetti'] > 0:
        print(f"  Focus su: {risultato_visivo['attenzione']['focus']}")
    
    # Audio simulato
    print("\n[3/6] UDITO: Input audio (simulato)...")
    risultato_audio = udito.ascolta("audio.wav")
    print(f"  Testo: '{risultato_audio['testo']}'")
    
    # Richiamo memoria
    print("\n[4/6] MEMORIA: Richiamo contestuale...")
    contesto = f"{risultato_visivo['descrizione']} {risultato_audio['testo']}"
    memorie_rilevanti, suggerimenti = ippocampo.richiama_contestuale(contesto, top_k=3)
    
    if memorie_rilevanti:
        print(f"  Memorie trovate: {len(memorie_rilevanti)}")
        for mem in memorie_rilevanti[:2]:
            print(f"    - {mem.contenuto[:40]}...")
    
    # Emozione
    print("\n[5/6] EMOZIONE: Valutazione...")
    risultato_emozione = amigdala.elabora({
        'percezioni': [risultato_visivo, risultato_audio],
        'memoria': {}
    })
    stato_emotivo = risultato_emozione.dati['stato_emotivo']
    valenza = risultato_emozione.dati['valenza']
    print(f"  Stato: {stato_emotivo.upper()} (valenza: {valenza:+.2f})")
    
    # Decisione
    print("\n[6/6] RAGIONAMENTO: Decisione...")
    decisione = prefrontale.ragiona(
        percezioni_visive=risultato_visivo,
        percezioni_uditive=risultato_audio,
        stato_emotivo=stato_emotivo,
        memoria=[m.contenuto for m in memorie_rilevanti]
    )
    
    # Applica suggerimenti memoria
    if suggerimenti.get('confidence', 0) > 0.7 and suggerimenti.get('azione_consigliata'):
        print(f"  [!] Memoria suggerisce: {suggerimenti['azione_consigliata']}")
        decisione['azione'] = suggerimenti['azione_consigliata']
    
    print(f"  Decisione: {decisione['azione'].upper()}")
    print(f"  Priorita: {decisione['priorita']:.2f}")
    
    # Salva frame annotato
    if risultato_visivo.get('num_oggetti', 0) > 0:
        frame_annotato = visione.annota(frame, risultato_visivo)
        cv2.imwrite("frame_annotato.jpg", frame_annotato)
        print(f"\n[OK] Frame annotato salvato: frame_annotato.jpg")
    
    print(f"\n{'='*70}")
    print("[OK] CICLO COMPLETATO CON SUCCESSO")
    print(f"{'='*70}\n")
    
    return True


def modalita_streaming():
    """Modalità streaming continuo dalla camera"""
    print("\n" + "="*70)
    print("[MODALITA' STREAMING CAMERA]")
    print("="*70)
    print("\n[!] Premi 'q' per uscire")
    print("[!] Premi 'c' per eseguire ciclo cognitivo")
    print("[!] Premi 's' per salvare frame\n")
    
    # Apri camera
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("[ERROR] Camera non disponibile!")
        return False
    
    # Imposta parametri
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    frame_count = 0
    cicli_eseguiti = 0
    
    print("[OK] Streaming attivo...\n")
    
    try:
        while True:
            ret, frame = cap.read()
            
            if not ret:
                print("[ERROR] Lettura frame fallita")
                break
            
            frame_count += 1
            
            # Mostra frame
            display_frame = frame.copy()
            
            # Info overlay
            cv2.putText(display_frame, f"Frame: {frame_count}", 
                       (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(display_frame, f"Cicli: {cicli_eseguiti}", 
                       (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(display_frame, "q=esci | c=ciclo | s=salva", 
                       (10, frame.shape[0]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
            
            cv2.imshow('Mente Artificiale - Camera', display_frame)
            
            # Gestione tasti
            key = cv2.waitKey(1) & 0xFF
            
            if key == ord('q'):
                print("\n[!] Uscita...")
                break
                
            elif key == ord('c'):
                print(f"\n[CICLO #{cicli_eseguiti + 1}] Elaborazione frame...")
                
                # Elabora con visione
                risultato = visione.elabora(frame)
                print(f"  {risultato['descrizione']}")
                
                # Annota frame
                if risultato['num_oggetti'] > 0:
                    frame_annotato = visione.annota(frame, risultato)
                    cv2.imshow('Mente Artificiale - Camera', frame_annotato)
                    cv2.waitKey(1000)  # Mostra per 1 secondo
                
                cicli_eseguiti += 1
                
            elif key == ord('s'):
                filename = f"camera_frame_{frame_count}.jpg"
                cv2.imwrite(filename, frame)
                print(f"\n[OK] Frame salvato: {filename}")
            
            # Elaborazione automatica ogni 30 frame (opzionale)
            # if frame_count % 30 == 0:
            #     risultato = visione.elabora(frame)
            
    except KeyboardInterrupt:
        print("\n\n[!] Interruzione manuale")
    
    finally:
        cap.release()
        cv2.destroyAllWindows()
        print(f"\n[REPORT]")
        print(f"  Frame processati: {frame_count}")
        print(f"  Cicli cognitivi: {cicli_eseguiti}")
        print(f"\n[OK] Camera chiusa\n")
    
    return True


def modalita_foto_analisi():
    """Cattura foto e analizza dettagliata"""
    print("\n" + "="*70)
    print("[MODALITA' FOTO ANALISI]")
    print("="*70)
    
    # Apri camera
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("[ERROR] Camera non disponibile!")
        return False
    
    print("\n[CAMERA] Preparazione scatto...")
    print("[!] Posizionati e premi SPAZIO per scattare")
    print("[!] Premi 'q' per annullare\n")
    
    foto_scattata = None
    
    try:
        while True:
            ret, frame = cap.read()
            
            if not ret:
                break
            
            # Mostra preview
            preview = frame.copy()
            cv2.putText(preview, "SPAZIO=scatta | q=annulla", 
                       (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            
            cv2.imshow('Preview - Premi SPAZIO', preview)
            
            key = cv2.waitKey(1) & 0xFF
            
            if key == ord(' '):  # Spazio
                foto_scattata = frame.copy()
                print("\n[OK] Foto scattata!")
                
                # Flash effect
                white = frame.copy()
                white[:] = (255, 255, 255)
                cv2.imshow('Preview - Premi SPAZIO', white)
                cv2.waitKey(100)
                
                break
                
            elif key == ord('q'):
                print("\n[!] Annullato")
                cap.release()
                cv2.destroyAllWindows()
                return False
    
    finally:
        cap.release()
        cv2.destroyAllWindows()
    
    if foto_scattata is None:
        return False
    
    # Salva foto
    cv2.imwrite("foto_scattata.jpg", foto_scattata)
    print("[OK] Foto salvata: foto_scattata.jpg")
    
    # Analisi dettagliata
    print("\n[ANALISI DETTAGLIATA]")
    print("-" * 70)
    
    risultato = visione.elabora(foto_scattata)
    
    print(f"\n{risultato['descrizione']}")
    print(f"\nOggetti rilevati: {risultato['num_oggetti']}")
    
    if risultato['oggetti']:
        print("\nDettagli:")
        for i, obj in enumerate(risultato['oggetti'], 1):
            print(f"  {i}. {obj['classe']}")
            print(f"     Confidenza: {obj['confidenza']:.2%}")
            print(f"     Posizione: {obj['centro']}")
    
    print(f"\nFocus attenzione: {risultato['attenzione']['focus']}")
    print(f"Rilevanza: {risultato['attenzione']['rilevanza']:.2f}")
    
    # Mostra con annotazioni
    if risultato['num_oggetti'] > 0:
        print("\n[VISUALIZZAZIONE] Mostra frame annotato...")
        frame_annotato = visione.annota(foto_scattata, risultato)
        
        cv2.imshow('Analisi Completata - Premi tasto per chiudere', frame_annotato)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        # Salva annotato
        cv2.imwrite("foto_annotata.jpg", frame_annotato)
        print("[OK] Foto annotata salvata: foto_annotata.jpg")
    
    return True


def modalita_sorveglianza():
    """Modalità sorveglianza: rileva movimenti/persone"""
    print("\n" + "="*70)
    print("[MODALITA' SORVEGLIANZA]")
    print("="*70)
    print("\n[!] Sistema attivo - Premi 'q' per uscire\n")
    
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("[ERROR] Camera non disponibile!")
        return False
    
    # Inizializza moduli
    amigdala = emozione.get_instance()
    
    frame_count = 0
    allerte = 0
    
    print("[OK] Modalita sorveglianza attiva")
    print("[*] Rilevamento: person, car, bottle, phone...\n")
    
    try:
        while True:
            ret, frame = cap.read()
            
            if not ret:
                break
            
            frame_count += 1
            
            # Elabora ogni 15 frame (risparmio CPU)
            if frame_count % 15 == 0:
                risultato = visione.elabora(frame)
                
                # Check oggetti di interesse
                oggetti_interesse = ['person', 'car', 'dog', 'cat']
                rilevati = [obj for obj in risultato.get('oggetti', []) 
                          if obj['classe'] in oggetti_interesse]
                
                if rilevati:
                    allerte += 1
                    timestamp = time.strftime("%H:%M:%S")
                    
                    print(f"\n[ALLERTA #{allerte}] {timestamp}")
                    for obj in rilevati:
                        print(f"  - {obj['classe'].upper()} rilevato (conf: {obj['confidenza']:.2f})")
                    
                    # Salva frame allerta
                    filename = f"allerta_{allerte}_{timestamp.replace(':', '')}.jpg"
                    frame_annotato = visione.annota(frame, risultato)
                    cv2.imwrite(filename, frame_annotato)
                    print(f"  [OK] Salvato: {filename}")
            
            # Mostra live
            display = frame.copy()
            cv2.putText(display, f"Allerte: {allerte}", 
                       (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            cv2.putText(display, "SORVEGLIANZA ATTIVA", 
                       (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            
            cv2.imshow('Sorveglianza', display)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
    except KeyboardInterrupt:
        print("\n\n[!] Interruzione")
    
    finally:
        cap.release()
        cv2.destroyAllWindows()
        
        print(f"\n[REPORT SORVEGLIANZA]")
        print(f"  Frame processati: {frame_count}")
        print(f"  Allerte: {allerte}")
        print(f"\n[OK] Sistema disattivato\n")
    
    return True


if __name__ == "__main__":
    print("""
    ================================================================
    
           MENTE ARTIFICIALE - INTEGRAZIONE CAMERA
           
    ================================================================
    """)
    
    # Verifica camera
    try:
        import cv2
        camera_ok = test_camera()
    except ImportError:
        print("\n[ERROR] OpenCV non installato!")
        print("\nInstalla con: pip install opencv-python")
        camera_ok = False
    
    if not camera_ok:
        print("\n[!] Camera non disponibile, uscita...")
        sys.exit(1)
    
    # Menu
    print("\n" + "="*70)
    print("[MENU] Scegli modalita:")
    print("="*70)
    print("  1. Ciclo singolo con camera")
    print("  2. Streaming live (manuale)")
    print("  3. Foto e analisi dettagliata")
    print("  4. Sorveglianza automatica")
    print("="*70)
    
    try:
        scelta = input("\n>> Scelta (1-4): ").strip()
        
        if scelta == "1":
            ciclo_con_camera_singolo()
        elif scelta == "2":
            modalita_streaming()
        elif scelta == "3":
            modalita_foto_analisi()
        elif scelta == "4":
            modalita_sorveglianza()
        else:
            print("[ERROR] Scelta non valida")
            
    except KeyboardInterrupt:
        print("\n\n[!] Interruzione\n")
    except Exception as e:
        print(f"\n[ERROR] {e}")
        import traceback
        traceback.print_exc()

