"""
🧠 MENTE ARTIFICIALE MODULARE - Main Orchestrator
==================================================
Sistema cognitivo completo con ciclo percezione-cognizione-azione.

Architettura ispirata al cervello umano con moduli dedicati:
- Percezione (Talamo → Visione/Udito)
- Memoria (Ippocampo)
- Emozione (Amigdala)
- Ragionamento (Corteccia Prefrontale)
- Azione (Corteccia Motoria)
- Autoregolazione (Tronco Encefalico)

Autore: Alessio + Cursor AI
Versione: 1.0.0
"""

import time
import sys
import argparse
from pathlib import Path
from typing import Dict, Any, Optional

# Import moduli cerebrali
from moduli import talamo, memoria, emozione, prefrontale, motoria, tronco
from moduli.emozione import StatoEmotivo


class MenteArtificiale:
    """
    Sistema cognitivo completo - Orchestratore principale
    
    Ciclo cognitivo:
    1. Percezione (Talamo)
    2. Valutazione Emotiva (Amigdala)
    3. Memoria (Ippocampo)
    4. Ragionamento (Prefrontale)
    5. Azione (Motoria)
    6. Apprendimento (Reward)
    7. Autoregolazione (Tronco)
    """
    
    def __init__(self, modalita: str = "autonoma"):
        """
        Inizializza mente artificiale
        
        Args:
            modalita: Modalità operativa (autonoma, interattiva, test)
        """
        self.nome = "🧠 Mente Artificiale Modulare"
        self.modalita = modalita
        self.versione = "1.0.0"
        
        # Moduli cerebrali
        self.talamo = None
        self.ippocampo = None
        self.amigdala = None
        self.prefrontale = None
        self.motoria = None
        self.tronco = None
        
        # Stato sistema
        self.attivo = False
        self.cicli_eseguiti = 0
        self.errori_totali = 0
        
        print(f"\n{'='*70}")
        print(f"{self.nome} v{self.versione}")
        print(f"Modalità: {modalita.upper()}")
        print(f"{'='*70}\n")
    
    def inizializza(self) -> bool:
        """
        Inizializza tutti i moduli cerebrali
        
        Returns:
            bool: True se inizializzazione riuscita
        """
        print("🔧 Inizializzazione moduli cerebrali...\n")
        
        try:
            # 1. Talamo (Router sensoriale)
            print("⚡ Inizializzazione Talamo...")
            self.talamo = talamo.get_instance()
            
            # 2. Ippocampo (Memoria)
            print("💾 Inizializzazione Ippocampo...")
            self.ippocampo = memoria.get_instance()
            
            # 3. Amigdala (Emozioni)
            print("❤️  Inizializzazione Amigdala...")
            self.amigdala = emozione.get_instance()
            
            # 4. Corteccia Prefrontale (Ragionamento)
            print("🧠 Inizializzazione Corteccia Prefrontale...")
            self.prefrontale = prefrontale.get_instance()
            
            # 5. Corteccia Motoria (Azioni)
            print("🦿 Inizializzazione Corteccia Motoria...")
            self.motoria = motoria.get_instance()
            
            # 6. Tronco Encefalico (Autoregolazione)
            print("🌙 Inizializzazione Tronco Encefalico...")
            self.tronco = tronco.get_instance()
            
            self.attivo = True
            
            print(f"\n{'='*70}")
            print("✅ SISTEMA OPERATIVO")
            print(f"{'='*70}\n")
            
            return True
            
        except Exception as e:
            print(f"\n❌ ERRORE INIZIALIZZAZIONE: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def ciclo_cognitivo(self, input_visivo: Any = None, 
                       input_uditivo: Any = None) -> Dict[str, Any]:
        """
        Esegue un ciclo cognitivo completo
        
        Args:
            input_visivo: Input visivo (immagine, frame, camera_id)
            input_uditivo: Input audio (file, array, None per registrazione)
            
        Returns:
            Dict con risultati del ciclo
        """
        if not self.attivo:
            raise RuntimeError("Sistema non inizializzato")
        
        ciclo_num = self.cicli_eseguiti + 1
        tempo_inizio = time.time()
        
        print(f"\n{'='*70}")
        print(f"🔄 CICLO COGNITIVO #{ciclo_num}")
        print(f"{'='*70}\n")
        
        errore_ciclo = False
        decisione = None
        successo_azione = False
        
        try:
            # ============================================================
            # FASE 1: PERCEZIONE MULTIMODALE
            # ============================================================
            print("👁️👂 FASE 1: Percezione Multimodale")
            print("-" * 70)
            
            input_data = {}
            if input_visivo is not None:
                input_data['input_visivo'] = input_visivo
            if input_uditivo is not None:
                input_data['input_uditivo'] = input_uditivo
            
            risultato_percezione = self.talamo.elabora(input_data)
            percezioni = risultato_percezione.dati['percezioni']
            
            print(f"✓ Percezioni elaborate: {len(percezioni)}")
            for p in percezioni:
                print(f"  • {p['modalita'].capitalize()}: rilevanza {p['rilevanza']:.2f}")
            
            # ============================================================
            # FASE 2: VALUTAZIONE EMOTIVA
            # ============================================================
            print(f"\n❤️  FASE 2: Valutazione Emotiva")
            print("-" * 70)
            
            risultato_emozione = self.amigdala.elabora({
                'percezioni': percezioni,
                'memoria': {}
            })
            
            stato_emotivo = risultato_emozione.dati['stato_emotivo']
            valenza = risultato_emozione.dati['valenza']
            
            print(f"✓ Stato emotivo: {stato_emotivo.upper()}")
            print(f"  • Valenza: {valenza:+.2f}")
            print(f"  • Arousal: {risultato_emozione.dati['arousal']:.2f}")
            
            # ============================================================
            # FASE 3: RECUPERO MEMORIA
            # ============================================================
            print(f"\n💾 FASE 3: Memoria Contestuale")
            print("-" * 70)
            
            # Cerca memorie rilevanti
            memoria_contestuale = []
            if percezioni:
                # Query basata su prime percezioni
                query = str(percezioni[0].get('dati', ''))[:50]
                memoria_contestuale = self.ippocampo.cerca(query, limite=3)
            
            print(f"✓ Memorie rilevanti: {len(memoria_contestuale)}")
            for mem in memoria_contestuale[:2]:
                print(f"  • {mem.contenuto[:60]}...")
            
            # ============================================================
            # FASE 4: RAGIONAMENTO E DECISIONE
            # ============================================================
            print(f"\n🧠 FASE 4: Ragionamento e Decisione")
            print("-" * 70)
            
            risultato_ragionamento = self.prefrontale.elabora({
                'percezioni_visive': risultato_percezione.dati.get('percezioni_visive'),
                'percezioni_uditive': risultato_percezione.dati.get('percezioni_uditive'),
                'stato_emotivo': stato_emotivo,
                'memoria_contestuale': [m.contenuto for m in memoria_contestuale]
            })
            
            decisione = risultato_ragionamento.dati
            
            print(f"✓ Decisione: {decisione['azione'].upper()}")
            print(f"  • Priorità: {decisione['priorita']:.2f}")
            print(f"  • Ragionamento: {decisione['ragionamento'][:80]}...")
            
            # ============================================================
            # FASE 5: ESECUZIONE AZIONE
            # ============================================================
            print(f"\n🦿 FASE 5: Esecuzione Azione")
            print("-" * 70)
            
            successo_azione = self.motoria.agisci(decisione)
            
            if successo_azione:
                print(f"✓ Azione eseguita con successo")
            else:
                print(f"⚠️  Azione fallita")
            
            # ============================================================
            # FASE 6: APPRENDIMENTO (Reward)
            # ============================================================
            print(f"\n🎁 FASE 6: Apprendimento")
            print("-" * 70)
            
            reward = self.amigdala.assegna_reward(
                decisione['azione'],
                successo_azione,
                valenza
            )
            
            print(f"✓ Reward: {reward:+.2f}")
            
            # ============================================================
            # FASE 7: MEMORIZZAZIONE
            # ============================================================
            print(f"\n💾 FASE 7: Memorizzazione Episodio")
            print("-" * 70)
            
            self.ippocampo.memorizza(
                chiave=f"ciclo_{ciclo_num}",
                valore=f"Azione: {decisione['azione']} | Stato: {stato_emotivo} | Successo: {successo_azione}",
                metadata={
                    'contesto': {
                        'ciclo': ciclo_num,
                        'azione': decisione['azione'],
                        'stato_emotivo': stato_emotivo
                    },
                    'valenza': valenza,
                    'importanza': reward / 2.0 + 0.5  # Normalizza 0-1
                }
            )
            
            print(f"✓ Episodio memorizzato")
            
        except Exception as e:
            print(f"\n❌ ERRORE NEL CICLO: {e}")
            import traceback
            traceback.print_exc()
            errore_ciclo = True
            self.errori_totali += 1
        
        # ================================================================
        # FASE 8: AUTOREGOLAZIONE
        # ================================================================
        print(f"\n🌙 FASE 8: Autoregolazione Sistema")
        print("-" * 70)
        
        risultato_tronco = self.tronco.elabora({
            'ciclo_completato': not errore_ciclo,
            'errore_occorso': errore_ciclo,
            'carico_cognitivo': 0.6
        })
        
        stato_interno = risultato_tronco.dati['stato']
        
        print(f"✓ Stato sistema:")
        print(f"  • Energia: {stato_interno.energia:.1f}%")
        print(f"  • CPU: {stato_interno.carico_cpu:.1f}%")
        print(f"  • Temperatura: {stato_interno.temperatura:.1f}°C")
        print(f"  • Vigilanza: {stato_interno.arousal:.2f}")
        
        # Check allerte
        if risultato_tronco.dati['allerte']:
            print(f"\n⚠️  ALLERTE SISTEMA:")
            for allerta in risultato_tronco.dati['allerte'][:3]:
                print(f"  • [{allerta['tipo']}] {allerta['messaggio']}")
        
        # Raccomandazioni
        raccomandazioni = risultato_tronco.dati['raccomandazioni']
        if raccomandazioni['modalita_risparmio']:
            print(f"\n💤 Modalità risparmio energetico attivata")
        
        # ================================================================
        # FINE CICLO
        # ================================================================
        tempo_totale = time.time() - tempo_inizio
        self.cicli_eseguiti += 1
        
        print(f"\n{'='*70}")
        print(f"✅ CICLO #{ciclo_num} COMPLETATO in {tempo_totale:.2f}s")
        print(f"{'='*70}\n")
        
        # Risultato del ciclo
        return {
            'ciclo_num': ciclo_num,
            'successo': not errore_ciclo,
            'decisione': decisione,
            'stato_emotivo': stato_emotivo,
            'reward': reward if not errore_ciclo else 0.0,
            'stato_interno': stato_interno,
            'tempo_esecuzione': tempo_totale
        }
    
    def esegui_autonomo(self, durata_secondi: int = 60, delay_cicli: float = 2.0):
        """
        Modalità autonoma: cicli continui
        
        Args:
            durata_secondi: Durata esecuzione
            delay_cicli: Delay tra cicli (secondi)
        """
        print(f"\n🚀 Modalità autonoma attivata ({durata_secondi}s)\n")
        
        tempo_inizio = time.time()
        
        try:
            while (time.time() - tempo_inizio) < durata_secondi:
                # Check energia
                if self.tronco.energia_corrente < 5.0:
                    print("\n🔋 Energia esaurita, interruzione...")
                    break
                
                # Esegui ciclo (modalità simulata senza input)
                self.ciclo_cognitivo()
                
                # Delay tra cicli
                time.sleep(delay_cicli)
                
        except KeyboardInterrupt:
            print("\n\n⏸️  Interruzione manuale (Ctrl+C)")
        
        self.report_finale()
    
    def esegui_interattivo(self):
        """Modalità interattiva: ciclo con input utente"""
        print(f"\n🎮 Modalità interattiva")
        print("Comandi: 'q' per uscire, Enter per ciclo, 'stats' per statistiche\n")
        
        try:
            while True:
                comando = input(">>> ").strip().lower()
                
                if comando == 'q' or comando == 'quit':
                    break
                elif comando == 'stats':
                    self.mostra_statistiche()
                elif comando == 'ricarica':
                    self.tronco.ricarica_energia(50.0)
                elif comando == '':
                    # Esegui ciclo
                    self.ciclo_cognitivo()
                else:
                    print("Comando non riconosciuto")
                    
        except KeyboardInterrupt:
            print("\n\n⏸️  Interruzione")
        
        self.report_finale()
    
    def mostra_statistiche(self):
        """Mostra statistiche dettagliate"""
        print(f"\n{'='*70}")
        print("📊 STATISTICHE SISTEMA")
        print(f"{'='*70}")
        
        # Sistema
        stats_sistema = self.tronco.get_statistiche_sistema()
        print(f"\n🌙 Sistema:")
        for key, value in stats_sistema.items():
            print(f"  • {key}: {value}")
        
        # Memoria
        stats_memoria = self.ippocampo.get_statistiche()
        print(f"\n💾 Memoria:")
        for key, value in stats_memoria.items():
            print(f"  • {key}: {value}")
        
        # Emozioni/Reward
        stats_reward = self.amigdala.get_statistiche_reward()
        print(f"\n❤️  Reward:")
        for key, value in stats_reward.items():
            if key != 'ultimi_10':
                print(f"  • {key}: {value}")
        
        print(f"\n{'='*70}\n")
    
    def report_finale(self):
        """Report finale sessione"""
        print(f"\n{'='*70}")
        print("📋 REPORT FINALE SESSIONE")
        print(f"{'='*70}")
        
        print(f"\nCicli eseguiti: {self.cicli_eseguiti}")
        print(f"Errori totali: {self.errori_totali}")
        print(f"Tasso successo: {((self.cicli_eseguiti - self.errori_totali) / max(1, self.cicli_eseguiti) * 100):.1f}%")
        
        # Statistiche moduli
        self.mostra_statistiche()
        
        print(f"{'='*70}\n")
    
    def chiudi(self):
        """Shutdown completo sistema"""
        print(f"\n{'='*70}")
        print("🛑 SHUTDOWN SISTEMA")
        print(f"{'='*70}\n")
        
        # Chiudi moduli in ordine
        if self.motoria:
            self.motoria.fermati()
        
        if self.ippocampo:
            self.ippocampo.salva_su_disco()
            self.ippocampo.chiudi()
        
        if self.tronco:
            self.tronco.chiudi()
        
        if self.talamo:
            self.talamo.chiudi()
        
        self.attivo = False
        print(f"\n✅ Sistema spento correttamente\n")


def main():
    """Entry point principale"""
    
    # Parsing argomenti
    parser = argparse.ArgumentParser(
        description='🧠 Mente Artificiale Modulare - Sistema Cognitivo'
    )
    parser.add_argument(
        '--modalita',
        choices=['autonoma', 'interattiva', 'test'],
        default='autonoma',
        help='Modalità operativa'
    )
    parser.add_argument(
        '--durata',
        type=int,
        default=60,
        help='Durata modalità autonoma (secondi)'
    )
    parser.add_argument(
        '--delay',
        type=float,
        default=2.0,
        help='Delay tra cicli (secondi)'
    )
    
    args = parser.parse_args()
    
    # Banner
    print("""
    ╔════════════════════════════════════════════════════════════════╗
    ║                                                                ║
    ║           🧠 MENTE ARTIFICIALE MODULARE v1.0                  ║
    ║                                                                ║
    ║     Sistema cognitivo ispirato al cervello umano              ║
    ║                                                                ║
    ╚════════════════════════════════════════════════════════════════╝
    """)
    
    # Crea e inizializza mente
    mente = MenteArtificiale(modalita=args.modalita)
    
    if not mente.inizializza():
        print("❌ Inizializzazione fallita")
        return 1
    
    try:
        # Esegui modalità selezionata
        if args.modalita == 'autonoma':
            mente.esegui_autonomo(durata_secondi=args.durata, delay_cicli=args.delay)
        
        elif args.modalita == 'interattiva':
            mente.esegui_interattivo()
        
        elif args.modalita == 'test':
            # Esegui singolo ciclo di test
            print("\n🧪 Modalità test: singolo ciclo\n")
            mente.ciclo_cognitivo()
            mente.report_finale()
        
    except Exception as e:
        print(f"\n❌ ERRORE FATALE: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    finally:
        # Cleanup
        mente.chiudi()
    
    return 0


if __name__ == "__main__":
    sys.exit(main())

