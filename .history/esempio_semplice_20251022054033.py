"""
🎯 ESEMPIO SEMPLICE - Ciclo Cognitivo Minimale
================================================
Dimostrazione base del funzionamento della mente artificiale.
Ideale per capire il flusso di elaborazione.
"""

from moduli import visione, udito, prefrontale, motoria

def ciclo_cognitivo_semplice():
    """
    Ciclo cognitivo minimale come da esempio del README
    """
    print("="*60)
    print("🧠 ESEMPIO CICLO COGNITIVO SEMPLICE")
    print("="*60 + "\n")
    
    # 1. PERCEZIONE VISIVA
    print("👁️  VISIONE: Elaborazione immagine...")
    risultato_visivo = visione.elabora("immagine.jpg")
    print(f"   Risultato: {risultato_visivo['descrizione']}")
    print(f"   Oggetti: {risultato_visivo['num_oggetti']}\n")
    
    # 2. PERCEZIONE UDITIVA
    print("👂 UDITO: Ascolto audio...")
    risultato_audio = udito.ascolta("audio.wav")
    print(f"   Trascrizione: '{risultato_audio['testo']}'")
    print(f"   Tono: {risultato_audio['tono']}\n")
    
    # 3. RAGIONAMENTO
    print("🧠 PREFRONTALE: Ragionamento...")
    decisione = prefrontale.ragiona(
        percezioni_visive=risultato_visivo,
        percezioni_uditive=risultato_audio
    )
    print(f"   Decisione: {decisione['azione']}")
    print(f"   Ragionamento: {decisione['ragionamento'][:60]}...\n")
    
    # 4. AZIONE
    print("🦿 MOTORIA: Esecuzione azione...")
    successo = motoria.agisci(decisione)
    print(f"   Risultato: {'✅ Successo' if successo else '❌ Fallito'}\n")
    
    print("="*60)
    print("✅ CICLO COMPLETATO")
    print("="*60)


if __name__ == "__main__":
    # Esempio minimale
    ciclo_cognitivo_semplice()

