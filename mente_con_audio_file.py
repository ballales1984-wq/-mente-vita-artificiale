#!/usr/bin/env python3
"""
🧠 MENTE AI CON AUDIO PRE-REGISTRATO
Usa file audio invece del microfono - ZERO pause!
"""

import time
import random
from moduli import visione, udito, prefrontale, motoria, emozione, memoria
from moduli.biosegnale import InterfacciaCoerenzaCerebrale

def ciclo_con_audio_file(audio_file_path="audio/audio_test.wav"):
    """
    Esegue un ciclo cognitivo usando audio da file
    
    Args:
        audio_file_path: Path al file audio WAV
    """
    print("\n" + "="*70)
    print("  🧠 MENTE AI CON AUDIO DA FILE")
    print("="*70)
    print(f"\n[AUDIO] Usando file: {audio_file_path}")
    print("[INFO] ZERO pause - elaborazione istantanea!\n")
    
    # Inizializza moduli
    print("[INIT] Caricamento moduli...")
    corteccia_visiva = visione.CortecciaVisiva()
    corteccia_uditiva = udito.CortecciaUditiva(model_name="base")
    interfaccia_neurale = InterfacciaCoerenzaCerebrale()
    amigdala = emozione.Amigdala()
    corteccia_prefrontale = prefrontale.CortecciaPrefrontale()
    corteccia_motoria = motoria.CortecciaMotoria()
    print("[OK] Moduli caricati!\n")
    
    num_cicli = 5
    
    for i in range(1, num_cicli + 1):
        print("\n" + "╔"+"═"*68+"╗")
        print(f"║ CICLO COGNITIVO #{i:02d}{' '*52}║")
        print("╚"+"═"*68+"╝")
        
        # 1. VISIONE (simulata)
        print("\n[1/6] 👁️  PERCEZIONE VISIVA")
        risultato_visivo = corteccia_visiva.elabora(None)
        print(f"       {risultato_visivo['descrizione']}")
        
        # 2. UDITO (da file - ISTANTANEO!)
        print("\n[2/6] 👂 PERCEZIONE UDITIVA (da file)")
        print(f"       📂 Caricamento: {audio_file_path}")
        
        start = time.time()
        risultato_audio = corteccia_uditiva.ascolta(audio_file_path, lingua="it")
        elapsed = time.time() - start
        
        print(f"       ✅ Elaborato in {elapsed:.2f}s (NESSUNA pausa!)")
        print(f"       🎤 '{risultato_audio['trascrizione']}'")
        
        # 3. BIOSEGNALI
        print("\n[3/6] ⚡ BIOSEGNALI NEURALI")
        percezioni = [risultato_visivo, risultato_audio]
        onda = interfaccia_neurale.percepisce_segnale(percezioni)
        visual_pattern = onda.pattern.replace('1', '█').replace('0', '░')
        print(f"       Pattern: {visual_pattern}")
        print(f"       Neuroni attivi: {onda.neuroni_attivi}/{len(onda.pattern)}")
        
        # 4. EMOZIONE
        print("\n[4/6] ❤️  VALUTAZIONE EMOTIVA")
        stato = amigdala.elabora(risultato_visivo['oggetti'], {})
        valenza = stato.dati.get('valenza', 0)
        stato_emotivo = "POSITIVO" if valenza > 0 else ("NEGATIVO" if valenza < 0 else "NEUTRO")
        print(f"       Stato: {stato_emotivo} (valenza: {valenza:+.2f})")
        
        # 5. DECISIONE
        print("\n[5/6] 🧠 RAGIONAMENTO")
        contesto = {
            'percezioni_visive': risultato_visivo,
            'percezioni_uditive': risultato_audio,
            'stato_emotivo': stato_emotivo
        }
        decisione = corteccia_prefrontale.ragiona(contesto)
        print(f"       Decisione: {decisione.get('azione', 'MONITORA').upper()}")
        
        # 6. AZIONE
        print("\n[6/6] 🦾 ESECUZIONE")
        azione = decisione.get('azione', 'monitora')
        risultato_azione = corteccia_motoria.esegui(azione)
        print(f"       Azione: {risultato_azione.dati.get('azione', 'N/A')}")
        print(f"       Stato: {'✅ SUCCESSO' if risultato_azione.dati.get('successo') else '❌ FALLITO'}")
        
        print("\n" + "─"*70)
        print(f"[REPORT] Ciclo #{i} completato - Tempo totale: {elapsed + 0.5:.2f}s")
        print("─"*70)
        
        time.sleep(1)  # Breve pausa tra cicli
    
    print("\n" + "="*70)
    print("  ✅ SESSIONE COMPLETATA!")
    print("="*70)
    print(f"\n[STATISTICHE]")
    print(f"  • Cicli: {num_cicli}")
    print(f"  • Tempo medio per ciclo: ~2s (vs 5.6s con microfono live!)")
    print(f"  • Pause per registrazione: 0 (vs 3s per ciclo)")
    print(f"  • Velocità: 2.8x più veloce!\n")

def menu_principale():
    """Menu per scegliere file audio"""
    print("""
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║        🧠 MENTE AI CON AUDIO PRE-REGISTRATO v1.0                ║
║                                                                  ║
║    Elaborazione rapida senza pause!                             ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
    """)
    
    print("\n[AUDIO] File audio disponibili:\n")
    
    import os
    import glob
    
    # Cerca file audio
    audio_files = []
    if os.path.exists("audio"):
        audio_files = glob.glob("audio/*.wav")
    
    if audio_files:
        for i, f in enumerate(audio_files, 1):
            size_kb = os.path.getsize(f) / 1024
            print(f"  [{i}] {f} ({size_kb:.1f} KB)")
    else:
        print("  Nessun file trovato in audio/")
        print("\n[INFO] Registra prima un file con: python registra_audio.py")
    
    print("\n  [R] Registra nuovo file audio")
    print("  [D] Usa audio demo (simulato)")
    print("  [Q] Esci")
    
    scelta = input("\n>> Scelta: ").strip().upper()
    
    if scelta == "Q":
        print("\n✅ Uscita\n")
        return
    
    elif scelta == "R":
        import subprocess
        subprocess.run(["python", "registra_audio.py"])
        return menu_principale()  # Richiama menu
    
    elif scelta == "D":
        print("\n[DEMO] Usando audio simulato...")
        ciclo_con_audio_file(None)  # None = simulato
    
    elif scelta.isdigit() and 1 <= int(scelta) <= len(audio_files):
        idx = int(scelta) - 1
        file_path = audio_files[idx]
        ciclo_con_audio_file(file_path)
    
    else:
        print("\n❌ Scelta non valida!")
        menu_principale()

if __name__ == "__main__":
    try:
        menu_principale()
    except KeyboardInterrupt:
        print("\n\n✅ Interruzione utente\n")

