# 📊 Dashboard Streamlit - Guida Completa

## 🎯 Cos'è

Dashboard web interattiva per visualizzare in tempo reale:
- 👁️ Feed camera e oggetti rilevati
- 🎤 Trascrizioni audio
- 💾 Memoria episodica
- ❤️ Emozioni e reward
- ⚡ Biosegnali neurali
- 🧠 Decisioni e ragionamento

---

## 🚀 Quick Start

### 1. Installa Streamlit

```bash
pip install streamlit pandas
```

### 2. Avvia Dashboard

```bash
streamlit run dashboard.py
```

### 3. Apri Browser

Automaticamente si apre: `http://localhost:8501`

---

## 📊 Sezioni Dashboard

### 📈 **Stato Sistema** (In Alto)

Metriche principali:
- Cicli eseguiti
- Memorie totali
- Reward accumulato
- Uptime

### 👁️👂 **Percezione Multimodale**

**Tab Visione:**
- Feed camera (ultimo frame)
- Oggetti rilevati con confidence
- Annotazioni YOLOv8

**Tab Udito:**
- Trascrizione testo
- Tono vocale
- Intenzione rilevata

### ⚡ **Biosegnali Neurali**

- Pattern binario visualizzato
- Neuroni attivi
- Arousal e ritmo
- Energia neurale

### 💾 **Memoria Episodica**

- Lista episodi con filtri
- Timeline temporale
- Valenza e importanza
- Numero accessi

### ❤️ **Sistema Emotivo**

- Stato emotivo corrente
- Valenza emotiva
- Grafico evoluzione emozioni
- Reward statistiche

### 🧠 **Ragionamento**

- Ultima decisione
- Priorità
- Fonte decisione (memoria/rete/ragionamento)
- Distribuzione azioni

### 🎓 **Apprendimento**

- Cicli training
- Loss media
- Stato modello
- Performance

### 📅 **Timeline**

- Cronologia completa
- Espansibile per dettagli
- Filtri e ricerca

---

## 🎮 Utilizzo

### Modalità 1: Monitor Passivo

```bash
# Terminal 1: Esegui sistema
python mente_completa_finale.py

# Terminal 2: Avvia dashboard
streamlit run dashboard.py
```

Dashboard mostra dati in tempo reale!

### Modalità 2: Con Auto-Refresh

1. Avvia dashboard
2. Spunta "Auto-refresh (5s)" nella sidebar
3. Dashboard si aggiorna automaticamente ogni 5 secondi

### Modalità 3: Esplorazione Dati

- Naviga tra tab
- Espandi episodi nella timeline
- Filtra memorie
- Analizza grafici

---

## 📂 File Monitorati

La dashboard legge:

| File | Contenuto |
|------|-----------|
| `data/memoria.json` | Memoria episodica completa |
| `frame_*.jpg` | Frame catturati da camera |
| `camera_*.jpg` | Screenshot camera |
| `data/modello_online.pt` | Rete neurale salvata |

---

## 🎨 Personalizzazione

### Modifica Colori

```python
# In dashboard.py
st.markdown("""
<style>
    .metric-card {
        background-color: #YOUR_COLOR;
    }
</style>
""", unsafe_allow_html=True)
```

### Aggiungi Sezioni

```python
# Nuova sezione
st.header("🆕 Nuova Sezione")
# ... tuo codice ...
```

### Modifica Layout

```python
# Cambia numero colonne
col1, col2, col3, col4, col5 = st.columns(5)
```

---

## 🔧 Troubleshooting

### Dashboard non si apre

```bash
# Verifica installazione
pip install streamlit

# Riavvia
streamlit run dashboard.py
```

### Dati non visualizzati

```bash
# Verifica file memoria
dir data\memoria.json

# Se manca, esegui almeno 1 ciclo
python esempio_semplice.py
```

### Errori import

```bash
# Installa dipendenze
pip install pandas plotly
```

---

## 📸 Screenshot

### Vista Principale
```
+----------------------------------+------------------+
|  Stato Sistema                   |   Sidebar       |
|  Cicli: 15 | Memorie: 35        |   ⚙️ Controlli   |
+----------------------------------+   🎛️ Config      |
|  👁️ Visione    | 👂 Udito        |                  |
|  [Frame Camera] | "Vieni qui"    |                  |
+----------------------------------+------------------+
|  ⚡ Biosegnali                   |
|  ░░░███████████░░               |
+----------------------------------+
|  💾 Memoria                      |
|  [Tabella episodi...]           |
+----------------------------------+
```

---

## 🌟 Funzionalità Avanzate

### Esportazione Dati

```python
# Aggiungi a dashboard.py
if st.button("📥 Esporta CSV"):
    df.to_csv("episodi_export.csv")
    st.download_button("Download", data="...")
```

### Grafici Interattivi

```python
import plotly.express as px

fig = px.line(df_emozioni, x='Ciclo', y='Valenza')
st.plotly_chart(fig)
```

### Filtri

```python
# Filtra per valenza
min_valenza = st.slider("Valenza minima", -1.0, 1.0, 0.0)
memorie_filtrate = [m for m in memorie if m['valenza_emotiva'] >= min_valenza]
```

---

## 🚀 Deploy

### Locale

```bash
streamlit run dashboard.py --server.port 8501
```

### Cloud (Streamlit Cloud)

1. Push su GitHub
2. Vai su https://streamlit.io/cloud
3. Connect repository
4. Deploy!

### Network

```bash
# Accessibile da altri PC nella rete
streamlit run dashboard.py --server.address 0.0.0.0
```

Apri da altro PC: `http://IP_PC:8501`

---

## 📋 Checklist

Prima di usare:

- [ ] Streamlit installato
- [ ] File `data/memoria.json` esiste
- [ ] Eseguito almeno 1 ciclo
- [ ] Port 8501 libera

---

## ✅ Pronto!

**Avvia dashboard:**
```bash
streamlit run dashboard.py
```

**Poi esegui sistema:**
```bash
python mente_completa_finale.py
```

**Osserva la mente pensare in tempo reale!** 🧠✨

---

**File creato:** `dashboard.py` (completo e funzionante)  
**Dipendenze:** Aggiunte a `requirements.txt`

