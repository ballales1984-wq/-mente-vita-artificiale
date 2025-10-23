#!/usr/bin/env python3
"""
🧠 MENTE AI CON BUFFER TEMPORANEO
File audio/video riscrivibili - Eliminati automaticamente
"""

import os
import time
import cv2
import numpy as np
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

class BufferTemp:
    """Gestisce file temporanei riscrivibili"""
    
    def __init__(self):
        self.temp_dir = Path("temp_buffer")
        self.temp_dir.mkdir(exist_ok=True)
        self.audio_temp = self.temp_dir / "audio.wav"
        self.video_temp = self.temp_dir / "frame.jpg"
        print(f"[Buffer] Temp: {self.temp_dir}")
    
    def registra_audio(self, durata=4.0):
        """Registra audio (sovrascrive)"""
        if not AUDIO_OK:
            return None
        try:
            print(f"[Buffer] 🎤 Registrazione {durata}s...")
            audio = sd.rec(int(durata * 16000), samplerate=16000, channels=1, dtype='float32')
            sd.wait()
            wavfile.write(str(self.audio_temp), 16000, np.int16(audio * 32767))
            print(f"[Buffer] ✅ Audio salvato")
            return self.audio_temp
        except Exception as e:
            print(f"[Buffer] ❌ {e}")
            return None
    
    def cattura_frame(self, camera):
        """Cattura frame (sovrascrive)"""
        if camera is None:
            return None
        try:
            ret, frame = camera.read()
            if ret:
                cv2.imwrite(str(self.video_temp), frame)
                print(f"[Buffer] 📷 Frame salvato")
                return self.video_temp
        except:
            pass
        return None
    
    def elimina_tutto(self):
        """Elimina tutti i temp"""
        for f in [self.audio_temp, self.video_temp]:
            if f.exists():
                f.unlink()
        print(f"[Buffer] 🗑️  File eliminati")
    
    def pulisci(self):
        """Rimuove cartella temp"""
        import shutil
        if self.temp_dir.exists():
            shutil.rmtree(self.temp_dir)
            print(f"[Buffer] ✅ Cartella rimossa")


class MenteBufferTemp:
    """Mente AI con buffer temporanei"""
    
    def __init__(self, usa_camera=True, usa_mic=True):
        print("\n" + "="*70)
        print("  🧠 MENTE AI - BUFFER TEMPORANEO v1.0")
        print("="*70)
        
        self.buffer = BufferTemp()
        self.usa_camera = usa_camera
        self.usa_mic = usa_mic and AUDIO_OK
        
        # Moduli
        self.visione = visione.CortecciaVisiva()
        self.udito = udito.CortecciaUditiva()
        self.biosegnali = InterfacciaCoerenzaCerebrale()
        self.emozione = emozione.Amigdala()
        self.emozione.inizializza()
        self.prefrontale = prefrontale.CortecciaPrefrontale()
        self.prefrontale.inizializza()
        self.motoria = motoria.CortecciaMotoria()
        
        # Memoria permanente 2GB
        self.memoria_permanente = MemoriaPermanente(max_size_gb=2)
        print(f"  ✅ Memoria permanente: {self.memoria_permanente.get_size_mb():.1f}MB usati")
        
        # Camera
        self.camera = None
        if usa_camera:
            try:
                self.camera = cv2.VideoCapture(0)
                if self.camera.isOpened():
                    print("  ✅ Camera OK")
                else:
                    self.usa_camera = False
            except:
                self.usa_camera = False
        
        print("[OK] Sistema pronto!\n")
    
    def ciclo(self):
        """Un ciclo cognitivo"""
        # Visione
        print("\n[1/6] 👁️  VISIONE")
        if self.usa_camera:
            frame_path = self.buffer.cattura_frame(self.camera)
        vis = self.visione.elabora(None)
        print(f"       {vis['descrizione']}")
        
        # Udito
        print("\n[2/6] 👂 UDITO")
        if self.usa_mic:
            audio_path = self.buffer.registra_audio(4.0)
            if audio_path:
                aud = self.udito.ascolta(str(audio_path))
            else:
                aud = self.udito.ascolta(None)
        else:
            aud = self.udito.ascolta(None)
        testo = aud.get('testo', aud.get('trascrizione', 'N/A'))
        print(f"       '{testo}'")
        
        # Biosegnali
        print("\n[3/6] ⚡ BIOSEGNALI")
        onda = self.biosegnali.percepisce_segnale([vis, aud])
        pattern = onda.pattern.replace('1', '█').replace('0', '░')
        print(f"       {pattern}")
        
        # Emozione
        print("\n[4/6] ❤️  EMOZIONE")
        stato = self.emozione.elabora({'percezioni': [vis, aud]})
        valenza = stato.dati.get('valenza', 0)
        print(f"       {'+' if valenza > 0 else '-'}{abs(valenza):.2f}")
        
        # Decisione
        print("\n[5/6] 🧠 DECISIONE")
        dec = self.prefrontale.ragiona({'percezioni_visive': vis, 'percezioni_uditive': aud})
        print(f"       {dec.get('azione', 'monitora').upper()}")
        
        # Azione
        print("\n[6/6] 🦾 AZIONE")
        azione = dec.get('azione', 'monitora')
        successo = self.motoria.agisci({'azione': azione})
        print(f"       {azione.upper()} {'✅' if successo else '❌'}")
        
        # NARRAZIONE: Cosa pensa e dice l'AI
        print("\n" + "="*70)
        print("  💭 NARRAZIONE COGNITIVA")
        print("="*70)
        self._narrazione_cognitiva(vis, testo, valenza, pattern, azione, successo)
        
        # Salva memoria permanente
        print("\n[7/6] 💾 SALVATAGGIO MEMORIA")
        memoria_episodio = {
            'descrizione': vis.get('descrizione', ''),
            'audio_trascritto': testo,
            'emozione': 'positivo' if valenza > 0 else ('negativo' if valenza < 0 else 'neutro'),
            'valenza': valenza,
            'azione': azione,
            'successo': successo,
            'pattern_neurale': pattern,
            'oggetti_visti': vis.get('num_oggetti', 0)
        }
        if self.memoria_permanente.aggiungi_memoria(memoria_episodio):
            print(f"       💾 Memoria salvata permanentemente")
        
        # Elimina temp
        print("\n[CLEANUP]")
        self.buffer.elimina_tutto()
    
    def sessione(self, n=5):
        """Sessione di n cicli"""
        for i in range(1, n+1):
            print("\n" + "="*70)
            print(f"  CICLO #{i}/{n}")
            print("="*70)
            start = time.time()
            self.ciclo()
            print(f"\n[TEMPO] {time.time()-start:.2f}s")
            if i < n:
                time.sleep(1)
        print("\n✅ SESSIONE COMPLETATA\n")
        
        # Statistiche memoria permanente
        print("="*70)
        print("  💾 STATISTICHE MEMORIA PERMANENTE")
        print("="*70)
        stats = self.memoria_permanente.get_statistiche()
        print(f"  • Memorie salvate: {stats['totale_memorie']}")
        print(f"  • Spazio usato: {stats['spazio_usato_mb']:.2f}MB / 2048MB")
        print(f"  • Percentuale: {stats['percentuale_usata']:.1f}%")
        print(f"  • Spazio rimanente: {stats['spazio_rimanente_gb']:.3f}GB")
        print("="*70)
        print()
    
    def chiudi(self):
        """Chiude tutto"""
        if self.camera:
            self.camera.release()
            cv2.destroyAllWindows()
        self.buffer.pulisci()
        print("[OK] Chiuso\n")


if __name__ == "__main__":
    print("""
╔══════════════════════════════════════════════════════════════════╗
║  🧠 MENTE AI - BUFFER TEMPORANEO                                ║
║  File eliminati automaticamente dopo l'uso                      ║
╚══════════════════════════════════════════════════════════════════╝

[1] Solo simulazione
[2] Camera + Audio simulato
[3] Microfono + Video simulato  
[4] Camera + Microfono
[9] Esci
""")
    
    scelta = input(">> Scelta: ").strip()
    
    try:
        if scelta == "1":
            m = MenteBufferTemp(False, False)
        elif scelta == "2":
            m = MenteBufferTemp(True, False)
        elif scelta == "3":
            m = MenteBufferTemp(False, True)
        elif scelta == "4":
            m = MenteBufferTemp(True, True)
        else:
            print("\n✅ Uscita\n")
            exit()
        
        m.sessione(5)
        m.chiudi()
        
    except KeyboardInterrupt:
        print("\n\n✅ Interrotto\n")
        try:
            m.chiudi()
        except:
            pass


