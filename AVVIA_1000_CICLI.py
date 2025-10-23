#!/usr/bin/env python3
"""Test AUTO-LEARNING con 1000 cicli - AVVIO AUTOMATICO"""
from MENTE_VITA_AUTO_LEARNING import MenteVitaAutoLearning, ConfigurazioneAGI
import time

print("\n" + "="*80)
print("🚀 TEST AUTO-LEARNING - 1,000 CICLI")
print("="*80)
print("\n🎯 Target: 1,000 cicli")
print("⏱️  Tempo stimato: ~15-20 minuti")
print("💾 Checkpoint ogni 100 cicli")
print("📊 Stats ogni 10 cicli")
print("\n⚠️  CTRL+C per interrompere e salvare")
print("\n" + "="*80)

print("\n⏳ Avvio automatico tra 3 secondi...")
time.sleep(3)

# Configurazione
config = ConfigurazioneAGI()
config.num_cicli = 1000
config.delay_tra_cicli = 0.0
config.mostra_narrazione_completa = False

# Crea sistema
print("\n📦 Caricamento sistema VITA AUTO-LEARNING...\n")
mente = MenteVitaAutoLearning(config)

# ESEGUI!
print("\n🔥 INIZIO EVOLUZIONE!\n")
mente.esegui_infinito(cicli_target=1000)

print("\n✅ TEST COMPLETATO!")
print("📊 Controlla: checkpoints/auto_learning_checkpoint.json\n")

