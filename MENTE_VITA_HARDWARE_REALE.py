#!/usr/bin/env python3
"""
📹 MENTE VITA CON HARDWARE REALE - v7.1 Hardware
===================================================
Sistema VITA che USA camera e microfono REALI!

NOVITÀ:
- Webcam attiva (YOLOv8 su immagini reali)
- Microfono attivo (Whisper su audio reale)
- Vede e sente il mondo VERO!

Autore: Alessio + Cursor AI
Data: 23 Ottobre 2025
"""

import os
import sys
import time
from datetime import datetime
from pathlib import Path

from MENTE_VITA_ARTIFICIALE import MenteVitaArtificiale, ConfigurazioneAGI


class MenteVitaHardwareReale(MenteVitaArtificiale):
    """
    Sistema VITA con hardware reale
    Usa DAVVERO camera e microfono!
    """
    
    def __init__(self, config: ConfigurazioneAGI):
        super().__init__(config)
        
        print(f"\n{'='*80}")
        print(f"  📹 INIZIALIZZAZIONE HARDWARE REALE")
        print(f"{'='*80}\n")
        
        # Inizializza camera reale
        self.camera_attiva = False
        try:
            print("📷 Tentativo inizializzazione webcam...")
            if self.visione.inizializza_camera(camera_id=0):
                self.camera_attiva = True
                print("  ✅ WEBCAM ATTIVA!")
            else:
                print("  ⚠️  Webcam non disponibile, uso simulazione")
        except Exception as e:
            print(f"  ⚠️  Errore camera: {e}")
            print("  → Continuo con simulazione visiva")
        
        # Inizializza microfono reale
        self.microfono_attivo = False
        try:
            print("\n🎤 Tentativo inizializzazione microfono...")
            if self.udito.inizializza_microfono():
                self.microfono_attivo = True
                print("  ✅ MICROFONO ATTIVO!")
            else:
                print("  ⚠️  Microfono non disponibile, uso simulazione")
        except Exception as e:
            print(f"  ⚠️  Errore microfono: {e}")
            print("  → Continuo con simulazione audio")
        
        print(f"\n{'='*80}")
        print(f"  🎬 HARDWARE STATUS:")
        print(f"  • Camera: {'✅ REALE' if self.camera_attiva else '⚠️ Simulata'}")
        print(f"  • Microfono: {'✅ REALE' if self.microfono_attivo else '⚠️ Simulato'}")
        print(f"{'='*80}\n")
    
    def ciclo_agi_completo(self, num_ciclo):
        """Ciclo con hardware reale"""
        
        print(f"\n{'╔'+'═'*78+'╗'}")
        print(f"║ CICLO HARDWARE REALE #{num_ciclo:04d}{' '*51}║")
        print(f"{'╚'+'═'*78+'╝'}")
        
        # ========== PERCEZIONE CON HARDWARE REALE ==========
        print("\n[FASE 1] 👁️👂 PERCEZIONE REALE")
        
        # VISIONE REALE
        if self.camera_attiva:
            print("  📷 Cattura da webcam...")
            frame = self.visione.cattura_da_camera(camera_id=0)
            if frame is not None:
                vis = self.visione.elabora(frame)
                tipo = vis.get('tipo', 'unknown')
                print(f"  👁️  Vista {tipo.upper()}: {vis.get('descrizione', 'N/A')[:50]}...")
            else:
                vis = self.visione.elabora(None)
                print(f"  👁️  Vista simulata (camera fallita)")
        else:
            vis = self.visione.elabora(None)
            print(f"  👁️  Vista simulata: {vis.get('descrizione', '')[:50]}...")
        
        # UDITO REALE  
        # Nota: ascolta(None) già registra dal microfono automaticamente!
        aud = self.udito.ascolta(None, lingua="it")
        tipo_aud = aud.get('tipo', 'unknown')
        testo_aud = aud.get('testo', aud.get('trascrizione', ''))
        
        if tipo_aud == 'reale' and testo_aud:
            print(f"  👂 Audio REALE: '{testo_aud[:50]}'")
        elif testo_aud:
            print(f"  👂 Audio simulato: '{testo_aud[:30]}...'")
        else:
            print(f"  👂 Audio: Silenzio o segnale debole")
        
        # Resto del ciclo come sistema base
        onda = self.biosegnali.percepisce_segnale([vis, aud])
        pattern = onda.pattern.replace('1', '█').replace('0', '░')
        print(f"  ⚡ Biosegnali: {pattern}")
        
        stato_emo = self.emozione.elabora({'percezioni': [vis, aud]})
        valenza = stato_emo.dati.get('valenza', 0)
        print(f"  ❤️  Emozione: {valenza:+.2f}")
        
        # Cognizione
        print("\n[FASE 2-6] 🧠 COGNIZIONE & COSCIENZA")
        decisione_ctx = {
            'percezioni_visive': vis,
            'percezioni_uditive': aud,
            'valenza': valenza
        }
        dec = self.prefrontale.ragiona(decisione_ctx)
        azione_proposta = dec.get('azione', 'monitora')
        
        # Coscienza
        episodio = {
            'descrizione': vis.get('descrizione', ''),
            'audio': aud.get('testo', ''),
            'emozione': 'positivo' if valenza > 0 else 'neutro',
            'valenza': valenza
        }
        
        contesto_cosc = {
            'percezione': vis.get('descrizione', '')[:50],
            'emozione': valenza,
            'obiettivo_corrente': 'osservazione_reale',
            'azione_proposta': azione_proposta,
            'motivazione_dominante': 'curiosità',
            'successi_recenti': 5,
            'livello_conoscenza_medio': 0.7,
            'interazioni_oggi': num_ciclo % 20,
            'momento': f"ciclo {num_ciclo}",
            'significativo': valenza > 0.5
        }
        coscienza_result = self.coscienza.elabora(contesto_cosc)
        print(f"  🧠 Riflessione: {coscienza_result['auto_riflessione'][:50]}...")
        
        # VITA
        print("\n[FASE 7] 🌌 VITA EMERGENTE")
        
        auto_ctx = {'azione_proposta': azione_proposta, 'coerenza': 0.8}
        auto_result = self.autoconservazione.elabora(auto_ctx)
        print(f"  🛡️  Autoconservazione: {auto_result['vitalita_complessiva']:.0%}")
        
        des_ctx = {'esperienza': {'successo': True, 'scoperta': False, 'descrizione': vis.get('descrizione', '')}}
        des_result = self.desiderio_continuita.elabora(des_ctx)
        print(f"  💫 Impulso vitale: {des_result['intensita_vitale']:.0%}")
        
        # Esecuzione
        print(f"\n[ESECUZIONE] 🦾 Azione: {azione_proposta.upper()}")
        successo = self.motoria.agisci({'azione': azione_proposta})
        print(f"  {'✅ Successo' if successo else '❌ Fallito'}")
        
        # Salva con flag hardware
        memoria_episodio = {
            **episodio,
            'azione': azione_proposta,
            'successo': successo,
            'ciclo': num_ciclo,
            'hardware': {
                'camera': self.camera_attiva,
                'microfono': self.microfono_attivo
            }
        }
        self.memoria.aggiungi_memoria(memoria_episodio)
        
        if successo:
            self.stats['successi'] += 1
        
        return successo
    
    def __del__(self):
        """Cleanup hardware al termine"""
        print("\n🛑 Chiusura hardware...")
        try:
            if self.camera_attiva:
                self.visione.chiudi()
                print("  ✅ Camera rilasciata")
        except:
            pass


def test_hardware_reale(num_cicli=5):
    """Test con hardware reale"""
    
    print("\n" + "="*80)
    print("📹 TEST MENTE VITA CON HARDWARE REALE")
    print("="*80)
    print("\n⚠️  REQUISITI:")
    print("  • Webcam collegata")
    print("  • Microfono funzionante")
    print("  • Permessi camera/mic (Windows)")
    print("\n💡 Se hardware non disponibile, userà simulazione")
    print("\n" + "="*80)
    
    input("\n🚀 Premi ENTER per iniziare...\n")
    
    config = ConfigurazioneAGI()
    config.num_cicli = num_cicli
    config.delay_tra_cicli = 1.0  # Più lento per vedere output
    config.mostra_narrazione_completa = False
    
    mente_hw = MenteVitaHardwareReale(config)
    mente_hw.esegui_sessione()
    
    print("\n" + "="*80)
    print("✅ TEST HARDWARE COMPLETATO!")
    print("="*80)
    
    if mente_hw.camera_attiva or mente_hw.microfono_attivo:
        print("\n🎉 Hardware reale utilizzato con successo!")
    else:
        print("\n⚠️  Hardware non disponibile, usata simulazione")
    
    print()


if __name__ == "__main__":
    import sys
    
    num_cicli = 5
    if len(sys.argv) > 1:
        try:
            num_cicli = int(sys.argv[1])
        except:
            num_cicli = 5
    
    test_hardware_reale(num_cicli)

