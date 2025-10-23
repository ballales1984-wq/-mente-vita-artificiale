#!/usr/bin/env python3
"""
🧠 DEMO CON NARRAZIONE COGNITIVA
Genera dati simulati + narrazione comprensibile
"""

import random
import time
import json
import os
from datetime import datetime

def genera_narrazione(oggetti, audio, valenza, azione):
    """Genera narrazione cognitiva completa"""
    
    narrazione = []
    narrazione.append("\n" + "="*70)
    narrazione.append("  💭 NARRAZIONE COGNITIVA")
    narrazione.append("="*70)
    
    # Vista
    emo_symbol = "[++]" if valenza > 0.5 else ("[+]" if valenza > 0 else "[-]")
    narrazione.append(f"\n[VISTA] {emo_symbol}")
    
    if len(oggetti) > 0:
        obj_str = ", ".join([f"{o['classe']}" for o in oggetti[:3]])
        narrazione.append(f'   "Vedo: {obj_str} nella scena"')
        narrazione.append(f'   "Ho rilevato {len(oggetti)} oggetti."')
    else:
        narrazione.append(f'   "Vedo: ambiente interno, nessun oggetto particolare"')
    
    # Udito
    narrazione.append(f"\n[UDITO]")
    if audio:
        narrazione.append(f'   "Ho sentito: \'{audio}\'"')
        if valenza > 0:
            narrazione.append(f'   "Il tono mi sembra amichevole."')
    else:
        narrazione.append(f'   "Non ho percepito parole chiare, solo silenzio."')
    
    # Emozioni
    if valenza > 0.5:
        stato = "positivo e fiducioso"
    elif valenza > 0:
        stato = "leggermente positivo"
    elif valenza < -0.5:
        stato = "preoccupato"
    else:
        stato = "neutro e calmo"
    
    neuroni = random.randint(8, 14)
    narrazione.append(f"\n[EMOZIONI] {emo_symbol}")
    narrazione.append(f'   "Mi sento {stato} (valenza: {valenza:+.2f})."')
    narrazione.append(f'   "La mia attività neurale è {neuroni} neuroni attivi su 15."')
    
    # Pensieri
    narrazione.append(f"\n[PENSIERI]")
    
    if audio:
        if any(w in audio.lower() for w in ['ciao', 'salve', 'buongiorno']):
            narrazione.append(f'   "Ho rilevato un saluto. È appropriato rispondere cordialmente."')
        
        if any(w in audio.lower() for w in ['vieni', 'avvicinati', 'qui']):
            narrazione.append(f'   "Mi viene richiesto di avvicinarmi. Valuto se è sicuro."')
        
        if any(w in audio.lower() for w in ['fermati', 'stop', 'aspetta']):
            narrazione.append(f'   "Comando di stop ricevuto. Devo interrompere ogni movimento."')
    
    if len(oggetti) > 0 and valenza > 0:
        narrazione.append(f'   "La situazione sembra sicura, posso procedere con l\'azione."')
    elif len(oggetti) > 0:
        narrazione.append(f'   "Rilevo oggetti ma sono incerto, meglio mantenere prudenza."')
    else:
        narrazione.append(f'   "Nessun elemento particolare, procedo in modalità standard."')
    
    # Decisione
    narrazione.append(f"\n[DECISIONE]")
    narrazione.append(f'   "Ho deciso di: {azione.upper().replace("_", " ")}"')
    
    # Motivazione
    motivazioni = {
        'avvicinati': "Percepisco una richiesta diretta e la situazione è sicura.",
        'allontanati': "La situazione mi sembra incerta, meglio prendere distanza.",
        'fermati': "Ho ricevuto un comando esplicito di stop.",
        'mantieni_distanza': "Mantengo una posizione di osservazione prudente.",
        'monitora': "Continuo a osservare e analizzare senza intervenire.",
        'esegui_comando': "Ho ricevuto un comando che posso eseguire.",
    }
    
    narrazione.append(f"\n[MOTIVAZIONE]")
    motivazione = motivazioni.get(azione, "Questa è l'azione più appropriata.")
    narrazione.append(f'   "{motivazione}"')
    
    # Esito
    narrazione.append(f"\n[ESITO]")
    narrazione.append(f'   "Ho eseguito l\'azione con successo. Tutto è andato come previsto."')
    
    # Apprendimento
    narrazione.append(f"\n[APPRENDIMENTO]")
    if valenza > 0:
        narrazione.append(f'   "Questa esperienza positiva rafforza il mio comportamento."')
    elif valenza < 0:
        narrazione.append(f'   "Memorizzo questa situazione per evitarla in futuro."')
    else:
        narrazione.append(f'   "Aggiungo questa esperienza alla memoria per riferimenti futuri."')
    
    narrazione.append("\n" + "="*70)
    
    return "\n".join(narrazione)

def genera_episodio():
    """Genera episodio con narrazione"""
    oggetti_possibili = [
        {'classe': 'person', 'confidenza': 0.92},
        {'classe': 'chair', 'confidenza': 0.85},
        {'classe': 'bottle', 'confidenza': 0.78},
        {'classe': 'laptop', 'confidenza': 0.88},
        {'classe': 'book', 'confidenza': 0.72},
        {'classe': 'cup', 'confidenza': 0.81}
    ]
    
    frasi_possibili = [
        "Ciao, come stai? Vieni qui per favore.",
        "Guarda quella bottiglia sul tavolo.",
        "Fermati e aspetta il mio comando.",
        "Perfetto, continua così!",
        "Avvicinati lentamente.",
        ""  # Silenzio
    ]
    
    azioni_possibili = [
        'avvicinati', 'mantieni_distanza', 'monitora', 
        'esegui_comando', 'fermati'
    ]
    
    # Genera dati casuali
    num_oggetti = random.randint(0, 3)
    oggetti = random.sample(oggetti_possibili, num_oggetti) if num_oggetti > 0 else []
    
    frase = random.choice(frasi_possibili)
    valenza = random.uniform(-0.2, 0.9)
    azione = random.choice(azioni_possibili)
    
    pattern = ''.join(random.choice('01') for _ in range(15))
    pattern_visual = pattern.replace('1', '█').replace('0', '░')
    
    # Genera narrazione
    narrazione_text = genera_narrazione(oggetti, frase, valenza, azione)
    
    # Salva per dashboard
    episodio = {
        'episodio_id': f"ep_{int(time.time())}",
        'timestamp': datetime.now().isoformat(),
        'oggetti': oggetti,
        'num_oggetti': len(oggetti),
        'descrizione': f"Rilevati: {', '.join([o['classe'] for o in oggetti])}" if oggetti else "Ambiente vuoto",
        'audio': frase,
        'valenza': valenza,
        'emozione': 'positivo' if valenza > 0 else ('negativo' if valenza < 0 else 'neutro'),
        'azione': azione,
        'pattern': pattern_visual,
        'narrazione': narrazione_text
    }
    
    return episodio, narrazione_text

# Main
print("\n" + "="*70)
print("  🧠 DEMO CON NARRAZIONE COGNITIVA")
print("="*70)
print("\n[INFO] Generazione episodi con narrazione completa...")
print("[INFO] Premi CTRL+C per fermare\n")

os.makedirs("data", exist_ok=True)
episodi = []

# Apri file log per salvare TUTTO
log_file = open("NARRAZIONE_LOG.txt", "w", encoding="utf-8")
log_file.write("="*70 + "\n")
log_file.write("  🧠 LOG NARRAZIONE COGNITIVA COMPLETA\n")
log_file.write("="*70 + "\n")
log_file.write(f"Inizio: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
log_file.write("="*70 + "\n\n")

try:
    for i in range(1, 11):  # 10 episodi
        print(f"\n{'╔'+'═'*68+'╗'}")
        print(f"║ EPISODIO #{i:02d}{' '*56}║")
        print(f"{'╚'+'═'*68+'╝'}")
        
        episodio, narrazione = genera_episodio()
        
        # Mostra narrazione
        print(narrazione)
        
        # Salva episodio
        episodi.append(episodio)
        
        # Salva files per dashboard
        with open("data/memoria.json", "w", encoding="utf-8") as f:
            json.dump(episodi, f, indent=2, ensure_ascii=False)
        
        with open("data/ultima_frase.txt", "w", encoding="utf-8") as f:
            f.write(episodio['audio'])
        
        with open("data/ultima_azione.txt", "w", encoding="utf-8") as f:
            f.write(episodio['azione'])
        
        with open("data/ultima_narrazione.txt", "w", encoding="utf-8") as f:
            f.write(narrazione)
        
        print(f"\n[💾] Episodio salvato: {episodio['episodio_id']}")
        print(f"[📊] Totale episodi: {len(episodi)}")
        
        time.sleep(3)  # Pausa tra episodi

except KeyboardInterrupt:
    print("\n\n[!] Interruzione utente")

print(f"\n{'='*70}")
print(f"  ✅ DEMO COMPLETATA")
print(f"{'='*70}")
print(f"\n[STATISTICHE]")
print(f"  • Episodi generati: {len(episodi)}")
print(f"  • File salvati in: data/")
print(f"  • Dashboard: http://localhost:8501")
print()

