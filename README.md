# 🧠 Mente Artificiale Modulare

<div align="center">

**Architettura Cognitiva Artificiale Ispirata al Cervello Umano**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://python.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-red.svg)](https://pytorch.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20RaspberryPi-orange.svg)](https://raspberrypi.org)

*Sistema cognitivo modulare con percezione multimodale, ragionamento autonomo e apprendimento continuo*

</div>

---

## 📋 Indice

- [Descrizione](#-descrizione)
- [Architettura](#-architettura-modulare)
- [Flusso Dati](#-flusso-dati-cognitivo)
- [Tecnologie](#-tecnologie-e-modelli-ai)
- [Installazione](#-installazione)
- [Utilizzo](#-utilizzo)
- [Hardware](#-requisiti-hardware)
- [Roadmap](#-roadmap)
- [Contributi](#-contributi)

---

## ✅ Descrizione Generale

Questo progetto implementa una **mente artificiale modulare** ispirata alla struttura funzionale del cervello umano, utilizzando componenti hardware e software moderni. Ogni modulo simula un'area cerebrale specifica, con flussi sensoriali, cognitivi e motori orchestrati in tempo reale.

### 🎯 Obiettivi

- ✨ **Percezione Multimodale**: Visione (YOLOv8) + Audio (Whisper)
- 🧠 **Ragionamento Autonomo**: LLM per decision making
- 💾 **Memoria Episodica**: Sistema di memoria a lungo termine
- ❤️ **Sistema Affettivo**: Valutazione emotiva e reward learning
- 🦾 **Coordinazione Motoria**: Planning e esecuzione azioni
- ⚡ **Autoregolazione**: Monitoraggio energia e stato interno

### 🚀 Use Cases

- 🤖 **Robot autonomi** per esplorazione e sorveglianza
- 🏠 **Assistenti domestici** con interazione naturale
- 🎓 **Ricerca** in intelligenza artificiale cognitiva
- 🎮 **Agenti virtuali** per simulazioni complesse
- 🏭 **Automazione industriale** con percezione avanzata

---

## 📐 Architettura Modulare

### 🧩 Mappa Funzionale Cervello → AI

| Area Cerebrale | Funzione Simulata | Tecnologia Proposta | Implementazione |
|----------------|-------------------|---------------------|-----------------|
| **Corteccia Visiva** | Visione artificiale | Fotocamera + NPU + CNN | YOLOv8 + OpenCV |
| **Corteccia Uditiva** | Riconoscimento vocale | Microfono + ASR + NLU | Whisper + Transformers |
| **Corteccia Motoria** | Movimento e azione | Python + Attuatori + PID | Control loops + Servo |
| **Corteccia Prefrontale** | Ragionamento e decisione | LLM + Orchestratore | GPT-2 / LLaMA / Claude |
| **Ippocampo** | Memoria semantica | RAM + SSD + Vector DB | FAISS / Pinecone |
| **Amigdala** | Ricompensa/emozione | RL Engine + Thresholds | Reward system + PPO |
| **Cervelletto** | Coordinazione motoria | CPU + Giroscopi + IMU | PID controller |
| **Tronco Encefalico** | Funzioni vitali | Microkernel OS + Watchdog | System monitor |
| **Sistema Reticolare** | Stato energetico | Batteria + UPS + Monitor | Power management |
| **Talamo** | Smistamento sensoriale | CPU + Bus + Scheduler | Event router |

### 🏗️ Diagramma Architetturale

```
╔═══════════════════════════════════════════════════════════════════════╗
║                     MENTE ARTIFICIALE MODULARE                        ║
╚═══════════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────────────────────────────┐
│                        LAYER SENSORIALE                             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┏━━━━━━━━━━━━━┓      ┏━━━━━━━━━━━━━┓      ┏━━━━━━━━━━━━━┓        │
│  ┃ 📷 Camera   ┃      ┃ 🎤 Microfono┃      ┃ 🤲 Sensori  ┃        │
│  ┃   (Video)   ┃      ┃   (Audio)   ┃      ┃  (Tattili)  ┃        │
│  ┗━━━━━┯━━━━━━━┛      ┗━━━━━┯━━━━━━━┛      ┗━━━━━┯━━━━━━━┛        │
│         │                     │                     │               │
│         ▼                     ▼                     ▼               │
│  ┌─────────────┐       ┌─────────────┐       ┌─────────────┐      │
│  │ NPU/GPU     │       │ NPU/CPU     │       │ CPU         │      │
│  │ YOLOv8      │       │ Whisper     │       │ Filters     │      │
│  │ (Detection) │       │ (Transcribe)│       │ (Process)   │      │
│  └──────┬──────┘       └──────┬──────┘       └──────┬──────┘      │
│         │                     │                     │               │
│         └─────────────────────┼─────────────────────┘               │
│                               │                                     │
└───────────────────────────────┼─────────────────────────────────────┘
                                │
                                ▼
┌───────────────────────────────────────────────────────────────────────┐
│                      LAYER COGNITIVO                                  │
├───────────────────────────────────────────────────────────────────────┤
│                                                                       │
│                    ┏━━━━━━━━━━━━━━━━━━━━━┓                          │
│                    ┃   ⚡ TALAMO         ┃                          │
│                    ┃  (Router Centrale)  ┃                          │
│                    ┗━━━━━━━━┯━━━━━━━━━━━━┛                          │
│                             │                                        │
│          ┌──────────────────┼──────────────────┐                    │
│          │                  │                  │                    │
│          ▼                  ▼                  ▼                    │
│  ┌───────────────┐  ┌───────────────┐  ┌───────────────┐          │
│  │ 💾 IPPOCAMPO  │  │ ❤️ AMIGDALA   │  │ 🧠 PREFRONTALE│          │
│  │               │  │               │  │               │          │
│  │ • Episodica   │  │ • Emozioni    │  │ • Reasoning   │          │
│  │ • Semantica   │  │ • Reward      │  │ • Planning    │          │
│  │ • Working Mem │  │ • Valenza     │  │ • Decision    │          │
│  └───────┬───────┘  └───────┬───────┘  └───────┬───────┘          │
│          │                  │                  │                    │
│          └──────────────────┼──────────────────┘                    │
│                             │                                        │
│                   ┌─────────▼─────────┐                             │
│                   │   LLM REASONING   │                             │
│                   │  (GPT-2/LLaMA)    │                             │
│                   │                   │                             │
│                   │ • Context window  │                             │
│                   │ • Chain-of-thought│                             │
│                   │ • Tool use        │                             │
│                   └─────────┬─────────┘                             │
│                             │                                        │
└─────────────────────────────┼─────────────────────────────────────────┘
                              │
                              ▼
┌───────────────────────────────────────────────────────────────────────┐
│                      LAYER MOTORIO                                    │
├───────────────────────────────────────────────────────────────────────┤
│                                                                       │
│                  ┏━━━━━━━━━━━━━━━━━━━━━┓                            │
│                  ┃  🦿 CORTECCIA      ┃                            │
│                  ┃     MOTORIA        ┃                            │
│                  ┗━━━━━━━━┯━━━━━━━━━━━┛                            │
│                           │                                          │
│              ┌────────────┼────────────┐                            │
│              │            │            │                            │
│              ▼            ▼            ▼                            │
│      ┌────────────┐ ┌────────────┐ ┌────────────┐                 │
│      │ Servo      │ │ Motori     │ │ Attuatori  │                 │
│      │ Control    │ │ Stepper    │ │ Lineari    │                 │
│      └────────────┘ └────────────┘ └────────────┘                 │
│              │            │            │                            │
│              └────────────┼────────────┘                            │
│                           │                                          │
│                    ┌──────▼──────┐                                  │
│                    │ 🌀 CERVELLETTO│                                  │
│                    │  (PID + IMU) │                                  │
│                    └──────────────┘                                  │
│                                                                       │
└───────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌───────────────────────────────────────────────────────────────────────┐
│                   LAYER AUTOREGOLAZIONE                               │
├───────────────────────────────────────────────────────────────────────┤
│                                                                       │
│    ┏━━━━━━━━━━━━━━━━━━━┓         ┏━━━━━━━━━━━━━━━━━━━┓            │
│    ┃ 🌙 SISTEMA        ┃         ┃ 🔋 TRONCO         ┃            │
│    ┃    RETICOLARE     ┃◄────────┃    ENCEFALICO     ┃            │
│    ┃ (Arousal/Veglia)  ┃         ┃ (Funzioni Vitali) ┃            │
│    ┗━━━━━━━━━━━━━━━━━━━┛         ┗━━━━━━━━━━━━━━━━━━━┛            │
│                                                                       │
│    • Monitoraggio energia        • Watchdog system                  │
│    • Gestione stato              • Health checks                     │
│    • Load balancing              • Error recovery                    │
│                                                                       │
└───────────────────────────────────────────────────────────────────────┘
```

---

## 🔄 Flusso Dati Cognitivo

### Pipeline Completo

```
[Input Sensoriale] 
    ↓
[NPU/GPU Processing]
    ↓
[CPU (Talamo) - Routing]
    ↓
[LLM + Memoria - Reasoning]
    ↓
[Motore Decisionale - Planning]
    ↓
[Output Motorio - Action]
    ↓
[Feedback Loop - Learning]
```

### Ciclo Cognitivo Dettagliato

```python
# 1️⃣ PERCEZIONE (50-100ms)
percezioni = talamo.elabora_sensoriale(camera, microfono, sensori)

# 2️⃣ EMOZIONE (10-20ms)
stato_emotivo = amigdala.valuta(percezioni, memoria)

# 3️⃣ RAGIONAMENTO (200-500ms)
decisione = prefrontale.analizza_e_decidi(
    percezioni=percezioni,
    emozione=stato_emotivo,
    memoria=ippocampo.richiama_contesto(),
    obiettivo_corrente=goal
)

# 4️⃣ AZIONE (10-50ms)
successo = corteccia_motoria.esegui(decisione)

# 5️⃣ APPRENDIMENTO (5-10ms)
reward = amigdala.reward(decisione.azione, successo)
ippocampo.memorizza(evento, contesto, reward)

# 6️⃣ AUTOREGOLAZIONE (1ms)
stato_interno = sistema_reticolare.monitora()
```

### Timing e Latenze

| Fase | Tempo | Componente |
|------|-------|------------|
| **Cattura frame** | ~30ms | Camera (30fps) |
| **Detection YOLO** | ~50ms | YOLOv8n su NPU |
| **Audio transcribe** | ~2s | Whisper base |
| **LLM reasoning** | ~500ms | GPT-2 inference |
| **Motor control** | ~10ms | PID controller |
| **Memoria write** | ~5ms | RAM/SSD |
| **Ciclo completo** | ~3s | Con audio |
| **Ciclo (solo visione)** | ~200ms | Senza audio |

---

## 📦 Tecnologie e Modelli AI

### 🧠 Large Language Models

| Modello | Parametri | RAM | Use Case |
|---------|-----------|-----|----------|
| **GPT-2** | 124M | 1GB | Raspberry Pi, quick inference |
| **GPT-J-6B** | 6B | 12GB | Workstation, complex reasoning |
| **LLaMA-2-7B** | 7B | 14GB | Best quality/speed balance |
| **Mistral-7B** | 7B | 14GB | Latest, efficient |

### 👁️ Computer Vision

| Modello | FPS (Pi4) | FPS (GPU) | Accuracy |
|---------|-----------|-----------|----------|
| **YOLOv8n** | ~15 | ~60 | 37.3 mAP |
| **YOLOv8s** | ~8 | ~45 | 44.9 mAP |
| **YOLOv8m** | ~4 | ~30 | 50.2 mAP |
| **MediaPipe** | ~30 | ~120 | Pose/Face |

### 👂 Speech Recognition

| Modello | Latenza | WER (IT) | Size |
|---------|---------|----------|------|
| **Whisper-tiny** | ~1s | ~15% | 39MB |
| **Whisper-base** | ~2s | ~10% | 74MB |
| **Whisper-small** | ~4s | ~7% | 244MB |
| **Vosk** | ~500ms | ~12% | 50MB |

### 💾 Vector Databases

- **FAISS** (Meta): In-memory, ultra-fast
- **Pinecone**: Cloud-based, scalable
- **Weaviate**: GraphQL, hybrid search
- **Chroma**: Lightweight, embeddings

### 🔧 Orchestrazione

- **ROS 2** (Robot Operating System): Standard robotica
- **Node-RED**: Visual programming, IoT
- **FastAPI**: REST API, async
- **MQTT**: Pub/sub messaging

### 🎮 Simulazione

- **Gazebo**: 3D robot simulation
- **Webots**: Multi-robot environments
- **PyBullet**: Physics engine
- **Unity ML-Agents**: 3D training

---

## 🚀 Installazione

### 📋 Prerequisiti

```bash
# Sistema operativo
Ubuntu 20.04+ / Raspberry Pi OS (64-bit)

# Python
Python 3.8+

# Hardware (minimo)
- CPU: 4 cores, 2GHz+
- RAM: 4GB (8GB raccomandati)
- Storage: 10GB liberi
- Camera USB o CSI
- Microfono USB
```

### ⚡ Setup Rapido (Linux/Raspberry Pi)

```bash
# 1. Clone repository
git clone https://github.com/your-repo/mente-artificiale.git
cd mente-artificiale

# 2. Esegui setup automatico
chmod +x setup_raspberry_pi.sh
./setup_raspberry_pi.sh

# 3. Test hardware
source venv_mente_ai/bin/activate
python test_hardware.py

# 4. Avvia la mente
python mente_ai_reale.py
```

### 🔧 Setup Manuale

```bash
# 1. Crea virtual environment
python3 -m venv venv_mente_ai
source venv_mente_ai/bin/activate

# 2. Installa dipendenze di sistema (Ubuntu/Debian)
sudo apt-get update
sudo apt-get install -y \
    python3-pip python3-dev \
    libportaudio2 libsndfile1 ffmpeg \
    libopencv-dev libatlas-base-dev

# 3. Installa pacchetti Python
pip install --upgrade pip
pip install -r requirements.txt

# 4. Download modelli (opzionale)
python -c "from ultralytics import YOLO; YOLO('yolov8n.pt')"
python -c "import whisper; whisper.load_model('base')"
```

### 🪟 Windows

```powershell
# Usa Anaconda o Miniconda
conda create -n mente_ai python=3.10
conda activate mente_ai

# Installa PyTorch
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia

# Installa altre dipendenze
pip install -r requirements.txt
```

---

## 🎮 Utilizzo

### 1️⃣ Modalità Interattiva

```bash
python mente_ai_reale.py
```

**Menu principale:**
```
1. 🔄 Ciclo singolo (debug)
2. 🚀 Modalità autonoma (60s)
3. 🎥 Video streaming
4. 🎤 Comando vocale
5. ℹ️ Info sistema
```

### 2️⃣ Modalità Programmata

```python
from mente_ai_reale import MenteArtificialeReale

# Inizializza
mente = MenteArtificialeReale()

# Loop continuo
while mente.stato.energia > 10:
    decisione = mente.ciclo_cognitivo()
    
    # Custom logic
    if decisione['priorita'] > 0.8:
        print(f"🚨 Azione urgente: {decisione['azione']}")
    
    time.sleep(0.1)

# Cleanup
mente.chiudi()
```

### 3️⃣ Integrazione ROS 2

```python
import rclpy
from mente_ai_reale import MenteArtificialeReale

def main():
    rclpy.init()
    node = rclpy.create_node('mente_artificiale_node')
    
    mente = MenteArtificialeReale()
    
    # Subscribe to sensors
    camera_sub = node.create_subscription(
        Image, '/camera/image_raw',
        lambda msg: mente.ciclo_cognitivo(frame=msg.data),
        10
    )
    
    # Publish actions
    action_pub = node.create_publisher(Twist, '/cmd_vel', 10)
    
    rclpy.spin(node)
```

### 4️⃣ API REST

```python
# server.py
from fastapi import FastAPI
from mente_ai_reale import MenteArtificialeReale

app = FastAPI()
mente = MenteArtificialeReale()

@app.post("/ciclo")
async def esegui_ciclo():
    decisione = mente.ciclo_cognitivo()
    return decisione

@app.get("/stato")
async def leggi_stato():
    return {
        "energia": mente.stato.energia,
        "stato_emotivo": mente.stato.stato_emotivo.value,
        "cicli": mente.stato.cicli_eseguiti
    }
```

```bash
# Avvia server
uvicorn server:app --host 0.0.0.0 --port 8000
```

---

## ⚙️ Requisiti Hardware

### 💻 Opzioni Hardware

#### 🥉 Entry Level (Simulazione)

- **PC Standard** con webcam e microfono
- RAM: 4GB+
- Storage: 10GB
- **Costo**: ~0€ (hardware esistente)

#### 🥈 Embedded (Prototipo)

- **Raspberry Pi 4/5** (8GB)
- Pi Camera Module v2/3
- USB Microfono
- MicroSD 64GB
- **Costo**: ~150€

#### 🥇 Production (Robot Reale)

- **NVIDIA Jetson Orin Nano** (8GB)
- Camera CSI 4K
- Array microfoni
- IMU (MPU6050)
- Servo/Motori
- Batteria LiPo
- **Costo**: ~500-1000€

#### 🏆 Workstation (Sviluppo/Training)

- **PC con GPU NVIDIA** (RTX 3060+, 12GB VRAM)
- Webcam 1080p
- Microfono professionale
- SSD NVMe 500GB
- **Costo**: ~1500-2500€

### 📊 Tabella Comparativa

| Componente | Entry | Embedded | Production | Workstation |
|------------|-------|----------|------------|-------------|
| **CPU** | i5/Ryzen 5 | ARM Cortex-A72 | ARM Cortex-A78 | i7/Ryzen 7 |
| **GPU** | Integrata | VideoCore VII | Ampere (1024 CUDA) | RTX 3060+ |
| **RAM** | 4-8GB | 8GB | 8GB | 16-32GB |
| **Storage** | HDD/SSD | MicroSD 64GB | NVMe 256GB | SSD 1TB |
| **Camera** | Webcam USB | Pi Camera v2 | CSI 4K | Pro Webcam |
| **Audio** | Mic integrato | USB Mic | Array Mic | Pro Mic |
| **Power** | AC | 5V/3A USB-C | Battery 12V | AC |
| **FPS (YOLO)** | ~30 | ~15 | ~45 | ~120 |
| **Latenza** | ~200ms | ~500ms | ~200ms | ~50ms |

### 🔌 Schema Connessioni (Raspberry Pi)

```
Raspberry Pi 4/5
├── CSI Port → Pi Camera Module v2
├── USB 3.0 → USB Microfono
├── USB 3.0 → USB Webcam (opzionale)
├── GPIO → Servo controller (PCA9685)
├── I2C → IMU (MPU6050/MPU9250)
├── UART → GPS Module (opzionale)
├── Ethernet/WiFi → Network
└── USB-C → Power Supply (5V/3A+)
```

---

## 🛠️ Configurazione Avanzata

### ⚡ Ottimizzazione Performance

#### Per Raspberry Pi

```python
# mente_ai_reale.py - Config class

class Config:
    # Usa modelli leggeri
    YOLO_MODEL = "yolov8n.pt"  # nano
    WHISPER_MODEL = "tiny"     # più veloce
    LLM_MODEL = "gpt2"         # 124M params
    
    # Riduci risoluzione
    CAMERA_WIDTH = 416
    CAMERA_HEIGHT = 416
    CAMERA_FPS = 10
    
    # Ottimizza inferenza
    USE_GPU = False
    BATCH_SIZE = 1
    NUM_THREADS = 4
```

#### Per GPU NVIDIA

```python
class Config:
    # Usa modelli più grandi
    YOLO_MODEL = "yolov8m.pt"
    WHISPER_MODEL = "small"
    LLM_MODEL = "gpt-j-6b"
    
    # Alta qualità
    CAMERA_WIDTH = 1280
    CAMERA_HEIGHT = 720
    CAMERA_FPS = 30
    
    # GPU acceleration
    USE_GPU = True
    DEVICE = "cuda"
    FP16 = True  # Mixed precision
```

### 🔐 Sicurezza

```bash
# Crea utente dedicato
sudo adduser mente_ai
sudo usermod -aG video,audio mente_ai

# Limita risorse
sudo systemctl set-property mente_ai.service MemoryLimit=2G
sudo systemctl set-property mente_ai.service CPUQuota=50%
```

### 📡 Networking

```python
# Esponi API
uvicorn server:app --host 0.0.0.0 --port 8000

# WebSocket per streaming
from fastapi import WebSocket

@app.websocket("/ws/stream")
async def websocket_stream(websocket: WebSocket):
    await websocket.accept()
    while True:
        frame = mente.talamo.visione.cattura_frame()
        await websocket.send_bytes(frame.tobytes())
```

---

## 📊 Benchmark e Testing

### 🧪 Test Suite

```bash
# Test completo
python test_hardware.py

# Test specifici
python -m pytest tests/test_visione.py
python -m pytest tests/test_audio.py
python -m pytest tests/test_memoria.py
python -m pytest tests/test_integrazione.py
```

### 📈 Metriche Performance

```python
# Profiling
import cProfile
import pstats

profiler = cProfile.Profile()
profiler.enable()

# Run cognitive cycle
mente.ciclo_cognitivo()

profiler.disable()
stats = pstats.Stats(profiler)
stats.sort_stats('cumulative')
stats.print_stats(20)
```

---

## 🔮 Roadmap

### ✅ Fase 1: Base (Completata)
- [x] Architettura modulare
- [x] Integrazione YOLOv8
- [x] Integrazione Whisper
- [x] Integrazione LLM (GPT-2)
- [x] Sistema memoria episodica
- [x] Sistema reward base

### 🚧 Fase 2: Avanzata (In Corso)
- [ ] Vector database (FAISS/Pinecone)
- [ ] Fine-tuning modelli custom
- [ ] Integrazione sensori IoT
- [ ] ROS 2 integration
- [ ] Web dashboard monitoring

### 🔜 Fase 3: Produzione (Pianificata)
- [ ] Multi-agent communication
- [ ] Cloud synchronization
- [ ] Edge deployment optimization
- [ ] Hardware custom (PCB)
- [ ] Mobile app controller

### 💡 Fase 4: Ricerca (Futuro)
- [ ] Meta-learning
- [ ] Transfer learning
- [ ] Sim-to-real training
- [ ] Cognitive architectures comparison
- [ ] Neuromorphic computing

---

## 📚 Documentazione Estesa

- 📖 **[Guida Installazione](docs/INSTALL.md)** - Setup dettagliato
- 🏗️ **[Architettura](docs/ARCHITECTURE.md)** - Design patterns
- 🔌 **[API Reference](docs/API.md)** - Documentazione API
- 🎓 **[Tutorial](docs/TUTORIALS.md)** - Guide passo-passo
- 🐛 **[Troubleshooting](docs/TROUBLESHOOTING.md)** - Risoluzione problemi
- 📊 **[Benchmark](docs/BENCHMARKS.md)** - Performance analysis

---

## 🤝 Contributi

Contributi benvenuti! Come contribuire:

1. **Fork** il repository
2. **Crea** un branch (`git checkout -b feature/amazing-feature`)
3. **Commit** i cambiamenti (`git commit -m 'Add amazing feature'`)
4. **Push** al branch (`git push origin feature/amazing-feature`)
5. **Apri** una Pull Request

### 🎯 Aree di Interesse

- 🧪 **Testing**: Nuovi test cases, edge cases
- ⚡ **Ottimizzazione**: Performance improvements
- 🔧 **Hardware**: Nuovi sensori/attuatori
- 🤖 **Modelli**: Fine-tuning, nuovi modelli
- 📱 **Platform**: Android, iOS, Web
- 📚 **Documentazione**: Tutorial, esempi

---

## 📄 Licenza

MIT License - Vedi [LICENSE](LICENSE) per dettagli.

Puoi usare liberamente questo codice per:
- ✅ Progetti personali
- ✅ Progetti commerciali
- ✅ Ricerca accademica
- ✅ Modifiche e derivazioni

---

## 🙏 Credits

### Modelli AI
- **YOLOv8**: Ultralytics
- **Whisper**: OpenAI
- **Transformers**: Hugging Face
- **PyTorch**: Meta AI

### Ispirazione
- Neuroscienze cognitive
- Architetture multi-agente
- Robot Operating System (ROS)

---

## 📬 Contatti

- **Issues**: [GitHub Issues](https://github.com/your-repo/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-repo/discussions)
- **Email**: your-email@example.com

---

## ⭐ Star History

Se trovi utile questo progetto, lascia una ⭐!

---

<div align="center">

**🧠 Costruito con passione per l'Intelligenza Artificiale Cognitiva**

*"Non è magia, è ingegneria cognitiva"*

</div>

