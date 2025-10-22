Perfetto alessio! Ecco il modulo base `apprendimento.py` che puoi integrare nel tuo progetto per iniziare la **Fase 3: Apprendimento Adattivo**. Questo modulo assegna un punteggio ai pensieri, aggiorna la memoria e modifica il comportamento futuro in base all’esperienza.

---

## 📁 `apprendimento.py`

```python
import json
import random

# Valuta il pensiero in base all'esito
def valuta_pensiero(pensiero):
    esito = pensiero.get("esito", "")
    if "riuscita" in esito.lower():
        return +1
    elif "fallita" in esito.lower():
        return -1
    else:
        return 0

# Aggiorna il pensiero con la valutazione
def aggiorna_pensiero(pensiero):
    punteggio = valuta_pensiero(pensiero)
    pensiero["valutazione"] = punteggio
    return pensiero

# Modifica la probabilità di scelta futura
def aggiorna_comportamento(pensiero, probabilita):
    decisione = pensiero.get("decisione", "")
    punteggio = pensiero.get("valutazione", 0)

    if decisione not in probabilita:
        probabilita[decisione] = 1.0

    # Rafforza o indebolisce la decisione
    probabilita[decisione] += punteggio * 0.1
    probabilita[decisione] = max(0.1, min(probabilita[decisione], 5.0))  # limiti

    return probabilita

# Salva il pensiero aggiornato
def salva_pensiero(pensiero, path="memoria/pensieri_valutati.jsonl"):
    with open(path, "a") as file:
        file.write(json.dumps(pensiero) + "\n")
```

---

## 🧪 Esempio di utilizzo nel tuo `main.py`

```python
from apprendimento import aggiorna_pensiero, aggiorna_comportamento, salva_pensiero

probabilita = {}  # dizionario per apprendimento decisionale

for i in range(1000):
    pensiero = genera_pensiero_simulato()  # funzione tua
    pensiero = aggiorna_pensiero(pensiero)
    probabilita = aggiorna_comportamento(pensiero, probabilita)
    salva_pensiero(pensiero)
```

---

## 🧠 Cosa fa questo modulo?

- Valuta ogni pensiero in base all’esito
- Assegna un punteggio (+1, 0, -1)
- Modifica la probabilità di scegliere certe azioni
- Salva tutto per analisi futura

---

Vuoi che ti aiuti a creare anche un sistema che analizza i pensieri salvati e trova schemi ricorrenti? Sarebbe il prossimo passo per far evolvere la mente. Posso prepararlo per te.