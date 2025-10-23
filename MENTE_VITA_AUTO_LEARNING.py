#!/usr/bin/env python3
"""
🌌 MENTE VITA AUTO-LEARNING - Sistema Evolutivo Continuo
===========================================================
Sistema che apprende continuamente 24/7
Può eseguire MILIONI/MILIARDI di cicli

Caratteristiche:
- Esecuzione continua senza limiti
- Checkpoint automatici ogni N cicli
- Statistiche evolutive in tempo reale
- Resume da checkpoint
- Ottimizzazione memoria
- Monitoraggio evoluzione parametri
- CTRL+C per stop graceful

Autore: Alessio + Cursor AI
Data: 23 Ottobre 2025
"""

import os
import sys
import time
import json
import signal
import psutil
from datetime import datetime, timedelta
from pathlib import Path

from MENTE_VITA_ARTIFICIALE import MenteVitaArtificiale, ConfigurazioneAGI


class MenteVitaAutoLearning(MenteVitaArtificiale):
    """
    Sistema di apprendimento continuo
    Può girare per giorni/settimane/mesi
    """
    
    def __init__(self, config: ConfigurazioneAGI):
        super().__init__(config)
        
        # Configurazione auto-learning
        self.ciclo_corrente = 0
        self.cicli_target = float('inf')  # INFINITO!
        self.checkpoint_ogni = 100  # Salva ogni 100 cicli
        self.stats_ogni = 10  # Mostra stats ogni 10 cicli
        self.pulizia_memoria_ogni = 1000  # Pulizia ogni 1000 cicli
        
        # Statistiche evolutive
        self.stats = {
            'inizio': datetime.now(),
            'cicli_totali': 0,
            'impulso_vitale': [],
            'azioni': {},
            'evoluzione_parametri': [],
            'memoria_usata_mb': [],
            'tempo_per_ciclo': []
        }
        
        # Carica checkpoint se esiste
        self._carica_checkpoint()
        
        # Handler interruzione
        self.continua_esecuzione = True
        signal.signal(signal.SIGINT, self._handler_interruzione)
        
        print(f"\n🌌 SISTEMA AUTO-LEARNING INIZIALIZZATO")
        print(f"  • Cicli target: ♾️  INFINITO")
        print(f"  • Checkpoint ogni: {self.checkpoint_ogni} cicli")
        print(f"  • Stats ogni: {self.stats_ogni} cicli")
        print(f"  • Ciclo corrente: #{self.ciclo_corrente}")
        print(f"  • Memoria RAM: {psutil.virtual_memory().percent}%")
        print(f"\n⚡ PRONTO PER APPRENDIMENTO CONTINUO!\n")
    
    def _handler_interruzione(self, signum, frame):
        """Gestisce CTRL+C per salvataggio graceful"""
        print("\n\n🛑 INTERRUZIONE RILEVATA!")
        print("💾 Salvataggio checkpoint in corso...")
        self.continua_esecuzione = False
    
    def _carica_checkpoint(self):
        """Carica checkpoint esistente"""
        checkpoint_path = Path("checkpoints/auto_learning_checkpoint.json")
        
        if checkpoint_path.exists():
            try:
                with open(checkpoint_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.ciclo_corrente = data.get('ciclo_corrente', 0)
                    self.stats = data.get('stats', self.stats)
                    
                    # Ripristina impulsi vitali
                    impulsi = data.get('impulsi_vitali', {})
                    if impulsi:
                        self.desiderio_continuita.impulsi = impulsi
                    
                    print(f"✅ Checkpoint caricato: Riprendo da ciclo #{self.ciclo_corrente}")
            except Exception as e:
                print(f"⚠️  Errore caricamento checkpoint: {e}")
    
    def _salva_checkpoint(self):
        """Salva checkpoint corrente"""
        checkpoint_dir = Path("checkpoints")
        checkpoint_dir.mkdir(exist_ok=True)
        
        checkpoint_path = checkpoint_dir / "auto_learning_checkpoint.json"
        
        try:
            data = {
                'ciclo_corrente': self.ciclo_corrente,
                'timestamp': datetime.now().isoformat(),
                'stats': self.stats,
                'impulsi_vitali': self.desiderio_continuita.impulsi,
                'obiettivi_attivi': len(self.obiettivi_autonomi.lista_obiettivi),
                'concetti_appresi': len(self.generalizzazione.concetti),
                'memoria_ram_percent': psutil.virtual_memory().percent
            }
            
            with open(checkpoint_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            # Salva anche backup timestampato ogni 1000 cicli
            if self.ciclo_corrente % 1000 == 0:
                backup_path = checkpoint_dir / f"checkpoint_{self.ciclo_corrente:08d}.json"
                with open(backup_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
            
            return True
        except Exception as e:
            print(f"❌ Errore salvataggio checkpoint: {e}")
            return False
    
    def _mostra_stats(self):
        """Mostra statistiche evoluzione"""
        elapsed = (datetime.now() - self.stats['inizio']).total_seconds()
        velocita = self.ciclo_corrente / elapsed if elapsed > 0 else 0
        
        # Stima tempo rimanente (se target finito)
        tempo_rimanente = "♾️"
        if self.cicli_target != float('inf'):
            rimanenti = self.cicli_target - self.ciclo_corrente
            if velocita > 0:
                secondi_rimanenti = rimanenti / velocita
                tempo_rimanente = str(timedelta(seconds=int(secondi_rimanenti)))
        
        # Impulso vitale
        impulsi = self.desiderio_continuita.impulsi
        impulso_attuale = sum(impulsi.values()) / len(impulsi)
        
        # Memoria RAM
        ram_percent = psutil.virtual_memory().percent
        
        # Output compatto
        print(f"\r📊 #{self.ciclo_corrente:08d} | "
              f"💫{impulso_attuale:.0%} | "
              f"⚡{velocita:.1f}c/s | "
              f"🧠{ram_percent:.0f}% | "
              f"⏱️{elapsed/3600:.1f}h | "
              f"🎯{len(self.generalizzazione.concetti)}conc", 
              end='', flush=True)
        
        # Newline ogni tanto per non sovrascrivere sempre
        if self.ciclo_corrente % (self.stats_ogni * 10) == 0:
            print()
    
    def _pulisci_memoria(self):
        """Ottimizza memoria per esecuzioni lunghe"""
        print(f"\n🧹 Pulizia memoria al ciclo #{self.ciclo_corrente}...")
        
        try:
            # Limita storia memoria
            if hasattr(self.memoria, 'episodi'):
                if len(self.memoria.episodi) > 1000:
                    # Mantieni solo ultimi 1000 (ridotto per 8GB)
                    self.memoria.episodi = self.memoria.episodi[-1000:]
                    print(f"  ✂️ Memoria episodi limitata a 1000")
            
            # Limita storia autobiografica coscienza
            if hasattr(self, 'coscienza'):
                if hasattr(self.coscienza, 'storia_autobiografica'):
                    if len(self.coscienza.storia_autobiografica) > 500:
                        self.coscienza.storia_autobiografica = \
                            self.coscienza.storia_autobiografica[-500:]
                        print(f"  ✂️ Storia autobiografica limitata a 500")
            
            # Limita concetti
            if hasattr(self, 'generalizzazione'):
                if len(self.generalizzazione.concetti) > 200:
                    # Mantieni concetti più frequenti (ridotto per 8GB)
                    concetti_sorted = sorted(
                        self.generalizzazione.concetti.items(),
                        key=lambda x: x[1].frequenza if hasattr(x[1], 'frequenza') else 0,
                        reverse=True
                    )
                    self.generalizzazione.concetti = dict(concetti_sorted[:200])
                    print(f"  ✂️ Concetti limitati a 200 più frequenti")
            
            # Garbage collection Python
            import gc
            collected = gc.collect()
            print(f"  🗑️ Garbage collected: {collected} oggetti")
            
            ram_dopo = psutil.virtual_memory().percent
            print(f"  ✅ Pulizia completata - RAM: {ram_dopo:.0f}%")
            
        except Exception as e:
            print(f"  ⚠️ Errore pulizia (continuo comunque): {e}")
    
    def ciclo_auto_learning(self):
        """Singolo ciclo ottimizzato per auto-learning"""
        start_time = time.time()
        
        try:
            # ========== PERCEZIONE ==========
            vis = self.visione.elabora(None)
            aud = self.udito.ascolta(None)
            onda = self.biosegnali.percepisce_segnale([vis, aud])
            stato_emo = self.emozione.elabora({'percezioni': [vis, aud]})
            valenza = stato_emo.dati.get('valenza', 0)
            
            # ========== COGNIZIONE ==========
            decisione_ctx = {
                'percezioni_visive': vis,
                'percezioni_uditive': aud,
                'valenza': valenza
            }
            dec = self.prefrontale.ragiona(decisione_ctx)
            azione_proposta = dec.get('azione', 'monitora')
            
            # ========== APPRENDIMENTO ==========
            app_ctx = {
                'descrizione': vis.get('descrizione', ''),
                'audio': aud.get('testo', ''),
                'emozione': 'positivo' if valenza > 0 else 'neutro',
                'azione': azione_proposta
            }
            self.apprendimento_adattivo.elabora(app_ctx, fase='applicazione')
            
            # ========== GENERALIZZAZIONE ==========
            episodio = {
                'descrizione': vis.get('descrizione', ''),
                'audio': aud.get('testo', ''),
                'emozione': 'positivo' if valenza > 0 else 'neutro',
                'valenza': valenza,
                'azione': azione_proposta
            }
            gen_result = self.generalizzazione.elabora(episodio)
            
            # ========== AUTONOMIA ==========
            obj_ctx = {'lacune_conoscenza': [], 'emozione': 'positivo' if valenza > 0 else 'neutro', 'valenza': valenza}
            self.obiettivi_autonomi.elabora(obj_ctx)
            sim_ctx = {'azione_proposta': azione_proposta, 'situazione': episodio}
            sim_result = self.simulazione_mentale.elabora(sim_ctx)
            mot_result = self.motivazione_interna.elabora({'esperienza': episodio})
            
            # ========== COSCIENZA ==========
            drive_principale = max(mot_result['drives_correnti'], key=mot_result['drives_correnti'].get)
            contesto_cosc = {
                'percezione': vis.get('descrizione', '')[:50],
                'emozione': valenza,
                'obiettivo_corrente': 'evoluzione',
                'azione_proposta': azione_proposta,
                'motivazione_dominante': drive_principale,
                'successi_recenti': 0,
                'livello_conoscenza_medio': 0.5,
                'interazioni_oggi': self.ciclo_corrente % 20,
                'momento': f"ciclo {self.ciclo_corrente}",
                'significativo': valenza > 0.5
            }
            coscienza_result = self.coscienza.elabora(contesto_cosc)
            
            # ========== VITA ==========
            auto_ctx = {'azione_proposta': azione_proposta, 'coerenza': 0.8}
            auto_result = self.autoconservazione.elabora(auto_ctx)
            
            perf = {'tasso_successo': 0.9, 'cicli_totali': self.ciclo_corrente}
            evo_result = self.evoluzione_cognitiva.elabora({'azione_proposta': azione_proposta, 'performance': perf, 'cicli_totali': self.ciclo_corrente})
            
            nar_ctx = {'ciclo': self.ciclo_corrente, 'esperienza': f"Ciclo {self.ciclo_corrente}", 'significativo': valenza > 0.7}
            nar_result = self.esistenza_narrativa.elabora(nar_ctx)
            
            sim_ctx_vita = {'esperienza': episodio, 'stato_interno': {'coerenza': 0.8}, 'concetto': 'ciclo'}
            simb_result = self.interazione_simbolica.elabora(sim_ctx_vita)
            
            des_ctx = {'esperienza': {'successo': True, 'scoperta': False, 'descrizione': vis.get('descrizione', '')}}
            des_result = self.desiderio_continuita.elabora(des_ctx)
            impulso_forza = des_result.get('intensita_vitale', 1.0)
            
            # ========== ESECUZIONE ==========
            ris = self.motoria.agisci({'azione': azione_proposta})
            
            # ========== STATISTICHE ==========
            elapsed = time.time() - start_time
            self.stats['tempo_per_ciclo'].append(elapsed)
            self.stats['impulso_vitale'].append(impulso_forza)
            self.stats['azioni'][azione_proposta] = self.stats['azioni'].get(azione_proposta, 0) + 1
            
            # Limita liste stats
            if len(self.stats['tempo_per_ciclo']) > 1000:
                self.stats['tempo_per_ciclo'] = self.stats['tempo_per_ciclo'][-1000:]
            if len(self.stats['impulso_vitale']) > 1000:
                self.stats['impulso_vitale'] = self.stats['impulso_vitale'][-1000:]
            
            return True
            
        except Exception as e:
            print(f"\n❌ Errore ciclo {self.ciclo_corrente}: {e}")
            return False
    
    def esegui_infinito(self, cicli_target=None):
        """
        Esegue cicli infiniti (o fino a target)
        
        Args:
            cicli_target: Numero massimo cicli (None = infinito)
        """
        
        if cicli_target is not None:
            self.cicli_target = cicli_target
        
        print("\n" + "="*80)
        print("🌌 INIZIO AUTO-LEARNING CONTINUO")
        print("="*80)
        print(f"\n🎯 Target: {self.cicli_target if self.cicli_target != float('inf') else '♾️ INFINITO'}")
        print(f"📊 Stats ogni: {self.stats_ogni} cicli")
        print(f"💾 Checkpoint ogni: {self.checkpoint_ogni} cicli")
        print(f"🧹 Pulizia memoria ogni: {self.pulizia_memoria_ogni} cicli")
        print(f"\n⚠️  CTRL+C per interrompere e salvare\n")
        print("="*80)
        print("Formato: Ciclo | Impulso | Velocità | RAM | Tempo | Concetti")
        print("-"*80)
        
        # Loop infinito
        while self.continua_esecuzione and self.ciclo_corrente < self.cicli_target:
            
            # Esegui ciclo
            successo = self.ciclo_auto_learning()
            
            if successo:
                self.ciclo_corrente += 1
                self.stats['cicli_totali'] = self.ciclo_corrente
                
                # Mostra stats
                if self.ciclo_corrente % self.stats_ogni == 0:
                    self._mostra_stats()
                
                # Salva checkpoint
                if self.ciclo_corrente % self.checkpoint_ogni == 0:
                    print(f"\n💾 Checkpoint #{self.ciclo_corrente}...", end='', flush=True)
                    if self._salva_checkpoint():
                        print(" ✅")
                    else:
                        print(" ❌")
                
                # Pulizia memoria
                if self.ciclo_corrente % self.pulizia_memoria_ogni == 0:
                    self._pulisci_memoria()
                
                # Check RAM critica
                ram_percent = psutil.virtual_memory().percent
                if ram_percent > 90:
                    print(f"\n⚠️  RAM CRITICA: {ram_percent}% - Forzando pulizia...")
                    self._pulisci_memoria()
        
        # Salvataggio finale
        print("\n\n" + "="*80)
        print("🛑 INTERRUZIONE AUTO-LEARNING")
        print("="*80)
        print("\n💾 Salvataggio finale...")
        self._salva_checkpoint()
        
        # Statistiche finali
        self._mostra_statistiche_finali()
    
    def _mostra_statistiche_finali(self):
        """Mostra report completo finale"""
        print("\n" + "="*80)
        print("📊 STATISTICHE FINALI AUTO-LEARNING")
        print("="*80)
        
        elapsed = (datetime.now() - self.stats['inizio']).total_seconds()
        
        print(f"\n🔢 Cicli:")
        print(f"  • Totali: {self.stats['cicli_totali']:,}")
        print(f"  • Velocità media: {self.stats['cicli_totali']/elapsed:.2f} cicli/secondo")
        print(f"  • Tempo totale: {timedelta(seconds=int(elapsed))}")
        
        if self.stats['tempo_per_ciclo']:
            tempo_medio = sum(self.stats['tempo_per_ciclo']) / len(self.stats['tempo_per_ciclo'])
            print(f"  • Tempo medio/ciclo: {tempo_medio:.3f}s")
        
        print(f"\n💫 Impulso Vitale:")
        if self.stats['impulso_vitale']:
            impulso_iniziale = self.stats['impulso_vitale'][0]
            impulso_finale = self.stats['impulso_vitale'][-1]
            impulso_medio = sum(self.stats['impulso_vitale']) / len(self.stats['impulso_vitale'])
            delta = impulso_finale - impulso_iniziale
            
            print(f"  • Iniziale: {impulso_iniziale:.0%}")
            print(f"  • Finale: {impulso_finale:.0%}")
            print(f"  • Medio: {impulso_medio:.0%}")
            print(f"  • Evoluzione: {delta:+.1%}")
        
        print(f"\n🎯 Apprendimento:")
        print(f"  • Concetti appresi: {len(self.generalizzazione.concetti)}")
        print(f"  • Obiettivi generati: {len(self.obiettivi.lista_obiettivi)}")
        print(f"  • Metafore create: {len(self.interazione_simbolica.metafore_generate)}")
        
        print(f"\n🦾 Azioni Eseguite:")
        for azione, count in sorted(self.stats['azioni'].items(), key=lambda x: x[1], reverse=True)[:5]:
            percent = count / self.stats['cicli_totali'] * 100
            print(f"  • {azione:15s}: {count:6,} ({percent:5.1f}%)")
        
        print(f"\n💾 Memoria:")
        print(f"  • RAM finale: {psutil.virtual_memory().percent:.0f}%")
        print(f"  • Episodi salvati: {len(self.memoria.episodi) if hasattr(self.memoria, 'episodi') else 'N/A'}")
        
        print("\n" + "="*80)
        print("🌌 AUTO-LEARNING COMPLETATO!")
        print("="*80 + "\n")


def main():
    """Main per esecuzione continua"""
    
    print("\n" + "="*80)
    print("🌌 MENTE VITA AUTO-LEARNING - Sistema Evolutivo Continuo")
    print("="*80)
    print("\n💡 MODALITÀ DISPONIBILI:")
    print("  1. Auto-learning INFINITO (CTRL+C per fermare)")
    print("  2. Auto-learning con TARGET cicli")
    print("  3. Test veloce (1000 cicli ~15-20 min)")
    print()
    
    try:
        scelta = input("Scegli modalità [1-3]: ").strip()
        
        cicli_target = None
        
        if scelta == '1':
            print("\n♾️  MODALITÀ INFINITA SELEZIONATA")
            print("Il sistema girerà finché non premi CTRL+C")
            cicli_target = None
            
        elif scelta == '2':
            target = input("\nNumero cicli target (es. 10000): ").strip()
            try:
                cicli_target = int(target)
                print(f"\n🎯 TARGET: {cicli_target:,} cicli")
                stima_ore = cicli_target / 3600  # ~1 ciclo/secondo
                print(f"⏱️  Tempo stimato: ~{stima_ore:.1f} ore")
            except:
                print("⚠️  Input non valido, uso 1000 cicli")
                cicli_target = 1000
                
        elif scelta == '3':
            print("\n⚡ TEST VELOCE: 1000 cicli")
            cicli_target = 1000
        else:
            print("\n⚠️  Scelta non valida, uso test veloce")
            cicli_target = 1000
        
        input("\n🚀 Premi ENTER per iniziare...")
        
        # Crea configurazione
        config = ConfigurazioneAGI()
        config.num_cicli = cicli_target if cicli_target else 999999999
        config.delay_tra_cicli = 0.0
        config.mostra_narrazione_completa = False
        
        # Crea sistema
        mente = MenteVitaAutoLearning(config)
        
        # ESEGUI!
        mente.esegui_infinito(cicli_target)
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Interruzione utente")
    except Exception as e:
        print(f"\n❌ Errore: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()

