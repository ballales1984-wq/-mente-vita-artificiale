"""
🧠 MENTE AI DEMO - Simulazione Cognitiva
========================================
Genera dati simulati per testare la dashboard senza hardware.

Ideale per:
- Presentazioni
- Demo
- Sviluppo offline
- Test interfaccia

Esegui: python mente_ai_demo.py
"""

import random
import time
import json
import os
from datetime import datetime

def genera_codice_binario(lunghezza=15):
    """Genera pattern binario simmetrico"""
    # Pattern simmetrico: centro attivo che si espande
    patterns = [
        "0000001000000",
        "0000010100000",
        "0000101010000",
        "0001010101000",
        "0010101010100",
        "0101010101010",
        "1010101010101",
        "░░░░░█░░░░░",
        "░░░░█████░░░░",
        "░░░███████░░░",
        "░░█████████░░",
        "░███████████░"
    ]
    return random.choice(patterns)

def genera_episodio(ciclo_num):
    """Genera episodio simulato completo"""
    
    # Dati casuali realistici
    oggetti = [
        ("person", 0.92),
        ("bottle", 0.87),
        ("laptop", 0.95),
        ("book", 0.78),
        ("phone", 0.91),
        ("chair", 0.85),
        ("cup", 0.88),
        ("keyboard", 0.89)
    ]
    
    frasi = [
        "Portami la bottiglia sul tavolo",
        "Dov'è il mio telefono?",
        "Accendi la luce per favore",
        "Prendi il libro rosso",
        "Metti via le chiavi",
        "Vieni qui un momento",
        "Aiutami con questo",
        "Cosa vedi davanti a te?"
    ]
    
    toni = ["amichevole", "urgente", "neutro", "curioso"]
    intenzioni = ["comando", "domanda", "richiesta"]
    azioni = [
        "monitora_ambiente",
        "avvicinati",
        "esegui_comando",
        "cerca_oggetto",
        "mantieni_distanza"
    ]
    
    # Genera valori
    oggetto, confidenza = random.choice(oggetti)
    frase = random.choice(frasi)
    tono = random.choice(toni)
    intenzione = random.choice(intenzioni)
    
    # Valenza emotiva basata su tono
    valenza_map = {
        "amichevole": random.uniform(0.5, 1.0),
        "urgente": random.uniform(0.2, 0.6),
        "neutro": random.uniform(-0.2, 0.2),
        "curioso": random.uniform(0.3, 0.7)
    }
    valenza = valenza_map[tono]
    
    intensita = round(random.uniform(0.4, 0.9), 2)
    codifica = genera_codice_binario()
    azione = random.choice(azioni)
    priorita = round(random.uniform(0.6, 0.95), 2)
    
    risposta = f"Ho rilevato {oggetto}. {random.choice(['Procedo.', 'Eseguo.', 'Confermo.', 'Compreso.'])}"
    
    # Costruisci episodio
    episodio = {
        "id": f"episodio_{ciclo_num:03d}",
        "timestamp": time.time(),
        "contenuto": f"V:{oggetto} | A:{frase[:30]} | {azione}",
        "valenza_emotiva": round(valenza, 2),
        "importanza": round(priorita + random.uniform(-0.2, 0.3), 2),
        "accessi": 0,
        "contesto": {
            "ciclo": ciclo_num,
            "oggetto_visivo": oggetto,
            "confidenza_visiva": confidenza,
            "frase_audio": frase,
            "tono": tono,
            "intenzione": intenzione,
            "azione_eseguita": azione,
            "priorita_decisione": priorita,
            "successo": random.choice([True, True, True, False]),  # 75% successo
            "pattern_neurale": codifica
        },
        "stimoli": {
            "visivo": {
                "oggetto": oggetto,
                "confidenza": confidenza,
                "modello": "YOLOv8 (simulato)"
            },
            "uditivo": {
                "trascrizione": frase,
                "tono": tono,
                "intenzione": intenzione,
                "modello": "Whisper (simulato)"
            }
        },
        "emozione": {
            "valenza": round(valenza, 2),
            "intensità": intensita,
            "stato": "POSITIVO" if valenza > 0.3 else "NEUTRO" if valenza > -0.3 else "NEGATIVO"
        },
        "biosegnale": {
            "codifica": codifica,
            "tipo": "binaria simmetrica",
            "neuroni_attivi": codifica.count('█') if '█' in codifica else codifica.count('1')
        },
        "decisione": {
            "azione": azione,
            "risposta": risposta,
            "priorita": priorita
        }
    }
    
    return episodio, frase, risposta, azione

def main():
    """Simulazione continua"""
    
    print("="*70)
    print("  🧠 MENTE AI DEMO - Simulazione Cognitiva")
    print("="*70)
    print()
    print("[INFO] Generazione episodi simulati...")
    print("[INFO] I dati saranno visualizzati in dashboard.py")
    print()
    
    # Crea directory data se non esiste
    os.makedirs("data", exist_ok=True)
    
    # Carica episodi esistenti o inizia da zero
    memoria_path = "data/memoria.json"
    
    try:
        if os.path.exists(memoria_path):
            with open(memoria_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                episodi = data.get('episodica', [])
                print(f"[OK] Caricate {len(episodi)} memorie esistenti")
        else:
            episodi = []
            print("[OK] Nuova memoria inizializzata")
    except:
        episodi = []
        print("[OK] Nuova memoria inizializzata")
    
    print()
    print("[START] Simulazione in corso... (CTRL+C per fermare)")
    print("-"*70)
    print()
    
    ciclo_num = len(episodi) + 1
    
    try:
        while True:
            # Genera episodio
            episodio, frase, risposta, azione = genera_episodio(ciclo_num)
            episodi.append(episodio)
            
            # Mantieni solo ultimi 50 episodi
            if len(episodi) > 50:
                episodi = episodi[-50:]
            
            # Salva memoria
            memoria_data = {
                "episodica": episodi,
                "meta": {
                    "memorizzazioni_totali": ciclo_num,
                    "ultimo_aggiornamento": datetime.now().isoformat(),
                    "richiami_totali": random.randint(10, 100),
                    "consolidamenti": ciclo_num // 5,
                    "reward_totale": round(sum(e.get('valenza_emotiva', 0) for e in episodi), 2),
                    "reward_medio": round(sum(e.get('valenza_emotiva', 0) for e in episodi) / len(episodi), 2) if episodi else 0
                }
            }
            
            with open(memoria_path, "w", encoding="utf-8") as f:
                json.dump(memoria_data, f, indent=2, ensure_ascii=False)
            
            # Salva file per dashboard
            with open("data/ultima_frase.txt", "w", encoding="utf-8") as f:
                f.write(frase)
            
            with open("data/ultima_risposta.txt", "w", encoding="utf-8") as f:
                f.write(risposta)
            
            with open("data/ultima_azione.txt", "w", encoding="utf-8") as f:
                f.write(f"Azione: {azione}")
            
            # Log console
            timestamp = datetime.now().strftime("%H:%M:%S")
            print(f"[{timestamp}] Ciclo #{ciclo_num:03d}")
            print(f"  👁️  Visivo: {episodio['stimoli']['visivo']['oggetto']} ({episodio['stimoli']['visivo']['confidenza']:.0%})")
            print(f"  👂 Audio: '{frase[:40]}...'")
            print(f"  ❤️  Emozione: {episodio['emozione']['stato']} (v:{episodio['valenza_emotiva']:+.2f})")
            print(f"  ⚡ Biosegnale: {episodio['biosegnale']['codifica']}")
            print(f"  🧠 Decisione: {azione}")
            print(f"  💾 Memorie: {len(episodi)}")
            print()
            
            ciclo_num += 1
            time.sleep(3)  # Pausa tra cicli
            
    except KeyboardInterrupt:
        print()
        print("-"*70)
        print("[STOP] Simulazione interrotta")
        print(f"[OK] Generati {ciclo_num-1} episodi")
        print(f"[OK] Dati salvati in: {memoria_path}")
        print()
        print("="*70)

if __name__ == "__main__":
    main()



