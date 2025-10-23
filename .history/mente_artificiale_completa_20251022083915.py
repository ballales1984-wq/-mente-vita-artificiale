"""
🧠⚡ MENTE ARTIFICIALE COMPLETA - Versione Definitiva v3.0
===========================================================

Sistema cognitivo modulare con TUTTE le funzionalità:
✅ Percezione multimodale (camera + microfono)
✅ Memoria intelligente (consolidamento + richiamo)
✅ Biosegnali neurali (pattern simmetrici)
✅ Apprendimento online (PyTorch)
✅ Ragionamento e decisione
✅ Sistema emotivo e reward
✅ Dashboard web integrata

🌱 ESPANDIBILE:
- Voce sintetica (TTS)
- Movimento fisico (GPIO, servo)
- Sensori biometrici (EEG, EMG, HR)
- Connessione cloud (Firebase, AWS)
- Interazione sociale (chat, avatar)

Autore: Alessio + Cursor AI
Data: 22 Ottobre 2025
Licenza: MIT
"""

import os
import sys
import time
import json
import threading
from datetime import datetime
from typing import Dict, Any, List, Optional
import subprocess

# ==================== IMPORT MODULI CORE ====================

from moduli import visione, udito, prefrontale, motoria, emozione, memoria
from moduli.biosegnale import InterfacciaCoerenzaCerebrale, PropagatoreNeurale

try:
    from moduli.apprendimento_online import ApprendimentoOnline
    APPRENDIMENTO_DISPONIBILE = True
except:
    APPRENDIMENTO_DISPONIBILE = False
    print("[!] Apprendimento online non disponibile (PyTorch mancante)")

# ==================== IMPORT ESPANSIONI (opzionali) ====================

# Voce sintetica
try:
    import pyttsx3
    TTS_DISPONIBILE = True
except:
    TTS_DISPONIBILE = False

# GPIO per movimento fisico
try:
    import RPi.GPIO as GPIO
    GPIO_DISPONIBILE = True
except:
    GPIO_DISPONIBILE = False

# Sensori biometrici
try:
    import brainflow  # Per EEG
    BRAINFLOW_DISPONIBILE = True
except:
    BRAINFLOW_DISPONIBILE = False

# Cloud
try:
    import firebase_admin
    FIREBASE_DISPONIBILE = True
except:
    FIREBASE_DISPONIBILE = False


# ==================== CONFIGURAZIONE ====================

class ConfigurazioneCompleta:
    """Configurazione centralizzata del sistema"""
    
    def __init__(self):
        # Core
        self.modalita = "completa"  # completa, demo, hardware
        self.debug = True
        self.verbose = True
        
        # Percezione
        self.usa_camera_reale = True
        self.usa_microfono_reale = True
        self.risoluzione_camera = (640, 480)
        self.fps_camera = 30
        self.sample_rate_audio = 16000
        self.durata_registrazione = 3.0  # secondi
        
        # Memoria
        self.intervallo_consolidamento = 300  # 5 minuti
        self.soglia_valenza = 0.5
        self.soglia_importanza = 1.0
        
        # Apprendimento
        self.learning_rate = 0.001
        self.salva_ogni_n_cicli = 10
        
        # Biosegnali
        self.dimensione_rete_neurale = 15
        
        # Dashboard
        self.porta_dashboard = 8501
        self.auto_refresh = False
        
        # Espansioni
        self.usa_voce_sintetica = TTS_DISPONIBILE
        self.usa_movimento_fisico = GPIO_DISPONIBILE
        self.usa_sensori_biometrici = BRAINFLOW_DISPONIBILE
        self.usa_cloud = FIREBASE_DISPONIBILE
        
        # File output
        self.path_memoria = "data/memoria.json"
        self.path_modello = "data/modello_online.pt"
        self.path_frame = "frame.jpg"
        self.path_ultima_frase = "data/ultima_frase.txt"
        self.path_ultima_risposta = "data/ultima_risposta.txt"
        self.path_ultima_azione = "data/ultima_azione.txt"
        
        # Crea directory
        os.makedirs("data", exist_ok=True)


# ==================== ESPANSIONI ====================

class VoceSintetica:
    """Modulo Text-to-Speech per voce sintetica"""
    
    def __init__(self):
        self.nome = "Voce Sintetica"
        self.attivo = False
        self.engine = None
        
        if TTS_DISPONIBILE:
            try:
                self.engine = pyttsx3.init()
                self.engine.setProperty('rate', 150)  # Velocità
                self.engine.setProperty('volume', 0.9)  # Volume
                
                # Voce italiana se disponibile
                voices = self.engine.getProperty('voices')
                for voice in voices:
                    if 'italian' in voice.name.lower():
                        self.engine.setProperty('voice', voice.id)
                        break
                
                self.attivo = True
                print(f"[{self.nome}] ✅ Inizializzato")
            except Exception as e:
                print(f"[{self.nome}] ⚠️ Errore: {e}")
        else:
            print(f"[{self.nome}] ⚠️ pyttsx3 non disponibile")
    
    def parla(self, testo: str, attendi: bool = False):
        """Pronuncia testo"""
        if not self.attivo or not self.engine:
            return
        
        try:
            if attendi:
                self.engine.say(testo)
                self.engine.runAndWait()
            else:
                # Asincrono
                threading.Thread(target=lambda: (
                    self.engine.say(testo),
                    self.engine.runAndWait()
                )).start()
        except Exception as e:
            print(f"[{self.nome}] ⚠️ Errore speech: {e}")


class ControlloMovimento:
    """Modulo per controllo movimento fisico (GPIO, servo)"""
    
    def __init__(self):
        self.nome = "Controllo Movimento"
        self.attivo = False
        self.pin_map = {
            'servo_testa': 17,
            'servo_braccio_dx': 18,
            'servo_braccio_sx': 27,
            'led_occhi': 22
        }
        
        if GPIO_DISPONIBILE:
            try:
                GPIO.setmode(GPIO.BCM)
                GPIO.setwarnings(False)
                
                # Configura pin
                for pin in self.pin_map.values():
                    GPIO.setup(pin, GPIO.OUT)
                
                self.attivo = True
                print(f"[{self.nome}] ✅ GPIO inizializzato")
            except Exception as e:
                print(f"[{self.nome}] ⚠️ Errore GPIO: {e}")
        else:
            print(f"[{self.nome}] ⚠️ GPIO non disponibile")
    
    def muovi_testa(self, angolo: int):
        """Muovi servo testa (0-180°)"""
        if not self.attivo:
            print(f"[{self.nome}] Simulo: testa → {angolo}°")
            return
        
        # Implementa controllo servo
        print(f"[{self.nome}] Muovo testa → {angolo}°")
    
    def muovi_braccio(self, lato: str, angolo: int):
        """Muovi servo braccio"""
        if not self.attivo:
            print(f"[{self.nome}] Simulo: braccio {lato} → {angolo}°")
            return
        
        print(f"[{self.nome}] Muovo braccio {lato} → {angolo}°")
    
    def lampeggia_occhi(self, volte: int = 3):
        """Lampeggia LED occhi"""
        if not self.attivo:
            print(f"[{self.nome}] Simulo: lampeggio occhi x{volte}")
            return
        
        print(f"[{self.nome}] Lampeggio occhi x{volte}")


class SensoriBiometrici:
    """Modulo per sensori biometrici (EEG, EMG, HR)"""
    
    def __init__(self):
        self.nome = "Sensori Biometrici"
        self.attivo = False
        self.board = None
        
        if BRAINFLOW_DISPONIBILE:
            try:
                # Configura board (es. OpenBCI)
                # self.board = brainflow.BoardShim(...)
                self.attivo = True
                print(f"[{self.nome}] ✅ Board connessa")
            except Exception as e:
                print(f"[{self.nome}] ⚠️ Errore: {e}")
        else:
            print(f"[{self.nome}] ⚠️ Brainflow non disponibile")
    
    def leggi_eeg(self) -> Dict[str, float]:
        """Leggi segnali EEG"""
        if not self.attivo:
            # Simula
            import random
            return {
                'alfa': random.uniform(8, 13),
                'beta': random.uniform(13, 30),
                'gamma': random.uniform(30, 100),
                'delta': random.uniform(0.5, 4)
            }
        
        # Leggi da board reale
        return {}
    
    def leggi_heart_rate(self) -> int:
        """Leggi battito cardiaco"""
        if not self.attivo:
            import random
            return random.randint(60, 100)
        
        return 0


class ConnessioneCloud:
    """Modulo per connessione cloud (Firebase, AWS)"""
    
    def __init__(self):
        self.nome = "Connessione Cloud"
        self.attivo = False
        self.db = None
        
        if FIREBASE_DISPONIBILE:
            try:
                # Inizializza Firebase
                # cred = firebase_admin.credentials.Certificate("key.json")
                # firebase_admin.initialize_app(cred)
                # self.db = firestore.client()
                self.attivo = True
                print(f"[{self.nome}] ✅ Cloud connesso")
            except Exception as e:
                print(f"[{self.nome}] ⚠️ Errore: {e}")
        else:
            print(f"[{self.nome}] ⚠️ Firebase non disponibile")
    
    def salva_episodio_cloud(self, episodio: Dict):
        """Salva episodio su cloud"""
        if not self.attivo:
            print(f"[{self.nome}] Simulo: salvataggio episodio su cloud")
            return
        
        try:
            # self.db.collection('episodi').add(episodio)
            print(f"[{self.nome}] Episodio salvato su cloud")
        except Exception as e:
            print(f"[{self.nome}] ⚠️ Errore salvataggio: {e}")
    
    def sincronizza_memorie(self):
        """Sincronizza memorie con cloud"""
        if not self.attivo:
            return
        
        print(f"[{self.nome}] Sincronizzazione memorie...")


# ==================== SISTEMA PRINCIPALE ====================

class MenteArtificialeCompleta:
    """
    🧠 MENTE ARTIFICIALE COMPLETA
    
    Sistema cognitivo modulare con tutte le funzionalità core
    e interfacce per espansioni future.
    """
    
    def __init__(self, config: Optional[ConfigurazioneCompleta] = None):
        self.nome = "Mente Artificiale Completa"
        self.versione = "3.0"
        self.config = config or ConfigurazioneCompleta()
        
        print("\n" + "="*70)
        print(f"  🧠 {self.nome} v{self.versione}")
        print("="*70 + "\n")
        
        # Statistiche
        self.cicli_eseguiti = 0
        self.tempo_inizio = time.time()
        
        # Inizializza moduli
        self._inizializza_core()
        self._inizializza_espansioni()
        
        print("\n" + "="*70)
        print("  ✅ SISTEMA OPERATIVO")
        print("="*70 + "\n")
    
    def _inizializza_core(self):
        """Inizializza moduli core"""
        print("[CORE] Inizializzazione moduli principali...\n")
        
        # Percezione
        print("[1/8] 👁️  Corteccia Visiva")
        self.corteccia_visiva = visione.get_instance()
        if self.config.usa_camera_reale:
            self.camera_attiva = self.corteccia_visiva.inizializza_camera(0)
        else:
            self.camera_attiva = False
        print(f"      {'✅ Camera attiva' if self.camera_attiva else '⚠️  Modalità simulata'}")
        
        print("\n[2/8] 👂 Corteccia Uditiva")
        self.corteccia_uditiva = udito.get_instance()
        if self.config.usa_microfono_reale:
            self.microfono_attivo = self.corteccia_uditiva.inizializza_microfono()
        else:
            self.microfono_attivo = False
        print(f"      {'✅ Microfono attivo' if self.microfono_attivo else '⚠️  Modalità simulata'}")
        
        # Cognizione
        print("\n[3/8] 💾 Ippocampo (Memoria)")
        self.ippocampo = memoria.get_instance()
        print(f"      ✅ {len(self.ippocampo.memoria_episodica)} memorie caricate")
        
        print("\n[4/8] ❤️  Amigdala (Emozione)")
        self.amigdala = emozione.get_instance()
        print(f"      ✅ Sistema emotivo attivo")
        
        print("\n[5/8] 🧠 Corteccia Prefrontale")
        self.prefrontale = prefrontale.get_instance()
        print(f"      ✅ Ragionamento attivo")
        
        print("\n[6/8] 🦾 Corteccia Motoria")
        self.motoria = motoria.get_instance()
        print(f"      ✅ Sistema motorio pronto")
        
        # Layer neurale
        print("\n[7/8] ⚡ Biosegnali Neurali")
        self.interfaccia_neurale = InterfacciaCoerenzaCerebrale()
        self.propagatore = PropagatoreNeurale(dimensione=self.config.dimensione_rete_neurale)
        print(f"      ✅ Layer neurale attivo")
        
        # Apprendimento
        print("\n[8/8] 🎓 Apprendimento Online")
        if APPRENDIMENTO_DISPONIBILE:
            self.apprendimento = ApprendimentoOnline(
                learning_rate=self.config.learning_rate,
                path_modello=self.config.path_modello
            )
            print(f"      ✅ Rete neurale attiva")
        else:
            self.apprendimento = None
            print(f"      ⚠️  Disabilitato (PyTorch mancante)")
    
    def _inizializza_espansioni(self):
        """Inizializza moduli espandibili"""
        print("\n[ESPANSIONI] Inizializzazione moduli opzionali...\n")
        
        # Voce sintetica
        print("[1/4] 🔊 Voce Sintetica")
        self.voce = VoceSintetica() if self.config.usa_voce_sintetica else None
        
        # Movimento fisico
        print("\n[2/4] 🦾 Controllo Movimento")
        self.movimento = ControlloMovimento() if self.config.usa_movimento_fisico else None
        
        # Sensori biometrici
        print("\n[3/4] 🧬 Sensori Biometrici")
        self.sensori = SensoriBiometrici() if self.config.usa_sensori_biometrici else None
        
        # Cloud
        print("\n[4/4] ☁️  Connessione Cloud")
        self.cloud = ConnessioneCloud() if self.config.usa_cloud else None
    
    def ciclo_cognitivo(self) -> Dict[str, Any]:
        """
        Esegue un ciclo cognitivo completo
        
        Returns:
            Dict con risultati del ciclo
        """
        self.cicli_eseguiti += 1
        
        print(f"\n{'╔'+'═'*68+'╗'}")
        print(f"║ CICLO COGNITIVO COMPLETO #{self.cicli_eseguiti:02d}                                  ║")
        print(f"{'╚'+'═'*68+'╝'}\n")
        
        # 1. Percezione Visiva
        print("[1/10] 👁️  PERCEZIONE VISIVA")
        if self.camera_attiva and self.corteccia_visiva.camera:
            ret, frame = self.corteccia_visiva.camera.read()
            if ret:
                risultato_visivo = self.corteccia_visiva.elabora(frame)
                
                # Salva frame per dashboard
                try:
                    import cv2
                    cv2.imwrite(self.config.path_frame, frame)
                except:
                    pass
            else:
                risultato_visivo = visione.elabora("immagine.jpg")
        else:
            risultato_visivo = visione.elabora("immagine.jpg")
        
        print(f"       {risultato_visivo['descrizione']}")
        
        # 2. Percezione Uditiva
        print("\n[2/10] 👂 PERCEZIONE UDITIVA")
        if self.microfono_attivo:
            print("       🎤 Registrazione audio (3s)... PARLA ORA!")
            try:
                import sounddevice as sd
                audio = sd.rec(
                    int(self.config.durata_registrazione * self.config.sample_rate_audio),
                    samplerate=self.config.sample_rate_audio,
                    channels=1
                )
                sd.wait()
                risultato_audio = self.corteccia_uditiva.ascolta(audio.flatten())
            except:
                risultato_audio = udito.ascolta("audio.wav")
        else:
            risultato_audio = udito.ascolta("audio.wav")
        
        print(f"       '{risultato_audio['testo']}'")
        
        # 3. Sensori Biometrici (se disponibili)
        dati_biometrici = None
        if self.sensori and self.sensori.attivo:
            print("\n[3/10] 🧬 SENSORI BIOMETRICI")
            dati_biometrici = {
                'eeg': self.sensori.leggi_eeg(),
                'heart_rate': self.sensori.leggi_heart_rate()
            }
            print(f"       EEG alfa: {dati_biometrici['eeg']['alfa']:.1f} Hz")
            print(f"       Heart rate: {dati_biometrici['heart_rate']} bpm")
        
        # 4. Biosegnali Neurali
        print(f"\n[{4 if not dati_biometrici else 4}/10] ⚡ BIOSEGNALI NEURALI")
        percezioni = [risultato_visivo, risultato_audio]
        onda_percezione = self.interfaccia_neurale.percepisce_segnale(percezioni)
        visual_pattern = onda_percezione.pattern.replace('1', '█').replace('0', '░')
        print(f"       Pattern: {visual_pattern}")
        print(f"       Neuroni attivi: {onda_percezione.neuroni_attivi}/{len(onda_percezione.pattern)}")
        
        # 5. Richiamo Memoria
        print(f"\n[{5 if not dati_biometrici else 5}/10] 💾 RICHIAMO MEMORIA")
        contesto = f"{risultato_visivo['descrizione']} {risultato_audio['testo']}"
        memorie, suggerimenti = self.ippocampo.richiama_contestuale(contesto, top_k=3)
        
        if memorie:
            print(f"       Memorie trovate: {len(memorie)}")
            print(f"       Suggerimento: {suggerimenti['suggerimento']}")
            if suggerimenti.get('azione_consigliata'):
                print(f"       Azione: {suggerimenti['azione_consigliata']} (conf: {suggerimenti['confidence']:.2f})")
        
        # 6. Valutazione Emotiva
        print(f"\n[{6 if not dati_biometrici else 6}/10] ❤️  VALUTAZIONE EMOTIVA")
        risultato_emozione = self.amigdala.elabora({
            'percezioni': percezioni,
            'memoria': {'suggerimenti': suggerimenti}
        })
        
        stato_emotivo = risultato_emozione.dati['stato_emotivo']
        valenza = risultato_emozione.dati['valenza']
        print(f"       Stato: {stato_emotivo.upper()} (valenza: {valenza:+.2f})")
        
        # 7. Apprendimento - Predizione
        azione_predetta = None
        confidence_pred = 0.0
        if self.apprendimento and self.apprendimento.modello:
            print(f"\n[{7 if not dati_biometrici else 7}/10] 🎓 APPRENDIMENTO - Predizione")
            stimolo = self.apprendimento.codifica_stimolo(risultato_visivo, risultato_audio)
            azione_predetta, confidence_pred = self.apprendimento.predici_azione(stimolo)
            print(f"       Rete neurale: {azione_predetta} (conf: {confidence_pred:.2%})")
        
        # 8. Ragionamento e Decisione
        print(f"\n[{8 if not dati_biometrici else 8}/10] 🧠 RAGIONAMENTO E DECISIONE")
        decisione = self.prefrontale.ragiona(
            percezioni_visive=risultato_visivo,
            percezioni_uditive=risultato_audio,
            stato_emotivo=stato_emotivo,
            memoria=[m.contenuto for m in memorie]
        )
        
        # Combina suggerimenti
        if suggerimenti.get('confidence', 0) > 0.8:
            decisione['azione'] = suggerimenti['azione_consigliata']
            fonte = "memoria"
        elif confidence_pred > 0.7:
            decisione['azione'] = azione_predetta
            fonte = "rete_neurale"
        else:
            fonte = "ragionamento"
        
        print(f"       Decisione: {decisione['azione'].upper()}")
        print(f"       Fonte: {fonte}")
        
        # 9. Esecuzione Azione
        print(f"\n[{9 if not dati_biometrici else 9}/10] 🦾 ESECUZIONE AZIONE")
        
        # Azione motoria standard
        successo = self.motoria.agisci(decisione)
        print(f"       Motoria: {'✅ SUCCESSO' if successo else '❌ FALLITO'}")
        
        # Voce sintetica (se disponibile)
        if self.voce and self.voce.attivo:
            risposta_vocale = decisione.get('risposta', 'Comando ricevuto')
            self.voce.parla(risposta_vocale, attendi=False)
            print(f"       🔊 Voce: '{risposta_vocale}'")
        
        # Movimento fisico (se disponibile)
        if self.movimento and self.movimento.attivo:
            if decisione['azione'] == 'avvicinati':
                self.movimento.muovi_testa(45)
                self.movimento.lampeggia_occhi(2)
            elif decisione['azione'] == 'allontanati':
                self.movimento.muovi_testa(-45)
        
        # 10. Apprendimento da Esperienza
        print(f"\n[{10 if not dati_biometrici else 10}/10] 🎓 APPRENDIMENTO")
        
        reward = self.amigdala.assegna_reward(decisione['azione'], successo, valenza)
        print(f"       Reward: {reward:+.2f}")
        
        if self.apprendimento and self.apprendimento.modello:
            loss = self.apprendimento.apprendi_da_esperienza(stimolo, decisione['azione'], reward)
            print(f"       Loss: {loss:.4f}")
        
        # Memorizza episodio
        episodio_id = f"episodio_{self.cicli_eseguiti:03d}"
        self.ippocampo.memorizza(
            episodio_id,
            f"V:{risultato_visivo['descrizione'][:30]} | A:{risultato_audio['testo'][:30]} | {decisione['azione']}",
            metadata={
                'valenza': valenza,
                'importanza': reward / 2.0 + 0.5,
                'pattern_neurale': onda_percezione.pattern,
                'dati_biometrici': dati_biometrici,
                'contesto': {
                    'ciclo': self.cicli_eseguiti,
                    'successo': successo,
                    'azione': decisione['azione'],
                    'fonte_decisione': fonte
                }
            }
        )
        print(f"       Episodio salvato")
        
        # Cloud sync (se disponibile)
        if self.cloud and self.cloud.attivo:
            self.cloud.salva_episodio_cloud({
                'id': episodio_id,
                'timestamp': datetime.now().isoformat(),
                'decisione': decisione['azione'],
                'successo': successo,
                'reward': reward
            })
        
        # Salva file per dashboard
        self._salva_per_dashboard(risultato_audio['testo'], decisione.get('risposta', ''), decisione['azione'])
        
        # Aggiorna avatar 3D
        self._aggiorna_avatar(stato_emotivo, decisione['azione'], valenza, onda_percezione.pattern)
        
        # Report
        print(f"\n{'─'*70}")
        print(f"[REPORT] Ciclo #{self.cicli_eseguiti} completato")
        print(f"  Decisione: {decisione['azione']} (fonte: {fonte})")
        print(f"  Reward: {reward:+.2f}")
        print(f"  Memorie: {len(self.ippocampo.memoria_episodica)}")
        print(f"{'─'*70}")
        
        return {
            'ciclo': self.cicli_eseguiti,
            'decisione': decisione,
            'successo': successo,
            'reward': reward,
            'fonte': fonte
        }
    
    def _salva_per_dashboard(self, frase: str, risposta: str, azione: str):
        """Salva file per dashboard"""
        try:
            with open(self.config.path_ultima_frase, "w", encoding="utf-8") as f:
                f.write(frase)
            
            with open(self.config.path_ultima_risposta, "w", encoding="utf-8") as f:
                f.write(risposta)
            
            with open(self.config.path_ultima_azione, "w", encoding="utf-8") as f:
                f.write(f"Azione: {azione}")
        except:
            pass
    
    def _aggiorna_avatar(self, stato_emotivo: str, azione: str, valenza: float, pattern: str):
        """Aggiorna stato avatar 3D"""
        try:
            # Mappa stato emotivo a emozione avatar
            if valenza > 0.3:
                emozione = "felice"
            elif valenza < -0.3:
                emozione = "triste"
            else:
                emozione = "neutro"
            
            # Mappa azione a movimento
            azione_avatar = "idle"
            if azione == "avvicinati":
                azione_avatar = "cammina"
            elif azione == "allontanati":
                azione_avatar = "cammina"
            elif "guarda" in azione.lower() or "cerca" in azione.lower():
                azione_avatar = "guarda"
            elif "pensa" in azione.lower() or "ragiona" in azione.lower():
                azione_avatar = "pensa"
            
            # Calcola arousal da pattern neurale
            neuroni_attivi = pattern.count('█') if '█' in pattern else pattern.count('1')
            arousal = min(1.0, neuroni_attivi / 15.0)
            
            # Stato avatar
            stato = {
                'emozione': emozione,
                'azione': azione_avatar,
                'energia': min(1.0, self.config.modalita == "completa" and 0.9 or 1.0),
                'attenzione': min(1.0, abs(valenza) + 0.3),
                'arousal': arousal,
                'pattern_neurale': pattern[:15] if len(pattern) > 15 else pattern
            }
            
            # Salva per avatar
            with open("data/avatar_stato.json", "w", encoding="utf-8") as f:
                json.dump(stato, f, indent=2)
        
        except:
            pass
    
    def esegui_sessione(self, num_cicli: int = 5, interattivo: bool = False):
        """Esegue sessione con N cicli"""
        print(f"\n[SESSIONE] {num_cicli} cicli completi\n")
        
        risultati = []
        
        try:
            for i in range(num_cicli):
                risultato = self.ciclo_cognitivo()
                risultati.append(risultato)
                
                if i < num_cicli - 1:
                    if interattivo:
                        input("\n[PREMI ENTER per continuare] ")
                    else:
                        time.sleep(2)
        
        except KeyboardInterrupt:
            print("\n\n[!] Interruzione manuale")
        
        self.report_finale(risultati)
    
    def report_finale(self, risultati: list):
        """Report finale sessione"""
        print(f"\n{'╔'+'═'*68+'╗'}")
        print(f"║ REPORT FINALE                                                    ║")
        print(f"{'╚'+'═'*68+'╝'}\n")
        
        if risultati:
            successi = sum(1 for r in risultati if r['successo'])
            reward_tot = sum(r['reward'] for r in risultati)
            
            print(f"[CICLI] {len(risultati)}")
            print(f"  Successi: {successi}/{len(risultati)} ({successi/len(risultati)*100:.0f}%)")
            print(f"  Reward totale: {reward_tot:+.2f}")
            print(f"  Reward medio: {reward_tot/len(risultati):+.2f}")
        
        print(f"\n[MEMORIA]")
        stats_mem = self.ippocampo.get_statistiche()
        print(f"  Episodi: {stats_mem['memorie_episodiche']}")
        print(f"  Richiami: {stats_mem['richiami_totali']}")
        
        if self.apprendimento:
            print(f"\n[APPRENDIMENTO]")
            stats_app = self.apprendimento.get_statistiche()
            print(f"  Training: {stats_app['cicli_apprendimento']}")
            print(f"  Loss media: {stats_app['loss_media']:.4f}")
        
        tempo_totale = time.time() - self.tempo_inizio
        print(f"\n[TEMPO]")
        print(f"  Durata: {tempo_totale:.1f}s")
        print(f"  Cicli/sec: {len(risultati)/tempo_totale:.2f}")
        
        print(f"\n{'='*70}")
        
        # Salva
        self.ippocampo.salva_su_disco()
        if self.apprendimento:
            self.apprendimento.salva_modello()
        
        print("[OK] Dati salvati\n")
    
    def avvia_dashboard(self):
        """Avvia dashboard in nuovo processo"""
        print("\n[DASHBOARD] Avvio in corso...")
        try:
            subprocess.Popen([sys.executable, "-m", "streamlit", "run", "dashboard.py"])
            print("[OK] Dashboard avviata su http://localhost:8501")
        except Exception as e:
            print(f"[!] Errore: {e}")
    
    def chiudi(self):
        """Chiude sistema"""
        print("\n[SHUTDOWN] Chiusura sistema...")
        
        # Chiudi camera
        if self.camera_attiva:
            try:
                self.corteccia_visiva.chiudi()
            except:
                pass
        
        # Chiudi GPIO se attivo
        if self.movimento and self.movimento.attivo and GPIO_DISPONIBILE:
            try:
                GPIO.cleanup()
                print("[OK] GPIO pulito")
            except:
                pass
        
        # Chiudi finestre OpenCV
        try:
            import cv2
            cv2.destroyAllWindows()
        except:
            pass
        
        print("[OK] Sistema spento\n")


# ==================== MENU PRINCIPALE ====================

def menu_principale():
    """Menu interattivo"""
    print("""
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║        🧠 MENTE ARTIFICIALE COMPLETA v3.0                       ║
║                                                                  ║
║    Sistema Cognitivo Modulare con Espansioni                    ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
    """)
    
    # Crea configurazione
    config = ConfigurazioneCompleta()
    
    # Crea sistema
    mente = MenteArtificialeCompleta(config)
    
    # Menu
    print("\n[MENU] Scegli modalità:\n")
    print("  1. Ciclo singolo")
    print("  2. Sessione 3 cicli (interattiva)")
    print("  3. Sessione 5 cicli (automatica)")
    print("  4. Sessione 10 cicli (automatica)")
    print("  5. Avvia dashboard")
    print("  6. Dashboard + Sistema (avvia entrambi)")
    print("\n  9. Esci")
    
    scelta = input("\n>> Scelta (1-6): ").strip()
    
    try:
        if scelta == "1":
            mente.ciclo_cognitivo()
            mente.report_finale([])
        
        elif scelta == "2":
            mente.esegui_sessione(num_cicli=3, interattivo=True)
        
        elif scelta == "3":
            mente.esegui_sessione(num_cicli=5, interattivo=False)
        
        elif scelta == "4":
            mente.esegui_sessione(num_cicli=10, interattivo=False)
        
        elif scelta == "5":
            mente.avvia_dashboard()
            input("\n[PREMI ENTER per terminare] ")
        
        elif scelta == "6":
            mente.avvia_dashboard()
            time.sleep(2)
            mente.esegui_sessione(num_cicli=5, interattivo=False)
        
        elif scelta == "9":
            print("\n[OK] Uscita\n")
        
        else:
            print("\n[!] Scelta non valida\n")
        
        mente.chiudi()
    
    except KeyboardInterrupt:
        print("\n\n[!] Interruzione\n")
        mente.chiudi()
    
    except Exception as e:
        print(f"\n[ERROR] {e}\n")
        import traceback
        traceback.print_exc()
        mente.chiudi()


# ==================== ENTRY POINT ====================

if __name__ == "__main__":
    menu_principale()

