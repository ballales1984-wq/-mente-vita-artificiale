# 🌱 GUIDA ESPANSIONI - Mente Artificiale Completa

## 📋 Indice
1. [Voce Sintetica (TTS)](#voce-sintetica)
2. [Movimento Fisico (GPIO)](#movimento-fisico)
3. [Sensori Biometrici (EEG/EMG)](#sensori-biometrici)
4. [Connessione Cloud](#connessione-cloud)
5. [Interazione Sociale](#interazione-sociale)
6. [Aggiungere Nuove Espansioni](#nuove-espansioni)

---

## 🔊 1. Voce Sintetica (TTS)

### Installazione
```bash
pip install pyttsx3
```

### Come Funziona
Il sistema rileva automaticamente se `pyttsx3` è installato e attiva la voce.

### Uso
```python
# Già integrato in mente_artificiale_completa.py
# La voce parla automaticamente quando esegue azioni
```

### Personalizzazione
```python
# In mente_artificiale_completa.py, modifica:
class VoceSintetica:
    def __init__(self):
        self.engine.setProperty('rate', 150)  # Velocità (default: 150)
        self.engine.setProperty('volume', 0.9)  # Volume (0-1)
```

---

## 🦾 2. Movimento Fisico (GPIO)

### Hardware Necessario
- Raspberry Pi (o simile con GPIO)
- Servo motori (es. SG90)
- LED per feedback visivo
- Driver servo (es. PCA9685)

### Installazione
```bash
pip install RPi.GPIO
# o per servo controller:
pip install adafruit-circuitpython-pca9685
```

### Connessioni
```python
# Pin GPIO (BCM numbering)
pin_map = {
    'servo_testa': 17,
    'servo_braccio_dx': 18,
    'servo_braccio_sx': 27,
    'led_occhi': 22
}
```

### Schema Wiring
```
Raspberry Pi → Servo Controller PCA9685
   Pin 3 (SDA) → SDA
   Pin 5 (SCL) → SCL
   Pin 2 (5V) → VCC
   Pin 6 (GND) → GND

Servo Controller → Servomotori
   Channel 0 → Servo Testa
   Channel 1 → Servo Braccio Dx
   Channel 2 → Servo Braccio Sx
```

### Uso
```python
# Già integrato!
# Quando la mente decide "avvicinati":
# → muove la testa
# → lampeggia occhi
```

### Aggiungere Nuovi Movimenti
```python
class ControlloMovimento:
    def gesto_saluto(self):
        """Gesto di saluto con braccio"""
        self.muovi_braccio('dx', 0)
        time.sleep(0.5)
        self.muovi_braccio('dx', 90)
        time.sleep(0.5)
        self.muovi_braccio('dx', 0)
```

---

## 🧬 3. Sensori Biometrici (EEG/EMG)

### Hardware Supportato
- **OpenBCI Cyton** (8 canali EEG)
- **OpenBCI Ganglion** (4 canali)
- **Muse Headband**
- **Sensori EMG** (MyoWare)
- **Heart Rate** (Polar H10, MAX30102)

### Installazione
```bash
# OpenBCI
pip install brainflow

# Muse
pip install muselsl

# Heart Rate
pip install max30102
```

### Configurazione OpenBCI
```python
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds

class SensoriBiometrici:
    def __init__(self):
        params = BrainFlowInputParams()
        params.serial_port = '/dev/ttyUSB0'  # Cambia per tuo dispositivo
        
        # Cyton board
        self.board_id = BoardIds.CYTON_BOARD
        self.board = BoardShim(self.board_id, params)
        self.board.prepare_session()
        self.board.start_stream()
```

### Lettura Dati
```python
def leggi_eeg(self) -> Dict[str, float]:
    # Leggi dati
    data = self.board.get_board_data()
    
    # Estrai bande frequenza
    eeg_channels = BoardShim.get_eeg_channels(self.board_id)
    
    # Analisi FFT per bande
    # alfa: 8-13 Hz
    # beta: 13-30 Hz
    # gamma: 30-100 Hz
    
    return {
        'alfa': alfa_power,
        'beta': beta_power,
        'gamma': gamma_power,
        'delta': delta_power
    }
```

### Integrazione con Biosegnali
```python
# Nel ciclo cognitivo, i dati EEG reali sostituiscono
# i pattern binari simulati:

if self.sensori.attivo:
    dati_eeg = self.sensori.leggi_eeg()
    
    # Usa alfa per arousal
    # Usa beta per concentrazione
    # Usa gamma per cognizione
    
    # Influenza decisioni
    if dati_eeg['alfa'] > 10:
        # Stato rilassato → decisioni calme
        pass
    elif dati_eeg['beta'] > 20:
        # Stato concentrato → decisioni precise
        pass
```

---

## ☁️ 4. Connessione Cloud

### Firebase Setup

#### 1. Crea Progetto Firebase
- Vai su: https://console.firebase.google.com
- Crea nuovo progetto
- Abilita Firestore Database

#### 2. Scarica Credenziali
- Project Settings → Service Accounts
- Generate New Private Key
- Salva come `firebase-key.json`

#### 3. Installazione
```bash
pip install firebase-admin
```

#### 4. Configurazione
```python
import firebase_admin
from firebase_admin import credentials, firestore

class ConnessioneCloud:
    def __init__(self):
        cred = credentials.Certificate("firebase-key.json")
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()
```

### AWS Setup (Alternativa)

```bash
pip install boto3
```

```python
import boto3

class ConnessioneCloud:
    def __init__(self):
        self.s3 = boto3.client('s3')
        self.dynamodb = boto3.resource('dynamodb')
```

### Funzionalità Cloud

#### Salva Episodio
```python
def salva_episodio_cloud(self, episodio: Dict):
    self.db.collection('episodi').add({
        'timestamp': firestore.SERVER_TIMESTAMP,
        'decisione': episodio['azione'],
        'valenza': episodio['valenza'],
        'reward': episodio['reward']
    })
```

#### Sincronizza Memorie
```python
def sincronizza_memorie(self):
    # Upload memorie locali → cloud
    memorie_locali = self.ippocampo.memoria_episodica
    
    for memoria in memorie_locali:
        self.db.collection('memorie').document(memoria.id).set({
            'contenuto': memoria.contenuto,
            'valenza': memoria.valenza_emotiva,
            'timestamp': memoria.timestamp
        })
```

#### Multi-Device Sync
```python
def carica_memorie_da_cloud(self):
    # Download memorie da cloud → locale
    docs = self.db.collection('memorie').stream()
    
    for doc in docs:
        data = doc.to_dict()
        # Aggiungi a memoria locale
```

---

## 👥 5. Interazione Sociale

### Chat Bot Integrato

```bash
pip install openai
```

```python
class InterazioneSociale:
    def __init__(self):
        import openai
        openai.api_key = "YOUR_API_KEY"
        self.client = openai.OpenAI()
    
    def chat(self, messaggio: str) -> str:
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Sei una mente artificiale..."},
                {"role": "user", "content": messaggio}
            ]
        )
        return response.choices[0].message.content
```

### Avatar 3D

```bash
pip install pygame
```

```python
class Avatar3D:
    def __init__(self):
        import pygame
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
    
    def mostra_emozione(self, emozione: str):
        # Cambia espressione facciale avatar
        if emozione == "felice":
            # Disegna sorriso
            pass
        elif emozione == "triste":
            # Disegna bocca verso giù
            pass
```

### Gesture Recognition

```bash
pip install mediapipe
```

```python
import mediapipe as mp

class RiconoscimentoGesti:
    def __init__(self):
        self.hands = mp.solutions.hands.Hands()
    
    def rileva_gesto(self, frame):
        results = self.hands.process(frame)
        
        if results.multi_hand_landmarks:
            # Analizza landmark mani
            # Riconosci gesti (👍, 👋, ✋)
            pass
```

---

## 🆕 6. Aggiungere Nuove Espansioni

### Template Modulo

```python
class NuovaEspansione:
    """Descrizione nuova funzionalità"""
    
    def __init__(self):
        self.nome = "Nuova Espansione"
        self.attivo = False
        
        try:
            # Inizializza hardware/software
            # ...
            
            self.attivo = True
            print(f"[{self.nome}] ✅ Inizializzato")
        
        except Exception as e:
            print(f"[{self.nome}] ⚠️ Errore: {e}")
    
    def funzione_principale(self, parametri):
        """Funzione principale"""
        if not self.attivo:
            # Fallback simulato
            return None
        
        # Implementazione reale
        return risultato
```

### Integrazione nel Sistema

#### 1. Aggiungi Import
```python
# In mente_artificiale_completa.py

try:
    from mio_modulo import NuovaEspansione
    NUOVA_DISPONIBILE = True
except:
    NUOVA_DISPONIBILE = False
```

#### 2. Aggiungi a Configurazione
```python
class ConfigurazioneCompleta:
    def __init__(self):
        # ...
        self.usa_nuova_espansione = NUOVA_DISPONIBILE
```

#### 3. Inizializza
```python
class MenteArtificialeCompleta:
    def _inizializza_espansioni(self):
        # ...
        print("[X/Y] 🆕 Nuova Espansione")
        self.nuova = NuovaEspansione() if self.config.usa_nuova_espansione else None
```

#### 4. Usa nel Ciclo
```python
def ciclo_cognitivo(self):
    # ...
    
    # Usa nuova espansione
    if self.nuova and self.nuova.attivo:
        risultato = self.nuova.funzione_principale(dati)
        # Integra risultato nel flusso cognitivo
```

---

## 📦 Librerie Suggerite

### Percezione Avanzata
```bash
pip install mediapipe  # Face/hand/pose detection
pip install dlib       # Face recognition
pip install face_recognition
```

### Movimento Robotico
```bash
pip install pyserial   # Comunicazione seriale Arduino
pip install dynamixel-sdk  # Servo Dynamixel
```

### NLP Avanzato
```bash
pip install spacy      # NLP processing
pip install transformers  # BERT, GPT models
```

### Visualizzazione
```bash
pip install pygame     # Graphics 2D
pip install panda3d    # Graphics 3D
pip install pyqt5      # GUI desktop
```

---

## 🎯 Esempi Completi

### Esempio 1: Mente con Voce

```python
from mente_artificiale_completa import MenteArtificialeCompleta, ConfigurazioneCompleta

config = ConfigurazioneCompleta()
config.usa_voce_sintetica = True

mente = MenteArtificialeCompleta(config)
mente.esegui_sessione(num_cicli=3)
```

### Esempio 2: Mente con Robot Fisico

```python
config = ConfigurazioneCompleta()
config.usa_movimento_fisico = True

mente = MenteArtificialeCompleta(config)
mente.ciclo_cognitivo()  # Muove servomotori reali!
```

### Esempio 3: Mente con EEG

```python
config = ConfigurazioneCompleta()
config.usa_sensori_biometrici = True

mente = MenteArtificialeCompleta(config)
# Legge segnali EEG reali e li integra nel ciclo cognitivo
```

---

## ✅ Checklist Espansione

Prima di aggiungere una nuova funzionalità:

- [ ] Libreria installabile con pip?
- [ ] Funziona senza hardware (fallback simulato)?
- [ ] Gestione errori implementata?
- [ ] Documentazione chiara?
- [ ] Test su hardware reale?
- [ ] Integrata nel ciclo cognitivo?

---

## 🆘 Troubleshooting

### GPIO non funziona
```bash
# Verifica permessi
sudo usermod -a -G gpio $USER

# Verifica pin
gpio readall
```

### Voce non si sente
```bash
# Linux
sudo apt-get install espeak

# Windows: usa SAPI voices
```

### Sensori EEG non connessi
```bash
# Verifica porta seriale
ls /dev/ttyUSB*

# Test connessione
python -m brainflow.board_shim --serial-port /dev/ttyUSB0
```

---

**Il tuo sistema è ESPANDIBILE ALL'INFINITO!** 🌱🚀

**File:** `mente_artificiale_completa.py` (pronto all'uso)  
**Versione:** 3.0  
**Data:** 22 Ottobre 2025

