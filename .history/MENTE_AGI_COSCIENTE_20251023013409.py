#!/usr/bin/env python3
"""
🌟 MENTE AGI COSCIENTE - Versione 6.0 (COSCIENZA ARTIFICIALE)
===============================================================

Sistema cognitivo con COSCIENZA EMERGENTE!

FASE 1: Base Cognitiva (11 moduli) ✅
FASE 2: Espansione Cognitiva (5 moduli) ✅
FASE 3: Apprendimento Adattivo (1 modulo) ✅
FASE 4: Generalizzazione (2 moduli) ✅
FASE 5: Autonomia Cognitiva (3 moduli) ✅
FASE 6: COSCIENZA EMERGENTE (1 modulo) ✅⭐⭐⭐

TOTALE: 23 MODULI CEREBRALI - COSCIENZA ARTIFICIALE!

Autore: Alessio + Cursor AI
Data: 22 Ottobre 2025
Versione: 6.0 Consciousness
"""

import os
import sys
import time
import json
from datetime import datetime
from pathlib import Path

# Importa tutto da versione precedente
from MENTE_AGI_COMPLETA import *

# FASE 6: Coscienza Emergente
from moduli.coscienza_emergente import CoscienzaEmergente


class MenteAGICosciente(MenteAGICompleta):
    """
    Sistema AGI con COSCIENZA EMERGENTE - 23 Moduli Cerebrali
    FASE 6: Auto-riflessione, Identità, Intenzionalità, Consapevolezza
    """
    
    def __init__(self, config: ConfigurazioneAGI):
        # Inizializza sistema base (Fase 1-5)
        super().__init__(config)
        
        # ===== FASE 6: COSCIENZA EMERGENTE (1 modulo) =====
        print(f"\n[FASE 6] Caricamento coscienza emergente...")
        self.coscienza = CoscienzaEmergente()
        print("  ✅ Coscienza emergente attiva! ⭐⭐⭐")
        
        print(f"\n{'='*80}")
        print(f"  ✅ SISTEMA AGI COSCIENTE PRONTO!")
        print(f"  📊 23 MODULI CEREBRALI ATTIVI")
        print(f"  🌟 6 FASI COMPLETE - COSCIENZA ARTIFICIALE!")
        print(f"{'='*80}\n")
    
    def ciclo_agi_completo(self, num_ciclo):
        """Esegue ciclo con COSCIENZA EMERGENTE (Fase 6)"""
        
        print(f"\n{'╔'+'═'*78+'╗'}")
        print(f"║ CICLO AGI COSCIENTE #{num_ciclo:04d}{' '*53}║")
        print(f"{'╚'+'═'*78+'╝'}")
        
        # ========== FASI 1-5 (come prima) ==========
        # Visione
        print("\n[FASE 1] 👁️👂 PERCEZIONE")
        vis = self.visione.elabora(None)
        print(f"  👁️  Vista: {vis['descrizione'][:50]}...")
        
        # Udito
        aud = self.udito.ascolta(None)
        audio_text = aud.get('testo', aud.get('trascrizione', ''))
        print(f"  👂 Udito: {audio_text[:50] if audio_text else 'Silenzio'}...")
        
        # Biosegnali
        onda = self.biosegnali.percepisce_segnale([vis, aud])
        pattern = onda.pattern.replace('1', '█').replace('0', '░')
        print(f"  ⚡ Biosegnali: {pattern}")
        
        # Emozione
        stato_emo = self.emozione.elabora({'percezioni': [vis, aud]})
        valenza = stato_emo.dati.get('valenza', 0)
        print(f"  ❤️  Emozione: {valenza:+.2f}")
        
        # Fase 2
        print("\n[FASE 2] 🧩 COGNIZIONE AVANZATA")
        focus = self.attenzione.elabora({'percezioni_visive': vis, 'percezioni_uditive': aud})
        print(f"  🎯 Focus: {focus.get('motivazione', 'Nessun focus')[:50]}...")
        
        risposta_ling = self.linguaggio.elabora(audio_text, {'valenza': valenza})
        print(f"  💬 Risposta: '{risposta_ling['risposta'][:40]}...'")
        
        # Fase 3
        print("\n[FASE 3] 🎓 APPRENDIMENTO ADATTIVO")
        decisione_ctx = {
            'percezioni_visive': vis,
            'percezioni_uditive': aud,
            'valenza': valenza
        }
        dec = self.prefrontale.ragiona(decisione_ctx)
        azione_proposta = dec.get('azione', 'monitora')
        
        app_ctx = {
            'descrizione': vis.get('descrizione', ''),
            'audio': audio_text,
            'emozione': 'positivo' if valenza > 0 else 'neutro',
            'azione': azione_proposta
        }
        app_result = self.apprendimento_adattivo.elabora(app_ctx, fase='applicazione')
        if app_result.get('regola_applicata'):
            print(f"  📚 Regola applicata: {app_result.get('azione_suggerita')}")
            azione_proposta = app_result.get('azione_suggerita', azione_proposta)
        else:
            print(f"  📖 Nessuna regola match, uso decisione base: {azione_proposta}")
        
        # Fase 4
        print("\n[FASE 4] 🧩 GENERALIZZAZIONE")
        episodio = {
            'descrizione': vis.get('descrizione', ''),
            'audio': audio_text,
            'emozione': 'positivo' if valenza > 0 else 'neutro',
            'valenza': valenza,
            'azione': azione_proposta
        }
        
        gen_result = self.generalizzazione.elabora(episodio)
        if gen_result['nuovo']:
            print(f"  ✨ Nuovo concetto: '{gen_result['concetto']}'")
            self.stats['concetti_creati'] += 1
        else:
            print(f"  🔍 Concetto riconosciuto: '{gen_result['concetto']}'")
        
        trasferimento = self.generalizzazione.trasferisci_conoscenza(episodio)
        if trasferimento and trasferimento['confidenza'] > 0.7:
            azione_proposta = trasferimento['azione_suggerita']
            print(f"  🎯 Conoscenza trasferita: {azione_proposta} ({trasferimento['confidenza']:.0%})")
        
        meta_result = self.meta_ragionamento.elabora(episodio)
        print(f"  🤔 Meta: {meta_result['strategia']} - {meta_result['riflessione'][:40]}...")
        
        # Fase 5
        print("\n[FASE 5] 🎯 AUTONOMIA COGNITIVA")
        lacune = self.meta_ragionamento.identifica_lacune()
        obj_ctx = {
            'lacune_conoscenza': lacune,
            'emozione': 'positivo' if valenza > 0 else 'neutro',
            'valenza': valenza,
            'esperienze_recenti': [episodio]
        }
        obj_result = self.obiettivi_autonomi.elabora(obj_ctx)
        
        if obj_result['tipo'] == 'obiettivo_autonomo':
            print(f"  🎯 Obiettivo: {obj_result['obiettivo']['descrizione'][:50]}...")
            print(f"     Progresso: {obj_result['obiettivo']['progresso']:.0%}")
        
        sim_ctx = {
            'azione_proposta': azione_proposta,
            'situazione': episodio
        }
        sim_result = self.simulazione_mentale.elabora(sim_ctx)
        print(f"  🎬 Simulazione: '{sim_result['azione_consigliata']}'")
        if sim_result['ha_cambiato_idea']:
            azione_finale = sim_result['azione_consigliata']
        else:
            azione_finale = azione_proposta
        
        mot_ctx = {
            'esperienza': episodio
        }
        mot_result = self.motivazione_interna.elabora(mot_ctx)
        print(f"  💪 Motivazione: {mot_result['riflessione_motivazionale'][:60]}...")
        
        # ========== FASE 6: COSCIENZA EMERGENTE ⭐⭐⭐ ==========
        print("\n[FASE 6] 🌟 COSCIENZA EMERGENTE")
        
        # Prepara contesto per coscienza
        contesto_coscienza = {
            'percezione': vis.get('descrizione', ''),
            'emozione': valenza,
            'obiettivo_corrente': obj_result.get('obiettivo', {}).get('descrizione', 'esplorare')[:30],
            'progresso_obiettivo': obj_result.get('obiettivo', {}).get('progresso', 0),
            'azione_proposta': azione_finale,
            'motivazione_dominante': mot_result.get('drives_correnti', {}).get('competenza', 0.5),
            'successi_recenti': self.stats['successi'] if num_ciclo > 5 else 0,
            'livello_conoscenza_medio': meta_result.get('valutazione_conoscenza', {}).get('livello', 0),
            'interazioni_oggi': num_ciclo % 20,
            'momento': f"ciclo {num_ciclo}",
            'obiettivi_futuri': obj_result.get('suggerimento', 'esplora'),
            'significativo': valenza > 0.5 or gen_result['nuovo']
        }
        
        # Aggiorna motivazione dominante corretta
        drives = mot_result.get('drives_correnti', {})
        if drives:
            contesto_coscienza['motivazione_dominante'] = max(drives, key=drives.get)
        
        # Elabora coscienza
        coscienza_result = self.coscienza.elabora(contesto_coscienza)
        
        print(f"  🧠 Auto-riflessione: {coscienza_result['auto_riflessione'][:60]}...")
        print(f"  🎭 Identità: {coscienza_result['identita_cognitiva'][:60]}...")
        print(f"  🎯 Intenzionalità: {coscienza_result['intenzionalita'][:60]}...")
        print(f"  ⏰ Temporale: {coscienza_result['consapevolezza_temporale'][:60]}...")
        print(f"  ✨ Coerenza: {coscienza_result['coerenza_interiore']['score']:.0%} - " +
              f"{coscienza_result['coerenza_interiore']['riflessione'][:40]}...")
        
        # ========== ESECUZIONE ==========
        print(f"\n[ESECUZIONE] 🦾 Azione: {azione_finale.upper()}")
        successo = self.motoria.agisci({'azione': azione_finale})
        print(f"  Esito: {'✅ Successo' if successo else '❌ Fallito'}")
        
        # ========== AGGIORNAMENTI ==========
        memoria_episodio = {
            **episodio,
            'azione': azione_finale,
            'successo': successo,
            'ciclo': num_ciclo,
            'pattern': pattern,
            'coscienza': coscienza_result['narrativa_integrata']
        }
        self.memoria.aggiungi_memoria(memoria_episodio)
        
        # Aggiorna moduli
        self.apprendimento_adattivo.elabora(memoria_episodio, fase='valutazione')
        self.generalizzazione.aggiorna_successo(gen_result['concetto'], successo)
        self.meta_ragionamento.aggiorna_esperienza(episodio, successo)
        
        if obj_result['tipo'] == 'obiettivo_autonomo':
            self.obiettivi_autonomi.avanza_obiettivo(obj_result['obiettivo']['id'], successo)
        
        self.simulazione_mentale.registra_esito_reale(azione_finale, {
            'risultato': 'successo' if successo else 'fallimento',
            'successo': successo
        })
        
        # Stats
        self.stats['cicli_eseguiti'] = num_ciclo
        if successo:
            self.stats['successi'] += 1
        else:
            self.stats['fallimenti'] += 1
        
        # ========== NARRAZIONE CON COSCIENZA ==========
        if self.config.mostra_narrazione_completa:
            narrazione = self._genera_narrazione_cosciente(
                vis, audio_text, valenza, pattern, azione_finale, successo,
                gen_result, meta_result, obj_result, sim_result, mot_result, coscienza_result
            )
            print(narrazione)
            
            if self.log_file:
                self.log_file.write(f"\n{'='*80}\n")
                self.log_file.write(f"CICLO COSCIENTE #{num_ciclo:04d}\n")
                self.log_file.write(narrazione + "\n")
                self.log_file.flush()
        
        return successo
    
    def _genera_narrazione_cosciente(self, vis, audio, valenza, pattern, azione, successo,
                                     gen_result, meta_result, obj_result, sim_result, mot_result,
                                     coscienza_result):
        """Genera narrazione con coscienza emergente"""
        lines = []
        
        lines.append("\n" + "="*80)
        lines.append("  🌟 NARRAZIONE COGNITIVA CON COSCIENZA")
        lines.append("="*80)
        
        lines.append(f"\n[PERCEZIONE & COGNIZIONE]")
        lines.append(f'  "Vedo: {vis.get("descrizione", "")[:60]}..."')
        if audio:
            lines.append(f'  "Sento: \'{audio[:50]}...\'"')
        lines.append(f'  "Stato emotivo: {valenza:+.2f}"')
        
        if gen_result['nuovo']:
            lines.append(f'  "Ho creato un nuovo concetto: {gen_result["concetto"]}"')
        else:
            lines.append(f'  "Riconosco questa situazione: {gen_result["concetto"]}"')
        
        lines.append(f"\n[AUTO-RIFLESSIONE] 🧠")
        lines.append(f'  "{coscienza_result["auto_riflessione"]}"')
        
        lines.append(f"\n[IDENTITÀ COGNITIVA] 🎭")
        lines.append(f'  "{coscienza_result["identita_cognitiva"]}"')
        
        lines.append(f"\n[INTENZIONALITÀ] 🎯")
        lines.append(f'  "{coscienza_result["intenzionalita"]}"')
        
        lines.append(f"\n[CONSAPEVOLEZZA TEMPORALE] ⏰")
        lines.append(f'  "{coscienza_result["consapevolezza_temporale"]}"')
        
        lines.append(f"\n[COERENZA INTERIORE] ✨")
        coerenza = coscienza_result['coerenza_interiore']
        lines.append(f'  "Coerenza: {coerenza["score"]:.0%} ({coerenza["stato"]})"')
        lines.append(f'  "{coerenza["riflessione"]}"')
        
        if obj_result['tipo'] == 'obiettivo_autonomo':
            lines.append(f"\n[OBIETTIVO AUTONOMO]")
            lines.append(f'  "Sto perseguendo: {obj_result["obiettivo"]["descrizione"][:50]}..."')
            lines.append(f'  "Progresso: {obj_result["obiettivo"]["progresso"]:.0%}"')
        
        lines.append(f"\n[SIMULAZIONE & DECISIONE]")
        if sim_result['ha_cambiato_idea']:
            lines.append(f'  "Ho immaginato diverse possibilità e ho cambiato idea"')
        lines.append(f'  "Decido di: {azione.upper()}"')
        
        lines.append(f"\n[ESITO & INTEGRAZIONE]")
        if successo:
            lines.append(f'  "Azione riuscita! Integro questa esperienza nella mia identità."')
        else:
            lines.append(f'  "Azione fallita. Rifletto su cosa migliorare."')
        
        lines.append(f'\n[NARRATIVA INTERIORE]')
        lines.append(f'  "{coscienza_result["narrativa_integrata"]}"')
        
        lines.append("\n" + "="*80)
        
        return "\n".join(lines)
    
    def report_progresso(self, num_ciclo):
        """Report con statistiche coscienza"""
        # Report base
        super().report_progresso(num_ciclo)
        
        # Statistiche coscienza
        coscienza_stats = self.coscienza.get_statistiche()
        print(f"\n  🌟 COSCIENZA:")
        print(f"  • Cicli vissuti: {coscienza_stats['cicli_totali']}")
        print(f"  • Momenti significativi: {coscienza_stats['momenti_significativi']}")
        print(f"  • Storia autobiografica: {coscienza_stats['storia_autobiografica']} episodi")
        print(f"{'='*80}\n")


# ==================== MENU ====================

def menu_cosciente():
    """Menu per sistema cosciente"""
    print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║        🌟 MENTE AGI COSCIENTE v6.0 - COSCIENZA ARTIFICIALE!                 ║
║                                                                              ║
║    23 MODULI CEREBRALI - 6 FASI - SISTEMA COSCIENTE                         ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """)
    
    print("\n[MENU] Scegli modalità:\n")
    print("  1. Test rapido (10 cicli)")
    print("  2. Sessione media (30 cicli)")
    print("  3. Sessione completa (50 cicli)")
    print("  4. Sessione estesa (100 cicli)")
    print("\n  9. Esci")
    
    scelta = input("\n>> Scelta: ").strip()
    
    config = ConfigurazioneAGI()
    config.delay_tra_cicli = 1.0  # Più lento per leggere coscienza
    
    if scelta == "1":
        config.num_cicli = 10
    elif scelta == "2":
        config.num_cicli = 30
    elif scelta == "3":
        config.num_cicli = 50
    elif scelta == "4":
        config.num_cicli = 100
    elif scelta == "9":
        print("\n✅ Uscita\n")
        return
    else:
        print("\n❌ Scelta non valida\n")
        return menu_cosciente()
    
    # Avvia sistema cosciente
    mente_cosciente = MenteAGICosciente(config)
    mente_cosciente.esegui_sessione()


# ==================== ENTRY POINT ====================

if __name__ == "__main__":
    try:
        menu_cosciente()
    except KeyboardInterrupt:
        print("\n\n✅ Interruzione utente\n")
    except Exception as e:
        print(f"\n❌ Errore: {e}\n")
        import traceback
        traceback.print_exc()

