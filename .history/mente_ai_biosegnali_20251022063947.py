"""
🧠⚡ MENTE ARTIFICIALE CON BIOSEGNALI NEURALI
==============================================
Sistema cognitivo completo con layer di segnali bioelettrici.

Caratteristiche:
- Ogni ciclo ha una "firma binaria" neurale
- Stimoli interni spontanei simulano pensieri
- Pattern neurali influenzano emozioni e decisioni
- Pronto per sensori EEG/EMG reali
- Visualizzazione attività neurale in tempo reale
"""

import time
import sys
from typing import Dict, Any, List
from moduli import visione, udito, prefrontale, motoria, emozione, memoria
from moduli.biosegnale import PropagatoreNeurale, InterfacciaCoerenzaCerebrale, StimoloInterno, RitmoNeurale, VisualizzatoreNeurale


class MenteConBiosegnali:
    """
    Mente Artificiale con sistema di biosegnali neurali integrato
    
    Architettura:
    [Layer Neurale] → Pattern binari, propagazione, ritmi
         ↓
    [Layer Cognitivo] → Percezione, ragionamento, azione
         ↓
    [Layer Motorio] → Output azioni
    """
    
    def __init__(self):
        self.nome = "Mente con Biosegnali"
        self.versione = "2.0"
        
        # Layer neurale
        self.interfaccia_neurale = InterfacciaCoerenzaCerebrale()
        self.generatore_stimoli = StimoloInterno()
        self.ritmo_neurale = RitmoNeurale(dimensione=15)
        
        # Moduli cognitivi
        self.ippocampo = memoria.get_instance()
        self.amigdala = emozione.get_instance()
        
        # Storia attività neurale
        self.storia_pattern_neurali = []
        self.energia_neurale = 100.0
        
        # Stato arousal
        self.arousal = 0.5  # 0=calmo, 1=eccitato
        
    def ciclo_completo_con_biosegnali(self, input_visivo=None, input_uditivo=None):
        """
        Ciclo cognitivo completo con biosegnali neurali
        
        Returns:
            Dict con risultati e pattern neurale
        """
        ciclo_num = len(self.storia_pattern_neurali) + 1
        
        print(f"\n{'='*70}")
        print(f"[CICLO NEURALE #{ciclo_num}]")
        print(f"{'='*70}\n")
        
        # ================================================================
        # LAYER NEURALE: Generazione pattern bioelettrico
        # ================================================================
        print("[LAYER NEURALE] Generazione firma binaria ciclo...")
        
        # Stato base neurale (ritmo di background)
        if self.arousal < 0.3:
            # Calmo → ritmo alfa
            print("  Ritmo base: ALFA (rilassato)")
            pattern_base = self.ritmo_neurale.genera_ritmo_alfa(durata_cicli=3)
        elif self.arousal > 0.7:
            # Eccitato → ritmo gamma
            print("  Ritmo base: GAMMA (concentrato)")
            pattern_base = self.ritmo_neurale.genera_ritmo_gamma(durata_cicli=3)
        else:
            # Normale → ritmo beta
            print("  Ritmo base: BETA (attivo)")
            pattern_base = self.ritmo_neurale.genera_ritmo_beta(durata_cicli=3)
        
        firma_neurale = pattern_base[-1]
        print(f"  Firma neurale ciclo: {firma_neurale.pattern}")
        print(f"  Neuroni attivi: {firma_neurale.neuroni_attivi}")
        print(f"  Stato: {firma_neurale.stato.value}")
        
        # ================================================================
        # STIMOLO INTERNO: Pensiero spontaneo (10% probabilità)
        # ================================================================
        import random
        if random.random() < 0.1:
            print("\n[STIMOLO INTERNO] Generazione pensiero spontaneo...")
            pensiero = self.generatore_stimoli.genera_pensiero_spontaneo()
            print(f"  Pensiero generato: {len(pensiero)} cicli di attivazione")
            print(f"  Pattern: {pensiero[-1].pattern}")
            
            # Il pensiero influenza l'arousal
            self.arousal = min(1.0, self.arousal + 0.1)
        
        # ================================================================
        # LAYER COGNITIVO: Percezione
        # ================================================================
        print(f"\n[LAYER COGNITIVO] Elaborazione percezioni...")
        
        # Visione
        risultato_visivo = visione.elabora(input_visivo or "immagine.jpg")
        print(f"  Visione: {risultato_visivo['descrizione']}")
        
        # Udito
        risultato_audio = udito.ascolta(input_uditivo or "audio.wav")
        print(f"  Udito: '{risultato_audio['testo']}'")
        
        # Converti percezioni in segnale neurale
        percezioni = [risultato_visivo, risultato_audio]
        onda_percezione = self.interfaccia_neurale.percepisce_segnale(percezioni)
        print(f"\n  Codifica neurale percezioni: {onda_percezione.pattern}")
        print(f"  Intensita neurale: {onda_percezione.neuroni_attivi}/{len(onda_percezione.pattern)}")
        
        # ================================================================
        # RICHIAMO MEMORIA CONTESTUALE
        # ================================================================
        print(f"\n[MEMORIA] Richiamo contestuale...")
        contesto = f"{risultato_visivo['descrizione']} {risultato_audio['testo']}"
        memorie_rilevanti, suggerimenti = self.ippocampo.richiama_contestuale(contesto, top_k=3)
        
        if memorie_rilevanti:
            print(f"  Memorie trovate: {len(memorie_rilevanti)}")
            for mem in memorie_rilevanti[:2]:
                print(f"    - {mem.contenuto[:45]}...")
        else:
            print(f"  Nessuna memoria rilevante")
        
        # ================================================================
        # EMOZIONE (influenzata da pattern neurale)
        # ================================================================
        print(f"\n[EMOZIONE] Valutazione (influenzata da biosegnali)...")
        
        risultato_emozione = self.amigdala.elabora({
            'percezioni': percezioni,
            'memoria': {'suggerimenti': suggerimenti}
        })
        
        stato_emotivo = risultato_emozione.dati['stato_emotivo']
        valenza = risultato_emozione.dati['valenza']
        
        # Genera pattern neurale dell'emozione
        onda_emozione = self.interfaccia_neurale.stato_emotivo_a_pattern(stato_emotivo, valenza)
        
        print(f"  Stato: {stato_emotivo.upper()} (valenza: {valenza:+.2f})")
        print(f"  Pattern neurale emozione: {onda_emozione.pattern}")
        
        # ================================================================
        # DECISIONE (influenzata da pattern neurale)
        # ================================================================
        print(f"\n[RAGIONAMENTO] Decisione con influenza neurale...")
        
        # Decodifica pattern per decision making
        influenza_neurale = self.interfaccia_neurale.decodifica_per_decisione(onda_percezione)
        
        decisione = prefrontale.ragiona(
            percezioni_visive=risultato_visivo,
            percezioni_uditive=risultato_audio,
            stato_emotivo=stato_emotivo,
            memoria=[m.contenuto for m in memorie_rilevanti]
        )
        
        # Applica influenza biosegnali
        print(f"\n  Influenza biosegnali:")
        print(f"    Intensita cognitiva: {influenza_neurale['intensita_cognitiva']:.2f}")
        print(f"    Urgenza: {influenza_neurale['urgenza']:.2f}")
        print(f"    Consiglio neurale: {influenza_neurale['consiglio']}")
        
        # Modifica priorità basata su urgenza neurale
        decisione['priorita'] = min(1.0, decisione['priorita'] * (1 + influenza_neurale['urgenza'] * 0.3))
        
        # Se suggerimento memoria con alta confidence
        if suggerimenti.get('confidence', 0) > 0.7 and suggerimenti.get('azione_consigliata'):
            decisione['azione'] = suggerimenti['azione_consigliata']
            print(f"    [!] Decisione modificata dalla memoria!")
        
        print(f"\n  Decisione finale: {decisione['azione'].upper()}")
        print(f"  Priorita: {decisione['priorita']:.2f}")
        
        # ================================================================
        # AZIONE
        # ================================================================
        print(f"\n[AZIONE] Esecuzione...")
        successo = motoria.agisci(decisione)
        print(f"  Risultato: {'[OK]' if successo else '[FAIL]'}")
        
        # ================================================================
        # APPRENDIMENTO
        # ================================================================
        reward = self.amigdala.assegna_reward(decisione['azione'], successo, valenza)
        
        # Memorizza con pattern neurale
        self.ippocampo.memorizza(
            f"ciclo_{ciclo_num}",
            f"{decisione['azione']} | {stato_emotivo} | Pattern:{firma_neurale.pattern[:15]}...",
            metadata={
                'valenza': valenza,
                'importanza': reward / 2.0 + 0.5,
                'pattern_neurale': firma_neurale.pattern,
                'arousal': self.arousal,
                'contesto': {'ciclo': ciclo_num, 'successo': successo}
            }
        )
        
        # ================================================================
        # AGGIORNA STATO NEURALE
        # ================================================================
        # Arousal influenzato da risultato
        if successo and valenza > 0.5:
            self.arousal = min(1.0, self.arousal + 0.05)  # Aumenta eccitazione
        elif not successo:
            self.arousal = max(0.0, self.arousal - 0.1)  # Diminuisce
        
        # Energia neurale
        self.energia_neurale -= 0.5
        
        # Salva pattern in storia
        self.storia_pattern_neurali.append({
            'ciclo': ciclo_num,
            'firma': firma_neurale.pattern,
            'percezione': onda_percezione.pattern,
            'emozione': onda_emozione.pattern,
            'arousal': self.arousal,
            'reward': reward
        })
        
        # ================================================================
        # REPORT CICLO
        # ================================================================
        print(f"\n{'─'*70}")
        print(f"[REPORT CICLO]")
        print(f"  Reward: {reward:+.2f}")
        print(f"  Arousal neurale: {self.arousal:.2f}")
        print(f"  Energia neurale: {self.energia_neurale:.1f}%")
        print(f"  Pattern registrati: {len(self.storia_pattern_neurali)}")
        print(f"{'─'*70}")
        
        return {
            'decisione': decisione,
            'successo': successo,
            'pattern_neurale': firma_neurale,
            'influenza_neurale': influenza_neurale,
            'arousal': self.arousal
        }
    
    def esegui_sessione(self, num_cicli: int = 5, delay: float = 2.0, visualizza: bool = True):
        """
        Esegue sessione completa con visualizzazione neurale
        
        Args:
            num_cicli: Numero di cicli
            delay: Pausa tra cicli
            visualizza: Se mostrare visualizzazione pattern
        """
        print(f"\n{'='*70}")
        print(f"[SESSIONE] {num_cicli} cicli con biosegnali neurali")
        print(f"{'='*70}\n")
        
        try:
            for i in range(num_cicli):
                risultato = self.ciclo_completo_con_biosegnali()
                
                # Visualizza pattern neurale
                if visualizza and i % 2 == 0:  # Ogni 2 cicli
                    self._visualizza_attivita_neurale()
                
                if i < num_cicli - 1:
                    print(f"\n[PAUSA] {delay}s...")
                    time.sleep(delay)
                    
        except KeyboardInterrupt:
            print(f"\n\n[!] Interruzione manuale\n")
        
        # Report finale
        self.report_finale()
    
    def _visualizza_attivita_neurale(self):
        """Visualizza attività neurale corrente"""
        if not self.storia_pattern_neurali:
            return
        
        ultimo = self.storia_pattern_neurali[-1]
        
        print(f"\n  [ATTIVITA' NEURALE]")
        print(f"  Firma:      {ultimo['firma'].replace('1', '█').replace('0', '░')}")
        print(f"  Percezione: {ultimo['percezione'].replace('1', '█').replace('0', '░')}")
        print(f"  Emozione:   {ultimo['emozione'].replace('1', '█').replace('0', '░')}")
        print(f"  Arousal:    {'█' * int(ultimo['arousal'] * 20):<20} {ultimo['arousal']:.2f}")
    
    def report_finale(self):
        """Report finale con analisi pattern neurali"""
        print(f"\n{'='*70}")
        print(f"[REPORT FINALE - ANALISI NEURALE]")
        print(f"{'='*70}")
        
        print(f"\n[SISTEMA COGNITIVO]")
        stats_memoria = self.ippocampo.get_statistiche()
        stats_reward = self.amigdala.get_statistiche_reward()
        
        print(f"  Cicli: {len(self.storia_pattern_neurali)}")
        print(f"  Memorie: {stats_memoria['memorie_episodiche']}")
        print(f"  Reward totale: {stats_reward['reward_totale']:.2f}")
        print(f"  Reward medio: {stats_reward['reward_medio']:.2f}")
        
        print(f"\n[ATTIVITA' NEURALE]")
        print(f"  Pattern registrati: {len(self.storia_pattern_neurali)}")
        print(f"  Arousal finale: {self.arousal:.2f}")
        print(f"  Energia neurale: {self.energia_neurale:.1f}%")
        
        # Analisi pattern
        if self.storia_pattern_neurali:
            arousal_medio = sum(p['arousal'] for p in self.storia_pattern_neurali) / len(self.storia_pattern_neurali)
            print(f"  Arousal medio: {arousal_medio:.2f}")
        
        # Visualizza evoluzione pattern
        print(f"\n[EVOLUZIONE PATTERN NEURALI]")
        print(f"  Ultimi 5 cicli:\n")
        for i, pattern_data in enumerate(self.storia_pattern_neurali[-5:], 1):
            visual = pattern_data['firma'].replace('1', '█').replace('0', '░')
            print(f"  Ciclo {pattern_data['ciclo']:2d}: {visual} | Reward: {pattern_data['reward']:+.2f}")
        
        print(f"\n{'='*70}")
        
        # Salva
        self.ippocampo.salva_su_disco()
        print(f"[OK] Memoria e pattern salvati\n")


class SimulatoreEEG:
    """
    Simulatore di segnali EEG (pronto per sensori reali)
    
    Quando collegherai un sensore EEG reale, sostituisci
    generate_signal() con lettura dal dispositivo.
    """
    
    def __init__(self):
        self.nome = "Simulatore EEG"
        self.canali = 4  # Fp1, Fp2, O1, O2 (simulati)
        self.sample_rate = 256  # Hz
        
    def leggi_segnale(self, durata_ms: float = 100) -> Dict[str, Any]:
        """
        Legge segnale EEG (simulato, pronto per sensore reale)
        
        Args:
            durata_ms: Durata lettura in millisecondi
            
        Returns:
            Dict con segnali da canali
        """
        # SIMULATO: genera dati random
        # TODO: Sostituisci con lettura da sensore reale
        import random
        
        segnali_canali = {}
        
        for canale_id in range(self.canali):
            # Simula ampiezza segnale
            ampiezza = random.uniform(10, 100)  # microVolt
            frequenza = random.choice([8, 10, 12, 20, 40])  # Hz
            
            segnali_canali[f'canale_{canale_id}'] = {
                'ampiezza': ampiezza,
                'frequenza': frequenza,
                'tipo_onda': self._classifica_frequenza(frequenza)
            }
        
        return {
            'canali': segnali_canali,
            'timestamp': time.time(),
            'durata_ms': durata_ms
        }
    
    def _classifica_frequenza(self, freq_hz: float) -> str:
        """Classifica frequenza in banda EEG"""
        if freq_hz < 4:
            return "delta"  # Sonno profondo
        elif freq_hz < 8:
            return "theta"  # Drowsy
        elif freq_hz < 13:
            return "alfa"  # Rilassato
        elif freq_hz < 30:
            return "beta"  # Attivo
        else:
            return "gamma"  # Concentrato
    
    def converti_a_pattern_binario(self, segnale_eeg: Dict) -> str:
        """
        Converte segnale EEG in pattern binario
        
        Args:
            segnale_eeg: Dati EEG
            
        Returns:
            Pattern binario (es. "0010100")
        """
        # Usa ampiezza media per determinare intensità
        canali = segnale_eeg['canali']
        ampiezze = [c['ampiezza'] for c in canali.values()]
        ampiezza_media = sum(ampiezze) / len(ampiezze)
        
        # Normalizza (10-100 μV → 0-1)
        intensita = (ampiezza_media - 10) / 90
        
        # Genera pattern proporzionale
        propagatore = PropagatoreNeurale(dimensione=15)
        onde = propagatore.propaga_n_cicli(int(intensita * 5))
        
        return onde[-1].pattern if onde else "0" * 15


# ==================== DEMO E TEST ====================

def demo_cicli_neurali():
    """Demo cicli con biosegnali"""
    print("""
    ================================================================
    
           MENTE ARTIFICIALE CON BIOSEGNALI NEURALI
           Layer neurale bioelettrico integrato
           
    ================================================================
    """)
    
    mente = MenteConBiosegnali()
    
    print("\n[INFO] Sistema inizializzato")
    print(f"  Layer neurale: attivo")
    print(f"  Dimensione rete: 15 neuroni")
    print(f"  Ritmi disponibili: alfa, beta, gamma")
    
    # Esegui sessione
    mente.esegui_sessione(num_cicli=3, delay=1.5, visualizza=True)


def demo_eeg_simulato():
    """Demo simulazione EEG"""
    print("\n" + "="*70)
    print("[DEMO EEG] Simulazione Sensori Biologici")
    print("="*70)
    
    eeg = SimulatoreEEG()
    
    print(f"\n[EEG] Lettura segnale (100ms)...")
    segnale = eeg.leggi_segnale(durata_ms=100)
    
    print(f"\n  Canali attivi: {len(segnale['canali'])}")
    for nome, dati in segnale['canali'].items():
        print(f"    {nome}: {dati['ampiezza']:.1f}μV @ {dati['frequenza']}Hz ({dati['tipo_onda']})")
    
    # Converti in pattern
    pattern = eeg.converti_a_pattern_binario(segnale)
    print(f"\n  Pattern binario: {pattern}")
    print(f"  Visualizzazione: {pattern.replace('1', '█').replace('0', '░')}")


def demo_stimoli_spontanei():
    """Demo pensieri spontanei"""
    print("\n" + "="*70)
    print("[DEMO] Stimoli Interni Spontanei")
    print("="*70)
    
    stimolo = StimoloInterno()
    
    print("\n[PENSIERO] Generazione attivita spontanea...")
    pensiero = stimolo.genera_pensiero_spontaneo()
    
    print(f"\n  Evoluzione pensiero ({len(pensiero)} fasi):")
    for onda in pensiero:
        visual = onda.pattern.replace('1', '█').replace('0', '░')
        print(f"    {visual} | {onda.neuroni_attivi} attivi")
    
    print("\n[INSIGHT] Attivazione improvvisa...")
    insight = stimolo.genera_insight()
    visual = insight.pattern.replace('1', '█').replace('0', '░')
    print(f"  Pattern: {visual}")
    print(f"  Neuroni: {insight.neuroni_attivi}")


if __name__ == "__main__":
    import sys
    
    print("\n[MENU] Scegli demo:")
    print("  1. Cicli cognitivi con biosegnali (3 cicli)")
    print("  2. Simulazione EEG")
    print("  3. Stimoli interni spontanei")
    print("  4. Tutte le demo")
    
    try:
        scelta = input("\n>> Scelta (1-4): ").strip()
        
        if scelta == "1":
            demo_cicli_neurali()
        elif scelta == "2":
            demo_eeg_simulato()
        elif scelta == "3":
            demo_stimoli_spontanei()
        elif scelta == "4":
            demo_cicli_neurali()
            demo_eeg_simulato()
            demo_stimoli_spontanei()
        else:
            print("[!] Scelta non valida")
            
    except KeyboardInterrupt:
        print("\n\n[!] Interruzione\n")
    except Exception as e:
        print(f"\n[ERROR] {e}")
        import traceback
        traceback.print_exc()

