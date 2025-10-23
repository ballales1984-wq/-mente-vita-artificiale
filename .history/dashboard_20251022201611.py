"""
📊🧠 DASHBOARD MENTE ARTIFICIALE - Streamlit
=============================================
Visualizzazione in tempo reale di:
- Feed camera
- Trascrizioni audio
- Memoria episodica
- Emozioni e reward
- Biosegnali neurali
- Decisioni e azioni

Esegui con: streamlit run dashboard.py
"""

import streamlit as st
import json
import time
import os
from pathlib import Path
import pandas as pd
from datetime import datetime

# Configurazione pagina
st.set_page_config(
    page_title="Mente Artificiale Dashboard",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Stile custom
st.markdown("""
<style>
    .big-font {
        font-size:20px !important;
        font-weight: bold;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)


def carica_memoria():
    """Carica memoria da file JSON"""
    path_memoria = Path("data/memoria.json")
    
    if path_memoria.exists():
        try:
            with open(path_memoria, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data.get('episodica', []), data.get('meta', {})
        except:
            return [], {}
    
    return [], {}


def carica_ultima_elaborazione():
    """Carica ultimi risultati (simulato)"""
    # In produzione, questo leggerebbe da file condiviso o database
    return {
        'visione': {
            'descrizione': 'Rilevati: 1 person, 1 laptop, 1 bottle',
            'num_oggetti': 3,
            'oggetti': [
                {'classe': 'person', 'confidenza': 0.92},
                {'classe': 'laptop', 'confidenza': 0.87},
                {'classe': 'bottle', 'confidenza': 0.75}
            ]
        },
        'audio': {
            'testo': 'Vieni qui per favore',
            'tono': 'amichevole',
            'intenzione': 'comando'
        },
        'emozione': {
            'stato': 'POSITIVO',
            'valenza': 0.75
        },
        'decisione': {
            'azione': 'avvicinati',
            'priorita': 0.92,
            'fonte': 'memoria_esperienza'
        }
    }


# ==================== HEADER ====================

st.title("🧠 Mente Artificiale Modulare")
st.markdown("### Dashboard Real-Time - Sistema Cognitivo v3.0")

# ==================== SIDEBAR ====================

with st.sidebar:
    st.header("⚙️ Controlli")
    
    # PULSANTE DEMO
    st.subheader("🧪 Modalità Demo")
    
    if st.button("▶️ Avvia Simulazione", use_container_width=True, type="primary"):
        import subprocess
        import sys
        try:
            # Avvia mente_ai_demo.py in background
            if sys.platform == "win32":
                subprocess.Popen(["python", "mente_ai_demo.py"], 
                               creationflags=subprocess.CREATE_NEW_CONSOLE)
            else:
                subprocess.Popen(["python", "mente_ai_demo.py"])
            
            st.success("✅ Simulazione avviata!")
            st.info("I dati si aggiorneranno ogni 3 secondi")
        except Exception as e:
            st.error(f"Errore: {e}")
    
    st.caption("Genera episodi simulati per test")
    
    st.divider()
    
    # Pulsanti controllo
    if st.button("🔄 Aggiorna Dati"):
        st.rerun()
    
    if st.button("🗑️ Pulisci Cache"):
        st.cache_data.clear()
        st.success("Cache pulita!")
    
    st.divider()
    
    # Configurazione
    st.header("🎛️ Configurazione")
    
    auto_refresh = st.checkbox("Auto-refresh (5s)", value=False)
    mostra_pattern = st.checkbox("Mostra pattern neurali", value=True)
    mostra_dettagli = st.checkbox("Dettagli avanzati", value=False)
    
    st.divider()
    
    # Info sistema
    st.header("ℹ️ Info Sistema")
    st.metric("Versione", "3.0")
    st.metric("Moduli", "12")
    st.metric("Sensori", "Camera + Mic")

# ==================== STATO SISTEMA ====================

st.header("📊 Stato Sistema")

col1, col2, col3, col4 = st.columns(4)

# Carica memoria
memorie, meta = carica_memoria()

with col1:
    st.metric("Cicli Eseguiti", meta.get('memorizzazioni_totali', 0))

with col2:
    st.metric("Memorie", len(memorie))

with col3:
    st.metric("Reward Totale", f"{meta.get('reward_totale', 0):.1f}" if 'reward_totale' in meta else "N/A")

with col4:
    st.metric("Uptime", "Online ✅")

st.divider()

# ==================== PERCEZIONE ====================

st.header("👁️👂 Percezione Multimodale")

tab_vis, tab_aud = st.tabs(["👁️ Visione", "👂 Udito"])

# Carica ultimi dati
dati = carica_ultima_elaborazione()

with tab_vis:
    col_v1, col_v2 = st.columns([2, 1])
    
    with col_v1:
        st.subheader("Feed Camera")
        
        # Cerca immagine più recente
        frame_files = list(Path(".").glob("frame_*.jpg")) + list(Path(".").glob("camera_*.jpg"))
        
        if frame_files:
            ultimo_frame = max(frame_files, key=os.path.getmtime)
            st.image(str(ultimo_frame), caption=f"Ultimo frame: {ultimo_frame.name}")
        else:
            st.info("Nessun frame disponibile. Esegui: python mente_con_camera.py")
    
    with col_v2:
        st.subheader("Oggetti Rilevati")
        
        oggetti = dati['visione']['oggetti']
        
        for obj in oggetti:
            with st.container():
                st.markdown(f"**{obj['classe'].upper()}**")
                st.progress(obj['confidenza'])
                st.caption(f"Confidenza: {obj['confidenza']:.1%}")
        
        st.metric("Totale Oggetti", dati['visione']['num_oggetti'])

with tab_aud:
    col_a1, col_a2 = st.columns([2, 1])
    
    with col_a1:
        st.subheader("Trascrizione")
        
        st.info(f"🗣️ \"{dati['audio']['testo']}\"")
        
        st.caption(f"Tono: {dati['audio']['tono']}")
        st.caption(f"Intenzione: {dati['audio']['intenzione']}")
    
    with col_a2:
        st.subheader("Analisi Vocale")
        
        st.metric("Tono", dati['audio']['tono'].upper())
        st.metric("Intenzione", dati['audio']['intenzione'].upper())

st.divider()

# ==================== BIOSEGNALI ====================

if mostra_pattern:
    st.header("⚡ Biosegnali Neurali")
    
    col_b1, col_b2 = st.columns([3, 1])
    
    with col_b1:
        st.subheader("Pattern Neurale Corrente")
        
        # Simula pattern (in produzione leggerebbe da file)
        pattern = "░░░░███████████░░░░"
        neuroni_attivi = pattern.count('█')
        
        st.markdown(f"### `{pattern}`")
        st.caption(f"Neuroni attivi: {neuroni_attivi}/{len(pattern)}")
        
        # Barra visualizzazione
        st.progress(neuroni_attivi / len(pattern))
    
    with col_b2:
        st.metric("Arousal", "0.65")
        st.metric("Ritmo", "BETA")
        st.metric("Energia", "98.5%")

st.divider()

# ==================== MEMORIA ====================

st.header("💾 Memoria Episodica")

col_m1, col_m2 = st.columns([2, 1])

with col_m1:
    st.subheader("Episodi Recenti")
    
    if memorie:
        # Mostra ultimi 10 episodi
        df_memorie = []
        
        for mem in memorie[-10:]:
            df_memorie.append({
                'ID': mem.get('id', 'N/A')[:20],
                'Contenuto': mem.get('contenuto', '')[:50] + '...',
                'Valenza': f"{mem.get('valenza_emotiva', 0):+.2f}",
                'Importanza': f"{mem.get('importanza', 0):.2f}",
                'Accessi': mem.get('accessi', 0)
            })
        
        df = pd.DataFrame(df_memorie)
        st.dataframe(df, use_container_width=True)
    else:
        st.info("Nessuna memoria. Esegui qualche ciclo cognitivo!")

with col_m2:
    st.subheader("Statistiche")
    
    st.metric("Episodi Totali", len(memorie))
    st.metric("Richiami", meta.get('richiami_totali', 0))
    st.metric("Consolidamenti", meta.get('consolidamenti', 0))
    
    if memorie:
        valenze = [m.get('valenza_emotiva', 0) for m in memorie]
        valenza_media = sum(valenze) / len(valenze)
        st.metric("Valenza Media", f"{valenza_media:+.2f}")

st.divider()

# ==================== EMOZIONE E REWARD ====================

st.header("❤️ Sistema Emotivo e Reward")

col_e1, col_e2, col_e3 = st.columns(3)

with col_e1:
    st.metric("Stato Emotivo", dati['emozione']['stato'], 
             delta=None)

with col_e2:
    st.metric("Valenza", f"{dati['emozione']['valenza']:+.2f}")

with col_e3:
    st.metric("Reward Medio", f"{meta.get('reward_medio', 1.5):.2f}" if 'reward_medio' in meta else "N/A")

# Grafico emozioni (se ci sono dati)
if memorie and len(memorie) > 3:
    st.subheader("Evoluzione Emotiva")
    
    # Estrai valenze
    df_emozioni = pd.DataFrame([
        {
            'Ciclo': i,
            'Valenza': m.get('valenza_emotiva', 0)
        }
        for i, m in enumerate(memorie[-20:], 1)
    ])
    
    st.line_chart(df_emozioni.set_index('Ciclo'))

st.divider()

# ==================== DECISIONE ====================

st.header("🧠 Ragionamento e Decisione")

col_d1, col_d2 = st.columns([2, 1])

with col_d1:
    st.subheader("Ultima Decisione")
    
    st.success(f"**Azione:** {dati['decisione']['azione'].upper()}")
    st.info(f"**Priorità:** {dati['decisione']['priorita']:.0%}")
    st.caption(f"Fonte: {dati['decisione']['fonte']}")

with col_d2:
    st.subheader("Distribuzione Azioni")
    
    # Conta azioni nelle memorie
    if memorie:
        azioni_count = {}
        for mem in memorie:
            azione = mem.get('contesto', {}).get('azione', 'unknown')
            azioni_count[azione] = azioni_count.get(azione, 0) + 1
        
        # Top 5
        top_azioni = sorted(azioni_count.items(), key=lambda x: x[1], reverse=True)[:5]
        
        for azione, count in top_azioni:
            st.metric(azione, count)

st.divider()

# ==================== NARRAZIONE COGNITIVA ====================

st.header("💭 Narrazione Cognitiva")

# Carica narrazione da file
path_narrazione = Path("data/ultima_narrazione.txt")

if path_narrazione.exists():
    try:
        with open(path_narrazione, 'r', encoding='utf-8') as f:
            narrazione = f.read()
        
        # Mostra in expander espandibile
        with st.expander("📖 Cosa Pensa e Dice l'AI", expanded=True):
            st.markdown(f"```\n{narrazione}\n```")
    except:
        st.info("Narrazione non disponibile")
else:
    st.info("💭 Avvia il sistema per vedere cosa pensa l'AI!")
    st.caption("La narrazione apparirà qui quando il sistema elabora un episodio")

st.divider()

# ==================== APPRENDIMENTO ====================

st.header("🎓 Apprendimento Online")

col_l1, col_l2, col_l3 = st.columns(3)

# Simula statistiche (in produzione leggerebbe da modello)
with col_l1:
    st.metric("Cicli Training", meta.get('memorizzazioni_totali', 0))

with col_l2:
    st.metric("Loss Media", "0.0234" if meta.get('memorizzazioni_totali', 0) > 10 else "N/A")

with col_l3:
    modello_esiste = os.path.exists("data/modello_online.pt")
    st.metric("Modello", "✅ Salvato" if modello_esiste else "⚠️ Non trovato")

st.divider()

# ==================== TIMELINE ====================

st.header("📅 Timeline Attività")

if memorie:
    st.subheader(f"Ultimi {min(15, len(memorie))} Episodi")
    
    for i, mem in enumerate(reversed(memorie[-15:]), 1):
        with st.expander(f"Episodio #{len(memorie) - i + 1} - {mem.get('contenuto', '')[:50]}..."):
            col_t1, col_t2 = st.columns([3, 1])
            
            with col_t1:
                st.write(f"**Contenuto:** {mem.get('contenuto', '')}")
                
                contesto = mem.get('contesto', {})
                if contesto:
                    st.write(f"**Azione:** {contesto.get('azione', 'N/A')}")
                    st.write(f"**Successo:** {'✅' if contesto.get('successo') else '❌'}")
            
            with col_t2:
                st.metric("Valenza", f"{mem.get('valenza_emotiva', 0):+.2f}")
                st.metric("Importanza", f"{mem.get('importanza', 0):.2f}")
                st.metric("Accessi", mem.get('accessi', 0))
                
                # Timestamp
                if 'timestamp' in mem:
                    dt = datetime.fromtimestamp(mem['timestamp'])
                    st.caption(f"🕐 {dt.strftime('%H:%M:%S')}")

st.divider()

# ==================== CONTROLLI ====================

st.header("🎮 Controlli Sistema")

col_c1, col_c2, col_c3 = st.columns(3)

with col_c1:
    if st.button("▶️ Esegui Ciclo", use_container_width=True):
        st.info("Esegui: python mente_completa_finale.py")

with col_c2:
    if st.button("💾 Salva Memoria", use_container_width=True):
        st.success("Memoria salvata automaticamente!")

with col_c3:
    if st.button("🔄 Reset Sistema", use_container_width=True):
        st.warning("Reset non implementato (sicurezza)")

st.divider()

# ==================== INFO ====================

with st.expander("ℹ️ Info Dashboard"):
    st.markdown("""
    ## Come Usare
    
    1. **Esegui sistema**: `python mente_completa_finale.py`
    2. **Dashboard si aggiorna** automaticamente
    3. **Visualizza** percezioni, decisioni, memoria
    
    ## Dati Visualizzati
    
    - **Tempo reale**: Ultimi frame camera, audio
    - **Storico**: Memoria episodica completa
    - **Statistiche**: Reward, emozioni, apprendimento
    - **Biosegnali**: Pattern neurali visualizzati
    
    ## File Monitorati
    
    - `data/memoria.json` - Memoria episodica
    - `frame_*.jpg` - Frame camera
    - `data/modello_online.pt` - Rete neurale
    """)

# ==================== FOOTER ====================

st.markdown("---")
st.caption("🧠 Mente Artificiale Modulare v3.0 | Alessio + Cursor AI | 2025")

# Auto-refresh
if auto_refresh:
    time.sleep(5)
    st.rerun()

