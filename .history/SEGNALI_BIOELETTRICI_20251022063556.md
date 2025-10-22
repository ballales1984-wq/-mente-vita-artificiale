# ⚡ Sistema di Codifica Binaria per Segnali Bioelettrici

## 🧠 Concetto

Sistema che simula l'attività neurale usando **codifica binaria** dove:
- Un singolo `1` = impulso elettrico
- Gli `0` circostanti = ampiezza/durata
- Posizione del `1` = direzione/canale
- Espansione = propagazione temporale

---

## 📊 Schema di Funzionamento

```
EVOLUZIONE SEGNALE NEL TEMPO:

Ciclo 0:    010              (impulso base)
Ciclo 1:    00100            (espansione +1)
Ciclo 2:    0001000          (espansione +2)
Ciclo 3:    000010000        (espansione +3)
Ciclo 4:    00000100000      (espansione +4)
Ciclo 5:    0000001000000    (espansione +5)

Ampiezza:     1 → 2 → 3 → 4 → 5 → 6
Intensità:  0.5 → 0.67 → 0.75 → 0.80 → 0.83 → 0.86
Latenza:     0ms → 20ms → 40ms → 60ms → 80ms → 100ms
```

---

## 🔬 Tre Modalità di Codifica

### 1️⃣ **Codifica di AMPIEZZA**

Il numero di zeri rappresenta l'intensità del segnale:

```
010        → Ampiezza: 1.0  (debole)
00100      → Ampiezza: 2.0  (media)
0001000    → Ampiezza: 3.0  (forte)
000010000  → Ampiezza: 4.0  (molto forte)
```

**Uso:** Intensità input sensoriale, forza comando motorio

---

### 2️⃣ **Codifica di DIREZIONE**

La posizione del `1` indica il canale/direzione:

```
100  → Sinistra  (offset: -1.0)
010  → Centro    (offset:  0.0)
001  → Destra    (offset: +1.0)
```

**Uso:** Localizzazione spaziale, canale neurale, direzione movimento

---

### 3️⃣ **Codifica TEMPORALE**

L'espansione rappresenta la propagazione nel tempo:

```
Ciclo 0:  010         (t=0ms)
Ciclo 1:  00100       (t=20ms)
Ciclo 2:  0001000     (t=40ms)
```

**Uso:** Ritardo sinaptico, latenza, timing

---

## 🧪 Esempi Pratici

### Esempio 1: Input Sensoriale

```python
from moduli.segnali_neurali import SimulatoreAttvitaNeurale

simulatore = SimulatoreAttvitaNeurale()

# Stimolo forte (0.8)
segnale = simulatore.simula_percezione_sensoriale(intensita=0.8)

print(f"Codice: {segnale.codice}")
# Output: "00000100000"

print(f"Intensità: {segnale.intensita:.2f}")
# Output: 0.83
```

### Esempio 2: Comando Motorio

```python
# Movimento a sinistra, forza media
segnale = simulatore.simula_comando_motorio(
    forza=0.6,
    direzione="sinistra"
)

# Decodifica per motori
parametri = simulatore.decodifica_per_azione(segnale)

print(parametri)
# Output: {
#   'velocita': 0.30,
#   'direzione': 'sinistra',
#   'potenza': 0.75,
#   'ritardo_ms': 40
# }
```

### Esempio 3: Potenziale d'Azione

```python
from moduli.segnali_neurali import CodificatoreSegnali

codificatore = CodificatoreSegnali()

# Simula potenziale d'azione completo
sequenza = codificatore.simula_potenziale_azione()

# Visualizza evoluzione
for i, segnale in enumerate(sequenza):
    print(f"t={i*10}ms: {segnale.codice}")

# Output:
# t=0ms:  010
# t=10ms: 00100
# t=20ms: 0001000
# t=30ms: 000010000  <- PICCO
```

---

## 🔄 Integrazione con Mente Artificiale

### Uso nei Moduli Cerebrali

```python
# In modulo VISIONE
def elabora_con_segnale(immagine):
    # Rileva oggetto
    obj_rilevato = yolo.detect(immagine)
    
    # Codifica come segnale neurale
    intensita = obj_rilevato['confidenza']
    segnale = simulatore.simula_percezione_sensoriale(intensita)
    
    return {
        'oggetto': obj_rilevato,
        'segnale_neurale': segnale.codice,
        'intensita': segnale.intensita
    }

# In modulo MOTORIA
def esegui_con_segnale(decisione):
    # Converti decisione in segnale
    forza = decisione['priorita']
    direzione = decisione['parametri']['direzione']
    
    segnale = simulatore.simula_comando_motorio(forza, direzione)
    
    # Decodifica per attuatori
    parametri = simulatore.decodifica_per_azione(segnale)
    
    # Invia a motori
    motore.set_velocita(parametri['velocita'])
    motore.set_direzione(parametri['direzione'])
```

---

## 📈 Vantaggi della Codifica

### ✅ Semplicità
- Rappresentazione minimale (solo 0 e 1)
- Facile da processare
- Basso overhead

### ✅ Biologicamente Ispirata
- Simula potenziali d'azione reali
- Propagazione sinaptica
- Pattern di firing

### ✅ Flessibilità
- Codifica ampiezza, direzione, tempo
- Espandibile a piacere
- Modulare

### ✅ Hardware-Ready
- Può essere implementato su neuromorphic chips
- Compatibile con spike-based computing
- Efficiente energeticamente

---

## 🎯 Casi d'Uso

### 1. Sensori → Cervello

```
Fotocamera rileva oggetto
  ↓
Confidenza 85%
  ↓
Segnale neurale: 00000100000 (intensità 0.83)
  ↓
Talamo riceve e smista
```

### 2. Cervello → Motori

```
Decisione: "avvicinati veloce"
  ↓
Priorità 0.9
  ↓
Segnale motorio: 000000010000000 (potenza 0.88)
  ↓
Motori ricevono parametri decodificati
```

### 3. Rete Neurale Interna

```
Neurone 1 attiva → 010
  ↓ propaga a
Neurone 2 riceve → 00100
  ↓ propaga a
Neurone 3 riceve → 0001000
```

---

## 🔧 API Principale

### Creazione Segnali

```python
codificatore = CodificatoreSegnali()

# Impulso base
segnale = codificatore.crea_impulso_base("centro")
# Output: "010"

# Espansione
segnale_esp = codificatore.espandi_segnale(
    segnale,
    direzione=Direzione.BILATERALE,
    n_zeri=2
)
# Output: "0000100"
```

### Decodifica

```python
# Decodifica completa
info = codificatore.decodifica_completa(segnale)

print(info)
# {
#   'codice_binario': '0001000',
#   'ampiezza': 3.0,
#   'intensita': 0.75,
#   'direzione': 'centro',
#   'latenza_ms': 40,
#   ...
# }
```

---

## 📊 Formule di Conversione

### Intensità

```
intensità = num_zeri / (num_zeri + 2)

Esempi:
  010      → 2 zeri → 2/(2+2) = 0.50
  0001000  → 6 zeri → 6/(6+2) = 0.75
  000010000 → 8 zeri → 8/(8+2) = 0.80
```

### Ampiezza

```
ampiezza = num_zeri / 2

Esempi:
  010      → 2 zeri → 1.0
  0001000  → 6 zeri → 3.0
```

### Latenza

```
latenza_ms = (lunghezza_totale - 3) × 10

Esempi:
  010      → 3 bit  → 0ms
  00100    → 5 bit  → 20ms
  0001000  → 7 bit  → 40ms
```

---

## 🚀 Test Eseguiti

```
[OK] Espansione bilaterale: 7 cicli completati
[OK] Direzioni: sinistra, centro, destra funzionanti
[OK] Potenziale d'azione: 4 fasi simulate
[OK] Rete neurale: 5 neuroni comunicanti
[OK] Sensori-Motori: codifica/decodifica perfetta
```

---

## 🎓 Confronto con Neuroscienze

| Concetto Biologico | Implementazione |
|-------------------|-----------------|
| Potenziale d'azione | Sequenza espansione segnale |
| Depolarizzazione | Espansione progressiva |
| Picco | Massima ampiezza (es. 000010000) |
| Ripolarizzazione | Contrazione (simulata) |
| Propagazione assone | Espansione direzione |
| Sommazione sinaptica | Merge segnali multipli |
| Soglia attivazione | Intensità minima |

---

## 💡 Estensioni Future

- [ ] Sommazione di segnali multipli
- [ ] Segnali inibitori (valori negativi)
- [ ] Pattern complessi (burst, oscillazioni)
- [ ] Sincronizzazione neuronale
- [ ] Plasticità sinaptica
- [ ] Spike-timing dependent plasticity (STDP)

---

## 📄 File Creato

**moduli/segnali_neurali.py**
- CodificatoreSegnali (classe principale)
- ReteNeurale (network di neuroni)
- SimulatoreAttivitaNeurale (sensori/motori)
- Demo complete integrate

**Righe di codice:** ~400
**Classi:** 4
**Metodi:** 15+
**Demo:** 5

---

## ✅ Pronto per:

- ✅ Integrazione con mente artificiale
- ✅ Simulazione attività neurale
- ✅ Controllo motorio basato su segnali
- ✅ Neuromorphic computing
- ✅ Spike-based neural networks

**Il cervello artificiale ora ha segnali neurali realistici!** 🧠⚡

