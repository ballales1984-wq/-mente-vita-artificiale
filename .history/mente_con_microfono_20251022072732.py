"""
🎤🧠 MENTE ARTIFICIALE CON MICROFONO REALE
===========================================
Sistema che usa il microfono per input audio reale e trascrizione vocale.

Funzionalità:
- Registrazione audio dal microfono
- Trascrizione real-time con Whisper
- Riconoscimento comandi vocali
- Ciclo cognitivo con input vocale
"""

import time
import sys
import numpy as np
from moduli import udito, visione, prefrontale, motoria, emozione, memoria

try:
    import sounddevice as sd
    AUDIO_OK = True
except ImportError:
    AUDIO_OK = False


def test_microfono():
    """Testa se il microfono è disponibile"""
    print("="*70)
    print("[TEST MICROFONO] Verifica disponibilita...")
    print("="*70)
    
    if not AUDIO_OK:
        print("\n[ERROR] SoundDevice non installato!")
        print("\nInstalla con: pip install sounddevice soundfile")
        return False
    
    try:
        # Lista dispositivi
        devices = sd.query_devices()
        
        input_devices = []
        for i, device in enumerate(devices):
            if device['max_input_channels'] > 0:
                input_devices.append((i, device))
        
        if not input_devices:
            print("\n[ERROR] Nessun microfono trovato!")
            return False
        
        print(f"\n[OK] Trovati {len(input_devices)} microfoni:")
        for idx, device in input_devices:
            default = " [DEFAULT]" if idx == sd.default.device[0] else ""
            print(f"  [{idx}] {device['name']}{default}")
            print(f"      Canali: {device['max_input_channels']}")
        
        # Test registrazione
        print(f"\n[TEST] Registrazione 1 secondo...")
        print("[!] Fai un rumore...")
        
        audio = sd.rec(
            int(1 * 16000),
            samplerate=16000,
            channels=1,
            dtype='float32'
        )
        sd.wait()
        
        energy = np.sum(audio ** 2) / len(audio)
        max_amp = np.max(np.abs(audio))
        
        print(f"\n[RISULTATO]")
        print(f"  Energia segnale: {energy:.6f}")
        print(f"  Ampiezza max: {max_amp:.3f}")
        
        if energy < 1e-8:
            print(f"  [WARNING] Segnale molto debole!")
            print(f"  Verifica:")
            print(f"    - Volume microfono")
            print(f"    - Permessi audio")
            print(f"    - Microfono selezionato corretto")
        else:
            print(f"  [OK] Microfono funzionante!")
        
        return True
        
    except Exception as e:
        print(f"\n[ERROR] {e}")
        return False


def ciclo_con_comando_vocale():
    """Esegue ciclo cognitivo con comando vocale dal microfono"""
    print("\n" + "="*70)
    print("[CICLO COGNITIVO CON COMANDO VOCALE]")
    print("="*70)
    
    # Inizializza moduli
    corteccia_uditiva = udito.get_instance()
    ippocampo = memoria.get_instance()
    amigdala = emozione.get_instance()
    
    # Inizializza microfono
    print("\n[STEP 1/6] Inizializzazione microfono...")
    if not corteccia_uditiva.inizializza_microfono():
        print("[ERROR] Impossibile inizializzare microfono!")
        print("\nUsa modalita simulata: python esempio_semplice.py")
        return False
    
    # Registra comando
    print("\n[STEP 2/6] REGISTRAZIONE AUDIO...")
    print(f"[!] Parla ora! (3 secondi)")
    print("[!] Esempi: 'Vieni qui', 'Fermati', 'Vai avanti'\n")
    
    # Countdown
    for i in range(3, 0, -1):
        print(f"  {i}...")
        time.sleep(0.8)
    
    print("  🎤 REGISTRAZIONE IN CORSO...")
    
    # Registra
    audio = sd.rec(
        int(3 * 16000),
        samplerate=16000,
        channels=1,
        dtype='float32'
    )
    sd.wait()
    
    print("  [OK] Audio registrato\n")
    
    # Trascrivi con Whisper
    print("[STEP 3/6] TRASCRIZIONE con Whisper...")
    risultato_audio = corteccia_uditiva.ascolta(audio.flatten(), lingua="it")
    
    print(f"\n  Trascrizione: '{risultato_audio['testo']}'")
    print(f"  Tono: {risultato_audio['tono']}")
    print(f"  Intenzione: {risultato_audio['intenzione']}")
    print(f"  Emozione: {risultato_audio['emozione']}")
    
    # Visione simulata
    print("\n[STEP 4/6] VISIONE: Input simulato...")
    risultato_visivo = visione.elabora("immagine.jpg")
    print(f"  {risultato_visivo['descrizione']}")
    
    # Richiamo memoria
    print("\n[STEP 5/6] MEMORIA: Richiamo contestuale...")
    contesto = f"{risultato_visivo['descrizione']} {risultato_audio['testo']}"
    memorie, suggerimenti = ippocampo.richiama_contestuale(contesto, top_k=3)
    
    if memorie:
        print(f"  Memorie trovate: {len(memorie)}")
    
    # Emozione
    print("\n[STEP 6/6] EMOZIONE e DECISIONE...")
    risultato_emozione = amigdala.elabora({
        'percezioni': [risultato_visivo, risultato_audio],
        'memoria': {}
    })
    
    stato_emotivo = risultato_emozione.dati['stato_emotivo']
    valenza = risultato_emozione.dati['valenza']
    
    print(f"  Stato emotivo: {stato_emotivo.upper()}")
    print(f"  Valenza: {valenza:+.2f}")
    
    # Ragionamento
    decisione = prefrontale.ragiona(
        percezioni_visive=risultato_visivo,
        percezioni_uditive=risultato_audio,
        stato_emotivo=stato_emotivo,
        memoria=[m.contenuto for m in memorie]
    )
    
    # Applica suggerimenti
    if suggerimenti.get('confidence', 0) > 0.7 and suggerimenti.get('azione_consigliata'):
        decisione['azione'] = suggerimenti['azione_consigliata']
    
    print(f"\n  DECISIONE: {decisione['azione'].upper()}")
    print(f"  Priorita: {decisione['priorita']:.2f}")
    print(f"  Ragionamento: {decisione['ragionamento'][:60]}...")
    
    # Azione
    print(f"\n[AZIONE] Esecuzione...")
    successo = motoria.agisci(decisione)
    
    # Reward e memorizzazione
    reward = amigdala.assegna_reward(decisione['azione'], successo, valenza)
    
    ippocampo.memorizza(
        f"comando_vocale_{int(time.time())}",
        f"Comando: '{risultato_audio['testo']}' | Azione: {decisione['azione']} | Successo: {successo}",
        metadata={
            'valenza': valenza,
            'importanza': reward / 2.0 + 0.5,
            'contesto': {'audio': risultato_audio['testo'], 'tono': risultato_audio['tono']}
        }
    )
    
    print(f"\n{'='*70}")
    print(f"[OK] CICLO COMPLETATO - Reward: {reward:+.2f}")
    print(f"{'='*70}\n")
    
    return True


def modalita_ascolto_continuo():
    """Modalità ascolto continuo: registra e trascrivi in loop"""
    print("\n" + "="*70)
    print("[MODALITA' ASCOLTO CONTINUO]")
    print("="*70)
    print("\n[!] Sistema in ascolto continuo")
    print("[!] Premi CTRL+C per uscire\n")
    
    corteccia_uditiva = udito.get_instance()
    
    # Inizializza microfono
    if not corteccia_uditiva.inizializza_microfono():
        return False
    
    ciclo = 0
    
    try:
        while True:
            ciclo += 1
            
            print(f"\n[ASCOLTO #{ciclo}]")
            print(f"[!] Parla ora (3 secondi)...")
            print("  🎤 ", end='', flush=True)
            
            # Countdown visivo
            for i in range(3):
                time.sleep(1)
                print("█", end='', flush=True)
            
            print(" [OK]\n")
            
            # Registra
            audio = sd.rec(
                int(3 * 16000),
                samplerate=16000,
                channels=1,
                dtype='float32'
            )
            sd.wait()
            
            # Check se c'è audio significativo
            energy = np.sum(audio ** 2) / len(audio)
            
            if energy < 1e-6:
                print("  [SILENZIO] Nessun audio rilevato\n")
                time.sleep(1)
                continue
            
            # Trascrivi
            print("  [ELABORAZIONE] Trascrizione in corso...")
            risultato = corteccia_uditiva.ascolta(audio.flatten(), lingua="it")
            
            if risultato['testo']:
                print(f"\n  📝 Testo: '{risultato['testo']}'")
                print(f"  🎵 Tono: {risultato['tono']}")
                print(f"  💬 Intenzione: {risultato['intenzione']}")
                print(f"  ❤️  Emozione: {risultato['emozione']}")
            else:
                print("  [!] Nessun testo riconosciuto")
            
            # Pausa prima del prossimo ciclo
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("\n\n[!] Interruzione manuale")
    
    print(f"\n[REPORT]")
    print(f"  Cicli ascolto: {ciclo}")
    print(f"\n[OK] Sistema disattivato\n")
    
    return True


def modalita_comando_vocale_interattivo():
    """Modalità comando vocale interattivo"""
    print("\n" + "="*70)
    print("[MODALITA' COMANDO VOCALE INTERATTIVO]")
    print("="*70)
    print("\n[SISTEMA] Assistente vocale attivo")
    print("[!] Dì comandi come: 'vieni qui', 'fermati', 'vai avanti'\n")
    
    corteccia_uditiva = udito.get_instance()
    
    # Inizializza
    if not corteccia_uditiva.inizializza_microfono():
        return False
    
    comandi_eseguiti = 0
    
    try:
        while True:
            input("\n[PREMI ENTER per registrare comando] ")
            
            print("\n🎤 Registrazione (3 secondi)...")
            print("[!] Parla ORA!\n")
            
            # Registra
            audio = sd.rec(
                int(3 * 16000),
                samplerate=16000,
                channels=1,
                dtype='float32'
            )
            sd.wait()
            
            print("[*] Elaborazione...")
            
            # Trascrivi
            risultato = corteccia_uditiva.ascolta(audio.flatten(), lingua="it")
            
            if not risultato['testo']:
                print("[!] Nessun comando riconosciuto\n")
                continue
            
            print(f"\n✓ Comando riconosciuto: '{risultato['testo']}'")
            print(f"  Tono: {risultato['tono']}")
            print(f"  Intenzione: {risultato['intenzione']}")
            
            # Elabora comando
            if risultato['intenzione'] == 'comando':
                decisione = prefrontale.ragiona(
                    percezioni_visive={},
                    percezioni_uditive=risultato
                )
                
                print(f"\n→ Decisione: {decisione['azione'].upper()}")
                
                # Esegui
                motoria.agisci(decisione)
                comandi_eseguiti += 1
            else:
                print("  [!] Non è un comando riconosciuto")
            
    except KeyboardInterrupt:
        print("\n\n[!] Uscita")
    
    print(f"\n[REPORT]")
    print(f"  Comandi eseguiti: {comandi_eseguiti}")
    print(f"\n[OK] Sistema disattivato\n")
    
    return True


if __name__ == "__main__":
    print("""
    ================================================================
    
           MENTE ARTIFICIALE - INTEGRAZIONE MICROFONO
           Corteccia Uditiva con Whisper Real-Time
           
    ================================================================
    """)
    
    # Verifica dipendenze
    if not AUDIO_OK:
        print("\n[ERROR] SoundDevice non disponibile!")
        print("\nInstalla con:")
        print("  pip install sounddevice soundfile")
        print("\nPoi esegui di nuovo questo programma.")
        sys.exit(1)
    
    # Test microfono
    try:
        mic_ok = test_microfono()
    except Exception as e:
        print(f"\n[ERROR] {e}")
        mic_ok = False
    
    if not mic_ok:
        print("\n[!] Microfono non disponibile, uscita...")
        sys.exit(1)
    
    # Menu
    print("\n" + "="*70)
    print("[MENU] Scegli modalita:")
    print("="*70)
    print("  1. Ciclo singolo con comando vocale")
    print("  2. Ascolto continuo (loop trascrizione)")
    print("  3. Assistente vocale interattivo")
    print("  4. Lista microfoni disponibili")
    print("="*70)
    
    try:
        scelta = input("\n>> Scelta (1-4): ").strip()
        
        if scelta == "1":
            ciclo_con_comando_vocale()
        elif scelta == "2":
            modalita_ascolto_continuo()
        elif scelta == "3":
            modalita_comando_vocale_interattivo()
        elif scelta == "4":
            corteccia = udito.get_instance()
            corteccia.lista_microfoni()
        else:
            print("[ERROR] Scelta non valida")
            
    except KeyboardInterrupt:
        print("\n\n[!] Interruzione\n")
    except Exception as e:
        print(f"\n[ERROR] {e}")
        import traceback
        traceback.print_exc()

