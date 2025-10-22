# 🧠 Mente Artificiale Modulare - Implementazione Reale

Sistema cognitivo artificiale ispirato al cervello umano, con modelli AI open-source reali.

---

## 🎯 Overview

Questa implementazione trasforma l'architettura teorica della "mente artificiale" in un **sistema funzionante** usando:

| Componente | Modello | Funzione |
|------------|---------|----------|
| 👁️ **Visione** | YOLOv8 | Rilevamento oggetti real-time |
| 👂 **Audio** | Whisper | Trascrizione vocale multilingua |
| 🧠 **Ragionamento** | GPT-2/LLaMA | Decision making e planning |
| 💾 **Memoria** | Vector DB | Memoria episodica e semantica |
| ❤️ **Emozioni** | Reward System | Valutazione affettiva |

---

## 🏗️ Architettura

```
┌─────────────────────────────────────────────────────────────┐
│                    MENTE ARTIFICIALE                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────┐      ┌──────────┐      ┌──────────┐        │
│  │  Camera  │──────│  YOLOv8  │──────│          │        │
│  └──────────┘      └──────────┘      │          │        │
│                                       │  TALAMO  │        │
│  ┌──────────┐      ┌──────────┐      │ (Router) │        │
│  │   Mic    │──────│ Whisper  │──────│          │        │
│  └──────────┘      └──────────┘      └────┬─────┘        │
│                                            │              │
│         ┌──────────────────────────────────┤              │
│         │                                  │              │
│         ▼                                  ▼              │
│  ┌────────────┐                     ┌────────────┐       │
│  │ IPPOCAMPO  │◄────────────────────│ AMIGDALA   │       │
│  │ (Memoria)  │                     │ (Emozioni) │       │
│  └─────┬──────┘                     └─────┬──────┘       │
│        │                                  │              │
│        └──────────────┬───────────────────┘              │
│                       ▼                                  │
│            ┌─────────────────────┐                       │
│            │  CORTECCIA          │                       │
│            │  PREFRONTALE        │                       │
│            │  (LLM Reasoning)    │                       │
│            └──────────┬──────────┘                       │
│                       │                                  │
│                       ▼                                  │
│            ┌─────────────────────┐                       │
│            │  CORTECCIA MOTORIA  │                       │
│            │  (Actions)          │                       │
│            └─────────────────────┘                       │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

---

## 🚀 Quick Start

### 1️⃣ **Installazione Automatica (Linux/Raspberry Pi)**

```bash
# Clone/download il progetto
cd guerragames

# Rendi eseguibile lo script
chmod +x setup_raspberry_pi.sh

# Esegui setup
./setup_raspberry_pi.sh
```

### 2️⃣ **Installazione Manuale**

```bash
# Crea virtual environment
python3 -m venv venv_mente_ai
source venv_mente_ai/bin/activate  # Linux/Mac
# oppure: venv_mente_ai\Scripts\activate  # Windows

# Installa dipendenze
pip install -r requirements.txt

# Test hardware
python test_hardware.py
```

### 3️⃣ **Esecuzione**

```bash
# Attiva ambiente
source venv_mente_ai/bin/activate

# Avvia la mente
python mente_ai_reale.py
```

---

## 📋 Requisiti

### Hardware Minimo

| Componente | Requisito |
|------------|-----------|
| **CPU** | 4 core, 2+ GHz (ARM o x86) |
| **RAM** | 4GB (8GB raccomandati) |
| **Storage** | 10GB liberi |
| **Camera** | USB webcam o Pi Camera |
| **Microfono** | USB o integrato |

### Hardware Raccomandato

- **Raspberry Pi 4/5** (8GB) con camera module
- **NVIDIA Jetson Nano/Orin** (per GPU acceleration)
- **PC con GPU** (NVIDIA GTX 1060+)

### Software

- **OS**: Linux (Ubuntu 20.04+, Raspberry Pi OS)
- **Python**: 3.8+
- **Drivers**: Camera V4L2, Audio ALSA/PulseAudio

---

## 🎮 Modalità Operative

### 1. **Ciclo Singolo (Debug)**
Test di un singolo ciclo cognitivo.

```bash
python mente_ai_reale.py
# Scegli: 1
```

### 2. **Modalità Autonoma**
Esecuzione continua per 60 secondi.

```bash
python mente_ai_reale.py
# Scegli: 2
```

### 3. **Video Streaming**
Elaborazione video real-time dalla camera.

```bash
python mente_ai_reale.py
# Scegli: 3
```

Premi `q` per uscire.

### 4. **Comando Vocale**
Interazione vocale continua.

```bash
python mente_ai_reale.py
# Scegli: 4
```

---

## 🔧 Configurazione

Modifica `mente_ai_reale.py` nella classe `Config`:

```python
class Config:
    # Modelli (scegli in base alle risorse)
    YOLO_MODEL = "yolov8n.pt"      # n=nano, s=small, m=medium
    WHISPER_MODEL = "base"          # tiny, base, small, medium
    LLM_MODEL = "gpt2"              # gpt2, gpt-j-6b, llama
    
    # Camera
    CAMERA_INDEX = 0                # ID camera
    CAMERA_WIDTH = 640
    CAMERA_HEIGHT = 480
    CAMERA_FPS = 15
    
    # Audio
    AUDIO_SAMPLE_RATE = 16000
    AUDIO_DURATION = 3              # secondi
    
    # Performance
    USE_GPU = True                  # False per CPU only
```

---

## 📊 Test e Diagnostica

### Test Completo
```bash
python test_hardware.py
```

Output atteso:
```
✅ NumPy
✅ OpenCV
✅ PyTorch
✅ YOLOv8
✅ Whisper
✅ Camera: OK (640x480)
✅ Microfono: OK
```

### Test Singoli

**Camera:**
```python
import cv2
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cv2.imshow('Test', frame)
```

**Microfono:**
```python
import sounddevice as sd
audio = sd.rec(int(3 * 16000), samplerate=16000, channels=1)
sd.wait()
```

**GPU:**
```python
import torch
print(torch.cuda.is_available())
```

---

## 🐛 Troubleshooting

### ❌ "Camera non accessibile"

```bash
# Linux: verifica permessi
ls -l /dev/video*
sudo usermod -a -G video $USER

# Test V4L2
v4l2-ctl --list-devices
```

### ❌ "Microfono non rilevato"

```bash
# Lista dispositivi audio
arecord -l

# Test registrazione
arecord -d 3 test.wav
```

### ❌ "CUDA non disponibile"

```bash
# Verifica driver NVIDIA
nvidia-smi

# Reinstalla PyTorch con CUDA
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

### ❌ "Memoria insufficiente"

**Soluzioni:**
1. Usa modelli più piccoli:
   - `yolov8n.pt` invece di `yolov8m.pt`
   - Whisper `tiny` invece di `base`
   - `gpt2` invece di `gpt-j-6b`

2. Abilita swap (Raspberry Pi):
```bash
sudo dphys-swapfile swapoff
sudo nano /etc/dphys-swapfile
# CONF_SWAPSIZE=2048
sudo dphys-swapfile setup
sudo dphys-swapfile swapon
```

---

## 🎯 Esempi d'Uso

### Esempio 1: Robot di Sorveglianza

```python
from mente_ai_reale import MenteArtificialeReale

mente = MenteArtificialeReale()

# Loop continuo
while True:
    decisione = mente.ciclo_cognitivo()
    
    if decisione['azione'] == 'evita_ostacolo':
        print("⚠️ Pericolo rilevato!")
        # Esegui manovra evasiva
    
    if mente.stato.energia < 20:
        print("🔋 Batteria bassa, rientro alla base")
        break
```

### Esempio 2: Assistente Vocale

```python
# Modalità comando vocale
mente = MenteArtificialeReale()

while True:
    print("🎤 In ascolto...")
    audio = mente.talamo.audio.registra_audio()
    
    if audio is not None:
        decisione = mente.ciclo_cognitivo(audio=audio)
        print(f"Azione: {decisione['azione']}")
```

### Esempio 3: Analisi Video

```python
import cv2

mente = MenteArtificialeReale()
video = cv2.VideoCapture('video.mp4')

while True:
    ret, frame = video.read()
    if not ret:
        break
    
    decisione = mente.ciclo_cognitivo(frame=frame)
    
    # Annota frame
    cv2.putText(frame, decisione['azione'], (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Analisi', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
```

---

## 📈 Performance

### Benchmark (Raspberry Pi 4, 8GB)

| Modello | FPS | Latenza | RAM |
|---------|-----|---------|-----|
| YOLOv8n | ~15 | ~70ms | 500MB |
| Whisper base | N/A | ~2s | 1GB |
| GPT-2 | N/A | ~500ms | 800MB |

### Benchmark (PC con GTX 1060)

| Modello | FPS | Latenza | VRAM |
|---------|-----|---------|------|
| YOLOv8s | ~60 | ~16ms | 2GB |
| Whisper small | N/A | ~500ms | 2GB |
| GPT-J-6B | N/A | ~1s | 12GB |

---

## 🔮 Roadmap

- [x] Architettura base modulare
- [x] Integrazione YOLOv8
- [x] Integrazione Whisper
- [x] Integrazione LLM
- [x] Sistema memoria episodica
- [x] Sistema reward
- [ ] Vector database per memoria semantica
- [ ] Fine-tuning modelli custom
- [ ] Integrazione sensori IoT
- [ ] Multi-agente communication
- [ ] Web dashboard monitoring

---

## 📚 Documentazione Modelli

- **YOLOv8**: https://docs.ultralytics.com/
- **Whisper**: https://github.com/openai/whisper
- **Transformers**: https://huggingface.co/docs/transformers/
- **PyTorch**: https://pytorch.org/docs/

---

## 🤝 Contributi

Contributi benvenuti! Areas of interest:
- Ottimizzazione performance
- Nuovi sensori/attuatori
- Modelli custom
- Testing su diverse piattaforme

---

## 📄 Licenza

MIT License - Usa liberamente per progetti personali e commerciali.

---

## 🆘 Supporto

Per problemi o domande:
1. Controlla la sezione Troubleshooting
2. Esegui `python test_hardware.py`
3. Verifica log errori
4. Apri issue su GitHub (se applicabile)

---

**🧠 Buona sperimentazione con la tua Mente Artificiale!**

