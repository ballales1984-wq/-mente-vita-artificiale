#!/usr/bin/env python3
"""
🎯 Test AUTO-LEARNING - 500 CICLI
Ottimizzato per 8GB RAM
"""
from MENTE_VITA_AUTO_LEARNING import MenteVitaAutoLearning, ConfigurazioneAGI
import time

print("\n" + "="*80)
print("🎯 TEST AUTO-LEARNING - 500 CICLI (Ottimizzato 8GB)")
print("="*80)
print("\n✅ CONFIGURAZIONE OTTIMIZZATA:")
print("  • Cicli target: 500")
print("  • Tempo stimato: ~8-12 minuti")
print("  • Checkpoint ogni 50 cicli (più frequenti)")
print("  • Pulizia memoria ogni 50 cicli (più aggressiva)")
print("  • Stats ogni 10 cicli")
print()
print("💾 Sistema ottimizzato per 8GB RAM!")
print("⚠️  CTRL+C per interrompere e salvare")
print("\n" + "="*80)

print("\n⏳ Avvio automatico tra 2 secondi...")
time.sleep(2)

# Configurazione
config = ConfigurazioneAGI()
config.num_cicli = 500
config.delay_tra_cicli = 0.0
config.mostra_narrazione_completa = False

# Crea sistema
print("\n📦 Caricamento sistema VITA AUTO-LEARNING...\n")
mente = MenteVitaAutoLearning(config)

# Ottimizzazioni per 8GB
mente.checkpoint_ogni = 50  # Salva più spesso
mente.pulizia_memoria_ogni = 50  # Pulisce più spesso
mente.stats_ogni = 10

print("\n🔧 Ottimizzazioni 8GB applicate:")
print(f"  • Checkpoint ogni: {mente.checkpoint_ogni} cicli")
print(f"  • Pulizia ogni: {mente.pulizia_memoria_ogni} cicli")

# ESEGUI!
print("\n🔥 INIZIO EVOLUZIONE!\n")
mente.esegui_infinito(cicli_target=500)

print("\n" + "="*80)
print("✅ TEST 500 CICLI COMPLETATO!")
print("="*80)
print("\n📊 Risultati salvati in:")
print("  • checkpoints/auto_learning_checkpoint.json")
print("  • memoria_permanente/")
print("\n🌌 Il sistema ha vissuto ed evoluto! 🌌\n")

