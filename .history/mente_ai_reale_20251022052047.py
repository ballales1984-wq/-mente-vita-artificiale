"""
🧠 MENTE ARTIFICIALE REALE - Implementazione con modelli open-source
=====================================================================
Sistema cognitivo modulare con:
- Whisper (OpenAI) per audio
- YOLOv8 per visione
- LLaMA/GPT-J per ragionamento
- Integrazione hardware reale (Raspberry Pi / AI PC)
"""

import asyncio
import time
import threading
import queue
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from enum import Enum
import json
import numpy as np
from datetime import datetime

# ==================== IMPORTS MODELLI AI ====================
# Installare con: pip install -r requirements.txt

try:
    # Visione - YOLOv8
    from ultralytics import YOLO
    YOLO_AVAILABLE = True
except ImportError:
    YOLO_AVAILABLE = False
    print("⚠️  YOLOv8 non disponibile. Usa modalità simulazione per visione.")

try:
    # Audio - Whisper
    import whisper
    WHISPER_AVAILABLE = True
except ImportError:
    WHISPER_AVAILABLE = False
    print("⚠️  Whisper non disponibile. Usa modalità simulazione per audio.")

try:
    # LLM - Transformers
    from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
    import torch
    LLM_AVAILABLE = True
except ImportError:
    LLM_AVAILABLE = False
    print("⚠️  Transformers non disponibile. Usa modalità simulazione per LLM.")

try:
    # Audio input
    import sounddevice as sd
    import soundfile as sf
    AUDIO_INPUT_AVAILABLE = True
except ImportError:
    AUDIO_INPUT_AVAILABLE = False
    print("⚠️  Sounddevice non disponibile. Audio input disabilitato.")

try:
    # Video input
    import cv2
    VIDEO_AVAILABLE = True
except ImportError:
    VIDEO_AVAILABLE = False
    print("⚠️  OpenCV non disponibile. Video input disabilitato.")


# ==================== CONFIGURAZIONE ====================

class Config:
    """Configurazione sistema"""
    
    # Modelli
    YOLO_MODEL = "yolov8n.pt"  # nano model per Raspberry Pi
    WHISPER_MODEL = "base"  # tiny, base, small, medium, large
    LLM_MODEL = "gpt2"  # gpt2, gpt-j-6b, llama-2-7b
    
    # Hardware
    CAMERA_INDEX = 0
    CAMERA_WIDTH = 640
    CAMERA_HEIGHT = 480
    CAMERA_FPS = 15
    
    AUDIO_SAMPLE_RATE = 16000
    AUDIO_CHANNELS = 1
    AUDIO_DURATION = 3  # secondi
    
    # Performance
    USE_GPU = torch.cuda.is_available() if LLM_AVAILABLE else False
    DEVICE = "cuda" if USE_GPU else "cpu"
    
    # Thresholds
    YOLO_CONFIDENCE = 0.5
    AUDIO_ENERGY_THRESHOLD = 0.01
    
    # Sistema
    COGNITIVE_CYCLE_DELAY = 0.1  # secondi
    BATTERY_DRAIN_RATE = 0.3  # % per ciclo


# ==================== STRUTTURE DATI ====================

class StatoEmotivo(Enum):
    NEUTRO = "neutro"
    POSITIVO = "positivo"
    NEGATIVO = "negativo"
    ALLERTA = "allerta"
    CALMO = "calmo"


@dataclass
class DatoSensoriale:
    tipo: str
    contenuto: Any
    timestamp: float
    priorita: int = 1
    metadata: Dict = field(default_factory=dict)


@dataclass
class PercezioneElaborata:
    tipo: str
    descrizione: str
    entita: List[str]
    rilevanza: float
    timestamp: float
    dati_raw: Optional[Any] = None


@dataclass
class StatoInterno:
    energia: float = 100.0
    temperatura: float = 45.0
    carico_cognitivo: float = 0.3
    stato_emotivo: StatoEmotivo = StatoEmotivo.NEUTRO
    allerta: float = 0.5
    cicli_eseguiti: int = 0


# ==================== MODULI PERCETTIVI REALI ====================

class ModuloVisioneReale:
    """Elaborazione visiva con YOLOv8"""
    
    def __init__(self):
        self.nome = "Modulo Visione (YOLOv8)"
        self.model = None
        self.camera = None
        self.attivo = False
        
        if YOLO_AVAILABLE:
            try:
                print(f"🔵 [{self.nome}] Caricamento modello YOLOv8...")
                self.model = YOLO(Config.YOLO_MODEL)
                print(f"✅ Modello caricato: {Config.YOLO_MODEL}")
            except Exception as e:
                print(f"❌ Errore caricamento YOLO: {e}")
                
        if VIDEO_AVAILABLE:
            try:
                self.camera = cv2.VideoCapture(Config.CAMERA_INDEX)
                self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, Config.CAMERA_WIDTH)
                self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, Config.CAMERA_HEIGHT)
                self.camera.set(cv2.CAP_PROP_FPS, Config.CAMERA_FPS)
                self.attivo = True
                print(f"✅ Camera inizializzata")
            except Exception as e:
                print(f"❌ Errore inizializzazione camera: {e}")
    
    def cattura_frame(self) -> Optional[np.ndarray]:
        """Cattura frame dalla camera"""
        if not self.attivo or self.camera is None:
            return None
            
        ret, frame = self.camera.read()
        if ret:
            return frame
        return None
    
    def rileva_oggetti(self, frame: np.ndarray) -> List[Dict]:
        """Rileva oggetti nel frame usando YOLO"""
        if self.model is None:
            return []
        
        try:
            results = self.model(frame, conf=Config.YOLO_CONFIDENCE, verbose=False)
            
            detections = []
            for result in results:
                boxes = result.boxes
                for box in boxes:
                    cls = int(box.cls[0])
                    conf = float(box.conf[0])
                    coords = box.xyxy[0].tolist()
                    
                    detections.append({
                        'classe': result.names[cls],
                        'confidenza': conf,
                        'bbox': coords
                    })
            
            return detections
        except Exception as e:
            print(f"❌ Errore rilevamento: {e}")
            return []
    
    def processa(self, frame: Optional[np.ndarray] = None) -> List[PercezioneElaborata]:
        """Pipeline completa: cattura + rilevamento"""
        print(f"  👁️  [{self.nome}] Elaborazione frame...")
        
        if frame is None:
            frame = self.cattura_frame()
        
        if frame is None:
            return self._percezione_simulata()
        
        detections = self.rileva_oggetti(frame)
        
        percezioni = []
        for det in detections:
            rilevanza = det['confidenza']
            if det['classe'] == 'person':
                rilevanza += 0.2
                
            percezione = PercezioneElaborata(
                tipo="visivo",
                descrizione=f"{det['classe']} rilevata (conf: {det['confidenza']:.2f})",
                entita=[det['classe'], "oggetto_fisico"],
                rilevanza=rilevanza,
                timestamp=time.time(),
                dati_raw=det
            )
            percezioni.append(percezione)
        
        if percezioni:
            print(f"  ✅ Rilevati {len(percezioni)} oggetti")
        
        return percezioni
    
    def _percezione_simulata(self) -> List[PercezioneElaborata]:
        """Fallback simulato se hardware non disponibile"""
        return [
            PercezioneElaborata(
                tipo="visivo",
                descrizione="[SIMULATO] Ambiente indoor, nessun movimento",
                entita=["ambiente", "statico"],
                rilevanza=0.3,
                timestamp=time.time()
            )
        ]
    
    def chiudi(self):
        """Rilascia risorse"""
        if self.camera is not None:
            self.camera.release()


class ModuloAudioReale:
    """Elaborazione audio con Whisper"""
    
    def __init__(self):
        self.nome = "Modulo Audio (Whisper)"
        self.model = None
        
        if WHISPER_AVAILABLE:
            try:
                print(f"🔵 [{self.nome}] Caricamento modello Whisper...")
                self.model = whisper.load_model(Config.WHISPER_MODEL)
                print(f"✅ Modello caricato: {Config.WHISPER_MODEL}")
            except Exception as e:
                print(f"❌ Errore caricamento Whisper: {e}")
    
    def registra_audio(self, durata: float = None) -> Optional[np.ndarray]:
        """Registra audio dal microfono"""
        if not AUDIO_INPUT_AVAILABLE:
            return None
        
        durata = durata or Config.AUDIO_DURATION
        
        try:
            print(f"  🎤 Registrazione {durata}s...")
            audio = sd.rec(
                int(durata * Config.AUDIO_SAMPLE_RATE),
                samplerate=Config.AUDIO_SAMPLE_RATE,
                channels=Config.AUDIO_CHANNELS,
                dtype='float32'
            )
            sd.wait()
            
            # Check se c'è suono significativo
            energy = np.sum(audio ** 2) / len(audio)
            if energy < Config.AUDIO_ENERGY_THRESHOLD:
                return None
                
            return audio.flatten()
        except Exception as e:
            print(f"❌ Errore registrazione audio: {e}")
            return None
    
    def trascrivi(self, audio: np.ndarray) -> Optional[str]:
        """Trascrivi audio in testo usando Whisper"""
        if self.model is None or audio is None:
            return None
        
        try:
            result = self.model.transcribe(
                audio,
                language="it",
                fp16=False
            )
            return result['text'].strip()
        except Exception as e:
            print(f"❌ Errore trascrizione: {e}")
            return None
    
    def processa(self, audio: Optional[np.ndarray] = None) -> List[PercezioneElaborata]:
        """Pipeline completa: registra + trascrivi"""
        print(f"  👂 [{self.nome}] Elaborazione audio...")
        
        if audio is None:
            audio = self.registra_audio()
        
        if audio is None:
            return []
        
        testo = self.trascrivi(audio)
        
        if not testo:
            return []
        
        print(f"  ✅ Trascritto: '{testo}'")
        
        # Analisi sentiment base
        tono = "neutro"
        if any(word in testo.lower() for word in ["aiuto", "pericolo", "urgente"]):
            tono = "urgente"
        elif any(word in testo.lower() for word in ["bene", "grazie", "perfetto"]):
            tono = "positivo"
        
        percezione = PercezioneElaborata(
            tipo="uditivo",
            descrizione=f"Comando vocale: '{testo}' (tono: {tono})",
            entita=["voce_umana", "comando", tono],
            rilevanza=0.85,
            timestamp=time.time(),
            dati_raw={"testo": testo, "tono": tono}
        )
        
        return [percezione]


class ModuloRagionamentoReale:
    """Ragionamento con LLM (GPT-2 / GPT-J / LLaMA)"""
    
    def __init__(self):
        self.nome = "Modulo Ragionamento (LLM)"
        self.tokenizer = None
        self.model = None
        self.generator = None
        
        if LLM_AVAILABLE:
            try:
                print(f"🔵 [{self.nome}] Caricamento modello {Config.LLM_MODEL}...")
                
                self.tokenizer = AutoTokenizer.from_pretrained(Config.LLM_MODEL)
                
                # Carica modello con ottimizzazioni
                if Config.LLM_MODEL == "gpt2":
                    self.generator = pipeline(
                        'text-generation',
                        model=Config.LLM_MODEL,
                        device=0 if Config.USE_GPU else -1
                    )
                else:
                    self.model = AutoModelForCausalLM.from_pretrained(
                        Config.LLM_MODEL,
                        torch_dtype=torch.float16 if Config.USE_GPU else torch.float32,
                        device_map="auto" if Config.USE_GPU else None
                    )
                
                print(f"✅ Modello caricato su {Config.DEVICE}")
            except Exception as e:
                print(f"❌ Errore caricamento LLM: {e}")
    
    def ragiona(self, contesto: str, query: str) -> str:
        """Genera ragionamento usando LLM"""
        if self.generator is None:
            return self._ragionamento_rule_based(contesto, query)
        
        try:
            prompt = f"""Contesto: {contesto}
Domanda: {query}
Risposta breve e concisa:"""
            
            output = self.generator(
                prompt,
                max_length=150,
                num_return_sequences=1,
                temperature=0.7,
                do_sample=True
            )
            
            risposta = output[0]['generated_text']
            risposta = risposta.replace(prompt, "").strip()
            return risposta
        except Exception as e:
            print(f"❌ Errore generazione: {e}")
            return self._ragionamento_rule_based(contesto, query)
    
    def _ragionamento_rule_based(self, contesto: str, query: str) -> str:
        """Fallback: ragionamento basato su regole"""
        if "pericolo" in contesto.lower():
            return "Rilevato potenziale pericolo. Azione: allontanarsi con cautela."
        elif "persona" in contesto.lower():
            return "Presenza umana rilevata. Azione: mantieni distanza sicura."
        elif "comando" in contesto.lower():
            return "Comando ricevuto. Analisi: posso eseguirlo in sicurezza."
        else:
            return "Situazione normale. Azione: continua monitoraggio."


# ==================== ARCHITETTURA COGNITIVA COMPLETA ====================

class Talamo:
    """Router centrale multimodale"""
    
    def __init__(self):
        self.nome = "Talamo"
        self.visione = ModuloVisioneReale()
        self.audio = ModuloAudioReale()
        self.queue_percezioni = queue.Queue()
    
    def ciclo_percettivo(self, frame=None, audio=None) -> List[PercezioneElaborata]:
        """Elabora input multimodali"""
        print(f"\n⚡ [{self.nome}] Elaborazione multimodale...")
        
        percezioni = []
        
        # Elaborazione parallela (se possibile)
        percezioni_visive = self.visione.processa(frame)
        percezioni_uditive = self.audio.processa(audio)
        
        percezioni.extend(percezioni_visive)
        percezioni.extend(percezioni_uditive)
        
        return percezioni
    
    def chiudi(self):
        self.visione.chiudi()


class Ippocampo:
    """Sistema di memoria"""
    
    def __init__(self):
        self.nome = "Ippocampo"
        self.memoria_episodica = []
        self.memoria_semantica = {
            "comandi_noti": ["vieni", "fermati", "seguimi", "aspetta", "vai"],
            "oggetti_comuni": ["person", "car", "chair", "bottle", "phone"],
            "livelli_pericolo": {
                "car": 0.7,
                "person": 0.2,
                "chair": 0.1
            }
        }
    
    def memorizza(self, evento: str, contesto: Dict, valenza: float):
        """Salva evento in memoria episodica"""
        memoria = {
            "evento": evento,
            "contesto": contesto,
            "valenza": valenza,
            "timestamp": time.time()
        }
        self.memoria_episodica.append(memoria)
        
        # Mantieni solo ultime 100 memorie
        if len(self.memoria_episodica) > 100:
            self.memoria_episodica = self.memoria_episodica[-100:]
    
    def query_semantica(self, chiave: str) -> Any:
        """Recupera conoscenza semantica"""
        return self.memoria_semantica.get(chiave)


class Amigdala:
    """Valutazione emotiva e reward"""
    
    def __init__(self):
        self.nome = "Amigdala"
        self.stato = StatoEmotivo.NEUTRO
        self.storia_reward = []
    
    def valuta_emozione(self, percezioni: List[PercezioneElaborata], memoria: Ippocampo) -> StatoEmotivo:
        """Calcola stato emotivo basato su percezioni"""
        print(f"  ❤️  [{self.nome}] Valutazione emotiva...")
        
        valenza = 0.0
        
        for p in percezioni:
            # Check pericoli dalla memoria semantica
            livelli_pericolo = memoria.query_semantica("livelli_pericolo") or {}
            
            for entita in p.entita:
                if entita in livelli_pericolo:
                    valenza -= livelli_pericolo[entita]
            
            # Fattori positivi
            if "comando" in p.entita:
                valenza += 0.3
            if p.rilevanza > 0.8:
                valenza += 0.2
        
        # Determina stato
        if valenza > 0.4:
            self.stato = StatoEmotivo.POSITIVO
        elif valenza < -0.4:
            self.stato = StatoEmotivo.NEGATIVO
        elif valenza < -0.2:
            self.stato = StatoEmotivo.ALLERTA
        else:
            self.stato = StatoEmotivo.NEUTRO
        
        print(f"  💚 Stato: {self.stato.value} (valenza: {valenza:.2f})")
        return self.stato
    
    def reward(self, azione: str, successo: bool) -> float:
        """Sistema di ricompensa"""
        r = 1.0 if successo else -0.5
        self.storia_reward.append((azione, r, time.time()))
        return r


class CortecciaPrefrontale:
    """Decision making con LLM"""
    
    def __init__(self, ippocampo: Ippocampo, amigdala: Amigdala):
        self.nome = "Corteccia Prefrontale"
        self.ippocampo = ippocampo
        self.amigdala = amigdala
        self.llm = ModuloRagionamentoReale()
    
    def analizza_e_decidi(self, percezioni: List[PercezioneElaborata]) -> Dict[str, Any]:
        """Decision making di alto livello"""
        print(f"\n🧠 [{self.nome}] Analisi e decisione...")
        
        # Costruisci contesto
        contesto_str = self._costruisci_contesto(percezioni)
        
        # Ragionamento LLM
        ragionamento = self.llm.ragiona(
            contesto_str,
            "Quale azione dovrei intraprendere?"
        )
        
        print(f"  💭 Ragionamento: {ragionamento}")
        
        # Decisione strutturata
        decisione = self._genera_decisione(percezioni, ragionamento)
        
        print(f"  ✅ Decisione: {decisione['azione']}")
        
        return decisione
    
    def _costruisci_contesto(self, percezioni: List[PercezioneElaborata]) -> str:
        """Costruisce stringa di contesto per LLM"""
        parti = []
        for p in percezioni:
            parti.append(f"- {p.tipo}: {p.descrizione}")
        
        parti.append(f"- Stato emotivo: {self.amigdala.stato.value}")
        
        return "\n".join(parti)
    
    def _genera_decisione(self, percezioni: List[PercezioneElaborata], ragionamento: str) -> Dict:
        """Genera decisione strutturata"""
        
        # Logica decisionale base
        azione = "monitora_ambiente"
        priorita = 0.3
        
        for p in percezioni:
            if "comando" in p.entita:
                azione = "esegui_comando"
                priorita = 0.8
            elif "car" in p.entita or "pericolo" in p.descrizione.lower():
                azione = "evita_ostacolo"
                priorita = 0.9
            elif "person" in p.entita:
                azione = "mantieni_distanza"
                priorita = 0.6
        
        return {
            "azione": azione,
            "priorita": priorita,
            "ragionamento": ragionamento,
            "percezioni_processate": len(percezioni),
            "timestamp": time.time()
        }


class SistemaReticolare:
    """Monitoraggio stato interno"""
    
    def __init__(self):
        self.nome = "Sistema Reticolare"
    
    def monitora(self, stato: StatoInterno) -> StatoInterno:
        """Aggiorna stato interno"""
        stato.energia -= Config.BATTERY_DRAIN_RATE
        stato.cicli_eseguiti += 1
        
        # Calcola carico cognitivo (simulato)
        stato.carico_cognitivo = min(0.9, stato.cicli_eseguiti * 0.01)
        
        if stato.energia < 20:
            print(f"  ⚠️  Energia critica: {stato.energia:.1f}%")
        
        return stato


# ==================== MENTE ARTIFICIALE REALE ====================

class MenteArtificialeReale:
    """Sistema cognitivo completo con modelli reali"""
    
    def __init__(self):
        self.nome = "🧠 Mente Artificiale Reale"
        
        print(f"\n{'='*70}")
        print(f"{self.nome}")
        print(f"{'='*70}")
        print(f"Device: {Config.DEVICE.upper()}")
        print(f"Visione: {'✅ YOLOv8' if YOLO_AVAILABLE else '❌ Simulato'}")
        print(f"Audio: {'✅ Whisper' if WHISPER_AVAILABLE else '❌ Simulato'}")
        print(f"LLM: {'✅ ' + Config.LLM_MODEL if LLM_AVAILABLE else '❌ Rule-based'}")
        print(f"{'='*70}\n")
        
        # Inizializza moduli
        self.talamo = Talamo()
        self.ippocampo = Ippocampo()
        self.amigdala = Amigdala()
        self.prefrontale = CortecciaPrefrontale(self.ippocampo, self.amigdala)
        self.sistema_reticolare = SistemaReticolare()
        
        self.stato = StatoInterno()
        self.attivo = True
    
    def ciclo_cognitivo(self, frame=None, audio=None) -> Dict:
        """Ciclo cognitivo completo"""
        
        print(f"\n{'='*70}")
        print(f"🔄 CICLO COGNITIVO #{self.stato.cicli_eseguiti + 1}")
        print(f"{'='*70}")
        
        # 1. Percezione multimodale
        percezioni = self.talamo.ciclo_percettivo(frame, audio)
        
        if not percezioni:
            print("  ℹ️  Nessuna percezione significativa")
            time.sleep(Config.COGNITIVE_CYCLE_DELAY)
            return {"stato": "idle"}
        
        # 2. Valutazione emotiva
        stato_emotivo = self.amigdala.valuta_emozione(percezioni, self.ippocampo)
        self.stato.stato_emotivo = stato_emotivo
        
        # 3. Decision making
        decisione = self.prefrontale.analizza_e_decidi(percezioni)
        
        # 4. Memorizzazione
        self.ippocampo.memorizza(
            evento=f"Azione: {decisione['azione']}",
            contesto={"percezioni": len(percezioni), "stato": stato_emotivo.value},
            valenza=0.7
        )
        
        # 5. Reward
        self.amigdala.reward(decisione['azione'], True)
        
        # 6. Monitoraggio interno
        self.stato = self.sistema_reticolare.monitora(self.stato)
        
        print(f"\n{'='*70}")
        print(f"✅ CICLO COMPLETATO - Energia: {self.stato.energia:.1f}%")
        print(f"{'='*70}\n")
        
        time.sleep(Config.COGNITIVE_CYCLE_DELAY)
        
        return decisione
    
    def esegui_autonomo(self, durata_secondi: int = 60):
        """Modalità autonoma: cicli cognitivi continui"""
        print(f"\n🚀 Avvio modalità autonoma ({durata_secondi}s)...\n")
        
        start_time = time.time()
        
        try:
            while (time.time() - start_time) < durata_secondi and self.stato.energia > 5:
                self.ciclo_cognitivo()
                
        except KeyboardInterrupt:
            print("\n\n⏸️  Interruzione manuale")
        
        self.report_finale()
    
    def report_finale(self):
        """Report stato finale"""
        print(f"\n{'='*70}")
        print(f"📊 REPORT FINALE")
        print(f"{'='*70}")
        print(f"Cicli eseguiti: {self.stato.cicli_eseguiti}")
        print(f"Energia residua: {self.stato.energia:.1f}%")
        print(f"Memorie: {len(self.ippocampo.memoria_episodica)}")
        print(f"Reward totale: {sum(r[1] for r in self.amigdala.storia_reward):.2f}")
        print(f"Stato emotivo finale: {self.stato.stato_emotivo.value}")
        print(f"{'='*70}\n")
    
    def chiudi(self):
        """Cleanup risorse"""
        self.talamo.chiudi()
        print("👋 Sistema spento correttamente")


# ==================== MAIN ====================

def main():
    """Entry point principale"""
    
    print("""
    ╔════════════════════════════════════════════════════════════════╗
    ║                                                                ║
    ║        🧠 MENTE ARTIFICIALE REALE - Open Source Edition       ║
    ║                                                                ║
    ║    Architettura cognitiva modulare con AI models reali        ║
    ║                                                                ║
    ╚════════════════════════════════════════════════════════════════╝
    """)
    
    # Verifica dipendenze
    print("\n📦 Verifica dipendenze:")
    print(f"  • YOLOv8: {'✅' if YOLO_AVAILABLE else '❌'}")
    print(f"  • Whisper: {'✅' if WHISPER_AVAILABLE else '❌'}")
    print(f"  • Transformers: {'✅' if LLM_AVAILABLE else '❌'}")
    print(f"  • OpenCV: {'✅' if VIDEO_AVAILABLE else '❌'}")
    print(f"  • Audio Input: {'✅' if AUDIO_INPUT_AVAILABLE else '❌'}")
    
    if not any([YOLO_AVAILABLE, WHISPER_AVAILABLE, LLM_AVAILABLE]):
        print("\n⚠️  Nessun modello AI disponibile. Usa:")
        print("    pip install -r requirements.txt")
        print("\n  Continuando in modalità simulazione...\n")
    
    # Menu
    print("\n" + "="*70)
    print("MODALITÀ OPERATIVE:")
    print("="*70)
    print("1. 🔄 Ciclo singolo (manuale)")
    print("2. 🚀 Modalità autonoma (60 secondi)")
    print("3. 🎥 Modalità video streaming (richiede camera)")
    print("4. 🎤 Modalità comando vocale (richiede microfono)")
    print("5. ℹ️  Info sistema")
    print("="*70)
    
    scelta = input("\nScelta: ").strip()
    
    mente = MenteArtificialeReale()
    
    try:
        if scelta == "1":
            mente.ciclo_cognitivo()
            mente.report_finale()
            
        elif scelta == "2":
            mente.esegui_autonomo(durata_secondi=60)
            
        elif scelta == "3":
            if not VIDEO_AVAILABLE:
                print("❌ OpenCV non disponibile")
            else:
                modalita_video_streaming(mente)
                
        elif scelta == "4":
            if not AUDIO_INPUT_AVAILABLE:
                print("❌ Audio input non disponibile")
            else:
                modalita_comando_vocale(mente)
                
        elif scelta == "5":
            mostra_info_sistema()
            
        else:
            print("❌ Scelta non valida")
            
    except Exception as e:
        print(f"\n❌ Errore: {e}")
        import traceback
        traceback.print_exc()
    finally:
        mente.chiudi()


def modalita_video_streaming(mente: MenteArtificialeReale):
    """Modalità con video streaming continuo"""
    print("\n🎥 Modalità video streaming - Premi 'q' per uscire\n")
    
    camera = cv2.VideoCapture(Config.CAMERA_INDEX)
    
    try:
        while True:
            ret, frame = camera.read()
            if not ret:
                break
            
            # Elabora frame
            decisione = mente.ciclo_cognitivo(frame=frame)
            
            # Mostra frame con annotazioni
            cv2.putText(frame, f"Azione: {decisione.get('azione', 'N/A')}", 
                       (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(frame, f"Energia: {mente.stato.energia:.0f}%", 
                       (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            
            cv2.imshow('Mente Artificiale - Visione', frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
            if mente.stato.energia < 5:
                print("\n🔋 Energia esaurita")
                break
                
    finally:
        camera.release()
        cv2.destroyAllWindows()
        mente.report_finale()


def modalita_comando_vocale(mente: MenteArtificialeReale):
    """Modalità comando vocale interattivo"""
    print("\n🎤 Modalità comando vocale - Premi CTRL+C per uscire")
    print("    Parla dopo il beep...\n")
    
    try:
        while mente.stato.energia > 5:
            print(f"\n🎤 Registrazione audio (Energia: {mente.stato.energia:.0f}%)...")
            print("    [Parla ora!]")
            
            # Cattura audio
            audio = mente.talamo.audio.registra_audio()
            
            # Elabora
            decisione = mente.ciclo_cognitivo(audio=audio)
            
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n\n⏸️  Modalità vocale terminata")
    finally:
        mente.report_finale()


def mostra_info_sistema():
    """Mostra informazioni sul sistema"""
    print("\n" + "="*70)
    print("ℹ️  INFORMAZIONI SISTEMA")
    print("="*70)
    print(f"Configurazione:")
    print(f"  • Device computazione: {Config.DEVICE}")
    print(f"  • Modello visione: {Config.YOLO_MODEL}")
    print(f"  • Modello audio: Whisper-{Config.WHISPER_MODEL}")
    print(f"  • Modello LLM: {Config.LLM_MODEL}")
    print(f"\nHardware:")
    print(f"  • Camera: {Config.CAMERA_WIDTH}x{Config.CAMERA_HEIGHT}@{Config.CAMERA_FPS}fps")
    print(f"  • Microfono: {Config.AUDIO_SAMPLE_RATE}Hz, {Config.AUDIO_CHANNELS} ch")
    print(f"\nModuli disponibili:")
    print(f"  • YOLOv8: {'✅' if YOLO_AVAILABLE else '❌'}")
    print(f"  • Whisper: {'✅' if WHISPER_AVAILABLE else '❌'}")
    print(f"  • Transformers: {'✅' if LLM_AVAILABLE else '❌'}")
    print(f"  • OpenCV: {'✅' if VIDEO_AVAILABLE else '❌'}")
    print(f"  • Audio I/O: {'✅' if AUDIO_INPUT_AVAILABLE else '❌'}")
    print("="*70)


if __name__ == "__main__":
    main()

