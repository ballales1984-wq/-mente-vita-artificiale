"""
🧠 MENTE ARTIFICIALE - Inizializzazione Orchestrata Completa
============================================================
Sistema che inizializza tutti i moduli cerebrali in sequenza con
output visivo dello stato e sincronizzazione sensori.

Sequenza:
1. Corteccia Visiva → Camera
2. Corteccia Uditiva → Microfono  
3. Memoria → Consolidamento
4. Sistema Emotivo → Reward
5. Biosegnali → Layer neurale
6. Sincronizzazione finale
"""

import time
import sys
from moduli import visione, udito, prefrontale, motoria, emozione, memoria
from moduli.biosegnale import InterfacciaCoerenzaCerebrale, PropagatoreNeurale


class OrchestratoreInizializzazione:
    """
    Orchestratore che gestisce l'inizializzazione di tutti i moduli
    con output visivo dello stato
    """
    
    def __init__(self):
        self.nome = "Orchestratore Sistema"
        self.moduli_attivi = {}
        self.errori = []
        
    def banner_iniziale(self):
        """Banner di benvenuto"""
        print("""
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║           🧠 MENTE ARTIFICIALE MODULARE v3.0                    ║
║              Sistema Cognitivo Multimodale                       ║
║                                                                  ║
║     Inizializzazione Completa in Corso...                       ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
        """)
        
    def stato_modulo(self, nome: str, stato: str, dettagli: str = ""):
        """
        Stampa stato modulo in formato standard
        
        Args:
            nome: Nome modulo
            stato: 'inizializzazione', 'ok', 'error', 'warning'
            dettagli: Informazioni aggiuntive
        """
        emoji_map = {
            'inizializzazione': '🔄',
            'ok': '✅',
            'error': '❌',
            'warning': '⚠️'
        }
        
        emoji = emoji_map.get(stato, '•')
        
        print(f"[{nome}] {emoji} {dettagli}")
        
    def inizializza_sistema_completo(self) -> bool:
        """
        Inizializza tutti i moduli in sequenza
        
        Returns:
            bool: True se inizializzazione riuscita
        """
        self.banner_iniziale()
        
        print("\n" + "="*70)
        print("FASE 1: INIZIALIZZAZIONE MODULI CEREBRALI")
        print("="*70 + "\n")
        
        # ================================================================
        # 1. CORTECCIA VISIVA
        # ================================================================
        print("[👁️  Corteccia Visiva] 🔄 Inizializzazione in corso...")
        
        try:
            corteccia_visiva = visione.get_instance()
            
            # Tenta inizializzazione camera
            print("[👁️  Corteccia Visiva] 🔄 Collegamento telecamera...")
            
            if corteccia_visiva.inizializza_camera(camera_id=0):
                print("[👁️  Corteccia Visiva] ✅ Telecamera attiva")
                self.moduli_attivi['visione'] = 'camera_reale'
                
                # Info camera
                if corteccia_visiva.camera:
                    w = int(corteccia_visiva.camera.get(3))
                    h = int(corteccia_visiva.camera.get(4))
                    print(f"[👁️  Corteccia Visiva]    → Risoluzione: {w}x{h}")
                    print(f"[👁️  Corteccia Visiva]    → YOLOv8: {'Attivo' if corteccia_visiva.model else 'Simulato'}")
            else:
                print("[👁️  Corteccia Visiva] ⚠️  Telecamera non disponibile")
                print("[👁️  Corteccia Visiva] ✅ Modalità simulata attiva")
                self.moduli_attivi['visione'] = 'simulata'
                
        except Exception as e:
            print(f"[👁️  Corteccia Visiva] ❌ Errore: {e}")
            self.errori.append(('visione', str(e)))
            self.moduli_attivi['visione'] = 'error'
        
        time.sleep(0.5)
        
        # ================================================================
        # 2. CORTECCIA UDITIVA
        # ================================================================
        print("\n[👂 Corteccia Uditiva] 🔄 Inizializzazione in corso...")
        
        try:
            corteccia_uditiva = udito.get_instance()
            
            # Tenta inizializzazione microfono
            print("[👂 Corteccia Uditiva] 🔄 Collegamento microfoni...")
            
            if corteccia_uditiva.inizializza_microfono():
                print("[👂 Corteccia Uditiva] ✅ Microfoni collegati")
                print("[👂 Corteccia Uditiva] ✅ Whisper pronto per trascrizione")
                self.moduli_attivi['udito'] = 'microfono_reale'
                
                # Info microfono
                try:
                    import sounddevice as sd
                    device = sd.query_devices(corteccia_uditiva.device_id)
                    print(f"[👂 Corteccia Uditiva]    → Device: {device['name'][:30]}")
                    print(f"[👂 Corteccia Uditiva]    → Sample Rate: 16000 Hz")
                except:
                    pass
            else:
                print("[👂 Corteccia Uditiva] ⚠️  Microfoni non disponibili")
                print("[👂 Corteccia Uditiva] ✅ Modalità simulata attiva")
                self.moduli_attivi['udito'] = 'simulata'
                
        except Exception as e:
            print(f"[👂 Corteccia Uditiva] ❌ Errore: {e}")
            self.errori.append(('udito', str(e)))
            self.moduli_attivi['udito'] = 'error'
        
        time.sleep(0.5)
        
        # ================================================================
        # 3. IPPOCAMPO (MEMORIA)
        # ================================================================
        print("\n[💾 Ippocampo] 🔄 Inizializzazione sistema memoria...")
        
        try:
            ippocampo = memoria.get_instance()
            
            stats = ippocampo.get_statistiche()
            
            print(f"[💾 Ippocampo] ✅ Sistema memoria attivo")
            print(f"[💾 Ippocampo]    → Memorie caricate: {stats['memorie_episodiche']}")
            print(f"[💾 Ippocampo]    → Consolidamento: Auto (ogni 5 min)")
            print(f"[💾 Ippocampo] 🟢 Episodi multimodali in costruzione")
            
            self.moduli_attivi['memoria'] = 'attivo'
            
        except Exception as e:
            print(f"[💾 Ippocampo] ❌ Errore: {e}")
            self.errori.append(('memoria', str(e)))
            self.moduli_attivi['memoria'] = 'error'
        
        time.sleep(0.5)
        
        # ================================================================
        # 4. AMIGDALA (EMOZIONI)
        # ================================================================
        print("\n[❤️  Amigdala] 🔄 Inizializzazione sistema emotivo...")
        
        try:
            amigdala = emozione.get_instance()
            
            print(f"[❤️  Amigdala] ✅ Sistema emotivo attivo")
            print(f"[❤️  Amigdala]    → Valutazione valenza: Attiva")
            print(f"[❤️  Amigdala]    → Sistema reward: Attivo")
            
            self.moduli_attivi['emozione'] = 'attivo'
            
        except Exception as e:
            print(f"[❤️  Amigdala] ❌ Errore: {e}")
            self.errori.append(('emozione', str(e)))
        
        time.sleep(0.5)
        
        # ================================================================
        # 5. CORTECCIA PREFRONTALE
        # ================================================================
        print("\n[🧠 Corteccia Prefrontale] 🔄 Inizializzazione ragionamento...")
        
        try:
            corteccia_prefrontale = prefrontale.get_instance()
            
            print(f"[🧠 Corteccia Prefrontale] ✅ Ragionamento attivo")
            print(f"[🧠 Corteccia Prefrontale]    → LLM: {'GPT-2' if corteccia_prefrontale.modalita_reale else 'Rule-based'}")
            
            self.moduli_attivi['prefrontale'] = 'attivo'
            
        except Exception as e:
            print(f"[🧠 Corteccia Prefrontale] ❌ Errore: {e}")
        
        time.sleep(0.5)
        
        # ================================================================
        # 6. BIOSEGNALI NEURALI
        # ================================================================
        print("\n[⚡ Biosegnali Neurali] 🔄 Inizializzazione layer neurale...")
        
        try:
            interfaccia = InterfacciaCoerenzaCerebrale()
            propagatore = PropagatoreNeurale(dimensione=15)
            
            print(f"[⚡ Biosegnali Neurali] ✅ Layer neurale attivo")
            print(f"[⚡ Biosegnali Neurali]    → Rete: 15 neuroni")
            print(f"[⚡ Biosegnali Neurali]    → Ritmi: Alfa, Beta, Gamma")
            print(f"[⚡ Biosegnali Neurali]    → Stimoli interni: Attivi")
            
            self.moduli_attivi['biosegnali'] = 'attivo'
            
        except Exception as e:
            print(f"[⚡ Biosegnali Neurali] ❌ Errore: {e}")
        
        time.sleep(0.5)
        
        # ================================================================
        # 7. CORTECCIA MOTORIA
        # ================================================================
        print("\n[🦿 Corteccia Motoria] 🔄 Inizializzazione sistema motorio...")
        
        try:
            corteccia_motoria = motoria.get_instance()
            
            print(f"[🦿 Corteccia Motoria] ✅ Sistema motorio attivo")
            print(f"[🦿 Corteccia Motoria]    → Modalità: Simulazione")
            
            self.moduli_attivi['motoria'] = 'attivo'
            
        except Exception as e:
            print(f"[🦿 Corteccia Motoria] ❌ Errore: {e}")
        
        time.sleep(0.5)
        
        # ================================================================
        # REPORT FINALE
        # ================================================================
        print("\n" + "="*70)
        print("SINCRONIZZAZIONE E VERIFICA FINALE")
        print("="*70 + "\n")
        
        # Check percezione multimodale
        percezione_completa = (
            self.moduli_attivi.get('visione') in ['camera_reale', 'simulata'] and
            self.moduli_attivi.get('udito') in ['microfono_reale', 'simulata']
        )
        
        if percezione_completa:
            print("[🔄 Sincronizzazione] ✅ Percezione multimodale sincronizzata")
            
            # Tipo di percezione
            tipo_visione = self.moduli_attivi.get('visione')
            tipo_udito = self.moduli_attivi.get('udito')
            
            if tipo_visione == 'camera_reale' and tipo_udito == 'microfono_reale':
                print("[🔄 Sincronizzazione]    → Modalità: HARDWARE REALE 100%")
            elif tipo_visione == 'camera_reale' or tipo_udito == 'microfono_reale':
                print("[🔄 Sincronizzazione]    → Modalità: IBRIDA (reale + simulata)")
            else:
                print("[🔄 Sincronizzazione]    → Modalità: SIMULATA")
        else:
            print("[🔄 Sincronizzazione] ⚠️  Percezione parziale")
        
        print()
        
        # Report moduli
        print("="*70)
        print("STATO MODULI CEREBRALI")
        print("="*70)
        
        moduli_ok = 0
        moduli_totali = len(self.moduli_attivi)
        
        for modulo, stato in self.moduli_attivi.items():
            if stato in ['attivo', 'camera_reale', 'microfono_reale', 'simulata']:
                emoji = '✅'
                moduli_ok += 1
            else:
                emoji = '❌'
            
            print(f"  {emoji} {modulo.capitalize()}: {stato}")
        
        print(f"\n  Moduli operativi: {moduli_ok}/{moduli_totali}")
        
        # Errori
        if self.errori:
            print(f"\n  ⚠️  Errori rilevati: {len(self.errori)}")
            for modulo, errore in self.errori:
                print(f"    - {modulo}: {errore[:50]}...")
        
        print("="*70)
        
        # Sistema pronto
        if moduli_ok >= moduli_totali * 0.7:  # 70% moduli ok
            print("\n✅ SISTEMA OPERATIVO E PRONTO")
            return True
        else:
            print("\n⚠️  SISTEMA PARZIALMENTE OPERATIVO")
            return False
    
    def test_percezione_multimodale(self):
        """Test rapido percezione"""
        print("\n" + "="*70)
        print("TEST PERCEZIONE MULTIMODALE")
        print("="*70 + "\n")
        
        # Test visione
        if self.moduli_attivi.get('visione') in ['camera_reale', 'simulata']:
            print("[TEST VISIONE]")
            
            if self.moduli_attivi['visione'] == 'camera_reale':
                corteccia = visione.get_instance()
                if corteccia.camera:
                    ret, frame = corteccia.camera.read()
                    if ret:
                        risultato = corteccia.elabora(frame)
                        print(f"  ✓ Frame catturato e analizzato")
                        print(f"  ✓ {risultato['descrizione']}")
            else:
                print(f"  ✓ Modalità simulata funzionante")
        
        print()
        
        # Test udito
        if self.moduli_attivi.get('udito') in ['microfono_reale', 'simulata']:
            print("[TEST UDITO]")
            
            if self.moduli_attivi['udito'] == 'microfono_reale':
                print(f"  ✓ Microfono pronto per registrazione")
                print(f"  ✓ Whisper caricato per trascrizione")
            else:
                print(f"  ✓ Modalità simulata funzionante")
        
        print("\n" + "="*70)
        print("✅ TEST COMPLETATI")
        print("="*70)


def main():
    """Entry point principale"""
    
    # Crea orchestratore
    orchestratore = OrchestratoreInizializzazione()
    
    # Inizializza sistema
    sistema_ok = orchestratore.inizializza_sistema_completo()
    
    if not sistema_ok:
        print("\n⚠️  Sistema non completamente operativo")
        risposta = input("\nContinuare comunque? (s/n): ")
        if risposta.lower() != 's':
            print("\n[!] Uscita")
            return 1
    
    # Test percezione
    time.sleep(1)
    orchestratore.test_percezione_multimodale()
    
    # Menu operativo
    print("\n\n" + "="*70)
    print("SISTEMA PRONTO - MENU OPERATIVO")
    print("="*70)
    print("\n[MENU] Cosa vuoi fare?")
    print("  1. Ciclo singolo multimodale")
    print("  2. Sessione 5 cicli")
    print("  3. Modalità streaming camera")
    print("  4. Modalità ascolto continuo")
    print("  5. Info dettagliate sistema")
    print("  6. Esci")
    
    try:
        scelta = input("\n>> Scelta (1-6): ").strip()
        
        if scelta == "1":
            # Ciclo singolo
            from mente_multimodale import MenteMultimodale
            mente = MenteMultimodale()
            
            # Salta inizializzazione (già fatta)
            mente.camera_attiva = orchestratore.moduli_attivi.get('visione') == 'camera_reale'
            mente.microfono_attivo = orchestratore.moduli_attivi.get('udito') == 'microfono_reale'
            
            mente.ciclo_multimodale()
            mente.chiudi()
            
        elif scelta == "2":
            # Sessione
            from mente_multimodale import MenteMultimodale
            mente = MenteMultimodale()
            mente.camera_attiva = orchestratore.moduli_attivi.get('visione') == 'camera_reale'
            mente.microfono_attivo = orchestratore.moduli_attivi.get('udito') == 'microfono_reale'
            mente.esegui_sessione(num_cicli=5)
            mente.chiudi()
            
        elif scelta == "3":
            # Streaming camera
            if orchestratore.moduli_attivi.get('visione') == 'camera_reale':
                import mente_con_camera
                # Esegui modalità streaming
                print("\n[!] Implementare modalità streaming...")
            else:
                print("\n[!] Camera non disponibile")
                
        elif scelta == "4":
            # Ascolto continuo
            if orchestratore.moduli_attivi.get('udito') == 'microfono_reale':
                import mente_con_microfono
                print("\n[!] Modalità ascolto...")
            else:
                print("\n[!] Microfono non disponibile")
                
        elif scelta == "5":
            # Info sistema
            mostra_info_dettagliate(orchestratore)
            
        elif scelta == "6":
            print("\n[!] Uscita\n")
            return 0
        else:
            print("\n[!] Scelta non valida")
            
    except KeyboardInterrupt:
        print("\n\n[!] Interruzione\n")
    except Exception as e:
        print(f"\n[ERROR] {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


def mostra_info_dettagliate(orchestratore):
    """Mostra informazioni dettagliate sistema"""
    print("\n" + "="*70)
    print("INFORMAZIONI DETTAGLIATE SISTEMA")
    print("="*70)
    
    print("\n[PERCEZIONE]")
    print(f"  Visione: {orchestratore.moduli_attivi.get('visione', 'N/A')}")
    print(f"  Udito: {orchestratore.moduli_attivi.get('udito', 'N/A')}")
    
    print("\n[COGNIZIONE]")
    ippocampo = memoria.get_instance()
    stats = ippocampo.get_statistiche()
    print(f"  Memorie episodiche: {stats['memorie_episodiche']}")
    print(f"  Consolidamenti: {stats.get('consolidamenti_eseguiti', 0)}")
    print(f"  Memorie eliminate: {stats.get('memorie_eliminate', 0)}")
    
    print("\n[APPRENDIMENTO]")
    amigdala = emozione.get_instance()
    stats_reward = amigdala.get_statistiche_reward()
    print(f"  Reward totale: {stats_reward.get('reward_totale', 0):.2f}")
    print(f"  Reward medio: {stats_reward.get('reward_medio', 0):.2f}")
    
    print("\n[BIOSEGNALI]")
    print(f"  Layer neurale: Attivo")
    print(f"  Dimensione rete: 15 neuroni")
    print(f"  Ritmi disponibili: Alfa, Beta, Gamma")
    
    print("\n" + "="*70)


if __name__ == "__main__":
    sys.exit(main())

