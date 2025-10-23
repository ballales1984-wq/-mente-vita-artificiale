"""
🔄 MENTE ARTIFICIALE - Cicli Continui
======================================
Versione che esegue cicli cognitivi in loop continuo
"""

import time
import sys
from moduli import visione, udito, prefrontale, motoria, emozione, memoria

def ciclo_cognitivo_continuo(num_cicli=10, delay=2.0):
    """
    Esegue cicli cognitivi continui con:
    - Richiamo contestuale intelligente
    - Suggerimenti dalla memoria
    - Consolidamento automatico dopo 5 minuti
    
    Args:
        num_cicli: Numero di cicli da eseguire (0 = infinito)
        delay: Pausa tra cicli in secondi
    """
    print("="*70)
    print("[*] MENTE ARTIFICIALE - MODALITA' CICLI CONTINUI")
    print("="*70)
    print(f"\nCicli da eseguire: {num_cicli if num_cicli > 0 else 'INFINITI'}")
    print(f"Delay tra cicli: {delay} secondi")
    print("\n[!] Premi CTRL+C per interrompere\n")
    print("="*70)
    
    # Inizializza moduli
    ippocampo = memoria.get_instance()
    amigdala = emozione.get_instance()
    
    ciclo_num = 0
    
    try:
        while True:
            ciclo_num += 1
            
            # Check se raggiunto limite cicli
            if num_cicli > 0 and ciclo_num > num_cicli:
                break
            
            print(f"\n{'='*70}")
            print(f"[CICLO #{ciclo_num}]")
            print(f"{'='*70}\n")
            
            # ========================================
            # 1. PERCEZIONE VISIVA
            # ========================================
            print("[1/7] VISIONE: Elaborazione...")
            risultato_visivo = visione.elabora("immagine.jpg")
            print(f"   ✓ {risultato_visivo['descrizione']}")
            
            # ========================================
            # 2. PERCEZIONE UDITIVA
            # ========================================
            print("\n👂 [2/6] UDITO: Ascolto...")
            risultato_audio = udito.ascolta("audio.wav")
            print(f"   ✓ Trascritto: '{risultato_audio['testo']}'")
            print(f"   ✓ Tono: {risultato_audio['tono']}")
            
            # ========================================
            # 3. RICHIAMO MEMORIA CONTESTUALE
            # ========================================
            print("\n💭 [3/7] RICHIAMO CONTESTUALE: Memorie simili...")
            
            # Costruisci descrizione contesto
            contesto_str = f"{risultato_visivo['descrizione']} {risultato_audio['testo']}"
            
            # Richiama memorie simili con suggerimenti
            memorie_rilevanti, suggerimenti = ippocampo.richiama_contestuale(contesto_str, top_k=3)
            
            if memorie_rilevanti:
                print(f"   ✓ Trovate {len(memorie_rilevanti)} memorie rilevanti:")
                for i, mem in enumerate(memorie_rilevanti, 1):
                    print(f"      {i}. {mem.contenuto[:50]}... (valenza: {mem.valenza_emotiva:+.2f}, accessi: {mem.accessi})")
                print(f"   ✓ Suggerimento: {suggerimenti['suggerimento']}")
                print(f"   ✓ Confidence: {suggerimenti['confidence']:.2f}")
                if suggerimenti['azione_consigliata']:
                    print(f"   ✓ Azione consigliata dalla memoria: {suggerimenti['azione_consigliata']}")
            else:
                print(f"   ℹ️  Nessuna memoria rilevante trovata")
            
            # ========================================
            # 4. EMOZIONE
            # ========================================
            print("\n❤️  [4/7] EMOZIONE: Valutazione...")
            percezioni = [risultato_visivo, risultato_audio]
            risultato_emozione = amigdala.elabora({
                'percezioni': percezioni,
                'memoria': {'suggerimenti': suggerimenti}
            })
            stato_emotivo = risultato_emozione.dati['stato_emotivo']
            valenza = risultato_emozione.dati['valenza']
            print(f"   ✓ Stato: {stato_emotivo.upper()}")
            print(f"   ✓ Valenza: {valenza:+.2f}")
            
            # ========================================
            # 5. RAGIONAMENTO (con influenza memoria)
            # ========================================
            print("\n🧠 [5/7] RAGIONAMENTO: Decisione...")
            decisione = prefrontale.ragiona(
                percezioni_visive=risultato_visivo,
                percezioni_uditive=risultato_audio,
                stato_emotivo=stato_emotivo,
                memoria=[m.contenuto for m in memorie_rilevanti]
            )
            
            # Influenza decisione con suggerimenti memoria
            if suggerimenti['azione_consigliata'] and suggerimenti['confidence'] > 0.7:
                print(f"   💡 Memoria suggerisce: {suggerimenti['azione_consigliata']} (confidence: {suggerimenti['confidence']:.2f})")
                # Sovrascrivi azione se suggerimento molto affidabile
                decisione['azione'] = suggerimenti['azione_consigliata']
                decisione['priorita'] = min(0.95, decisione['priorita'] + suggerimenti['confidence'] * 0.2)
                decisione['fonte_decisione'] = 'memoria_esperienza'
            
            print(f"   ✓ Azione: {decisione['azione'].upper()}")
            print(f"   ✓ Priorità: {decisione['priorita']:.2f}")
            
            # ========================================
            # 6. AZIONE
            # ========================================
            print("\n🦿 [6/7] AZIONE: Esecuzione...")
            successo = motoria.agisci(decisione)
            print(f"   ✓ Risultato: {'✅ SUCCESSO' if successo else '❌ FALLITO'}")
            
            # ========================================
            # 7. APPRENDIMENTO & MEMORIA
            # ========================================
            print("\n💾 [7/7] APPRENDIMENTO: Memorizzazione...")
            
            # Reward
            reward = amigdala.assegna_reward(decisione['azione'], successo, valenza)
            print(f"   ✓ Reward: {reward:+.2f}")
            
            # Memorizza episodio
            ippocampo.memorizza(
                chiave=f"ciclo_{ciclo_num}",
                valore=f"Ciclo {ciclo_num}: {decisione['azione']} - {stato_emotivo}",
                metadata={
                    'valenza': valenza,
                    'importanza': reward / 2.0 + 0.5,
                    'contesto': {'ciclo': ciclo_num, 'successo': successo}
                }
            )
            print(f"   ✓ Episodio salvato")
            
            # ========================================
            # STATISTICHE CICLO
            # ========================================
            print(f"\n{'─'*70}")
            stats_reward = amigdala.get_statistiche_reward()
            stats_memoria = ippocampo.get_statistiche()
            
            print(f"📊 STATISTICHE:")
            print(f"   • Cicli completati: {ciclo_num}")
            print(f"   • Reward totale: {stats_reward['reward_totale']:.2f}")
            print(f"   • Reward medio: {stats_reward['reward_medio']:.2f}")
            print(f"   • Memorie: {stats_memoria['memorie_episodiche']}")
            print(f"{'─'*70}")
            
            # Pausa tra cicli
            if num_cicli == 0 or ciclo_num < num_cicli:
                print(f"\n⏸️  Pausa {delay}s... (CTRL+C per interrompere)")
                time.sleep(delay)
    
    except KeyboardInterrupt:
        print("\n\n⏸️  *** INTERRUZIONE MANUALE ***\n")
    
    # ========================================
    # REPORT FINALE
    # ========================================
    print(f"\n{'='*70}")
    print("📋 REPORT FINALE SESSIONE")
    print(f"{'='*70}")
    print(f"✓ Cicli eseguiti: {ciclo_num}")
    
    stats_reward = amigdala.get_statistiche_reward()
    stats_memoria = ippocampo.get_statistiche()
    
    print(f"\n❤️  REWARD:")
    print(f"   • Totale: {stats_reward['reward_totale']:.2f}")
    print(f"   • Media: {stats_reward['reward_medio']:.2f}")
    print(f"   • Max: {stats_reward.get('reward_max', 0):.2f}")
    print(f"   • Min: {stats_reward.get('reward_min', 0):.2f}")
    
    print(f"\n💾 MEMORIA:")
    print(f"   • Episodi: {stats_memoria['memorie_episodiche']}")
    print(f"   • Memorizzazioni: {stats_memoria['memorizzazioni_totali']}")
    print(f"   • Richiami: {stats_memoria['richiami_totali']}")
    print(f"   • Consolidamenti: {stats_memoria.get('consolidamenti_eseguiti', 0)}")
    print(f"   • Memorie eliminate: {stats_memoria.get('memorie_eliminate', 0)}")
    
    # Salva memoria su disco
    print(f"\n💾 Salvataggio memoria su disco...")
    ippocampo.salva_su_disco()
    print(f"   ✓ Memoria salvata")
    
    print(f"\n{'='*70}")
    print("✅ SESSIONE COMPLETATA")
    print(f"{'='*70}\n")


if __name__ == "__main__":
    print("""
    ================================================================
    
           MENTE ARTIFICIALE - CICLI CONTINUI
           Con Memoria Intelligente e Richiamo Contestuale
           
    ================================================================
    """)
    
    # Menu di scelta
    print("\n[MENU] MODALITA' DISPONIBILI:")
    print("  1. Test veloce (3 cicli, 1s pausa)")
    print("  2. Demo (10 cicli, 2s pausa)")
    print("  3. Esteso (30 cicli, 3s pausa)")
    print("  4. Continuo infinito (CTRL+C per fermare)")
    print("  5. Personalizzato")
    
    try:
        scelta = input("\n>> Scegli modalita (1-5): ").strip()
        
        if scelta == "1":
            ciclo_cognitivo_continuo(num_cicli=3, delay=1.0)
        elif scelta == "2":
            ciclo_cognitivo_continuo(num_cicli=10, delay=2.0)
        elif scelta == "3":
            ciclo_cognitivo_continuo(num_cicli=30, delay=3.0)
        elif scelta == "4":
            ciclo_cognitivo_continuo(num_cicli=0, delay=2.0)
        elif scelta == "5":
            num = int(input("  Numero cicli (0=infinito): "))
            pausa = float(input("  Pausa tra cicli (secondi): "))
            ciclo_cognitivo_continuo(num_cicli=num, delay=pausa)
        else:
            print("❌ Scelta non valida, uso demo (10 cicli)")
            ciclo_cognitivo_continuo(num_cicli=10, delay=2.0)
    
    except ValueError:
        print("❌ Input non valido, uso demo (10 cicli)")
        ciclo_cognitivo_continuo(num_cicli=10, delay=2.0)
    except Exception as e:
        print(f"❌ Errore: {e}")
        sys.exit(1)

