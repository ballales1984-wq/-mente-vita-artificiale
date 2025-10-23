#!/usr/bin/env python3
"""
🎙️ REGISTRATORE AUDIO - Crea File Audio per Test
Registra la tua voce e salvala per usarla nei cicli senza pause!
"""

import sounddevice as sd
import numpy as np
from scipy.io import wavfile
import os
import time

def lista_microfoni():
    """Mostra microfoni disponibili"""
    print("\n" + "="*70)
    print("  🎤 MICROFONI DISPONIBILI")
    print("="*70)
    devices = sd.query_devices()
    for i, device in enumerate(devices):
        if device['max_input_channels'] > 0:
            print(f"  [{i}] {device['name']}")
            print(f"      Canali: {device['max_input_channels']}, SR: {int(device['default_samplerate'])} Hz")
    print("="*70)

def registra_audio(durata=5, microfono_id=None, nome_file="audio_test"):
    """
    Registra audio dal microfono e salva in WAV
    
    Args:
        durata: Secondi di registrazione
        microfono_id: ID microfono (None = default)
        nome_file: Nome file output (senza estensione)
    """
    print("\n" + "="*70)
    print(f"  🎙️ REGISTRAZIONE AUDIO - {durata} secondi")
    print("="*70)
    
    sample_rate = 16000  # Hz (standard per Whisper)
    
    # Info microfono
    if microfono_id is None:
        device_info = sd.query_devices(kind='input')
    else:
        device_info = sd.query_devices(microfono_id)
    
    print(f"\n[MICROFONO] {device_info['name']}")
    print(f"[SAMPLE RATE] {sample_rate} Hz")
    print(f"[DURATA] {durata} secondi")
    print(f"[OUTPUT] {nome_file}.wav")
    
    # Countdown
    print("\n[PRONTO] Registrazione inizia tra:")
    for i in range(3, 0, -1):
        print(f"  {i}...")
        time.sleep(1)
    
    print("\n🔴 REGISTRAZIONE IN CORSO - PARLA ORA!")
    print("="*70)
    
    # Registra
    try:
        audio = sd.rec(
            int(durata * sample_rate),
            samplerate=sample_rate,
            channels=1,
            dtype='float32',
            device=microfono_id
        )
        sd.wait()  # Aspetta fine registrazione
        
        print("="*70)
        print("✅ REGISTRAZIONE COMPLETATA!")
        
        # Analizza
        energia = np.mean(np.abs(audio))
        volume_db = 20 * np.log10(energia + 1e-10)
        
        print(f"\n[ANALISI]")
        print(f"  • Energia media: {energia:.6f}")
        print(f"  • Volume: {volume_db:.1f} dB")
        print(f"  • Campioni: {len(audio)}")
        
        # Salva WAV
        os.makedirs("audio", exist_ok=True)
        output_path = f"audio/{nome_file}.wav"
        
        # Converti in int16 per WAV
        audio_int16 = np.int16(audio * 32767)
        wavfile.write(output_path, sample_rate, audio_int16)
        
        print(f"\n✅ File salvato: {output_path}")
        print(f"   Dimensione: {os.path.getsize(output_path) / 1024:.1f} KB")
        
        return output_path
        
    except Exception as e:
        print(f"\n❌ ERRORE: {e}")
        return None

def menu_principale():
    """Menu interattivo"""
    print("""
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║        🎙️ REGISTRATORE AUDIO v1.0                              ║
║                                                                  ║
║    Crea file audio per test senza pause!                        ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
    """)
    
    while True:
        print("\n[MENU] Scegli azione:\n")
        print("  1. Registra 3 secondi")
        print("  2. Registra 5 secondi")
        print("  3. Registra 10 secondi")
        print("  4. Durata personalizzata")
        print("  5. Lista microfoni")
        print("  9. Esci")
        
        scelta = input("\n>> Scelta: ").strip()
        
        if scelta == "1":
            nome = input("Nome file (default: audio_3s): ").strip() or "audio_3s"
            registra_audio(durata=3, nome_file=nome)
        
        elif scelta == "2":
            nome = input("Nome file (default: audio_5s): ").strip() or "audio_5s"
            registra_audio(durata=5, nome_file=nome)
        
        elif scelta == "3":
            nome = input("Nome file (default: audio_10s): ").strip() or "audio_10s"
            registra_audio(durata=10, nome_file=nome)
        
        elif scelta == "4":
            try:
                durata = int(input("Durata in secondi: ").strip())
                nome = input(f"Nome file (default: audio_{durata}s): ").strip() or f"audio_{durata}s"
                registra_audio(durata=durata, nome_file=nome)
            except ValueError:
                print("\n❌ Durata non valida!")
        
        elif scelta == "5":
            lista_microfoni()
        
        elif scelta == "9":
            print("\n✅ Uscita\n")
            break
        
        else:
            print("\n❌ Scelta non valida!")

if __name__ == "__main__":
    try:
        menu_principale()
    except KeyboardInterrupt:
        print("\n\n✅ Interruzione utente\n")


