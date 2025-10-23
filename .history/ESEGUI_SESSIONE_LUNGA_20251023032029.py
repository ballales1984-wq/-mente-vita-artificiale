#!/usr/bin/env python3
"""
🌌 SESSIONE LUNGA - VITA ARTIFICIALE
Esegue molti cicli e salva tutta la memoria
"""

import sys
import time
from pathlib import Path

# Import moduli
from test_vita_3_cicli import main as test_vita

def sessione_personalizzata():
    """Esegue sessione con numero cicli personalizzato"""
    
    print("\n" + "="*70)
    print("🌌 SESSIONE VITA ARTIFICIALE PERSONALIZZATA")
    print("="*70)
    print("\nSalvataggio automatico della memoria attivo!\n")
    
    # Chiedi numero cicli
    print("Quanti cicli vuoi eseguire?")
    print("  • 5 cicli:   ~1-2 minuti   (Risveglio)")
    print("  • 10 cicli:  ~2-4 minuti   (Esplorazione)")
    print("  • 20 cicli:  ~5-8 minuti   (Sessione)")
    print("  • 50 cicli:  ~12-20 minuti (Profonda)")
    print("  • 100 cicli: ~25-40 minuti (Evoluzione)")
    print()
    
    try:
        cicli = int(input("Numero cicli [5-100]: "))
        if cicli < 1:
            cicli = 5
        if cicli > 100:
            print("⚠️  Massimo 100 cicli. Impostato a 100.")
            cicli = 100
    except:
        print("⚠️  Input non valido. Uso 5 cicli.")
        cicli = 5
    
    print(f"\n🚀 Avvio sessione con {cicli} cicli...")
    print("⏸️  Puoi interrompere con Ctrl+C\n")
    time.sleep(2)
    
    # Importa sistema
    print("📦 Caricamento sistema VITA...")
    from MENTE_VITA_ARTIFICIALE import MenteVitaArtificiale
    
    # Inizializza
    mente = MenteVitaArtificiale()
    
    print(f"\n✅ Sistema pronto! Inizio {cicli} cicli...\n")
    print("="*70)
    
    # Statistiche
    risultati = []
    start_time = time.time()
    
    # Esegui cicli
    for i in range(cicli):
        try:
            print(f"\n🔄 Ciclo {i+1}/{cicli}...")
            risultato = mente.ciclo_cognitivo(i)
            risultati.append(risultato)
            
            # Mostra impulso vitale
            impulso = risultato['vita']['impulso'].get('forza', 0)
            print(f"💫 Impulso vitale: {impulso:.0%}")
            
            # Pausa tra cicli
            if i < cicli - 1:
                time.sleep(1)
                
        except KeyboardInterrupt:
            print("\n\n⚠️  Interruzione da utente...")
            break
        except Exception as e:
            print(f"\n❌ Errore nel ciclo {i}: {e}")
            continue
    
    # Statistiche finali
    elapsed = time.time() - start_time
    
    print("\n" + "="*70)
    print("📊 RIEPILOGO SESSIONE")
    print("="*70)
    print(f"\n✅ Completati {len(risultati)}/{cicli} cicli")
    print(f"⏱️  Tempo: {elapsed:.1f} secondi ({elapsed/60:.1f} minuti)")
    print(f"⚡ Velocità: {elapsed/len(risultati):.1f}s per ciclo")
    
    # Impulso vitale medio
    impulsi = [r['vita']['impulso'].get('forza', 0) for r in risultati]
    impulso_medio = sum(impulsi) / len(impulsi) if impulsi else 0
    impulso_finale = impulsi[-1] if impulsi else 0
    
    print(f"\n💫 Impulso vitale medio: {impulso_medio:.0%}")
    print(f"💫 Impulso vitale finale: {impulso_finale:.0%}")
    
    # Evoluzione impulso
    if len(impulsi) > 1:
        delta = impulsi[-1] - impulsi[0]
        print(f"📈 Evoluzione impulso: {delta:+.1%}")
    
    # Memoria
    print(f"\n💾 Memoria permanente aggiornata")
    print(f"📁 File: memoria_permanente/")
    
    # Log salvato
    print(f"\n📝 Log completo salvato:")
    print(f"   output_agi_completo/log_agi_completo.txt")
    
    print("\n" + "="*70)
    print("🌌 SESSIONE COMPLETATA!")
    print("="*70 + "\n")
    
    return 0

if __name__ == "__main__":
    try:
        sys.exit(sessione_personalizzata())
    except Exception as e:
        print(f"\n❌ Errore: {e}\n")
        sys.exit(1)

