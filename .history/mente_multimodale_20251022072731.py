"""
📷🎤🧠 MENTE ARTIFICIALE MULTIMODALE COMPLETA
==============================================
Sistema che integra CAMERA + MICROFONO per percezione multimodale reale.

Corteccia Visiva: YOLOv8 real-time
Corteccia Uditiva: Whisper speech-to-text
Integrazione: Sincronizzazione video + audio

Versione: 3.0 - Percezione Multimodale Reale
"""

import cv2
import time
import sys
import numpy as np
from moduli import visione, udito, prefrontale, motoria, emozione, memoria
from moduli.biosegnale import InterfacciaCoerenzaCerebrale

try:
    import sounddevice as sd
    AUDIO_OK = True
except ImportError:
    AUDIO_OK = False


class MenteMultimodale:
    """
    Sistema cognitivo con percezione multimodale reale
    
    Integra:
    - Camera (visione YOLOv8)
    - Microfono (audio Whisper)
    - Memoria intelligente
    - Biosegnali neurali
    - Decision making
    """
    
    def __init__(self):
        self.nome = "Mente Multimodale"
        
        # Moduli sensoriali
        self.corteccia_visiva = visione.get_instance()
        self.corteccia_uditiva = udito.get_instance()
        
        # Moduli cognitivi
        self.ippocampo = memoria.get_instance()
        self.amigdala = emozione.get_instance()
        
        # Layer neurale
        self.interfaccia_neurale = InterfacciaCoerenzaCerebrale()
        
        # Stato
        self.camera_attiva = False
        self.microfono_attivo = False
        self.cicli_eseguiti = 0
    
    def inizializza_sensori(self) -> bool:
        """
        Inizializza camera e microfono
        
        Returns:
            bool: True se almeno un sensore è attivo
        """
        print(f"\n{'='*70}")
        print(f"[{self.nome.upper()}] INIZIALIZZAZIONE SENSORI")
        print(f"{'='*70}\n")
        
        # Camera
        print("[1/2] Inizializzazione CAMERA...")
        self.camera_attiva = self.corteccia_visiva.inizializza_camera(camera_id=0)
        
        if self.camera_attiva:
            print("[OK] Camera pronta\n")
        else:
            print("[!] Camera non disponibile (usa modalita simulata)\n")
        
        # Microfono
        print("[2/2] Inizializzazione MICROFONO...")
        self.microfono_attivo = self.corteccia_uditiva.inizializza_microfono()
        
        if self.microfono_attivo:
            print("[OK] Microfono pronto\n")
        else:
            print("[!] Microfono non disponibile (usa modalita simulata)\n")
        
        # Report
        print(f"{'='*70}")
        print("[STATO SENSORI]")
        print(f"  Camera:    {'✅ ATTIVA' if self.camera_attiva else '❌ NON DISPONIBILE'}")
        print(f"  Microfono: {'✅ ATTIVO' if self.microfono_attivo else '❌ NON DISPONIBILE'}")
        print(f"{'='*70}\n")
        
        return self.camera_attiva or self.microfono_attivo
    
    def ciclo_multimodale(self) -> Dict:
        """
        Esegue ciclo cognitivo completo con input reali
        
        Returns:
            Dict con risultati
        """
        self.cicli_eseguiti += 1
        
        print(f"\n{'='*70}")
        print(f"[CICLO MULTIMODALE #{self.cicli_eseguiti}]")
        print(f"{'='*70}\n")
        
        # ================================================================
        # FASE 1: PERCEZIONE VISIVA
        # ================================================================
        print("[1/8] PERCEZIONE VISIVA...")
        
        if self.camera_attiva and self.corteccia_visiva.camera:
            # Cattura da camera reale
            ret, frame = self.corteccia_visiva.camera.read()
            if ret:
                risultato_visivo = self.corteccia_visiva.elabora(frame)
                print(f"  ✓ [REALE] {risultato_visivo['descrizione']}")
                
                # Salva frame
                cv2.imwrite(f"frame_ciclo_{self.cicli_eseguiti}.jpg", frame)
            else:
                risultato_visivo = visione.elabora("immagine.jpg")
                print(f"  ✓ [SIMULATO] {risultato_visivo['descrizione']}")
        else:
            risultato_visivo = visione.elabora("immagine.jpg")
            print(f"  ✓ [SIMULATO] {risultato_visivo['descrizione']}")
        
        # ================================================================
        # FASE 2: PERCEZIONE UDITIVA
        # ================================================================
        print("\n[2/8] PERCEZIONE UDITIVA...")
        
        if self.microfono_attivo:
            print("  🎤 Registrazione (3s)... PARLA ORA!")
            
            # Registra
            audio = sd.rec(
                int(3 * 16000),
                samplerate=16000,
                channels=1,
                device=self.corteccia_uditiva.device_id,
                dtype='float32'
            )
            sd.wait()
            
            # Trascrivi
            risultato_audio = self.corteccia_uditiva.ascolta(audio.flatten(), lingua="it")
            
            if risultato_audio['testo']:
                print(f"  ✓ [REALE] '{risultato_audio['testo']}'")
            else:
                print(f"  ✓ [SILENZIO] Nessun audio")
                risultato_audio = udito.ascolta("audio.wav")
        else:
            risultato_audio = udito.ascolta("audio.wav")
            print(f"  ✓ [SIMULATO] '{risultato_audio['testo']}'")
        
        # ================================================================
        # FASE 3: GENERAZIONE PATTERN NEURALE
        # ================================================================
        print("\n[3/8] BIOSEGNALI NEURALI...")
        
        percezioni = [risultato_visivo, risultato_audio]
        onda_percezione = self.interfaccia_neurale.percepisce_segnale(percezioni)
        
        print(f"  Pattern: {onda_percezione.pattern.replace('1', '█').replace('0', '░')}")
        print(f"  Neuroni attivi: {onda_percezione.neuroni_attivi}")
        
        # ================================================================
        # FASE 4: RICHIAMO MEMORIA
        # ================================================================
        print("\n[4/8] RICHIAMO MEMORIA...")
        
        contesto = f"{risultato_visivo['descrizione']} {risultato_audio['testo']}"
        memorie, suggerimenti = self.ippocampo.richiama_contestuale(contesto, top_k=3)
        
        if memorie:
            print(f"  ✓ Memorie: {len(memorie)}")
            for mem in memorie[:2]:
                print(f"    - {mem.contenuto[:45]}...")
        else:
            print(f"  ℹ️  Nessuna memoria rilevante")
        
        # ================================================================
        # FASE 5: VALUTAZIONE EMOTIVA
        # ================================================================
        print("\n[5/8] EMOZIONE...")
        
        risultato_emozione = self.amigdala.elabora({
            'percezioni': percezioni,
            'memoria': {'suggerimenti': suggerimenti}
        })
        
        stato_emotivo = risultato_emozione.dati['stato_emotivo']
        valenza = risultato_emozione.dati['valenza']
        
        print(f"  ✓ Stato: {stato_emotivo.upper()} (valenza: {valenza:+.2f})")
        
        # ================================================================
        # FASE 6: RAGIONAMENTO
        # ================================================================
        print("\n[6/8] RAGIONAMENTO...")
        
        decisione = prefrontale.ragiona(
            percezioni_visive=risultato_visivo,
            percezioni_uditive=risultato_audio,
            stato_emotivo=stato_emotivo,
            memoria=[m.contenuto for m in memorie]
        )
        
        # Influenza da memoria
        if suggerimenti.get('confidence', 0) > 0.7 and suggerimenti.get('azione_consigliata'):
            print(f"  💡 Memoria suggerisce: {suggerimenti['azione_consigliata']}")
            decisione['azione'] = suggerimenti['azione_consigliata']
        
        print(f"  ✓ Decisione: {decisione['azione'].upper()}")
        print(f"  ✓ Priorita: {decisione['priorita']:.2f}")
        
        # ================================================================
        # FASE 7: AZIONE
        # ================================================================
        print("\n[7/8] AZIONE...")
        successo = motoria.agisci(decisione)
        print(f"  ✓ Risultato: {'[OK]' if successo else '[FAIL]'}")
        
        # ================================================================
        # FASE 8: APPRENDIMENTO
        # ================================================================
        print("\n[8/8] APPRENDIMENTO...")
        
        reward = self.amigdala.assegna_reward(decisione['azione'], successo, valenza)
        
        self.ippocampo.memorizza(
            f"ciclo_multimodale_{self.cicli_eseguiti}",
            f"Visione: {risultato_visivo['descrizione'][:30]} | Audio: {risultato_audio['testo'][:30]} | Azione: {decisione['azione']}",
            metadata={
                'valenza': valenza,
                'importanza': reward / 2.0 + 0.5,
                'pattern_neurale': onda_percezione.pattern,
                'contesto': {
                    'visione_tipo': risultato_visivo['tipo'],
                    'audio_tipo': risultato_audio['tipo'],
                    'successo': successo
                }
            }
        )
        
        print(f"  ✓ Reward: {reward:+.2f}")
        
        # Report ciclo
        print(f"\n{'─'*70}")
        print(f"[REPORT] Ciclo #{self.cicli_eseguiti} completato")
        print(f"  Input visivo: {risultato_visivo['tipo'].upper()}")
        print(f"  Input audio: {risultato_audio['tipo'].upper()}")
        print(f"  Decisione: {decisione['azione']}")
        print(f"  Reward: {reward:+.2f}")
        print(f"{'─'*70}")
        
        return {
            'decisione': decisione,
            'successo': successo,
            'reward': reward,
            'pattern': onda_percezione.pattern
        }
    
    def esegui_sessione(self, num_cicli: int = 5):
        """
        Esegue sessione multimodale
        
        Args:
            num_cicli: Numero di cicli da eseguire
        """
        print(f"\n[SESSIONE] {num_cicli} cicli multimodali\n")
        
        try:
            for i in range(num_cicli):
                self.ciclo_multimodale()
                
                if i < num_cicli - 1:
                    input("\n[PREMI ENTER per prossimo ciclo] ")
                    
        except KeyboardInterrupt:
            print("\n\n[!] Interruzione manuale")
        
        # Report finale
        self.report_finale()
    
    def report_finale(self):
        """Report finale sessione"""
        print(f"\n{'='*70}")
        print(f"[REPORT FINALE SESSIONE MULTIMODALE]")
        print(f"{'='*70}")
        
        stats_memoria = self.ippocampo.get_statistiche()
        stats_reward = self.amigdala.get_statistiche_reward()
        
        print(f"\n[CICLI]")
        print(f"  Eseguiti: {self.cicli_eseguiti}")
        
        print(f"\n[SENSORI]")
        print(f"  Camera: {'✅' if self.camera_attiva else '❌'}")
        print(f"  Microfono: {'✅' if self.microfono_attivo else '❌'}")
        
        print(f"\n[COGNIZIONE]")
        print(f"  Memorie: {stats_memoria['memorie_episodiche']}")
        print(f"  Reward totale: {stats_reward['reward_totale']:.2f}")
        print(f"  Reward medio: {stats_reward['reward_medio']:.2f}")
        
        print(f"\n{'='*70}")
        
        # Salva
        self.ippocampo.salva_su_disco()
        print(f"[OK] Memoria salvata\n")
    
    def chiudi(self):
        """Chiude tutti i sensori"""
        if self.corteccia_visiva.camera:
            self.corteccia_visiva.camera.release()
            cv2.destroyAllWindows()
        
        print("[OK] Sensori chiusi")


if __name__ == "__main__":
    print("""
    ================================================================
    
           MENTE ARTIFICIALE MULTIMODALE v3.0
           Camera + Microfono + Biosegnali Neurali
           
    ================================================================
    """)
    
    # Verifica dipendenze
    print("\n[VERIFICA] Controllo dipendenze...")
    
    camera_disponibile = False
    try:
        import cv2
        camera_disponibile = True
        print("  ✅ OpenCV (camera)")
    except ImportError:
        print("  ❌ OpenCV non disponibile")
    
    if AUDIO_OK:
        print("  ✅ SoundDevice (microfono)")
    else:
        print("  ❌ SoundDevice non disponibile")
    
    if not camera_disponibile and not AUDIO_OK:
        print("\n[ERROR] Nessun sensore disponibile!")
        print("\nInstalla:")
        print("  pip install opencv-python sounddevice soundfile")
        sys.exit(1)
    
    # Crea mente
    mente = MenteMultimodale()
    
    # Inizializza sensori
    sensori_ok = mente.inizializza_sensori()
    
    if not sensori_ok:
        print("[ERROR] Inizializzazione fallita!")
        sys.exit(1)
    
    # Menu
    print("\n[MENU] Modalita disponibili:")
    print("  1. Ciclo singolo multimodale")
    print("  2. Sessione interattiva (5 cicli)")
    print("  3. Solo camera (streaming)")
    print("  4. Solo microfono (ascolto)")
    
    try:
        scelta = input("\n>> Scelta (1-4): ").strip()
        
        if scelta == "1":
            mente.ciclo_multimodale()
            mente.report_finale()
            
        elif scelta == "2":
            mente.esegui_sessione(num_cicli=5)
            
        elif scelta == "3":
            # Solo camera
            if mente.camera_attiva:
                print("\n[STREAMING CAMERA] Premi 'q' per uscire")
                
                while True:
                    ret, frame = mente.corteccia_visiva.camera.read()
                    if not ret:
                        break
                    
                    # Elabora ogni 15 frame
                    if mente.cicli_eseguiti % 15 == 0:
                        risultato = mente.corteccia_visiva.elabora(frame)
                        if risultato['num_oggetti'] > 0:
                            frame = visione.annota(frame, risultato)
                    
                    cv2.imshow('Camera', frame)
                    
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                    
                    mente.cicli_eseguiti += 1
                
                cv2.destroyAllWindows()
            else:
                print("[!] Camera non disponibile")
                
        elif scelta == "4":
            # Solo microfono
            if mente.microfono_attivo:
                print("\n[ASCOLTO CONTINUO] CTRL+C per uscire")
                
                try:
                    while True:
                        print(f"\n🎤 Registrazione...")
                        audio = sd.rec(int(3 * 16000), samplerate=16000, channels=1)
                        sd.wait()
                        
                        risultato = mente.corteccia_uditiva.ascolta(audio.flatten())
                        
                        if risultato['testo']:
                            print(f"  📝 '{risultato['testo']}'")
                        else:
                            print(f"  [SILENZIO]")
                        
                        time.sleep(1)
                        
                except KeyboardInterrupt:
                    print("\n[!] Interrotto")
            else:
                print("[!] Microfono non disponibile")
        else:
            print("[ERROR] Scelta non valida")
            
    except KeyboardInterrupt:
        print("\n\n[!] Interruzione")
    except Exception as e:
        print(f"\n[ERROR] {e}")
        import traceback
        traceback.print_exc()
    finally:
        mente.chiudi()

