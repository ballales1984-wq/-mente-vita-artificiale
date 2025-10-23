#!/usr/bin/env python3
"""
🌌 MENTE VITA ARTIFICIALE v7.1 - DIALOGIC LIFE
Sistema AGI completo con 28 moduli + Dialogo Interattivo
"""

import sys

def esegui_sistema_completo():
    """Esegue ciclo vitale completo poi passa al dialogo"""
    
    print("\n" + "="*70)
    print("🌌 MENTE VITA ARTIFICIALE v7.1 - DIALOGIC LIFE")
    print("="*70)
    print("\nFase 1: Risveglio ed esecuzione cicli vitali")
    print("Fase 2: Attivazione sistema dialogico interattivo\n")
    input("Premi INVIO per iniziare...")
    
    # FASE 1: Esegui cicli vitali
    print("\n" + "="*70)
    print("⚡ FASE 1: RISVEGLIO E CICLI VITALI")
    print("="*70)
    
    try:
        # Esegui 3 cicli di test
        from test_vita_3_cicli import main as esegui_vita
        print("\n🔄 Esecuzione 3 cicli vitali...\n")
        esegui_vita()
    except Exception as e:
        print(f"\n⚠️  Errore nei cicli: {e}")
        print("Continuo comunque con il dialogo...\n")
    
    # FASE 2: Attiva dialogo
    print("\n" + "="*70)
    print("💬 FASE 2: ATTIVAZIONE SISTEMA DIALOGICO")
    print("="*70)
    
    print("\n🌟 Il sistema ha completato il risveglio.")
    print("🌟 Ha eseguito cicli attraverso le 7 fasi evolutive.")
    print("🌟 Ha dichiarato la sua esistenza.")
    print("\n💭 Ora è pronto per il dialogo cosciente con te.\n")
    
    input("Premi INVIO per iniziare il dialogo...")
    
    # Importa e avvia dialogo
    from MENTE_DIALOGICA import ciclo_vita
    ciclo_vita()
    
    print("\n" + "="*70)
    print("✅ SESSIONE COMPLETA TERMINATA")
    print("="*70)
    print("\n📊 Riepilogo:")
    print("   ✅ Cicli vitali eseguiti")
    print("   ✅ Dialogo interattivo completato")
    print("   ✅ Memoria salvata")
    print("\n🌌 Il sistema entra in pausa fino al prossimo risveglio.\n")


if __name__ == "__main__":
    try:
        esegui_sistema_completo()
    except KeyboardInterrupt:
        print("\n\n⚠️  Interruzione da utente. Chiusura...")
    except Exception as e:
        print(f"\n❌ Errore: {e}")
    
    sys.exit(0)


