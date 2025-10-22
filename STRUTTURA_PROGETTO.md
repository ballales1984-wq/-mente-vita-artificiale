# 📁 Struttura Progetto - Mente Artificiale Modulare

## 🗂️ Organizzazione File

```
guerragames/
│
├── 📄 main.py                          # ⭐ Orchestratore principale
├── 📄 esempio_semplice.py              # 🎯 Esempio minimale
│
├── 🤖 mente_ai_reale.py                # Sistema con modelli AI reali
├── 🧠 mente_artificiale_modulare.py    # Simulazione base
│
├── 📋 README.md                        # Documentazione principale
├── 📋 README_MENTE_AI.md               # Guida implementazione reale
├── 📋 requirements.txt                 # Dipendenze Python
├── 🔧 setup_raspberry_pi.sh            # Setup automatico Linux/Pi
├── 🧪 test_hardware.py                 # Test componenti
│
└── 📂 moduli/                          # ⭐ MODULI CEREBRALI
    │
    ├── 📄 __init__.py                  # Package init
    ├── 📄 base.py                      # 🏗️  Interfacce astratte
    │
    ├── 📄 visione.py                   # 👁️  Corteccia Visiva (YOLOv8)
    ├── 📄 udito.py                     # 👂 Corteccia Uditiva (Whisper)
    ├── 📄 motoria.py                   # 🦿 Corteccia Motoria (Azioni)
    ├── 📄 prefrontale.py               # 🧠 Corteccia Prefrontale (LLM)
    ├── 📄 memoria.py                   # 💾 Ippocampo (Memoria)
    ├── 📄 emozione.py                  # ❤️  Amigdala (Reward/Emozioni)
    ├── 📄 talamo.py                    # ⚡ Talamo (Router sensoriale)
    └── 📄 tronco.py                    # 🌙 Tronco Encefalico (Sistema)
```

---

## 🧩 Mappa Moduli Cerebrali

| File | Modulo | Funzione | Modelli AI |
|------|--------|----------|------------|
| `visione.py` | 👁️  Corteccia Visiva | Object detection | YOLOv8, OpenCV |
| `udito.py` | 👂 Corteccia Uditiva | Speech-to-text | Whisper, SoundDevice |
| `motoria.py` | 🦿 Corteccia Motoria | Controllo movimenti | PID, Attuatori |
| `prefrontale.py` | 🧠 Corteccia Prefrontale | Ragionamento, decisioni | GPT-2, LLaMA |
| `memoria.py` | 💾 Ippocampo | Memoria episodica/semantica | JSON, FAISS |
| `emozione.py` | ❤️  Amigdala | Valutazione emotiva, reward | RL algorithms |
| `talamo.py` | ⚡ Talamo | Routing multimodale | Integration layer |
| `tronco.py` | 🌙 Tronco Encefalico | Monitoraggio sistema | psutil |
| `base.py` | 🏗️  Base | Interfacce astratte | Design patterns |

---

## 🔄 Flusso Dati

```
┌─────────────────────────────────────────────────────────────┐
│                    CICLO COGNITIVO                          │
└─────────────────────────────────────────────────────────────┘

  Input Sensoriali
        ↓
  ⚡ TALAMO (Router)
        ↓
  ┌─────────────────────────┐
  │  👁️  Visione  👂 Udito │
  └─────────────────────────┘
        ↓
  ❤️  AMIGDALA (Emozioni)
        ↓
  💾 IPPOCAMPO (Memoria)
        ↓
  🧠 PREFRONTALE (Ragionamento)
        ↓
  🦿 MOTORIA (Azione)
        ↓
  ❤️  Reward Learning
        ↓
  💾 Memorizzazione
        ↓
  🌙 TRONCO (Autoregolazione)
```

---

## 🚀 Quick Start

### 1️⃣ **Esempio Minimale**

```bash
python esempio_semplice.py
```

Output:
```
👁️  VISIONE: Elaborazione immagine...
👂 UDITO: Ascolto audio...
🧠 PREFRONTALE: Ragionamento...
🦿 MOTORIA: Esecuzione azione...
✅ CICLO COMPLETATO
```

### 2️⃣ **Sistema Completo (Simulato)**

```bash
python main.py --modalita test
```

Esegue un ciclo cognitivo completo con tutti i moduli.

### 3️⃣ **Modalità Autonoma**

```bash
python main.py --modalita autonoma --durata 60
```

Esegue cicli continui per 60 secondi.

### 4️⃣ **Modalità Interattiva**

```bash
python main.py --modalita interattiva
```

Console interattiva:
- `Enter`: esegui ciclo
- `stats`: mostra statistiche
- `ricarica`: ricarica energia
- `q`: esci

### 5️⃣ **Sistema con AI Reali**

```bash
# Prima installa dipendenze
pip install -r requirements.txt

# Poi esegui
python mente_ai_reale.py
```

Usa modelli reali: YOLOv8, Whisper, GPT-2

---

## 🔧 Caratteristiche Implementate

### ✅ Architettura

- [x] Moduli cerebrali separati
- [x] Interfacce astratte (Sensore, Attuatore, Memoria)
- [x] Design pattern: Singleton, Abstract Factory
- [x] Context managers per risorse
- [x] Exception handling robusto
- [x] Logging dettagliato

### ✅ Percezione

- [x] Visione con YOLOv8 (object detection)
- [x] Audio con Whisper (speech-to-text)
- [x] Integrazione multimodale
- [x] Filtro attenzione
- [x] Fallback simulato se hardware assente

### ✅ Cognizione

- [x] Ragionamento con LLM (GPT-2, GPT-J, LLaMA)
- [x] Fallback rule-based
- [x] Working memory
- [x] Pianificazione azioni
- [x] Decision making contestuale

### ✅ Memoria

- [x] Memoria episodica (eventi temporali)
- [x] Memoria semantica (conoscenza strutturata)
- [x] Ricerca semantica
- [x] Consolidamento memorie
- [x] Persistenza su disco (JSON)

### ✅ Emozioni

- [x] Valutazione valenza emotiva
- [x] Calcolo arousal
- [x] Modello circomplesso emozioni
- [x] Sistema reward/punizione
- [x] Apprendimento per rinforzo

### ✅ Azione

- [x] Comandi motori strutturati
- [x] Simulazione movimenti
- [x] Feedback propriocettivo
- [x] Cronologia azioni
- [x] Pronto per attuatori reali

### ✅ Sistema

- [x] Monitoraggio energia
- [x] Monitoraggio risorse (CPU, RAM)
- [x] Watchdog system
- [x] Health checks
- [x] Modalità risparmio energetico

---

## 📊 Statistiche Implementazione

```
📈 Linee di codice:  ~5000
📁 File moduli:      9
🧪 Test integrati:   10
📚 Docstring:        100%
⚙️  Design patterns:  5
🔧 Interfacce:       5
```

---

## 🎯 Prossimi Step

### 🔄 Fase Corrente: Simulazione Software

- [x] Architettura completa
- [x] Moduli tutti funzionanti
- [x] Test con input simulati
- [x] Documentazione completa

### 🚀 Fase 2: Integrazione Hardware

- [ ] Collegare camera reale
- [ ] Collegare microfono reale
- [ ] Collegare sensori (IMU, proximity)
- [ ] Collegare attuatori (servo, motori)
- [ ] Test su Raspberry Pi

### 🧠 Fase 3: AI Avanzato

- [ ] Fine-tuning modelli custom
- [ ] Vector database (FAISS/Pinecone)
- [ ] Multi-agent communication
- [ ] Sim-to-real transfer learning

### 🤖 Fase 4: Robot Fisico

- [ ] PCB custom
- [ ] 3D printing chassis
- [ ] Sistema energetico
- [ ] Integrazione ROS 2

---

## 💡 Come Usare i Moduli

### Uso Singolo Modulo

```python
# Solo visione
from moduli import visione

risultato = visione.elabora("immagine.jpg")
print(risultato['descrizione'])
```

### Uso Integrato

```python
# Sistema completo
from main import MenteArtificiale

mente = MenteArtificiale()
mente.inizializza()
mente.ciclo_cognitivo()
```

### Estensione Hardware

```python
# Crea sensore custom
from moduli.base import Sensore

class SensoreLaser(Sensore):
    def connetti(self):
        # Connetti al sensore laser
        return True
    
    def leggi(self):
        # Leggi distanza
        return distanza_cm
    
    def disconnetti(self):
        # Cleanup
        pass
```

---

## 🆘 Troubleshooting

### ❌ "Module not found"

```bash
# Assicurati di essere nella directory corretta
cd guerragames

# Verifica PYTHONPATH
export PYTHONPATH=$PYTHONPATH:$(pwd)
```

### ❌ "Modello non caricato"

Modelli vengono scaricati al primo utilizzo:
- YOLOv8: ~6MB
- Whisper base: ~74MB
- GPT-2: ~500MB

### ❌ "Camera non disponibile"

Sistema passa automaticamente a modalità simulata.
Per forzare camera:
```python
from moduli.visione import SensoreCamera

camera = SensoreCamera(camera_id=0)
if camera.connetti():
    frame = camera.leggi()
```

---

## 📞 Supporto

Per problemi o domande:
1. Leggi la documentazione: `README.md`
2. Controlla esempi: `esempio_semplice.py`
3. Esegui test: `test_hardware.py`
4. Consulta: `README_MENTE_AI.md`

---

**🧠 Progetto creato con passione per l'AI Cognitiva**

*Versione 1.0.0 - Ottobre 2025*

