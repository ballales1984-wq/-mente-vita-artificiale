"""
🧠⚡ MENTE ARTIFICIALE COMPLETA - Versione Finale v3.0
======================================================
Sistema cognitivo multimodale completo con:
- Percezione: Camera + Microfono
- Memoria: Intelligente con consolidamento
- Biosegnali: Layer neurale
- Apprendimento: Online learning con PyTorch
- Emozioni: Sistema reward
- Ragionamento: LLM + esperienza

Autore: Alessio + Cursor AI
Data: 22 Ottobre 2025
"""

import time
import sys
from typing import Dict, Any
from moduli import visione, udito, prefrontale, motoria, emozione, memoria
from moduli.biosegnale import InterfacciaCoerenzaCerebrale, PropagatoreNeurale
from moduli.apprendimento_online import ApprendimentoOnline


class MenteArtificialeCompleta:
    """
    Sistema cognitivo artificiale completo
    
    Architettura:
    [Layer Sensoriale] → Camera + Microfono
    [Layer Neurale] → Biosegnali, Pattern, Ritmi
    [Layer Cognitivo] → Memoria, Emozione, Ragionamento
    [Layer Apprendimento] → Online learning real-time
    [Layer Motorio] → Azioni, Feedback
    """
    
    def __init__(self):
        self.nome = "Mente Artificiale Completa"
        self.versione = "3.0"
        
        print(f"\n{'='*70}")
        print(f"[{self.nome}] v{self.versione}")
        print(f"{'='*70}\n")
        
        # Inizializzazione moduli
        self._inizializza_tutti_moduli()
    
    def _inizializza_tutti_moduli(self):
        """Inizializza tutti i moduli cerebrali"""
        
        print("[🧠] Inizio ciclo cognitivo completo\n")
        
        # PERCEZIONE
        print("[👁️ ] Corteccia Visiva: 🔄 Inizializzazione...")
        self.corteccia_visiva = visione.get_instance()
        self.camera_attiva = self.corteccia_visiva.inizializza_camera(0)
        if self.camera_attiva:
            print("[👁️ ] Corteccia Visiva: ✅ Telecamera attiva")
        else:
            print("[👁️ ] Corteccia Visiva: ⚠️  Modalità simulata")
        
        print("\n[👂] Corteccia Uditiva: 🔄 Collegamento microfoni...")
        self.corteccia_uditiva = udito.get_instance()
        self.microfono_attivo = self.corteccia_uditiva.inizializza_microfono()
        if self.microfono_attivo:
            print("[👂] Corteccia Uditiva: ✅ Microfoni collegati - Whisper pronto")
        else:
            print("[👂] Corteccia Uditiva: ⚠️  Modalità simulata")
        
        # MEMORIA
        print("\n[💾] Memoria: 🔄 Caricamento episodi...")
        self.ippocampo = memoria.get_instance()
        print("[💾] Memoria: ✅ Sistema memoria attivo")
        print("[💾] Memoria: 🟢 Episodi multimodali in costruzione")
        
        # EMOZIONI
        print("\n[😊] Emozione: 🔄 Inizializzazione...")
        self.amigdala = emozione.get_instance()
        print("[😊] Emozione: ✅ Valutazione stimoli attiva")
        
        # BIOSEGNALI
        print("\n[🧬] Biosegnali: 🔄 Inizializzazione...")
        self.interfaccia_neurale = InterfacciaCoerenzaCerebrale()
        self.propagatore = PropagatoreNeurale(dimensione=15)
        print("[🧬] Biosegnali: ✅ Codifica binaria attiva")
        
        # RAGIONAMENTO
        print("\n[🧠] Prefrontale: 🔄 Caricamento...")
        self.prefrontale = prefrontale.get_instance()
        print("[🧠] Prefrontale: ✅ Ragionamento operativo")
        
        # MOTORIA
        print("\n[🦾] Motoria: 🔄 Inizializzazione...")
        self.motoria = motoria.get_instance()
        print("[🦾] Motoria: ✅ Sistema motorio pronto")
        
        # APPRENDIMENTO ONLINE
        print("\n[🎓] Apprendimento: 🔄 Inizializzazione rete neurale...")
        self.apprendimento = ApprendimentoOnline()
        print("[🎓] Apprendimento: ✅ Online learning attivo")
        
        print(f"\n{'='*70}")
        print("[🚀] Sistema: ✅ Tutti i moduli inizializzati")
        print("[🚀] Sistema: ✅ Mente artificiale operativa")
        print(f"{'='*70}\n")
        
        self.cicli_eseguiti = 0
    
    def ciclo_cognitivo_completo(self) -> Dict[str, Any]:
        """
        Ciclo cognitivo completo con tutti i moduli
        
        Returns:
            Dict con risultati completi
        """
        self.cicli_eseguiti += 1
        
        print(f"\n{'╔'+'═'*68+'╗'}")
        print(f"║ CICLO COGNITIVO COMPLETO #{self.cicli_eseguiti:02d}                                  ║")
        print(f"{'╚'+'═'*68+'╝'}\n")
        
        # ================================================================
        # FASE 1: PERCEZIONE VISIVA
        # ================================================================
        print("[1/9] 👁️  PERCEZIONE VISIVA")
        
        if self.camera_attiva and self.corteccia_visiva.camera:
            ret, frame = self.corteccia_visiva.camera.read()
            if ret:
                risultato_visivo = self.corteccia_visiva.elabora(frame)
                tipo_vis = "CAMERA REALE"
            else:
                risultato_visivo = visione.elabora("immagine.jpg")
                tipo_vis = "SIMULATA"
        else:
            risultato_visivo = visione.elabora("immagine.jpg")
            tipo_vis = "SIMULATA"
        
        print(f"      {risultato_visivo['descrizione']} [{tipo_vis}]")
        
        # ================================================================
        # FASE 2: PERCEZIONE UDITIVA
        # ================================================================
        print("\n[2/9] 👂 PERCEZIONE UDITIVA")
        
        if self.microfono_attivo:
            print("      🎤 Registrazione (3s)... PARLA ORA!")
            
            import sounddevice as sd
            audio = sd.rec(int(3 * 16000), samplerate=16000, channels=1)
            sd.wait()
            
            risultato_audio = self.corteccia_uditiva.ascolta(audio.flatten())
            tipo_aud = "MICROFONO REALE" if risultato_audio['testo'] else "SILENZIO"
        else:
            risultato_audio = udito.ascolta("audio.wav")
            tipo_aud = "SIMULATA"
        
        print(f"      '{risultato_audio['testo']}' [{tipo_aud}]")
        
        # ================================================================
        # FASE 3: CODIFICA NEURALE
        # ================================================================
        print("\n[3/9] 🧬 BIOSEGNALI NEURALI")
        
        percezioni = [risultato_visivo, risultato_audio]
        onda_percezione = self.interfaccia_neurale.percepisce_segnale(percezioni)
        
        visual_pattern = onda_percezione.pattern.replace('1', '█').replace('0', '░')
        print(f"      Pattern: {visual_pattern}")
        print(f"      Neuroni attivi: {onda_percezione.neuroni_attivi}/{len(onda_percezione.pattern)}")
        
        # ================================================================
        # FASE 4: RICHIAMO MEMORIA
        # ================================================================
        print("\n[4/9] 💾 RICHIAMO MEMORIA CONTESTUALE")
        
        contesto = f"{risultato_visivo['descrizione']} {risultato_audio['testo']}"
        memorie, suggerimenti = self.ippocampo.richiama_contestuale(contesto, top_k=3)
        
        if memorie:
            print(f"      Memorie trovate: {len(memorie)}")
            print(f"      Suggerimento: {suggerimenti['suggerimento']}")
            if suggerimenti.get('azione_consigliata'):
                print(f"      Azione consigliata: {suggerimenti['azione_consigliata']} (conf: {suggerimenti['confidence']:.2f})")
        else:
            print(f"      Nessuna memoria rilevante")
        
        # ================================================================
        # FASE 5: VALUTAZIONE EMOTIVA
        # ================================================================
        print("\n[5/9] 😊 VALUTAZIONE EMOTIVA")
        
        risultato_emozione = self.amigdala.elabora({
            'percezioni': percezioni,
            'memoria': {'suggerimenti': suggerimenti}
        })
        
        stato_emotivo = risultato_emozione.dati['stato_emotivo']
        valenza = risultato_emozione.dati['valenza']
        
        print(f"      Stato: {stato_emotivo.upper()} (valenza: {valenza:+.2f})")
        
        # ================================================================
        # FASE 6: APPRENDIMENTO ONLINE (Predizione)
        # ================================================================
        print("\n[6/9] 🎓 APPRENDIMENTO ONLINE - Predizione")
        
        # Codifica stimolo
        stimolo = self.apprendimento.codifica_stimolo(risultato_visivo, risultato_audio)
        
        # Predici azione
        azione_predetta, confidence_pred = self.apprendimento.predici_azione(stimolo)
        
        print(f"      Rete neurale suggerisce: {azione_predetta} (conf: {confidence_pred:.2%})")
        
        # ================================================================
        # FASE 7: RAGIONAMENTO E DECISIONE
        # ================================================================
        print("\n[7/9] 🧠 RAGIONAMENTO E DECISIONE")
        
        decisione = self.prefrontale.ragiona(
            percezioni_visive=risultato_visivo,
            percezioni_uditive=risultato_audio,
            stato_emotivo=stato_emotivo,
            memoria=[m.contenuto for m in memorie]
        )
        
        # Combina suggerimenti: memoria + rete neurale
        if suggerimenti.get('confidence', 0) > 0.8:
            # Memoria molto sicura
            decisione['azione'] = suggerimenti['azione_consigliata']
            fonte = "memoria"
        elif confidence_pred > 0.7:
            # Rete neurale sicura
            decisione['azione'] = azione_predetta
            fonte = "rete_neurale"
        else:
            # Usa ragionamento base
            fonte = "ragionamento"
        
        print(f"      Decisione: {decisione['azione'].upper()}")
        print(f"      Fonte: {fonte}")
        print(f"      Priorità: {decisione['priorita']:.2f}")
        
        # ================================================================
        # FASE 8: ESECUZIONE AZIONE
        # ================================================================
        print("\n[8/9] 🦾 ESECUZIONE AZIONE")
        
        successo = self.motoria.agisci(decisione)
        print(f"      Risultato: {'✅ SUCCESSO' if successo else '❌ FALLITO'}")
        
        # ================================================================
        # FASE 9: APPRENDIMENTO E CONSOLIDAMENTO
        # ================================================================
        print("\n[9/9] 🎓 APPRENDIMENTO DA ESPERIENZA")
        
        # Reward
        reward = self.amigdala.assegna_reward(decisione['azione'], successo, valenza)
        print(f"      Reward: {reward:+.2f}")
        
        # Aggiorna rete neurale
        if self.apprendimento.modello:
            loss = self.apprendimento.apprendi_da_esperienza(stimolo, decisione['azione'], reward)
            print(f"      Loss rete: {loss:.4f}")
        
        # Memorizza episodio
        self.ippocampo.memorizza(
            f"ciclo_completo_{self.cicli_eseguiti}",
            f"V:{risultato_visivo['descrizione'][:25]} | A:{risultato_audio['testo'][:25]} | {decisione['azione']}",
            metadata={
                'valenza': valenza,
                'importanza': reward / 2.0 + 0.5,
                'pattern_neurale': onda_percezione.pattern,
                'tipo_visione': tipo_vis,
                'tipo_audio': tipo_aud,
                'fonte_decisione': fonte,
                'contesto': {
                    'ciclo': self.cicli_eseguiti,
                    'successo': successo,
                    'azione': decisione['azione']
                }
            }
        )
        
        print(f"      Episodio multimodale salvato")
        
        # ================================================================
        # REPORT CICLO
        # ================================================================
        print(f"\n{'─'*70}")
        print(f"[REPORT CICLO #{self.cicli_eseguiti}]")
        print(f"  Input: {tipo_vis} + {tipo_aud}")
        print(f"  Pattern: {onda_percezione.neuroni_attivi} neuroni attivi")
        print(f"  Memorie richiamate: {len(memorie)}")
        print(f"  Decisione: {decisione['azione']} (fonte: {fonte})")
        print(f"  Reward: {reward:+.2f}")
        
        # Statistiche apprendimento
        if self.apprendimento.modello:
            stats_app = self.apprendimento.get_statistiche()
            print(f"  Apprendimenti: {stats_app['cicli_apprendimento']}")
            print(f"  Loss media: {stats_app['loss_media']:.4f}")
        
        print(f"{'─'*70}")
        
        return {
            'ciclo': self.cicli_eseguiti,
            'decisione': decisione,
            'successo': successo,
            'reward': reward,
            'pattern': onda_percezione.pattern,
            'fonte': fonte
        }
    
    def esegui_sessione(self, num_cicli: int = 5, interattivo: bool = True):
        """
        Esegue sessione completa
        
        Args:
            num_cicli: Numero di cicli
            interattivo: Se chiedere conferma tra cicli
        """
        print(f"\n[SESSIONE] {num_cicli} cicli completi\n")
        
        risultati = []
        
        try:
            for i in range(num_cicli):
                risultato = self.ciclo_cognitivo_completo()
                risultati.append(risultato)
                
                if i < num_cicli - 1:
                    if interattivo:
                        input("\n[PREMI ENTER per continuare] ")
                    else:
                        time.sleep(2)
                        
        except KeyboardInterrupt:
            print("\n\n[!] Interruzione manuale")
        
        # Report finale
        self.report_finale(risultati)
    
    def report_finale(self, risultati: list):
        """Report finale dettagliato"""
        print(f"\n{'╔'+'═'*68+'╗'}")
        print(f"║ REPORT FINALE SESSIONE                                           ║")
        print(f"{'╚'+'═'*68+'╝'}\n")
        
        # Statistiche cicli
        print(f"[CICLI ESEGUITI] {len(risultati)}")
        
        if risultati:
            successi = sum(1 for r in risultati if r['successo'])
            reward_totale = sum(r['reward'] for r in risultati)
            
            print(f"  Successi: {successi}/{len(risultati)} ({successi/len(risultati)*100:.0f}%)")
            print(f"  Reward totale: {reward_totale:+.2f}")
            print(f"  Reward medio: {reward_totale/len(risultati):+.2f}")
        
        # Statistiche memoria
        print(f"\n[MEMORIA]")
        stats_mem = self.ippocampo.get_statistiche()
        print(f"  Episodi: {stats_mem['memorie_episodiche']}")
        print(f"  Richiami: {stats_mem['richiami_totali']}")
        print(f"  Consolidamenti: {stats_mem.get('consolidamenti_eseguiti', 0)}")
        print(f"  Eliminate: {stats_mem.get('memorie_eliminate', 0)}")
        
        # Statistiche apprendimento
        if self.apprendimento.modello:
            print(f"\n[APPRENDIMENTO]")
            stats_app = self.apprendimento.get_statistiche()
            print(f"  Cicli training: {stats_app['cicli_apprendimento']}")
            print(f"  Loss media: {stats_app['loss_media']:.4f}")
            print(f"  Modello salvato: {'✅' if stats_app['modello_salvato'] else '❌'}")
        
        # Analisi decisioni
        if risultati:
            print(f"\n[ANALISI DECISIONI]")
            fonti = {}
            for r in risultati:
                fonte = r.get('fonte', 'unknown')
                fonti[fonte] = fonti.get(fonte, 0) + 1
            
            for fonte, count in fonti.items():
                print(f"  {fonte}: {count}/{len(risultati)} ({count/len(risultati)*100:.0f}%)")
        
        print(f"\n{'='*70}")
        
        # Salva
        self.ippocampo.salva_su_disco()
        if self.apprendimento.modello:
            self.apprendimento.salva_modello()
        
        print("[OK] Memoria e modello salvati\n")
    
    def chiudi(self):
        """Chiude tutti i sensori"""
        print("\n[SHUTDOWN] Chiusura sistema...")
        
        # Chiudi camera
        try:
            self.corteccia_visiva.chiudi()
        except:
            pass
        
        # Chiudi finestre OpenCV
        try:
            import cv2
            cv2.destroyAllWindows()
        except:
            pass
        
        print("[OK] Sistema spento\n")


if __name__ == "__main__":
    print("""
====================================================================

        MENTE ARTIFICIALE COMPLETA v3.0
        
    Sistema Cognitivo Multimodale con Apprendimento Online
        
====================================================================
    """)
    
    try:
        # Crea mente
        mente = MenteArtificialeCompleta()
        
        # Menu
        print("\n[MENU] Modalità:")
        print("  1. Ciclo singolo")
        print("  2. Sessione 3 cicli (interattiva)")
        print("  3. Sessione 5 cicli (automatica)")
        
        scelta = input("\n>> Scelta (1-3): ").strip()
        
        if scelta == "1":
            mente.ciclo_cognitivo_completo()
            mente.report_finale([])
        elif scelta == "2":
            mente.esegui_sessione(num_cicli=3, interattivo=True)
        elif scelta == "3":
            mente.esegui_sessione(num_cicli=5, interattivo=False)
        else:
            print("[!] Scelta non valida")
        
        mente.chiudi()
        
    except KeyboardInterrupt:
        print("\n\n[!] Interruzione\n")
    except Exception as e:
        print(f"\n[ERROR] {e}")
        import traceback
        traceback.print_exc()

