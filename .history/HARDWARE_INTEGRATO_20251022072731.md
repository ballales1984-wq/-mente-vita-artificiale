# 📷🎤 Hardware Integrato - Camera + Microfono

## ✅ Corteccia Visiva + Uditiva ATTIVATE!

Entrambi i moduli sensoriali sono ora pronti per hardware reale!

---

## 📷 Corteccia Visiva (Camera)

### 🔧 Funzionalità Implementate

```python
corteccia_visiva = visione.get_instance()

# Inizializza camera
corteccia_visiva.inizializza_camera(camera_id=0)
# Output:
# [Corteccia Visiva] ✅ Camera inizializzata
#   • Risoluzione: 640x480
#   • FPS: 30.0

# Cattura e elabora
ret, frame = corteccia_visiva.camera.read()
risultato = corteccia_visiva.elabora(frame)

# Risultato:
# {
#   'tipo': 'reale',
#   'oggetti': [
#       {'classe': 'person', 'confidenza': 0.92, 'bbox': [...]}
#   ],
#   'descrizione': 'Rilevati: 1 person, 1 laptop'
# }
```

### 📋 Metodi Aggiunti

| Metodo | Funzione |
|--------|----------|
| `inizializza_camera(camera_id)` | Inizializza webcam |
| `camera_inizializzata` | Flag stato camera |
| `frame_corrente` | Ultimo frame catturato |

---

## 🎤 Corteccia Uditiva (Microfono)

### 🔧 Funzionalità Implementate

```python
corteccia_uditiva = udito.get_instance()

# Inizializza microfono
corteccia_uditiva.inizializza_microfono()
# Output:
# [Corteccia Uditiva] ✅ Microfono inizializzato
#   • Dispositivo: Microfono (Realtek Audio)
#   • Canali: 1
#   • Sample rate: 16000 Hz

# Registra e trascrivi
audio = sd.rec(int(3 * 16000), samplerate=16000, channels=1)
sd.wait()

risultato = corteccia_uditiva.ascolta(audio.flatten())

# Risultato:
# {
#   'tipo': 'reale',
#   'testo': 'Vieni qui per favore',
#   'tono': 'amichevole',
#   'intenzione': 'comando',
#   'emozione': 'neutro'
# }
```

### 📋 Metodi Aggiunti

| Metodo | Funzione |
|--------|----------|
| `inizializza_microfono(device_id)` | Inizializza microfono |
| `lista_microfoni()` | Elenca dispositivi audio |
| `microfono_inizializzato` | Flag stato microfono |

---

## 🎮 Programmi Creati

### 1. **mente_con_camera.py**
```bash
python mente_con_camera.py
```

**Modalità:**
- **1. Ciclo singolo** - Cattura → Analizza → Risultato
- **2. Streaming live** - Video continuo (Premi 'c')
- **3. Foto analisi** - Scatta (SPAZIO) → Analisi dettagliata
- **4. Sorveglianza** - Rileva persone/veicoli automaticamente

### 2. **mente_con_microfono.py**
```bash
python mente_con_microfono.py
```

**Modalità:**
- **1. Comando vocale** - Parla → Trascrivi → Esegui
- **2. Ascolto continuo** - Loop trascrizione infinito
- **3. Assistente vocale** - Interazione comando-risposta
- **4. Lista microfoni** - Mostra dispositivi

### 3. **mente_multimodale.py** ⭐
```bash
python mente_multimodale.py
```

**Sistema completo:**
- Camera + Microfono insieme
- Percezione multimodale sincronizzata
- Biosegnali neurali
- Memoria intelligente
- Decision making influenzato da entrambi

---

## 🔄 Flusso Multimodale

```
┌──────────────┐     ┌──────────────┐
│   CAMERA     │     │  MICROFONO   │
│   (Video)    │     │   (Audio)    │
└──────┬───────┘     └──────┬───────┘
       │                    │
       ▼                    ▼
┌──────────────┐     ┌──────────────┐
│  YOLOv8      │     │   Whisper    │
│ Object Det.  │     │ Speech-to-Text│
└──────┬───────┘     └──────┬───────┘
       │                    │
       └────────┬───────────┘
                │
                ▼
       ┌─────────────────┐
       │ INTEGRAZIONE    │
       │ MULTIMODALE     │
       └────────┬────────┘
                │
                ▼
       ┌─────────────────┐
       │ PATTERN NEURALE │
       │ ░░███████░░     │
       └────────┬────────┘
                │
                ▼
       ┌─────────────────┐
       │ DECISIONE       │
       │ influenzata da  │
       │ VISIONE + AUDIO │
       └─────────────────┘
```

---

## 🧪 Test

### Test Camera
```bash
python mente_con_camera.py
# Verifica:
# - Camera si apre
# - Frame catturati
# - YOLOv8 rileva oggetti
# - Annotazioni mostrate
```

### Test Microfono
```bash
python mente_con_microfono.py
# Verifica:
# - Microfono rilevato
# - Audio registrato
# - Whisper trascrive
# - Comandi riconosciuti
```

### Test Multimodale
```bash
python mente_multimodale.py
# Verifica:
# - Entrambi i sensori
# - Sincronizzazione
# - Decisioni da entrambi input
```

---

## 📊 Output Esempio

### Camera + Microfono Insieme:

```
[CICLO MULTIMODALE #1]

[1/8] PERCEZIONE VISIVA...
  ✓ [REALE] Rilevati: 1 person, 1 laptop, 1 bottle

[2/8] PERCEZIONE UDITIVA...
  🎤 Registrazione (3s)... PARLA ORA!
  ✓ [REALE] 'Vieni qui per favore'

[3/8] BIOSEGNALI NEURALI...
  Pattern: ░░███████████░░
  Neuroni attivi: 11

[4/8] RICHIAMO MEMORIA...
  ✓ Memorie: 3
    - Comando 'vieni qui' eseguito con successo...
    - Persona rilevata, mantenuta distanza...

[5/8] EMOZIONE...
  ✓ Stato: POSITIVO (valenza: +0.75)

[6/8] RAGIONAMENTO...
  💡 Memoria suggerisce: avvicinati
  ✓ Decisione: AVVICINATI
  ✓ Priorita: 0.95

[7/8] AZIONE...
  ✓ Risultato: [OK]

[8/8] APPRENDIMENTO...
  ✓ Reward: +1.73

──────────────────────────────────────
[REPORT] Ciclo #1 completato
  Input visivo: REALE ✅
  Input audio: REALE ✅
  Decisione: avvicinati
  Reward: +1.73
──────────────────────────────────────
```

---

## 🎯 Caratteristiche Chiave

### ✅ Sincronizzazione Perfetta
- Camera e microfono lavorano insieme
- Input temporalmente allineati
- Decisioni basate su entrambi

### ✅ Fallback Intelligente
- Se camera assente → usa simulazione visiva
- Se microfono assente → usa simulazione audio
- Sistema funziona sempre!

### ✅ Real-Time Processing
- YOLOv8: ~50ms per frame
- Whisper: ~2s per 3s audio
- Totale ciclo: ~3-4s

---

## 🔌 Hardware Supportato

### Camera
- ✅ Webcam USB
- ✅ Camera integrata laptop
- ✅ Pi Camera (Raspberry Pi)
- ✅ Camera IP (con modifiche)

### Microfono
- ✅ Microfono USB
- ✅ Microfono integrato
- ✅ Cuffie con microfono
- ✅ Array microfonici

---

## 🚀 Quick Start

### Modo 1: Solo Camera
```bash
python mente_con_camera.py
```

### Modo 2: Solo Microfono
```bash
python mente_con_microfono.py
```

### Modo 3: Entrambi ⭐
```bash
python mente_multimodale.py
```

---

## 💡 Esempi d'Uso

### Robot di Sorveglianza
```python
# Camera rileva persona
# Microfono cattura suono
# → Sistema decide: "mantieni_distanza"
```

### Assistente Domestico
```python
# Camera vede: bottiglia vuota
# Voce dice: "prendi la bottiglia"
# → Sistema decide: "avvicinati_e_prendi"
```

### Robot Sociale
```python
# Camera vede: persona che saluta
# Voce dice: "ciao"
# → Sistema decide: "saluta_di_ritorno"
```

---

## 🏆 Achievement Unlocked!

**"Sensory Master"** - Hai integrato camera E microfono reali!

Il sistema ora può:
- ✅ Vedere il mondo reale (YOLOv8)
- ✅ Sentire comandi vocali (Whisper)
- ✅ Processare entrambi insieme
- ✅ Decidere basandosi su percezione completa
- ✅ Apprendere dall'esperienza multimodale

**La mente artificiale ha OCCHI e ORECCHIE funzionanti!** 👁️🎤🧠

