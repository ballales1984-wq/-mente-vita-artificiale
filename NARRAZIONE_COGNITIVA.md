# 💭 Narrazione Cognitiva - L'AI Parla e Pensa

## 🎯 Funzionalità

Sistema di **narrazione cognitiva** che mostra in tempo reale cosa l'AI:
- 👁️ **Vede** (percezione visiva)
- 👂 **Sente** (percezione uditiva)  
- ❤️ **Prova emotivamente** (stato emotivo)
- 🧠 **Pensa** (processo di ragionamento)
- 💡 **Decide** (scelta dell'azione)
- 🎯 **Motiva** (perché agisce così)
- ✨ **Valuta** (esito dell'azione)
- 📚 **Impara** (consolidamento esperienza)

---

## 📊 Esempio Output

```
======================================================================
  💭 NARRAZIONE COGNITIVA
======================================================================

[VISTA] [++]
   "Vedo: Scena indoor: persona seduta vicino a una sedia"
   "Ho rilevato 2 oggetti nella scena."

[UDITO]
   "Ho sentito: 'Ciao, come stai? Vieni qui per favore.'"
   "Il tono mi sembra amichevole."

[EMOZIONI] [++]
   "Mi sento positivo e fiducioso (valenza: +0.70)."
   "La mia attività neurale è 11 neuroni attivi su 15."

[PENSIERI]
   "Ho rilevato un saluto. È appropriato rispondere in modo cordiale."
   "Mi viene richiesto di avvicinarmi. Valuto se è sicuro."
   "La situazione sembra sicura, posso procedere con l'azione."

[DECISIONE]
   "Ho deciso di: ESEGUI COMANDO"

[MOTIVAZIONE]
   "Ho ricevuto un comando che posso eseguire."

[ESITO]
   "Ho eseguito l'azione con successo. Tutto è andato come previsto."

[APPRENDIMENTO]
   "Questa esperienza positiva rafforza il mio comportamento."

======================================================================
```

---

## 🎨 Componenti della Narrazione

### 1. [VISTA] 
**Cosa mostra:**
- Descrizione della scena
- Numero di oggetti rilevati
- Stato emotivo visivo

**Esempio:**
```
[VISTA] [++]
   "Vedo: Scena indoor: persona seduta vicino a una sedia"
   "Ho rilevato 2 oggetti nella scena."
```

---

### 2. [UDITO]
**Cosa mostra:**
- Trascrizione audio
- Valutazione del tono

**Esempi:**
```
[UDITO]
   "Ho sentito: 'Ciao, come stai?'"
   "Il tono mi sembra amichevole."

[UDITO]
   "Non ho percepito parole chiare, solo silenzio o rumore di fondo."
```

---

### 3. [EMOZIONI]
**Cosa mostra:**
- Stato emotivo corrente
- Valenza numerica
- Attività neurale

**Stati emotivi:**
- `[++]` = positivo e fiducioso (>0.5)
- `[+]`  = leggermente positivo (>0)
- `[=]`  = neutro e calmo (=0)
- `[-]`  = neutro con cautela (<0)
- `[--]` = preoccupato (<-0.5)

**Esempio:**
```
[EMOZIONI] [++]
   "Mi sento positivo e fiducioso (valenza: +0.70)."
   "La mia attività neurale è 11 neuroni attivi su 15."
```

---

### 4. [PENSIERI]
**Cosa mostra:**
- Ragionamento interno
- Valutazione della situazione
- Considerazioni sulla sicurezza

**Riconoscimenti automatici:**
- **Saluti**: "ciao", "salve", "buongiorno"
- **Comandi avvicinamento**: "vieni", "avvicinati", "qui"
- **Comandi stop**: "fermati", "stop", "aspetta"
- **Valutazione sicurezza**: Analisi oggetti + emozione

**Esempi:**
```
[PENSIERI]
   "Ho rilevato un saluto. È appropriato rispondere in modo cordiale."
   "Mi viene richiesto di avvicinarmi. Valuto se è sicuro."
   "La situazione sembra sicura, posso procedere con l'azione."
```

---

### 5. [DECISIONE]
**Cosa mostra:**
- Azione scelta
- Formato leggibile

**Esempio:**
```
[DECISIONE]
   "Ho deciso di: ESEGUI COMANDO"
```

---

### 6. [MOTIVAZIONE]
**Cosa mostra:**
- Perché ha preso quella decisione
- Ragionamento alla base

**Motivazioni per azione:**
- **avvicinati**: "Percepisco una richiesta diretta e la situazione è sicura."
- **allontanati**: "La situazione mi sembra incerta, meglio prendere distanza."
- **fermati**: "Ho ricevuto un comando esplicito di stop."
- **mantieni_distanza**: "Mantengo una posizione di osservazione prudente."
- **monitora**: "Continuo a osservare e analizzare senza intervenire."
- **segui**: "Ho identificato un obiettivo da seguire."
- **esegui_comando**: "Ho ricevuto un comando che posso eseguire."
- **ruota**: "Devo cambiare orientamento per una visuale migliore."

**Esempio:**
```
[MOTIVAZIONE]
   "Ho ricevuto un comando che posso eseguire."
```

---

### 7. [ESITO]
**Cosa mostra:**
- Risultato dell'azione
- Valutazione del successo

**Esempi:**
```
[ESITO]
   "Ho eseguito l'azione con successo. Tutto è andato come previsto."

[ESITO]
   "L'azione non è riuscita completamente, dovrò adattarmi."
```

---

### 8. [APPRENDIMENTO]
**Cosa mostra:**
- Cosa impara dall'esperienza
- Come consolida la memoria

**Casistiche:**
- **Esperienza positiva + successo**: Rafforza comportamento
- **Esperienza negativa**: Memorizza per evitare
- **Esperienza neutra**: Aggiunge per riferimento futuro

**Esempi:**
```
[APPRENDIMENTO]
   "Questa esperienza positiva rafforza il mio comportamento."

[APPRENDIMENTO]
   "Memorizzo questa situazione per evitarla in futuro."

[APPRENDIMENTO]
   "Aggiungo questa esperienza alla mia memoria per riferimenti futuri."
```

---

## 🎮 Come Usare

### Avvio Normale
```bash
python mente_buffer_temp.py
```

La narrazione cognitiva appare **automaticamente** dopo ogni ciclo!

---

## 🧠 Intelligenza della Narrazione

### Riconoscimento Contesto

La narrazione **adatta** i pensieri in base a:

1. **Parole chiave** nell'audio:
   - Saluti → Risposta cordiale
   - Comandi → Valutazione sicurezza
   - Stop → Interruzione immediata

2. **Oggetti rilevati** nella visione:
   - Molti oggetti + positivo → Sicuro
   - Molti oggetti + negativo → Incerto
   - Pochi oggetti → Standard

3. **Stato emotivo** corrente:
   - Positivo → Fiducioso
   - Negativo → Cauto
   - Neutro → Calmo

4. **Successo dell'azione**:
   - Successo → Rafforza
   - Fallimento → Adatta

---

## 📝 Output Completo Esempio

```
======================================================================
  CICLO #1/5
======================================================================

[1/6] 👁️  VISIONE
       Scena indoor: persona seduta vicino a una sedia

[2/6] 👂 UDITO
[Buffer] 🎤 Registrazione 4.0s...
       'Ciao, come stai? Vieni qui per favore.'

[3/6] ⚡ BIOSEGNALI
       ░░███████████░░

[4/6] ❤️  EMOZIONE
       +0.70

[5/6] 🧠 DECISIONE
       ESEGUI_COMANDO

[6/6] 🦾 AZIONE
       ESEGUI_COMANDO ✅

======================================================================
  💭 NARRAZIONE COGNITIVA
======================================================================

[VISTA] [++]
   "Vedo: Scena indoor: persona seduta vicino a una sedia"
   "Ho rilevato 2 oggetti nella scena."

[UDITO]
   "Ho sentito: 'Ciao, come stai? Vieni qui per favore.'"
   "Il tono mi sembra amichevole."

[EMOZIONI] [++]
   "Mi sento positivo e fiducioso (valenza: +0.70)."
   "La mia attività neurale è 11 neuroni attivi su 15."

[PENSIERI]
   "Ho rilevato un saluto. È appropriato rispondere in modo cordiale."
   "Mi viene richiesto di avvicinarmi. Valuto se è sicuro."
   "La situazione sembra sicura, posso procedere con l'azione."

[DECISIONE]
   "Ho deciso di: ESEGUI COMANDO"

[MOTIVAZIONE]
   "Ho ricevuto un comando che posso eseguire."

[ESITO]
   "Ho eseguito l'azione con successo. Tutto è andato come previsto."

[APPRENDIMENTO]
   "Questa esperienza positiva rafforza il mio comportamento."

======================================================================

[7/6] 💾 SALVATAGGIO MEMORIA
       💾 Memoria salvata permanentemente

[CLEANUP]
       🗑️  File eliminati

[TEMPO] 11.2s
```

---

## 🎯 Vantaggi

✅ **Comprensibilità**: Capire cosa pensa l'AI in linguaggio naturale  
✅ **Trasparenza**: Vedere tutto il processo decisionale  
✅ **Debug**: Identificare errori di ragionamento  
✅ **Educativo**: Imparare come funziona l'AI  
✅ **Engagement**: Più coinvolgente da osservare  
✅ **Trust**: Aumenta la fiducia nell'AI  

---

## 🔧 Implementazione Tecnica

### Metodo Principale

```python
def _narrazione_cognitiva(self, vis, testo, valenza, pattern, azione, successo):
    """Genera narrazione di cosa pensa l'AI"""
    # Analizza contesto
    # Determina stato emotivo
    # Genera pensieri basati su parole chiave
    # Spiega decisione e motivazione
    # Valuta esito e apprendimento
```

### Integrazione nel Ciclo

```python
def ciclo(self):
    # ... elaborazione normale ...
    
    # NARRAZIONE: Cosa pensa e dice l'AI
    print("\n" + "="*70)
    print("  💭 NARRAZIONE COGNITIVA")
    print("="*70)
    self._narrazione_cognitiva(vis, testo, valenza, pattern, azione, successo)
```

---

## 📊 Statistiche Narrazione

**Lunghezza tipica:** 15-25 righe di testo  
**Tempo aggiunto:** ~0.1s per ciclo  
**Leggibilità:** 100% linguaggio naturale  
**Adattività:** 8 diversi contesti riconosciuti  

---

## 🎊 Conclusioni

La **Narrazione Cognitiva** trasforma il sistema AI da "scatola nera" a **compagno trasparente**!

**Ora puoi:**
- ✅ Vedere cosa pensa
- ✅ Capire perché decide
- ✅ Seguire il ragionamento
- ✅ Imparare dal processo
- ✅ Fidarti delle decisioni

---

**🧠 L'AI non è più un mistero - è un libro aperto! 📖**

---

