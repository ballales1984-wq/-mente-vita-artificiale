#!/usr/bin/env python3
"""
📺 MENTE VISUALE - Interfaccia Grafica Completa
Mostra tutto in finestre visive: video, narrazione, statistiche
"""

import cv2
import time
import numpy as np
from datetime import datetime
from pathlib import Path

from moduli import visione, udito, prefrontale, motoria, emozione
from moduli.biosegnale import InterfacciaCoerenzaCerebrale
from moduli.memoria_permanente import MemoriaPermanente

try:
    import sounddevice as sd
    from scipy.io import wavfile
    AUDIO_OK = True
except:
    AUDIO_OK = False

class MenteVisuale:
    """Mente AI con interfaccia grafica"""
    
    def __init__(self):
        print("\n" + "="*70)
        print("  📺 MENTE VISUALE - INTERFACCIA GRAFICA")
        print("="*70)
        
        # Moduli
        self.visione = visione.CortecciaVisiva()
        self.udito = udito.CortecciaUditiva()
        self.biosegnali = InterfacciaCoerenzaCerebrale()
        self.emozione = emozione.Amigdala()
        self.emozione.inizializza()
        self.prefrontale = prefrontale.CortecciaPrefrontale()
        self.prefrontale.inizializza()
        self.motoria = motoria.CortecciaMotoria()
        self.memoria = MemoriaPermanente(max_size_gb=2)
        
        # Camera
        self.camera = cv2.VideoCapture(0)
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        
        # Stato
        self.narrazione = []
        self.stats = {
            'cicli': 0,
            'oggetti_rilevati': 0,
            'audio_trascritto': '',
            'emozione': 'neutro',
            'valenza': 0.0,
            'azione': 'inizializzazione',
            'pattern': '░'*15
        }
        
        print("  ✅ Sistema pronto!")
        print("  📺 Apri le finestre grafiche...")
        print()
    
    def disegna_interfaccia(self, frame):
        """Disegna interfaccia grafica sul frame"""
        h, w = frame.shape[:2]
        
        # Crea canvas più grande per info
        canvas = np.zeros((h + 400, w, 3), dtype=np.uint8)
        canvas[0:h, 0:w] = frame
        
        # Sfondo per info
        cv2.rectangle(canvas, (0, h), (w, h+400), (30, 30, 30), -1)
        
        # Titolo
        cv2.putText(canvas, "MENTE ARTIFICIALE - VISIONE COGNITIVA", 
                   (20, h+40), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 255, 255), 2)
        
        # Statistiche
        y = h + 80
        cv2.putText(canvas, f"Ciclo: #{self.stats['cicli']}", 
                   (20, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        cv2.putText(canvas, f"Oggetti: {self.stats['oggetti_rilevati']}", 
                   (200, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        # Emozione con colore
        emo = self.stats['emozione']
        val = self.stats['valenza']
        color = (0, 255, 0) if val > 0 else ((0, 0, 255) if val < 0 else (128, 128, 128))
        cv2.putText(canvas, f"Emozione: {emo} ({val:+.2f})", 
                   (420, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
        
        # Pattern neurale
        y += 40
        pattern = self.stats['pattern']
        cv2.putText(canvas, f"Pattern Neurale: {pattern}", 
                   (20, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (100, 200, 255), 2)
        
        # Audio trascritto
        y += 40
        audio = self.stats['audio_trascritto']
        if audio:
            cv2.putText(canvas, f'Audio: "{audio[:60]}"', 
                       (20, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 200, 100), 2)
        else:
            cv2.putText(canvas, "Audio: [silenzio]", 
                       (20, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (128, 128, 128), 2)
        
        # Azione
        y += 40
        azione = self.stats['azione']
        cv2.putText(canvas, f"Azione: {azione.upper()}", 
                   (20, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        # Narrazione (ultime 5 righe)
        y += 60
        cv2.putText(canvas, "NARRAZIONE COGNITIVA:", 
                   (20, y), cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 255, 0), 2)
        
        y += 30
        for line in self.narrazione[-5:]:
            if y < h + 380:
                cv2.putText(canvas, line[:80], 
                           (20, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)
                y += 25
        
        # Istruzioni
        cv2.putText(canvas, "Premi 'Q' per uscire | 'SPAZIO' per ciclo | 'S' per screenshot", 
                   (20, h+395), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (100, 100, 100), 1)
        
        return canvas
    
    def ciclo_visuale(self):
        """Esegue un ciclo cognitivo con visualizzazione"""
        self.stats['cicli'] += 1
        self.narrazione = []
        
        # 1. VISIONE
        ret, frame = self.camera.read()
        if not ret:
            return None
        
        vis = self.visione.elabora(None)
        self.stats['oggetti_rilevati'] = vis.get('num_oggetti', 0)
        
        # 2. UDITO (silenzioso per non rallentare)
        aud = self.udito.ascolta(None)
        self.stats['audio_trascritto'] = aud.get('testo', aud.get('trascrizione', ''))
        
        # 3. BIOSEGNALI
        onda = self.biosegnali.percepisce_segnale([vis, aud])
        pattern = onda.pattern.replace('1', '█').replace('0', '░')
        self.stats['pattern'] = pattern
        
        # 4. EMOZIONE
        stato = self.emozione.elabora({'percezioni': [vis, aud]})
        valenza = stato.dati.get('valenza', 0)
        self.stats['valenza'] = valenza
        
        if valenza > 0.5:
            self.stats['emozione'] = "positivo fiducioso"
        elif valenza > 0:
            self.stats['emozione'] = "positivo"
        elif valenza < -0.5:
            self.stats['emozione'] = "preoccupato"
        elif valenza < 0:
            self.stats['emozione'] = "cauto"
        else:
            self.stats['emozione'] = "neutro"
        
        # 5. DECISIONE
        dec = self.prefrontale.ragiona({
            'percezioni_visive': vis,
            'percezioni_uditive': aud
        })
        azione = dec.get('azione', 'monitora')
        self.stats['azione'] = azione
        
        # 6. AZIONE
        successo = self.motoria.agisci({'azione': azione})
        
        # NARRAZIONE
        descrizione = vis.get('descrizione', '')
        testo = self.stats['audio_trascritto']
        
        self.narrazione.append(f"[VISTA] Vedo: {descrizione}")
        if vis.get('num_oggetti', 0) > 0:
            self.narrazione.append(f"  {vis.get('num_oggetti')} oggetti rilevati")
        
        if testo:
            self.narrazione.append(f"[UDITO] Ho sentito: '{testo}'")
        else:
            self.narrazione.append(f"[UDITO] Silenzio o rumore di fondo")
        
        self.narrazione.append(f"[EMOZIONE] Mi sento {self.stats['emozione']} ({valenza:+.2f})")
        
        if testo:
            if any(w in testo.lower() for w in ['ciao', 'salve']):
                self.narrazione.append(f"[PENSIERO] Ho rilevato un saluto")
            if any(w in testo.lower() for w in ['vieni', 'avvicinati']):
                self.narrazione.append(f"[PENSIERO] Mi viene richiesto di avvicinarmi")
        
        self.narrazione.append(f"[DECISIONE] Ho deciso: {azione.upper().replace('_', ' ')}")
        
        if successo:
            self.narrazione.append(f"[ESITO] Azione eseguita con successo")
        
        # Salva memoria
        memoria = {
            'descrizione': descrizione,
            'audio': testo,
            'emozione': self.stats['emozione'],
            'valenza': valenza,
            'azione': azione,
            'successo': successo
        }
        self.memoria.aggiungi_memoria(memoria)
        
        # Disegna annotazioni sul frame
        cv2.putText(frame, f"CICLO #{self.stats['cicli']}", 
                   (10, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 255), 2)
        
        cv2.putText(frame, descrizione, 
                   (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        
        # Emozione in alto a destra
        color = (0, 255, 0) if valenza > 0 else ((0, 0, 255) if valenza < 0 else (128, 128, 128))
        cv2.putText(frame, self.stats['emozione'].upper(), 
                   (frame.shape[1]-250, 30), cv2.FONT_HERSHEY_DUPLEX, 0.8, color, 2)
        
        return frame
    
    def esegui(self):
        """Loop principale con visualizzazione"""
        print("📺 Finestra video aperta!")
        print("   [SPAZIO] = Esegui ciclo cognitivo")
        print("   [C] = Ciclo automatico continuo")
        print("   [S] = Salva screenshot")
        print("   [Q] = Esci")
        print()
        
        continuo = False
        
        while True:
            # Cattura frame
            ret, frame = self.camera.read()
            if not ret:
                break
            
            # Esegui ciclo se richiesto
            if continuo:
                frame_elaborato = self.ciclo_visuale()
                if frame_elaborato is not None:
                    frame = frame_elaborato
                time.sleep(0.5)  # Pausa tra cicli
            
            # Disegna interfaccia
            display = self.disegna_interfaccia(frame)
            
            # Mostra
            cv2.imshow("MENTE ARTIFICIALE - VISIONE COGNITIVA", display)
            
            # Gestisci tasti
            key = cv2.waitKey(1) & 0xFF
            
            if key == ord('q') or key == ord('Q'):
                break
            elif key == ord(' '):  # Spazio
                print(f"\n[CICLO #{self.stats['cicli']+1}] Elaborazione...")
                frame = self.ciclo_visuale()
                if frame is None:
                    break
                print(f"[OK] Ciclo completato\n")
            elif key == ord('c') or key == ord('C'):
                continuo = not continuo
                if continuo:
                    print("\n🔄 Modalità continua ATTIVATA")
                else:
                    print("\n⏸️  Modalità continua DISATTIVATA")
            elif key == ord('s') or key == ord('S'):
                filename = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
                cv2.imwrite(filename, display)
                print(f"📸 Screenshot salvato: {filename}")
        
        # Chiudi
        self.camera.release()
        cv2.destroyAllWindows()
        
        # Statistiche finali
        print("\n" + "="*70)
        print("  📊 STATISTICHE FINALI")
        print("="*70)
        stats = self.memoria.get_statistiche()
        print(f"  • Cicli eseguiti: {self.stats['cicli']}")
        print(f"  • Memorie salvate: {stats['totale_memorie']}")
        print(f"  • Spazio usato: {stats['spazio_usato_mb']:.2f}MB")
        print("="*70)
        print()

if __name__ == "__main__":
    try:
        mente = MenteVisuale()
        mente.esegui()
    except KeyboardInterrupt:
        print("\n\n✅ Interruzione utente\n")
    except Exception as e:
        print(f"\n❌ Errore: {e}\n")
        import traceback
        traceback.print_exc()

