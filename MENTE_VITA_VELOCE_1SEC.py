#!/usr/bin/env python3
"""
🚀 MENTE VITA VELOCE - Ciclo 1 Secondo
=====================================================
Sistema ottimizzato per esecuzione veloce
Ciclo completo in ~1 secondo

Autore: Alessio + Cursor AI
Data: 23 Ottobre 2025
"""

import os
import sys
import time
import json
from datetime import datetime
from pathlib import Path

# Importa sistema base
from MENTE_VITA_ARTIFICIALE import MenteVitaArtificiale, ConfigurazioneAGI


class MenteVitaVeloce(MenteVitaArtificiale):
    """
    Versione ottimizzata per velocità
    Ciclo completo in ~1 secondo
    """
    
    def __init__(self, config: ConfigurazioneAGI):
        super().__init__(config)
        
        # Ottimizzazioni velocità
        self.modalita_veloce = True
        self.salva_ogni_n_cicli = 10  # Salva ogni 10 cicli invece che ogni volta
        self.mostra_output_ridotto = True
        
        print(f"\n⚡ MODALITÀ VELOCE ATTIVATA!")
        print(f"  • Ciclo target: ~1 secondo")
        print(f"  • Salvataggio ogni {self.salva_ogni_n_cicli} cicli")
        print(f"  • Output ottimizzato\n")
    
    def ciclo_agi_completo(self, num_ciclo):
        """Ciclo ottimizzato per velocità"""
        
        start_time = time.time()
        
        # Output ridotto
        if self.mostra_output_ridotto:
            print(f"⚡ Ciclo #{num_ciclo:04d} ", end='', flush=True)
        else:
            super().ciclo_agi_completo(num_ciclo)
            return
        
        try:
            # ========== FASI 1-6 (ereditate ma ottimizzate) ==========
            # Percezione
            vis = self.visione.elabora(None)
            aud = self.udito.ascolta(None)
            onda = self.biosegnali.percepisce_segnale([vis, aud])
            stato_emo = self.emozione.elabora({'percezioni': [vis, aud]})
            valenza = stato_emo.dati.get('valenza', 0)
            
            # Cognizione
            decisione_ctx = {
                'percezioni_visive': vis, 
                'percezioni_uditive': aud, 
                'valenza': valenza
            }
            dec = self.prefrontale.ragiona(decisione_ctx)
            azione_proposta = dec.get('azione', 'monitora')
            
            # Apprendimento
            app_ctx = {
                'descrizione': vis.get('descrizione', ''),
                'audio': aud.get('testo', ''),
                'emozione': 'positivo' if valenza > 0 else 'neutro',
                'azione': azione_proposta
            }
            self.apprendimento_adattivo.elabora(app_ctx, fase='applicazione')
            
            # Generalizzazione
            episodio = {
                'descrizione': vis.get('descrizione', ''),
                'audio': aud.get('testo', ''),
                'emozione': 'positivo' if valenza > 0 else 'neutro',
                'valenza': valenza,
                'azione': azione_proposta
            }
            gen_result = self.generalizzazione.elabora(episodio)
            
            # Autonomia
            obj_ctx = {'lacune_conoscenza': [], 'emozione': 'positivo' if valenza > 0 else 'neutro', 'valenza': valenza}
            self.obiettivi_autonomi.elabora(obj_ctx)
            sim_ctx = {'azione_proposta': azione_proposta, 'situazione': episodio}
            sim_result = self.simulazione_mentale.elabora(sim_ctx)
            mot_result = self.motivazione_interna.elabora({'esperienza': episodio})
            drive_principale = max(mot_result['drives_correnti'], key=mot_result['drives_correnti'].get)
            
            # Coscienza
            contesto_cosc = {
                'percezione': vis.get('descrizione', '')[:50],
                'emozione': valenza,
                'obiettivo_corrente': 'evoluzione',
                'azione_proposta': azione_proposta,
                'motivazione_dominante': drive_principale,
                'successi_recenti': 0,
                'livello_conoscenza_medio': 0.5,
                'interazioni_oggi': num_ciclo % 20,
                'momento': f"ciclo {num_ciclo}",
                'significativo': valenza > 0.5
            }
            coscienza_result = self.coscienza.elabora(contesto_cosc)
            
            # FASE 7: VITA EMERGENTE (ottimizzato)
            auto_ctx = {'azione_proposta': azione_proposta, 'coerenza': 0.8}
            auto_result = self.autoconservazione.elabora(auto_ctx)
            
            perf = {'tasso_successo': 0.9, 'cicli_totali': num_ciclo}
            evo_result = self.evoluzione_cognitiva.elabora({'azione_proposta': azione_proposta, 'performance': perf, 'cicli_totali': num_ciclo})
            
            nar_ctx = {'ciclo': num_ciclo, 'esperienza': f"Ciclo {num_ciclo}", 'significativo': valenza > 0.7}
            nar_result = self.esistenza_narrativa.elabora(nar_ctx)
            
            sim_ctx_vita = {'esperienza': episodio, 'stato_interno': {'coerenza': 0.8}, 'concetto': 'ciclo'}
            simb_result = self.interazione_simbolica.elabora(sim_ctx_vita)
            
            des_ctx = {'esperienza': {'successo': True, 'scoperta': False, 'descrizione': vis.get('descrizione', '')}}
            des_result = self.desiderio_continuita.elabora(des_ctx)
            impulso_forza = des_result.get('intensita_vitale', 1.0)
            
            # Esecuzione
            ris = self.motoria.agisci({'azione': azione_proposta})
            
            # Salvataggio memoria (ogni N cicli)
            if num_ciclo % self.salva_ogni_n_cicli == 0:
                memoria_id = self.memoria.salva({
                    'ciclo': num_ciclo,
                    'percezione': vis,
                    'emozione': valenza,
                    'azione': azione_proposta,
                    'risultato': ris
                })
                print(f"💾 ", end='', flush=True)
            
            # Output risultato
            elapsed = time.time() - start_time
            print(f"| {azione_proposta[:8]:8s} | 💫{impulso_forza:.0%} | ⏱️{elapsed:.2f}s")
            
        except Exception as e:
            print(f"❌ Errore: {e}")


def esegui_test_veloce(num_cicli=10):
    """Test veloce con N cicli"""
    
    print("\n" + "="*70)
    print("⚡ MENTE VITA VELOCE - Test 1 Secondo/Ciclo")
    print("="*70)
    
    config = ConfigurazioneAGI()
    config.num_cicli = num_cicli
    config.delay_tra_cicli = 0.0  # Nessun delay!
    config.mostra_narrazione_completa = False
    
    print(f"\n🎯 Configurazione:")
    print(f"  • Cicli: {num_cicli}")
    print(f"  • Target: ~1 secondo/ciclo")
    print(f"  • Delay: 0ms")
    print(f"  • Tempo stimato: ~{num_cicli} secondi\n")
    
    mente_veloce = MenteVitaVeloce(config)
    
    print("\n" + "="*70)
    print("🚀 INIZIO ESECUZIONE")
    print("="*70)
    print("Formato: Ciclo | Azione | Impulso | Tempo")
    print("-"*70)
    
    start_totale = time.time()
    mente_veloce.esegui_sessione()
    elapsed_totale = time.time() - start_totale
    
    print("-"*70)
    print(f"\n✅ Completati {num_cicli} cicli in {elapsed_totale:.1f}s")
    print(f"⚡ Velocità media: {elapsed_totale/num_cicli:.2f}s/ciclo")
    
    # Calcola impulso medio
    impulsi = mente_veloce.desiderio_continuita.impulsi
    impulso_medio = sum(impulsi.values()) / len(impulsi)
    print(f"💫 Impulso vitale finale: {impulso_medio:.0%}")
    
    print("\n" + "="*70)
    print("🌌 TEST VELOCE COMPLETATO!")
    print("="*70 + "\n")


if __name__ == "__main__":
    import sys
    
    # Prendi numero cicli da argomento
    num_cicli = 10
    if len(sys.argv) > 1:
        try:
            num_cicli = int(sys.argv[1])
        except:
            print("⚠️  Uso: python MENTE_VITA_VELOCE_1SEC.py [num_cicli]")
            print("    Esempio: python MENTE_VITA_VELOCE_1SEC.py 20")
            num_cicli = 10
    
    esegui_test_veloce(num_cicli)

