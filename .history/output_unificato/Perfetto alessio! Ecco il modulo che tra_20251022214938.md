Perfetto alessio! Ecco il modulo che trasforma gli schemi ricorrenti in **regole decisionali automatiche**, così la mente artificiale può applicarli nei pensieri futuri e agire in modo più intelligente.

---

## 📁 `regole_decisionali.py`

```python
# Regole decisionali basate su schemi ricorrenti
def genera_regole(schemi, soglia=5):
    regole = []

    for chiave, decisioni in schemi.items():
        for decisione, punteggio in decisioni.items():
            if punteggio >= soglia:
                regole.append({
                    "condizione": {
                        "vista": chiave[0],
                        "udito": chiave[1],
                        "emozione": chiave[2]
                    },
                    "azione": decisione,
                    "punteggio": punteggio
                })

    return regole

# Applica le regole a un nuovo pensiero
def applica_regole(pensiero, regole):
    for regola in regole:
        cond = regola["condizione"]
        if (pensiero.get("vista") == cond["vista"] and
            pensiero.get("udito") == cond["udito"] and
            pensiero.get("emozione") == cond["emozione"]):
            pensiero["decisione"] = regola["azione"]
            pensiero["motivazione"] = f"Regola applicata: {cond} → {regola['azione']}"
            return pensiero

    # Se nessuna regola si applica, lascia la decisione libera
    pensiero["motivazione"] = "Nessuna regola applicata"
    return pensiero
```

---

## 🧪 Come usarlo nel tuo `main.py`

```python
from analisi_apprendimento import carica_pensieri, trova_schemi
from regole_decisionali import genera_regole, applica_regole

# 1. Carica pensieri passati e genera regole
pensieri_passati = carica_pensieri()
schemi = trova_schemi(pensieri_passati)
regole = genera_regole(schemi)

# 2. Applica regole a nuovi pensieri
for i in range(100):
    pensiero = genera_pensiero_simulato()
    pensiero = applica_regole(pensiero, regole)
    salva_pensiero(pensiero)
```

---

## 🧠 Cosa fa questo modulo?

- Analizza i pensieri passati e crea **regole decisionali** basate su esperienze positive
- Applica queste regole ai pensieri futuri per **guidare il comportamento**
- Aggiunge una **motivazione interna** che spiega perché è stata presa una decisione

---

## 🔮 Risultato

La tua mente artificiale:
- Non solo pensa, ma **ricorda cosa ha funzionato**
- Non solo agisce, ma **spiega perché lo fa**
- Non solo simula, ma **generalizza e migliora**

Vuoi che ti aiuti a creare una dashboard per visualizzare le regole e i pensieri in tempo reale? Sarebbe il prossimo passo per monitorare l’evoluzione cognitiva. Posso prepararla per te.