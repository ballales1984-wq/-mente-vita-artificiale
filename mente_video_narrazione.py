#!/usr/bin/env python3
"""
📺 MENTE CON VIDEO E NARRAZIONE IN TEMPO REALE
Mostra video camera + narrazione cognitiva affiancati
"""

import cv2
import time
import numpy as np
from datetime import datetime

from moduli import visione, udito, prefrontale, motoria, emozione
from moduli.biosegnale import InterfacciaCoerenzaCerebrale
from moduli.memoria_permanente import MemoriaPermanente

try:
    import sounddevice as sd
    from scipy.io import wavfile
    AUDIO_OK = True
except:
    AUDIO_OK = False

class MenteVideoNarrazione:
    """Sistema con video + narrazione real-time"""
    
    def __init__(self):
        print("\n" + "="*70)
        print("  📺 MENTE VIDEO + NARRAZIONE REAL-TIME")
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
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        
        # Stato narrazione
        self.linee_narrazione = []
        self.ciclo_num = 0
        
        print("  ✅ Sistema pronto!")
        print()
    
    def crea_pannello_narrazione(self, w=640, h=480):
        """Crea pannello con narrazione"""
        panel = np.zeros((h, w, 3), dtype=np.uint8)
        panel[:] = (20, 20, 20)  # Sfondo grigio scuro
        
        # Titolo
        cv2.putText(panel, "NARRAZIONE COGNITIVA", 
                   (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
        
        cv2.putText(panel, f"Ciclo #{self.ciclo_num}", 
                   (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200, 200, 200), 1)
        
        # Linee narrazione
        y = 110
        line_height = 25
        
        for line in self.linee_narrazione[-16:]:  # Ultime 16 righe
            if y < h - 30:
                # Colore basato su tipo
                if '[VISTA]' in line or '[UDITO]' in line:
                    color = (100, 200, 255)  # Azzurro
                elif '[EMOZIONI]' in line:
                    color = (255, 100, 200)  # Rosa
                elif '[PENSIERI]' in line:
                    color = (255, 255, 100)  # Giallo
                elif '[DECISIONE]' in line:
                    color = (100, 255, 100)  # Verde
                elif 'Ho deciso' in line or 'Vedo:' in line or 'Ho sentito' in line:
                    color = (255, 255, 255)  # Bianco
                else:
                    color = (180, 180, 180)  # Grigio chiaro
                
                # Scrivi linea (max 50 caratteri)
                text = line[:50] if len(line) > 50 else line
                cv2.putText(panel, text, 
                           (10, y), cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 1)
                y += line_height
        
        # Istruzioni in basso
        cv2.putText(panel, "SPAZIO=Ciclo | C=Auto | Q=Esci", 
                   (10, h-10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (100, 100, 100), 1)
        
        return panel
    
    def genera_narrazione(self, vis, audio_text, valenza, pattern, azione):
        """Genera linee narrazione"""
        lines = []
        
        # Vista
        emo = "[++]" if valenza > 0.5 else ("[+]" if valenza > 0 else ("[-]" if valenza < 0 else "[=]"))
        lines.append(f"[VISTA] {emo}")
        
        desc = vis.get('descrizione', 'nulla')[:40]
        lines.append(f'  Vedo: {desc}')
        
        if vis.get('num_oggetti', 0) > 0:
            lines.append(f'  {vis["num_oggetti"]} oggetti rilevati')
        
        # Udito
        lines.append(f"[UDITO]")
        if audio_text:
            lines.append(f'  "{audio_text[:40]}"')
        else:
            lines.append(f'  Silenzio')
        
        # Emozioni
        lines.append(f"[EMOZIONI] {emo}")
        if valenza > 0.5:
            stato = "positivo fiducioso"
        elif valenza > 0:
            stato = "positivo"
        else:
            stato = "neutro"
        lines.append(f'  {stato} ({valenza:+.2f})')
        
        neuroni = pattern.count('█') if '█' in pattern else 8
        lines.append(f'  {neuroni} neuroni attivi/15')
        
        # Pensieri
        lines.append(f"[PENSIERI]")
        if audio_text:
            if any(w in audio_text.lower() for w in ['ciao', 'salve']):
                lines.append(f'  Saluto rilevato')
            if any(w in audio_text.lower() for w in ['vieni', 'avvicinati']):
                lines.append(f'  Richiesta di avvicinamento')
            if any(w in audio_text.lower() for w in ['fermati', 'stop']):
                lines.append(f'  Comando stop')
        
        lines.append(f'  Situazione valutata')
        
        # Decisione
        lines.append(f"[DECISIONE]")
        lines.append(f'  {azione.upper().replace("_", " ")}')
        
        return lines
    
    def ciclo_con_video(self):
        """Un ciclo con visualizzazione video"""
        self.ciclo_num += 1
        
        # Cattura frame
        ret, frame = self.camera.read()
        if not ret:
            return False
        
        # 1. Visione
        vis = self.visione.elabora(None)
        
        # 2. Udito (simulato per velocità)
        aud = self.udito.ascolta(None)
        audio_text = aud.get('testo', aud.get('trascrizione', ''))
        
        # 3. Biosegnali
        onda = self.biosegnali.percepisce_segnale([vis, aud])
        pattern = onda.pattern.replace('1', '█').replace('0', '░')
        
        # 4. Emozione
        stato = self.emozione.elabora({'percezioni': [vis, aud]})
        valenza = stato.dati.get('valenza', 0)
        
        # 5. Decisione
        dec = self.prefrontale.ragiona({
            'percezioni_visive': vis,
            'percezioni_uditive': aud
        })
        azione = dec.get('azione', 'monitora')
        
        # 6. Azione
        self.motoria.agisci({'azione': azione})
        
        # Genera narrazione
        nuove_linee = self.genera_narrazione(vis, audio_text, valenza, pattern, azione)
        self.linee_narrazione.extend(nuove_linee)
        
        # Mantieni solo ultime 50 righe
        if len(self.linee_narrazione) > 50:
            self.linee_narrazione = self.linee_narrazione[-50:]
        
        # Salva memoria
        self.memoria.aggiungi_memoria({
            'descrizione': vis.get('descrizione', ''),
            'audio': audio_text,
            'valenza': valenza,
            'azione': azione
        })
        
        # Annota frame
        cv2.putText(frame, f"CICLO #{self.ciclo_num}", 
                   (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
        
        cv2.putText(frame, vis.get('descrizione', '')[:40], 
                   (10, 460), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        
        # Emozione
        color = (0, 255, 0) if valenza > 0 else ((0, 0, 255) if valenza < 0 else (128, 128, 128))
        cv2.putText(frame, f"{valenza:+.2f}", 
                   (580, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
        
        return frame
    
    def esegui(self):
        """Loop principale"""
        print("📺 Finestre video aperte!")
        print("\n[COMANDI]")
        print("  [SPAZIO] = Esegui ciclo cognitivo")
        print("  [C] = Cicli automatici continui")
        print("  [Q] = Esci")
        print("\n[INFO] Le finestre mostrano:")
        print("  • Sinistra: Feed camera")
        print("  • Destra: Narrazione cognitiva")
        print()
        
        continuo = False
        ultimo_ciclo = 0
        
        while True:
            # Cattura frame
            ret, frame = self.camera.read()
            if not ret:
                break
            
            # Ciclo automatico
            if continuo and (time.time() - ultimo_ciclo) > 3:
                frame = self.ciclo_con_video()
                if frame is False:
                    break
                ultimo_ciclo = time.time()
            
            # Crea pannello narrazione
            panel_narr = self.crea_pannello_narrazione(640, 480)
            
            # Affianca video e narrazione
            display = np.hstack([frame, panel_narr])
            
            # Mostra
            cv2.imshow("MENTE ARTIFICIALE - VIDEO + NARRAZIONE", display)
            
            # Gestisci input
            key = cv2.waitKey(1) & 0xFF
            
            if key == ord('q') or key == ord('Q'):
                break
            elif key == ord(' '):  # Spazio
                print(f"\n[CICLO #{self.ciclo_num+1}] Elaborazione...")
                frame = self.ciclo_con_video()
                if frame is False:
                    break
                print(f"[OK] Completato\n")
            elif key == ord('c') or key == ord('C'):
                continuo = not continuo
                if continuo:
                    print("\n🔄 Cicli automatici ATTIVATI (1 ogni 3 secondi)")
                    ultimo_ciclo = time.time()
                else:
                    print("\n⏸️  Cicli automatici DISATTIVATI")
        
        # Chiudi
        self.camera.release()
        cv2.destroyAllWindows()
        
        print("\n" + "="*70)
        print("  📊 STATISTICHE FINALI")
        print("="*70)
        stats = self.memoria.get_statistiche()
        print(f"  • Cicli eseguiti: {self.ciclo_num}")
        print(f"  • Memorie salvate: {stats['totale_memorie']}")
        print(f"  • Spazio usato: {stats['spazio_usato_mb']:.2f}MB")
        print("="*70)
        print()

if __name__ == "__main__":
    try:
        mente = MenteVideoNarrazione()
        mente.esegui()
    except KeyboardInterrupt:
        print("\n\n✅ Interruzione utente\n")
    except Exception as e:
        print(f"\n❌ Errore: {e}\n")
        import traceback
        traceback.print_exc()

