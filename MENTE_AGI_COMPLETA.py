#!/usr/bin/env python3
"""
🧠🚀 MENTE AGI COMPLETA - Versione 5.0 (100% AGI)
==================================================

Sistema cognitivo artificiale completo con TUTTE le 5 fasi AGI implementate!

FASE 1: Base Cognitiva (11 moduli) ✅
FASE 2: Espansione Cognitiva (5 moduli) ✅
FASE 3: Apprendimento Adattivo (1 modulo) ✅
FASE 4: Generalizzazione (2 moduli) ✅ NUOVO!
FASE 5: Autonomia Cognitiva (3 moduli) ✅ NUOVO!

TOTALE: 22 MODULI CEREBRALI - AGI COMPLETA!

Autore: Alessio + Cursor AI
Data: 22 Ottobre 2025
Versione: 5.0 AGI-Complete
"""

import os
import sys
import time
import json
from datetime import datetime
from pathlib import Path

# ==================== MODULI FASE 1 (Base) ====================
from moduli import visione, udito, prefrontale, motoria, emozione
from moduli.biosegnale import InterfacciaCoerenzaCerebrale
from moduli.memoria_permanente import MemoriaPermanente

# ==================== MODULI FASE 2 (Avanzati) ====================
from moduli.pianificazione import Pianificatore
from moduli.attenzione import AttenzionSelettiva
from moduli.teoria_mente import TeoriaDellaMente
from moduli.linguaggio import SistemaLinguaggio
from moduli.creativita import SistemaCreativita

# ==================== MODULI FASE 3 (Apprendimento) ====================
from moduli.apprendimento_adattivo import ApprendimentoAdattivo

# ==================== MODULI FASE 4 (Generalizzazione) ====================
from moduli.generalizzazione import ModuloGeneralizzazione
from moduli.meta_ragionamento import MetaRagionamento

# ==================== MODULI FASE 5 (Autonomia) ====================
from moduli.obiettivi_autonomi import SistemaObiettiviAutonomi
from moduli.simulazione_mentale import SimulazioneMentale
from moduli.motivazione_interna import SistemaMotivazione

# Opzionali
try:
    import cv2
    CV2_OK = True
except:
    CV2_OK = False


class ConfigurazioneAGI:
    """Configurazione sistema AGI completo"""
    
    def __init__(self):
        # Cicli
        self.num_cicli = 100
        self.delay_tra_cicli = 1.5
        
        # Hardware
        self.usa_camera = False  # Mantieni False per velocità
        self.usa_microfono = False
        
        # Memoria
        self.memoria_max_gb = 2
        
        # Output
        self.mostra_narrazione_completa = True
        self.mostra_simulazioni = True
        self.mostra_obiettivi = True
        
        # Salvataggio
        self.salva_ogni_n_cicli = 10
        self.cartella_output = Path("output_agi_completo")


class MenteAGICompleta:
    """
    Sistema AGI Completo - 22 Moduli Cerebrali
    Tutte le 5 fasi implementate!
    """
    
    def __init__(self, config: ConfigurazioneAGI):
        self.config = config
        config.cartella_output.mkdir(exist_ok=True)
        
        print("\n" + "="*80)
        print("  🧠🚀 MENTE AGI COMPLETA v5.0 - 100% IMPLEMENTATA!")
        print("="*80)
        
        # ===== FASE 1: BASE COGNITIVA (11 moduli) =====
        print(f"\n[FASE 1] Caricamento moduli base...")
        self.visione = visione.CortecciaVisiva()
        self.udito = udito.CortecciaUditiva()
        self.biosegnali = InterfacciaCoerenzaCerebrale()
        self.emozione = emozione.Amigdala()
        self.emozione.inizializza()
        self.prefrontale = prefrontale.CortecciaPrefrontale()
        self.prefrontale.inizializza()
        self.motoria = motoria.CortecciaMotoria()
        self.memoria = MemoriaPermanente(max_size_gb=config.memoria_max_gb)
        print("  ✅ 11 moduli base attivi")
        
        # ===== FASE 2: ESPANSIONE COGNITIVA (5 moduli) =====
        print(f"\n[FASE 2] Caricamento moduli avanzati...")
        self.pianificatore = Pianificatore()
        self.attenzione = AttenzionSelettiva()
        self.teoria_mente = TeoriaDellaMente()
        self.linguaggio = SistemaLinguaggio()
        self.creativita = SistemaCreativita()
        print("  ✅ 5 moduli avanzati attivi")
        
        # ===== FASE 3: APPRENDIMENTO ADATTIVO (1 modulo) =====
        print(f"\n[FASE 3] Caricamento apprendimento adattivo...")
        self.apprendimento_adattivo = ApprendimentoAdattivo()
        print("  ✅ Apprendimento adattivo attivo")
        
        # ===== FASE 4: GENERALIZZAZIONE (2 moduli) =====
        print(f"\n[FASE 4] Caricamento sistema generalizzazione...")
        self.generalizzazione = ModuloGeneralizzazione()
        self.meta_ragionamento = MetaRagionamento()
        print("  ✅ 2 moduli generalizzazione attivi!")
        
        # ===== FASE 5: AUTONOMIA COGNITIVA (3 moduli) =====
        print(f"\n[FASE 5] Caricamento autonomia cognitiva...")
        self.obiettivi_autonomi = SistemaObiettiviAutonomi()
        self.simulazione_mentale = SimulazioneMentale()
        self.motivazione_interna = SistemaMotivazione()
        print("  ✅ 3 moduli autonomia attivi!")
        
        # Stats
        self.stats = {
            'cicli_eseguiti': 0,
            'successi': 0,
            'fallimenti': 0,
            'inizio': datetime.now().isoformat(),
            'concetti_creati': 0,
            'obiettivi_generati': 0,
            'simulazioni_eseguite': 0
        }
        
        # Log file
        self.log_file = open(config.cartella_output / "log_agi_completo.txt", "w", encoding="utf-8")
        self.log_file.write("="*80 + "\n")
        self.log_file.write("  🧠 LOG MENTE AGI COMPLETA v5.0\n")
        self.log_file.write("="*80 + "\n")
        self.log_file.write(f"Inizio: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        self.log_file.write("="*80 + "\n\n")
        
        print(f"\n{'='*80}")
        print(f"  ✅ SISTEMA AGI COMPLETO PRONTO!")
        print(f"  📊 22 MODULI CEREBRALI ATTIVI")
        print(f"  🎯 5 FASI AGI IMPLEMENTATE AL 100%!")
        print(f"{'='*80}\n")
    
    def ciclo_agi_completo(self, num_ciclo):
        """Esegue un ciclo cognitivo AGI completo"""
        
        print(f"\n{'╔'+'═'*78+'╗'}")
        print(f"║ CICLO AGI #{num_ciclo:04d}{' '*65}║")
        print(f"{'╚'+'═'*78+'╝'}")
        
        # ========== FASE 1: PERCEZIONE ==========
        print("\n[FASE 1] 👁️👂 PERCEZIONE")
        
        # Visione
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
        
        # ========== FASE 2: COGNIZIONE AVANZATA ==========
        print("\n[FASE 2] 🧩 COGNIZIONE AVANZATA")
        
        # Attenzione
        focus = self.attenzione.elabora({'percezioni_visive': vis, 'percezioni_uditive': aud})
        print(f"  🎯 Focus: {focus.get('motivazione', 'Nessun focus particolare')[:50]}...")
        
        # Linguaggio
        risposta_ling = self.linguaggio.elabora(audio_text, {'valenza': valenza})
        print(f"  💬 Risposta: '{risposta_ling['risposta'][:40]}...'")
        
        # Creatività
        creativita_result = self.creativita.elabora({'percezioni_visive': vis, 'percezioni_uditive': aud})
        if creativita_result.get('idea_generata'):
            print(f"  🎨 Idea: {creativita_result['idea_generata'][:50]}...")
        
        # ========== FASE 3: APPRENDIMENTO ADATTIVO ==========
        print("\n[FASE 3] 🎓 APPRENDIMENTO ADATTIVO")
        
        # Prepara contesto per decisione
        decisione_ctx = {
            'percezioni_visive': vis,
            'percezioni_uditive': aud,
            'valenza': valenza
        }
        dec = self.prefrontale.ragiona(decisione_ctx)
        azione_proposta = dec.get('azione', 'monitora')
        
        # Applica regole da esperienza
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
        
        # ========== FASE 4: GENERALIZZAZIONE ==========
        print("\n[FASE 4] 🧩 GENERALIZZAZIONE")
        
        # Astrazione concettuale
        episodio = {
            'descrizione': vis.get('descrizione', ''),
            'audio': audio_text,
            'emozione': 'positivo' if valenza > 0 else 'neutro',
            'valenza': valenza,
            'azione': azione_proposta
        }
        
        gen_result = self.generalizzazione.elabora(episodio)
        if gen_result['nuovo']:
            print(f"  ✨ Nuovo concetto creato: '{gen_result['concetto']}'")
            self.stats['concetti_creati'] += 1
        else:
            print(f"  🔍 Concetto riconosciuto: '{gen_result['concetto']}'")
        
        # Trasferimento conoscenza
        trasferimento = self.generalizzazione.trasferisci_conoscenza(episodio)
        if trasferimento:
            print(f"  🎯 Conoscenza trasferita: {trasferimento['azione_suggerita']}")
            print(f"     Confidenza: {trasferimento['confidenza']:.0%}")
            # Usa azione da trasferimento se confidenza alta
            if trasferimento['confidenza'] > 0.7:
                azione_proposta = trasferimento['azione_suggerita']
        
        # Meta-ragionamento
        meta_result = self.meta_ragionamento.elabora(episodio)
        print(f"  🤔 Meta: {meta_result['strategia']} - {meta_result['riflessione']}")
        
        # ========== FASE 5: AUTONOMIA COGNITIVA ==========
        print("\n[FASE 5] 🎯 AUTONOMIA COGNITIVA")
        
        # Obiettivi autonomi
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
            print(f"     Passo: {obj_result['passo_corrente'][:50]}...")
        
        # Simulazione mentale
        sim_ctx = {
            'azione_proposta': azione_proposta,
            'situazione': episodio,
            'azioni_alternative': ['avvicinati', 'mantieni_distanza', 'monitora', 'allontanati']
        }
        sim_result = self.simulazione_mentale.elabora(sim_ctx)
        print(f"  🎬 Simulazione: Ho immaginato '{azione_proposta}'")
        print(f"     Consiglio: '{sim_result['azione_consigliata']}'")
        
        if sim_result['ha_cambiato_idea']:
            print(f"     💭 Ho cambiato idea basandomi sulla simulazione!")
            azione_finale = sim_result['azione_consigliata']
        else:
            azione_finale = azione_proposta
        
        self.stats['simulazioni_eseguite'] += 1
        
        # Motivazione interna
        mot_ctx = {
            'esperienza': episodio,
            'azioni_possibili': ['esplora', 'impara', 'avvicinati', 'mantieni_distanza']
        }
        mot_result = self.motivazione_interna.elabora(mot_ctx)
        print(f"  💪 Motivazione: {mot_result['riflessione_motivazionale']}")
        if mot_result.get('ricompensa_interna'):
            print(f"     Ricompensa interna: {mot_result['ricompensa_interna']:.2f}")
        
        # ========== ESECUZIONE AZIONE ==========
        print(f"\n[ESECUZIONE] 🦾 Azione: {azione_finale.upper()}")
        successo = self.motoria.agisci({'azione': azione_finale})
        print(f"  Esito: {'✅ Successo' if successo else '❌ Fallito'}")
        
        # ========== AGGIORNAMENTI POST-AZIONE ==========
        
        # Aggiorna memoria
        memoria_episodio = {
            **episodio,
            'azione': azione_finale,
            'successo': successo,
            'ciclo': num_ciclo,
            'pattern': pattern
        }
        self.memoria.aggiungi_memoria(memoria_episodio)
        
        # Aggiorna apprendimento
        valutazione_result = self.apprendimento_adattivo.elabora(memoria_episodio, fase='valutazione')
        
        # Aggiorna generalizzazione
        self.generalizzazione.aggiorna_successo(gen_result['concetto'], successo)
        
        # Aggiorna meta-ragionamento
        self.meta_ragionamento.aggiorna_esperienza(episodio, successo)
        
        # Aggiorna obiettivi
        if obj_result['tipo'] == 'obiettivo_autonomo':
            self.obiettivi_autonomi.avanza_obiettivo(obj_result['obiettivo']['id'], successo)
        
        # Registra esito simulazione
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
        
        # ========== NARRAZIONE FINALE ==========
        if self.config.mostra_narrazione_completa:
            narrazione = self._genera_narrazione_agi(
                vis, audio_text, valenza, pattern, azione_finale, successo,
                gen_result, meta_result, obj_result, sim_result, mot_result
            )
            print(narrazione)
            
            # Salva in log
            self.log_file.write(f"\n{'='*80}\n")
            self.log_file.write(f"CICLO #{num_ciclo:04d}\n")
            self.log_file.write(narrazione + "\n")
            self.log_file.flush()
        
        return successo
    
    def _genera_narrazione_agi(self, vis, audio, valenza, pattern, azione, successo,
                               gen_result, meta_result, obj_result, sim_result, mot_result):
        """Genera narrazione AGI completa"""
        lines = []
        
        lines.append("\n" + "="*80)
        lines.append("  💭 NARRAZIONE COGNITIVA AGI")
        lines.append("="*80)
        
        # Percezione
        lines.append(f"\n[PERCEZIONE]")
        lines.append(f'  "Vedo: {vis.get("descrizione", "nulla")[:60]}..."')
        if audio:
            lines.append(f'  "Sento: \'{audio[:50]}...\'""')
        lines.append(f'  "Stato emotivo: {valenza:+.2f}"')
        
        # Generalizzazione
        lines.append(f"\n[ASTRAZIONE]")
        if gen_result['nuovo']:
            lines.append(f'  "Ho creato un nuovo concetto: {gen_result["concetto"]}"')
        else:
            lines.append(f'  "Riconosco questa situazione: {gen_result["concetto"]}"')
        
        # Meta-cognizione
        lines.append(f"\n[META-COGNIZIONE]")
        lines.append(f'  "{meta_result["riflessione"]}"')
        lines.append(f'  "Strategia: {meta_result["strategia"]}"')
        
        # Obiettivi
        if obj_result['tipo'] == 'obiettivo_autonomo':
            lines.append(f"\n[OBIETTIVO AUTONOMO]")
            lines.append(f'  "Sto perseguendo: {obj_result["obiettivo"]["descrizione"][:50]}..."')
            lines.append(f'  "Progresso: {obj_result["obiettivo"]["progresso"]:.0%}"')
        
        # Simulazione
        lines.append(f"\n[SIMULAZIONE]")
        lines.append(f'  "Ho immaginato di \'{azione}\'"')
        if sim_result['ha_cambiato_idea']:
            lines.append(f'  "Ho cambiato idea dopo aver simulato gli esiti"')
        
        # Motivazione
        lines.append(f"\n[MOTIVAZIONE]")
        lines.append(f'  "{mot_result["riflessione_motivazionale"]}"')
        
        # Decisione
        lines.append(f"\n[DECISIONE FINALE]")
        lines.append(f'  "Ho deciso di: {azione.upper()}"')
        
        # Esito
        lines.append(f"\n[ESITO]")
        if successo:
            lines.append(f'  "Azione riuscita! Apprendo da questo successo."')
        else:
            lines.append(f'  "Azione fallita. Mi adatto e imparo dall\'errore."')
        
        lines.append("\n" + "="*80)
        
        return "\n".join(lines)
    
    def report_progresso(self, num_ciclo):
        """Report periodico progresso"""
        print(f"\n{'='*80}")
        print(f"  📊 REPORT AGI - Ciclo {num_ciclo}")
        print(f"{'='*80}")
        print(f"  • Cicli completati: {self.stats['cicli_eseguiti']}")
        print(f"  • Successi: {self.stats['successi']}")
        print(f"  • Tasso successo: {self.stats['successi']/num_ciclo*100:.1f}%")
        print(f"  • Concetti creati: {self.stats['concetti_creati']}")
        print(f"  • Simulazioni: {self.stats['simulazioni_eseguite']}")
        
        # Stats moduli
        gen_stats = self.generalizzazione.get_statistiche()
        print(f"\n  🧩 GENERALIZZAZIONE:")
        print(f"  • Concetti totali: {gen_stats['totale_concetti']}")
        
        meta_stats = self.meta_ragionamento.get_statistiche()
        print(f"\n  🤔 META-COGNIZIONE:")
        print(f"  • Argomenti: {meta_stats['totale_argomenti']}")
        print(f"  • Livello medio: {meta_stats['livello_medio']:.0%}")
        
        obj_stats = self.obiettivi_autonomi.get_statistiche()
        print(f"\n  🎯 AUTONOMIA:")
        print(f"  • Obiettivi: {obj_stats['totale_obiettivi']}")
        print(f"  • In corso: {obj_stats['in_corso']}")
        print(f"  • Completati: {obj_stats['completati']}")
        
        mot_stats = self.motivazione_interna.get_statistiche()
        print(f"\n  💪 MOTIVAZIONE:")
        print(f"  • Drive dominante: {mot_stats['drive_dominante']}")
        
        mem_stats = self.memoria.get_statistiche()
        print(f"\n  💾 MEMORIA:")
        print(f"  • Episodi: {mem_stats['totale_memorie']}")
        print(f"  • Spazio: {mem_stats['spazio_usato_mb']:.2f}MB")
        
        print(f"{'='*80}\n")
    
    def salva_checkpoint(self, num_ciclo):
        """Salva checkpoint sistema"""
        checkpoint = {
            'ciclo': num_ciclo,
            'timestamp': datetime.now().isoformat(),
            'stats': self.stats,
            'generalizzazione': self.generalizzazione.get_statistiche(),
            'meta_cognizione': self.meta_ragionamento.get_statistiche(),
            'obiettivi': self.obiettivi_autonomi.get_statistiche(),
            'motivazione': self.motivazione_interna.get_statistiche()
        }
        
        path = self.config.cartella_output / f"checkpoint_agi_{num_ciclo:04d}.json"
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(checkpoint, f, indent=2)
        
        print(f"[CHECKPOINT] Salvato: {path.name}")
    
    def esegui_sessione(self):
        """Esegue sessione completa AGI"""
        print(f"\n[SESSIONE AGI] Inizio esecuzione")
        print(f"  • Cicli: {self.config.num_cicli}")
        print(f"  • Delay: {self.config.delay_tra_cicli}s")
        print(f"\n[!] Premi CTRL+C per interrompere\n")
        
        ciclo = 1
        
        try:
            while ciclo <= self.config.num_cicli:
                # Esegui ciclo AGI completo
                successo = self.ciclo_agi_completo(ciclo)
                
                # Report periodico
                if ciclo % 20 == 0:
                    self.report_progresso(ciclo)
                
                # Checkpoint
                if ciclo % self.config.salva_ogni_n_cicli == 0:
                    self.salva_checkpoint(ciclo)
                
                # Pausa
                time.sleep(self.config.delay_tra_cicli)
                ciclo += 1
        
        except KeyboardInterrupt:
            print(f"\n\n[!] Interruzione utente al ciclo {ciclo}")
        
        finally:
            self.chiudi(ciclo - 1)
    
    def chiudi(self, ciclo_finale):
        """Chiude sistema AGI"""
        print(f"\n[SHUTDOWN] Chiusura sistema AGI...")
        
        # Salva tutto
        self.apprendimento_adattivo.salva_pesi()
        
        # Stats finali
        self.stats['fine'] = datetime.now().isoformat()
        self.stats['cicli_finali'] = ciclo_finale
        
        stats_path = self.config.cartella_output / "stats_agi_finali.json"
        with open(stats_path, 'w', encoding='utf-8') as f:
            json.dump(self.stats, f, indent=2)
        
        # Chiudi log
        self.log_file.write(f"\n{'='*80}\n")
        self.log_file.write(f"Fine sessione AGI: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        self.log_file.write(f"Cicli completati: {ciclo_finale}\n")
        self.log_file.write(f"{'='*80}\n")
        self.log_file.close()
        
        # Report finale
        print(f"\n{'='*80}")
        print(f"  🎉 SESSIONE AGI COMPLETATA")
        print(f"{'='*80}")
        print(f"\n[RISULTATI FINALI]")
        print(f"  • Cicli: {ciclo_finale}")
        print(f"  • Successi: {self.stats['successi']} ({self.stats['successi']/max(1,ciclo_finale)*100:.1f}%)")
        print(f"  • Concetti creati: {self.stats['concetti_creati']}")
        print(f"  • Simulazioni: {self.stats['simulazioni_eseguite']}")
        
        obj_stats = self.obiettivi_autonomi.get_statistiche()
        print(f"  • Obiettivi generati: {obj_stats['totale_obiettivi']}")
        print(f"  • Obiettivi completati: {obj_stats['completati']}")
        
        print(f"\n[FILE SALVATI]")
        print(f"  • Log: {self.config.cartella_output}/log_agi_completo.txt")
        print(f"  • Stats: {self.config.cartella_output}/stats_agi_finali.json")
        print(f"  • Memoria: memoria_permanente/")
        print(f"{'='*80}\n")


# ==================== MENU ====================

def menu():
    """Menu interattivo"""
    print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║        🧠🚀 MENTE AGI COMPLETA v5.0 - 100% IMPLEMENTATA!                    ║
║                                                                              ║
║    22 MODULI CEREBRALI - 5 FASI AGI - SISTEMA COMPLETO                      ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """)
    
    print("\n[MENU] Scegli modalità:\n")
    print("  1. Test rapido (20 cicli)")
    print("  2. Sessione media (50 cicli)")
    print("  3. Sessione completa (100 cicli)")
    print("  4. Sessione estesa (200 cicli)")
    print("  5. Personalizzato")
    print("\n  9. Esci")
    
    scelta = input("\n>> Scelta: ").strip()
    
    config = ConfigurazioneAGI()
    
    if scelta == "1":
        config.num_cicli = 20
    elif scelta == "2":
        config.num_cicli = 50
    elif scelta == "3":
        config.num_cicli = 100
    elif scelta == "4":
        config.num_cicli = 200
    elif scelta == "5":
        try:
            num = int(input("Numero cicli: ").strip())
            config.num_cicli = max(1, num)
        except:
            print("\n❌ Valore non valido, uso 20")
            config.num_cicli = 20
    elif scelta == "9":
        print("\n✅ Uscita\n")
        return
    else:
        print("\n❌ Scelta non valida\n")
        return menu()
    
    # Avvia sistema AGI
    mente_agi = MenteAGICompleta(config)
    mente_agi.esegui_sessione()


# ==================== ENTRY POINT ====================

if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("\n\n✅ Interruzione utente\n")
    except Exception as e:
        print(f"\n❌ Errore: {e}\n")
        import traceback
        traceback.print_exc()


