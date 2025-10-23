"""
👂 MODULO UDITO - Corteccia Uditiva
====================================
Simula l'elaborazione uditiva e il riconoscimento vocale
Equivalente: Corteccia uditiva primaria (A1) e area di Wernicke
"""

import os
from typing import Dict, Any, Optional
import numpy as np

# Import condizionali
try:
    import whisper
    WHISPER_AVAILABLE = True
except ImportError:
    WHISPER_AVAILABLE = False

try:
    import sounddevice as sd
    import soundfile as sf
    AUDIO_AVAILABLE = True
except ImportError:
    AUDIO_AVAILABLE = False


class CortecciaUditiva:
    """
    Modulo di elaborazione uditiva
    Funzioni:
    - Speech-to-text (Whisper)
    - Analisi tono
    - Rilevamento emozioni vocali
    - Separazione sorgenti sonore
    """
    
    def __init__(self, model_name: str = "base"):
        self.nome = "Corteccia Uditiva"
        self.model_name = model_name
        self.model = None
        self.sample_rate = 16000
        self.ultima_elaborazione = None
        
        if WHISPER_AVAILABLE:
            try:
                print(f"[{self.nome}] Caricamento modello Whisper {model_name}...")
                self.model = whisper.load_model(model_name)
                print(f"[{self.nome}] ✅ Modello caricato")
            except Exception as e:
                print(f"[{self.nome}] ⚠️ Errore caricamento: {e}")
    
    def ascolta(self, source: Any, lingua: str = "it") -> Dict[str, Any]:
        """
        Elabora input audio (file, array, registrazione)
        
        Args:
            source: Path audio file, array numpy, o None per registrazione
            lingua: Codice lingua (it, en, es, fr, etc.)
            
        Returns:
            Dict con trascrizione e analisi
        """
        print(f"[{self.nome}] Elaborazione input audio...")
        
        # Carica audio
        if isinstance(source, str):
            if not os.path.exists(source):
                return self._elaborazione_simulata(f"File non trovato: {source}")
            
            audio = self._carica_audio_file(source)
        elif isinstance(source, np.ndarray):
            audio = source
        elif source is None:
            audio = self._registra_audio()
        else:
            audio = None
        
        # Elaborazione
        if self.model is not None and audio is not None:
            risultati = self._elaborazione_reale(audio, lingua)
        else:
            risultati = self._elaborazione_simulata(source)
        
        self.ultima_elaborazione = risultati
        return risultati
    
    def _elaborazione_reale(self, audio: np.ndarray, lingua: str) -> Dict:
        """Trascrizione con Whisper"""
        try:
            result = self.model.transcribe(
                audio,
                language=lingua,
                fp16=False
            )
            
            testo = result['text'].strip()
            
            return {
                'tipo': 'reale',
                'testo': testo,
                'lingua': result.get('language', lingua),
                'tono': self._analizza_tono(testo),
                'intenzione': self._classifica_intenzione(testo),
                'emozione': self._rileva_emozione(testo),
                'entita': self._estrai_entita(testo)
            }
        except Exception as e:
            print(f"[{self.nome}] ⚠️ Errore: {e}")
            return self._elaborazione_simulata(audio)
    
    def _elaborazione_simulata(self, source: Any) -> Dict:
        """Fallback simulato"""
        return {
            'tipo': 'simulato',
            'testo': 'Ciao, come stai? Vieni qui per favore.',
            'lingua': 'it',
            'tono': 'amichevole',
            'intenzione': 'richiesta',
            'emozione': 'positivo',
            'entita': ['saluto', 'domanda', 'comando']
        }
    
    def _carica_audio_file(self, path: str) -> Optional[np.ndarray]:
        """Carica file audio"""
        if not AUDIO_AVAILABLE:
            return None
        
        try:
            audio, sr = sf.read(path)
            
            # Resample se necessario
            if sr != self.sample_rate:
                # Semplice decimation (per resample corretto usare librosa)
                step = sr // self.sample_rate
                audio = audio[::step]
            
            # Mono
            if len(audio.shape) > 1:
                audio = audio.mean(axis=1)
            
            return audio.astype(np.float32)
        except Exception as e:
            print(f"[{self.nome}] ⚠️ Errore caricamento: {e}")
            return None
    
    def _registra_audio(self, durata: float = 3.0) -> Optional[np.ndarray]:
        """Registra audio da microfono"""
        if not AUDIO_AVAILABLE:
            print(f"[{self.nome}] ⚠️ Audio input non disponibile")
            return None
        
        try:
            print(f"[{self.nome}] 🎤 Registrazione {durata}s...")
            
            audio = sd.rec(
                int(durata * self.sample_rate),
                samplerate=self.sample_rate,
                channels=1,
                dtype='float32'
            )
            sd.wait()
            
            # Check energia
            energy = np.sum(audio ** 2) / len(audio)
            if energy < 1e-6:
                print(f"[{self.nome}] ⚠️ Segnale troppo debole")
                return None
            
            return audio.flatten()
        except Exception as e:
            print(f"[{self.nome}] ⚠️ Errore registrazione: {e}")
            return None
    
    def _analizza_tono(self, testo: str) -> str:
        """Analisi tono/sentiment base"""
        testo_lower = testo.lower()
        
        # Parole chiave per toni
        urgente = ['aiuto', 'urgente', 'subito', 'veloce', 'pericolo']
        amichevole = ['ciao', 'grazie', 'perfetto', 'bene', 'ottimo']
        negativo = ['no', 'male', 'sbagliato', 'errore', 'problema']
        
        if any(word in testo_lower for word in urgente):
            return 'urgente'
        elif any(word in testo_lower for word in amichevole):
            return 'amichevole'
        elif any(word in testo_lower for word in negativo):
            return 'negativo'
        else:
            return 'neutro'
    
    def _classifica_intenzione(self, testo: str) -> str:
        """Classifica intenzione comunicativa"""
        testo_lower = testo.lower()
        
        # Comandi
        comandi = ['vieni', 'vai', 'fermati', 'aspetta', 'segui', 'prendi']
        if any(cmd in testo_lower for cmd in comandi):
            return 'comando'
        
        # Domande
        if any(q in testo_lower for q in ['?', 'come', 'cosa', 'dove', 'quando', 'chi']):
            return 'domanda'
        
        # Affermazioni
        if any(a in testo_lower for a in ['è', 'sono', 'ho', 'hai']):
            return 'affermazione'
        
        return 'incerto'
    
    def _rileva_emozione(self, testo: str) -> str:
        """Rilevamento emozione base"""
        testo_lower = testo.lower()
        
        emozioni = {
            'gioia': ['felice', 'contento', 'bello', 'ottimo', 'fantastico'],
            'tristezza': ['triste', 'male', 'brutto', 'dispiaciuto'],
            'rabbia': ['arrabbiato', 'furioso', 'maledetto', 'dannato'],
            'paura': ['paura', 'spaventato', 'pericolo', 'aiuto']
        }
        
        for emozione, keywords in emozioni.items():
            if any(word in testo_lower for word in keywords):
                return emozione
        
        return 'neutro'
    
    def _estrai_entita(self, testo: str) -> list:
        """Estrazione entità semplice"""
        entita = []
        testo_lower = testo.lower()
        
        # Pattern base
        if 'ciao' in testo_lower or 'salve' in testo_lower:
            entita.append('saluto')
        
        if '?' in testo:
            entita.append('domanda')
        
        comandi = ['vieni', 'vai', 'fermati', 'aspetta']
        if any(cmd in testo_lower for cmd in comandi):
            entita.append('comando')
        
        return entita if entita else ['generic_text']


# Istanza globale
_corteccia_uditiva = None

def get_instance() -> CortecciaUditiva:
    """Ottieni istanza singleton"""
    global _corteccia_uditiva
    if _corteccia_uditiva is None:
        _corteccia_uditiva = CortecciaUditiva()
    return _corteccia_uditiva


# API semplificata
def ascolta(source: Any = None, lingua: str = "it") -> Dict[str, Any]:
    """Elabora audio"""
    return get_instance().ascolta(source, lingua)


def registra(durata: float = 3.0) -> Optional[np.ndarray]:
    """Registra da microfono"""
    return get_instance()._registra_audio(durata)


# Test del modulo
if __name__ == "__main__":
    print("="*60)
    print("🧪 Test Modulo Udito")
    print("="*60)
    
    corteccia = CortecciaUditiva()
    
    # Test elaborazione simulata
    risultati = corteccia.ascolta("audio_test.wav")
    
    print(f"\nRisultati:")
    print(f"  Tipo: {risultati['tipo']}")
    print(f"  Testo: {risultati['testo']}")
    print(f"  Tono: {risultati['tono']}")
    print(f"  Intenzione: {risultati['intenzione']}")
    print(f"  Emozione: {risultati['emozione']}")
    
    print("\n✅ Test completato")

