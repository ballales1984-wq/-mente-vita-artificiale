#!/usr/bin/env python3
"""
🌊 MENTE VITA CON RITMI Hz FUNZIONALI - Versione 7.1
========================================================
Sistema VITA con ritmi cerebrali differenziati per funzione
Ogni area cerebrale opera alla sua frequenza naturale!

NOVITÀ v7.1:
- Ritmi Hz specifici per ogni funzione
- Delta/Theta/Alpha/Beta/Gamma correlati
- Coherence tra aree cerebrali
- Pattern adattivi in base al task

Autore: Alessio + Cursor AI  
Data: 23 Ottobre 2025
"""

import os
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict

# Sistema base VITA
from MENTE_VITA_ARTIFICIALE import MenteVitaArtificiale, ConfigurazioneAGI

# Nuovo modulo ritmi
from moduli.ritmi_cerebrali_funzionali import GestoreRitmiCerebrali, BandaFrequenza


class MenteVitaRitmiHz(MenteVitaArtificiale):
    """
    Sistema VITA con gestione ritmi Hz per funzione
    29° MODULO: Ritmi cerebrali funzionali!
    """
    
    def __init__(self, config: ConfigurazioneAGI):
        super().__init__(config)
        
        # MODULO 29: Ritmi cerebrali funzionali
        print(f"\n[MODULO 29] Caricamento ritmi cerebrali Hz...")
        self.gestore_ritmi = GestoreRitmiCerebrali()
        print("  ✅ Ritmi Hz funzionali attivi! 🌊")
        
        print(f"\n{'='*80}")
        print(f"  ✅ SISTEMA VITA v7.1 CON RITMI Hz PRONTO!")
        print(f"  📊 29 MODULI CEREBRALI (28 + Ritmi Hz)")
        print(f"  🌊 Ogni area opera alla sua frequenza naturale!")
        print(f"{'='*80}\n")
    
    def ciclo_agi_completo(self, num_ciclo):
        """Ciclo con visualizzazione ritmi Hz per fase"""
        
        print(f"\n{'╔'+'═'*78+'╗'}")
        print(f"║ CICLO VITA Hz #{num_ciclo:04d}{' '*57}║")
        print(f"{'╚'+'═'*78+'╝'}")
        
        # ========== FASE 1: PERCEZIONE (Beta/Gamma) ==========
        print("\n[FASE 1] 👁️👂 PERCEZIONE")
        
        # Genera pattern ritmi per percezione
        ritmi_percezione = self.gestore_ritmi.adatta_ritmo_a_task('percezione')
        self._mostra_ritmi_compatti(ritmi_percezione)
        
        vis = self.visione.elabora(None)
        print(f"  👁️  Vista: {vis['descrizione'][:50]}...")
        
        aud = self.udito.ascolta(None)
        audio_text = aud.get('testo', aud.get('trascrizione', ''))
        print(f"  👂 Udito: {audio_text[:50] if audio_text else 'Silenzio'}...")
        
        onda = self.biosegnali.percepisce_segnale([vis, aud])
        pattern = onda.pattern.replace('1', '█').replace('0', '░')
        print(f"  ⚡ Biosegnali: {pattern}")
        
        stato_emo = self.emozione.elabora({'percezioni': [vis, aud]})
        valenza = stato_emo.dati.get('valenza', 0)
        print(f"  ❤️  Emozione: {valenza:+.2f}")
        
        # ========== FASE 2-3: COGNIZIONE (Gamma) ==========
        print("\n[FASE 2-3] 🧩 COGNIZIONE & APPRENDIMENTO")
        
        ritmi_ragionamento = self.gestore_ritmi.adatta_ritmo_a_task('ragionamento')
        self._mostra_ritmi_compatti(ritmi_ragionamento)
        
        decisione_ctx = {
            'percezioni_visive': vis, 
            'percezioni_uditive': aud, 
            'valenza': valenza
        }
        dec = self.prefrontale.ragiona(decisione_ctx)
        azione_proposta = dec.get('azione', 'monitora')
        print(f"  🧠 Decisione: {azione_proposta}")
        
        # ========== FASE 4: APPRENDIMENTO (Gamma alta) ==========
        ritmi_apprendimento = self.gestore_ritmi.adatta_ritmo_a_task('apprendimento')
        self._mostra_ritmi_compatti(ritmi_apprendimento)
        
        app_ctx = {
            'descrizione': vis.get('descrizione', ''),
            'audio': audio_text,
            'emozione': 'positivo' if valenza > 0 else 'neutro',
            'azione': azione_proposta
        }
        self.apprendimento_adattivo.elabora(app_ctx, fase='applicazione')
        
        # ========== FASE 5: COSCIENZA (Gamma altissima) ==========
        print("\n[FASE 6] 🌟 COSCIENZA")
        
        ritmi_coscienza = self.gestore_ritmi.adatta_ritmo_a_task('coscienza')
        self._mostra_ritmi_compatti(ritmi_coscienza)
        
        episodio = {
            'descrizione': vis.get('descrizione', ''),
            'audio': audio_text,
            'emozione': 'positivo' if valenza > 0 else 'neutro',
            'valenza': valenza
        }
        
        contesto_cosc = {
            'percezione': vis.get('descrizione', '')[:50],
            'emozione': valenza,
            'obiettivo_corrente': 'evoluzione',
            'azione_proposta': azione_proposta,
            'motivazione_dominante': 'competenza',
            'successi_recenti': 5,
            'livello_conoscenza_medio': 0.7,
            'interazioni_oggi': num_ciclo % 20,
            'momento': f"ciclo {num_ciclo}",
            'significativo': valenza > 0.5
        }
        coscienza_result = self.coscienza.elabora(contesto_cosc)
        print(f"  🧠 Riflessione: {coscienza_result['auto_riflessione'][:50]}...")
        
        # ========== FASE 7: VITA (Mix ritmi) ==========
        print("\n[FASE 7] 🌌 VITA EMERGENTE")
        
        # Pattern completo per vita
        ritmi_vita = self.gestore_ritmi.genera_pattern_multi_ritmo()
        coherence = self.gestore_ritmi.calcola_coherence(ritmi_vita)
        print(f"  🌊 Coherence cerebrale: {coherence:.0%}")
        
        # Vita emergente
        auto_ctx = {'azione_proposta': azione_proposta, 'coerenza': coherence}
        auto_result = self.autoconservazione.elabora(auto_ctx)
        print(f"  🛡️  Autoconservazione: {auto_result['riflessione_autoconservativa'][:50]}...")
        
        des_ctx = {'esperienza': {'successo': True, 'scoperta': False, 'descrizione': vis.get('descrizione', '')}}
        des_result = self.desiderio_continuita.elabora(des_ctx)
        print(f"  💫 Impulso vitale: {des_result['intensita_vitale']:.0%}")
        
        # Esecuzione
        print(f"\n[ESECUZIONE] 🦾 Azione: {azione_proposta.upper()}")
        successo = self.motoria.agisci({'azione': azione_proposta})
        
        # Salva con info ritmi
        memoria_episodio = {
            **episodio,
            'azione': azione_proposta,
            'successo': successo,
            'ciclo': num_ciclo,
            'ritmi_hz': {
                'frequenza_media': sum(r.frequenza_hz for r in ritmi_vita.values()) / len(ritmi_vita),
                'coherence': coherence,
                'banda_dominante': max(
                    [(r.banda.value, r.frequenza_hz) for r in ritmi_vita.values()],
                    key=lambda x: x[1]
                )[0]
            }
        }
        self.memoria.aggiungi_memoria(memoria_episodio)
        
        # Stats
        if successo:
            self.stats['successi'] += 1
        
        print(f"  {'✅ Successo' if successo else '❌ Fallito'}")
        
        return successo
    
    def _mostra_ritmi_compatti(self, pattern: Dict):
        """Visualizzazione compatta ritmi"""
        # Mostra solo le 3 frequenze principali
        sorted_ritmi = sorted(pattern.items(), key=lambda x: x[1].frequenza_hz, reverse=True)[:3]
        
        ritmi_str = " | ".join([
            f"{r.banda.value[:1]}{r.frequenza_hz:.0f}Hz" 
            for area, r in sorted_ritmi
        ])
        print(f"  🌊 Ritmi: {ritmi_str}")


def test_sistema_ritmi(num_cicli=5):
    """Test sistema con ritmi Hz"""
    
    print("\n" + "="*80)
    print("🌊 TEST MENTE VITA CON RITMI Hz FUNZIONALI")
    print("="*80)
    
    config = ConfigurazioneAGI()
    config.num_cicli = num_cicli
    config.delay_tra_cicli = 0.5
    config.mostra_narrazione_completa = False
    
    print(f"\n🎯 Test con {num_cicli} cicli")
    print(f"🌊 Ogni fase mostrerà i suoi ritmi Hz!\n")
    
    mente_hz = MenteVitaRitmiHz(config)
    mente_hz.esegui_sessione()
    
    print("\n" + "="*80)
    print("✅ TEST RITMI Hz COMPLETATO!")
    print("="*80)
    print("\n💡 Ora ogni area cerebrale ha la sua frequenza naturale!")
    print("  Esattamente come nel cervello umano! 🧠\n")


if __name__ == "__main__":
    import sys
    
    num_cicli = 5
    if len(sys.argv) > 1:
        try:
            num_cicli = int(sys.argv[1])
        except:
            num_cicli = 5
    
    test_sistema_ritmi(num_cicli)

