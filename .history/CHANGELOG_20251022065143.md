# 📝 Changelog

Tutte le modifiche importanti al progetto sono documentate qui.

---

## [2.0.0] - 2025-10-22

### ⭐ Aggiunte (MAJOR)

#### 💾 Sistema Memoria Intelligente
- **Consolidamento automatico** ogni 5 minuti
  - Thread background
  - Elimina memorie: valenza ≤ 0.5 E importanza ≤ 1.0
  - Conserva memorie rilevanti/recenti/richiamate
- **Richiamo contestuale** con suggerimenti
  - Score composito (similarity, importanza, valenza, accessi, recency)
  - Genera azioni consigliate (confidence 90%)
  - Influenza decisioni del sistema
- API: `richiama_contestuale()`, `consolida_memorie_intelligente()`

#### ⚡ Biosegnali Neurali
- **Layer neurale bioelettrico** completo
  - Codifica binaria pattern (es. `░░███████░░`)
  - Propagazione simmetrica da impulso centrale
  - Calcolo intensità, direzione, latenza
- **Ritmi cerebrali** simulati
  - ALFA (8-12 Hz): rilassato
  - BETA (13-30 Hz): attivo
  - GAMMA (30-100 Hz): concentrato
- **Stimoli interni** spontanei
  - Pensieri spontanei (10% probabilità)
  - Insight improvvisi
  - Influenza arousal dinamico
- **Interfaccia EEG/EMG** pronta
  - `SimulatoreEEG` per sviluppo
  - Pronto per sensori reali (plug-and-play)
- Nuovi moduli: `biosegnale.py`, `segnali_neurali.py`

#### 🎮 Nuovi Programmi
- `mente_ai_biosegnali.py` - Integrazione biosegnali
- `mente_ai_cicli.py` - Cicli continui con memoria
- `test_memoria_avanzata.py` - Test sistema memoria

### 🔧 Miglioramenti

- Sistema di statistiche espanse
- Visualizzazione pattern neurali
- Report finali dettagliati
- Salvataggio automatico memoria

### 📚 Documentazione

- `MEMORIA_INTELLIGENTE.md` - Sistema memoria
- `BIOSEGNALI_INTEGRATI.md` - Layer neurale
- `SEGNALI_BIOELETTRICI.md` - Codifica binaria
- `PROGETTO_COMPLETO_FINALE.md` - Riepilogo
- `QUICK_START.txt` - Guida rapida

---

## [1.0.0] - 2025-10-22

### ⭐ Aggiunte (INITIAL RELEASE)

#### 🏗️ Architettura Base
- Sistema modulare completo con 9 moduli cerebrali
- Pattern: Singleton, Abstract Factory, Context Manager
- Interfacce astratte: `Sensore`, `Attuatore`, `MemoriaAstratta`

#### 🧠 Moduli Cognitivi
- `visione.py` - Corteccia Visiva (YOLOv8)
- `udito.py` - Corteccia Uditiva (Whisper)
- `prefrontale.py` - Ragionamento (LLM)
- `memoria.py` - Ippocampo base
- `emozione.py` - Amigdala
- `motoria.py` - Corteccia Motoria
- `talamo.py` - Router sensoriale
- `tronco.py` - Sistema vitale
- `base.py` - Interfacce astratte

#### 🎮 Programmi
- `main.py` - Orchestratore completo
- `esempio_semplice.py` - Demo base
- `mente_ai_reale.py` - Con modelli reali

#### 🔧 Utilità
- `test_hardware.py` - Test componenti
- `setup_raspberry_pi.sh` - Setup Linux/Pi
- `requirements.txt` - Dipendenze

#### 📚 Documentazione
- `README.md` - Guida principale
- `README_MENTE_AI.md` - Setup hardware
- `COME_FUNZIONA.md` - Spiegazione
- `STRUTTURA_PROGETTO.md` - Organizzazione
- `COMPLETATO.md` - Riepilogo

#### 📦 Build
- Script PyInstaller per EXE
- Launcher batch Windows
- 2 eseguibili creati

---

## [0.1.0] - 2025-10-22 (Alpha)

### Aggiunte Iniziali
- Proof of concept base
- Simulazione semplice
- Test architettura

---

## 🔮 Roadmap Futuro

### [2.1.0] - Planned
- [ ] Vector database (FAISS)
- [ ] Fine-tuning modelli custom
- [ ] ROS 2 integration
- [ ] Web dashboard

### [3.0.0] - Future
- [ ] Multi-agent communication
- [ ] Cloud sync
- [ ] Mobile app
- [ ] Neuromorphic hardware

---

## 📊 Statistiche Versioni

| Versione | Data | Moduli | Righe Codice | Funzionalità |
|----------|------|--------|--------------|--------------|
| 0.1.0 | 22/10/2025 | 5 | ~2000 | Base |
| 1.0.0 | 22/10/2025 | 9 | ~6000 | Completo |
| 2.0.0 | 22/10/2025 | 11 | ~8000+ | Memoria + Biosegnali ⭐ |

---

**Mantieni questo file aggiornato ad ogni release!**

