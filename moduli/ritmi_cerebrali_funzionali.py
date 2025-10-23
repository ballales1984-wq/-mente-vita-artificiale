#!/usr/bin/env python3
"""
🌊 RITMI CEREBRALI FUNZIONALI - Sistema Multi-Hz
====================================================
Ogni area cerebrale opera alla sua frequenza naturale
Come nel cervello umano!

Ritmi:
- Delta (0.5-4 Hz): Riposo, consolidamento profondo
- Theta (4-8 Hz): Memoria, creatività, immaginazione
- Alpha (8-13 Hz): Rilassamento, integrazione
- Beta (13-30 Hz): Attenzione, ragionamento
- Gamma (30-100 Hz): Problem solving, apprendimento

Autore: Alessio + Cursor AI
Data: 23 Ottobre 2025
"""

import time
import math
from enum import Enum
from typing import Dict, List, Tuple
from dataclasses import dataclass


class BandaFrequenza(Enum):
    """Bande di frequenza cerebrali"""
    DELTA = "Delta"      # 0.5-4 Hz - Sonno profondo, consolidamento
    THETA = "Theta"      # 4-8 Hz - Creatività, memoria, immaginazione
    ALPHA = "Alpha"      # 8-13 Hz - Rilassamento, integrazione
    BETA = "Beta"        # 13-30 Hz - Attenzione, concentrazione
    GAMMA = "Gamma"      # 30-100 Hz - Problem solving, insight


@dataclass
class RitmoCerebrale:
    """Ritmo di una specifica area cerebrale"""
    area: str
    banda: BandaFrequenza
    frequenza_hz: float
    intensita: float  # 0.0 - 1.0
    fase: float  # 0-360 gradi
    
    def __repr__(self):
        return f"{self.area}:{self.banda.value}({self.frequenza_hz:.1f}Hz)"


class GestoreRitmiCerebrali:
    """
    Gestisce ritmi Hz differenziati per ogni funzione cerebrale
    Simula attività elettrica realistica del cervello
    """
    
    def __init__(self):
        self.nome = "Gestore Ritmi Cerebrali"
        
        # Mappatura: Area cerebrale → Banda frequenza dominante
        self.mappatura_funzioni = {
            # PERCEZIONE - Alta frequenza (Beta/Gamma)
            'visione': {
                'rilassata': ('BETA', 18.0),      # Visione passiva
                'attiva': ('GAMMA', 40.0),        # Riconoscimento oggetti
                'analisi': ('GAMMA', 60.0)        # Analisi dettagliata
            },
            'udito': {
                'ascolto': ('BETA', 20.0),        # Ascolto normale
                'linguaggio': ('GAMMA', 35.0),    # Comprensione parole
                'musica': ('ALPHA', 10.0)         # Apprezzamento musicale
            },
            
            # MEMORIA - Media/Bassa frequenza (Theta/Alpha)
            'memoria': {
                'recupero': ('ALPHA', 10.0),      # Richiamo memorie
                'consolidamento': ('THETA', 6.0), # Consolidamento profondo
                'encoding': ('BETA', 15.0)        # Creazione nuove memorie
            },
            
            # EMOZIONE - Media frequenza (Alpha/Beta)
            'emozione': {
                'valutazione': ('BETA', 16.0),    # Valutazione emotiva
                'positiva': ('ALPHA', 12.0),      # Emozioni positive
                'negativa': ('BETA', 22.0)        # Emozioni negative/allerta
            },
            
            # RAGIONAMENTO - Alta frequenza (Gamma)
            'ragionamento': {
                'semplice': ('BETA', 25.0),       # Decisioni semplici
                'complesso': ('GAMMA', 45.0),     # Ragionamento complesso
                'insight': ('GAMMA', 70.0)        # Momento "eureka"
            },
            
            # CREATIVITÀ - Bassa frequenza (Theta/Alpha)
            'creativita': {
                'ideazione': ('THETA', 7.0),      # Generazione idee
                'immaginazione': ('THETA', 5.0),  # Immaginazione libera
                'problem_solving': ('ALPHA', 11.0) # Soluzione creativa
            },
            
            # ATTENZIONE - Media/Alta (Beta)
            'attenzione': {
                'focus': ('BETA', 20.0),          # Attenzione focalizzata
                'vigilanza': ('BETA', 18.0),      # Stato di allerta
                'rilassata': ('ALPHA', 10.0)      # Attenzione rilassata
            },
            
            # PIANIFICAZIONE - Alta (Beta/Gamma)
            'pianificazione': {
                'strategica': ('GAMMA', 38.0),    # Pianificazione complessa
                'tattica': ('BETA', 24.0),        # Pianificazione immediata
                'revisione': ('ALPHA', 12.0)      # Revisione piani
            },
            
            # APPRENDIMENTO - Alta (Gamma)
            'apprendimento': {
                'acquisizione': ('GAMMA', 50.0),  # Apprendimento attivo
                'pratica': ('BETA', 20.0),        # Pratica ripetuta
                'integrazione': ('THETA', 7.0)    # Integrazione conoscenza
            },
            
            # COSCIENZA - Molto alta (Gamma)
            'coscienza': {
                'auto_riflessione': ('GAMMA', 80.0),  # Pensiero su di sé
                'metacognizione': ('GAMMA', 75.0),    # Pensare il pensiero
                'integrazione': ('GAMMA', 55.0)       # Integrazione esperienze
            },
            
            # MOTORIA - Media (Beta)
            'motoria': {
                'esecuzione': ('BETA', 20.0),     # Esecuzione movimenti
                'coordinazione': ('BETA', 18.0),  # Coordinazione fine
                'riposo': ('ALPHA', 9.0)          # Riposo motorio
            },
            
            # RIPOSO/IDLE - Bassa (Alpha/Theta)
            'riposo': {
                'rilassato': ('ALPHA', 10.0),     # Stato di riposo
                'profondo': ('THETA', 5.0),       # Riposo profondo
                'dormiente': ('DELTA', 2.0)       # "Sonno" sistema
            }
        }
        
        # Stati attuali delle aree
        self.stati_attuali = {}
        
        # Sincronizzazione tra aree (coherence)
        self.coherence_globale = 0.5  # 0.0 - 1.0
        
        print(f"[{self.nome}] Inizializzato")
        print(f"  • {len(self.mappatura_funzioni)} aree mappate")
        print(f"  • Range: 0.5 Hz (Delta) - 100 Hz (Gamma)")
    
    def get_frequenza_per_funzione(self, area: str, stato: str = 'default') -> Tuple[float, BandaFrequenza]:
        """
        Restituisce frequenza appropriata per area e stato
        
        Args:
            area: Nome area cerebrale (es. 'visione', 'memoria')
            stato: Stato specifico (es. 'attiva', 'consolidamento')
            
        Returns:
            (frequenza_hz, banda)
        """
        if area not in self.mappatura_funzioni:
            # Default beta se area sconosciuta
            return (20.0, BandaFrequenza.BETA)
        
        stati_area = self.mappatura_funzioni[area]
        
        if stato not in stati_area:
            # Prendi primo stato disponibile
            stato = list(stati_area.keys())[0]
        
        banda_nome, freq = stati_area[stato]
        banda = BandaFrequenza[banda_nome]
        
        return (freq, banda)
    
    def genera_ritmo(self, area: str, stato: str, intensita: float = 0.7) -> RitmoCerebrale:
        """
        Genera ritmo specifico per area in certo stato
        
        Args:
            area: Area cerebrale
            stato: Stato funzionale
            intensita: Intensità attività (0.0-1.0)
            
        Returns:
            RitmoCerebrale configurato
        """
        freq, banda = self.get_frequenza_per_funzione(area, stato)
        
        # Genera fase casuale ma coerente
        fase = (time.time() * freq * 360) % 360
        
        ritmo = RitmoCerebrale(
            area=area,
            banda=banda,
            frequenza_hz=freq,
            intensita=intensita,
            fase=fase
        )
        
        # Memorizza stato
        self.stati_attuali[area] = ritmo
        
        return ritmo
    
    def genera_pattern_multi_ritmo(self) -> Dict[str, RitmoCerebrale]:
        """
        Genera pattern completo di tutti i ritmi attivi
        Simula snapshot istantaneo attività cerebrale
        
        Returns:
            Dict con ritmo per ogni area attiva
        """
        pattern = {}
        
        # Esempio di attivazione multi-area
        pattern['visione'] = self.genera_ritmo('visione', 'attiva', 0.8)
        pattern['udito'] = self.genera_ritmo('udito', 'ascolto', 0.6)
        pattern['memoria'] = self.genera_ritmo('memoria', 'recupero', 0.7)
        pattern['emozione'] = self.genera_ritmo('emozione', 'valutazione', 0.5)
        pattern['ragionamento'] = self.genera_ritmo('ragionamento', 'complesso', 0.9)
        pattern['attenzione'] = self.genera_ritmo('attenzione', 'focus', 0.8)
        pattern['apprendimento'] = self.genera_ritmo('apprendimento', 'acquisizione', 0.85)
        
        return pattern
    
    def calcola_coherence(self, pattern: Dict[str, RitmoCerebrale]) -> float:
        """
        Calcola coerenza tra ritmi (quanto sono sincronizzati)
        
        Alta coherence = aree lavorano bene insieme
        Bassa coherence = attività disorganizzata
        """
        if len(pattern) < 2:
            return 1.0
        
        # Calcola differenze di fase tra aree
        fasi = [r.fase for r in pattern.values()]
        
        # Coherence basata su similarità fasi (semplificato)
        varianza_fasi = sum((f - sum(fasi)/len(fasi))**2 for f in fasi) / len(fasi)
        coherence = 1.0 / (1.0 + varianza_fasi / 10000)
        
        return min(1.0, max(0.0, coherence))
    
    def visualizza_pattern(self, pattern: Dict[str, RitmoCerebrale]) -> str:
        """Visualizza pattern multi-ritmo in formato leggibile"""
        lines = []
        lines.append("\n🌊 PATTERN MULTI-RITMO CEREBRALE:")
        lines.append("="*70)
        
        # Ordina per frequenza
        sorted_pattern = sorted(pattern.items(), key=lambda x: x[1].frequenza_hz)
        
        for area, ritmo in sorted_pattern:
            # Barra intensità
            barra = "█" * int(ritmo.intensita * 10) + "░" * (10 - int(ritmo.intensita * 10))
            
            # Emoji per banda
            emoji_banda = {
                BandaFrequenza.DELTA: "💤",
                BandaFrequenza.THETA: "🧘",
                BandaFrequenza.ALPHA: "😌",
                BandaFrequenza.BETA: "🎯",
                BandaFrequenza.GAMMA: "⚡"
            }
            emoji = emoji_banda.get(ritmo.banda, "🌊")
            
            lines.append(f"{emoji} {area:15s} | {ritmo.banda.value:6s} | "
                        f"{ritmo.frequenza_hz:5.1f} Hz | {barra} {ritmo.intensita:.0%}")
        
        # Coherence globale
        coherence = self.calcola_coherence(pattern)
        coherence_bar = "█" * int(coherence * 20) + "░" * (20 - int(coherence * 20))
        lines.append("="*70)
        lines.append(f"🔗 Coherence: {coherence_bar} {coherence:.0%}")
        
        return "\n".join(lines)
    
    def adatta_ritmo_a_task(self, task_corrente: str) -> Dict[str, RitmoCerebrale]:
        """
        Adatta ritmi cerebrali in base al task corrente
        
        Args:
            task_corrente: 'percezione', 'apprendimento', 'ragionamento', etc.
            
        Returns:
            Pattern ottimizzato per quel task
        """
        pattern = {}
        
        if task_corrente == 'percezione':
            # Alta attività percettiva
            pattern['visione'] = self.genera_ritmo('visione', 'attiva', 0.9)
            pattern['udito'] = self.genera_ritmo('udito', 'ascolto', 0.8)
            pattern['attenzione'] = self.genera_ritmo('attenzione', 'focus', 0.85)
            pattern['memoria'] = self.genera_ritmo('memoria', 'encoding', 0.6)
            
        elif task_corrente == 'ragionamento':
            # Gamma alta per pensiero complesso
            pattern['ragionamento'] = self.genera_ritmo('ragionamento', 'complesso', 0.95)
            pattern['memoria'] = self.genera_ritmo('memoria', 'recupero', 0.8)
            pattern['attenzione'] = self.genera_ritmo('attenzione', 'focus', 0.9)
            pattern['coscienza'] = self.genera_ritmo('coscienza', 'metacognizione', 0.85)
            
        elif task_corrente == 'apprendimento':
            # Gamma per acquisizione
            pattern['apprendimento'] = self.genera_ritmo('apprendimento', 'acquisizione', 0.9)
            pattern['memoria'] = self.genera_ritmo('memoria', 'encoding', 0.85)
            pattern['attenzione'] = self.genera_ritmo('attenzione', 'focus', 0.8)
            pattern['emozione'] = self.genera_ritmo('emozione', 'positiva', 0.7)
            
        elif task_corrente == 'creativita':
            # Theta per immaginazione
            pattern['creativita'] = self.genera_ritmo('creativita', 'ideazione', 0.8)
            pattern['memoria'] = self.genera_ritmo('memoria', 'recupero', 0.6)
            pattern['ragionamento'] = self.genera_ritmo('ragionamento', 'semplice', 0.5)
            
        elif task_corrente == 'consolidamento':
            # Theta/Delta per consolidamento memoria
            pattern['memoria'] = self.genera_ritmo('memoria', 'consolidamento', 0.9)
            pattern['emozione'] = self.genera_ritmo('emozione', 'valutazione', 0.6)
            
        elif task_corrente == 'coscienza':
            # Gamma molto alta per auto-riflessione
            pattern['coscienza'] = self.genera_ritmo('coscienza', 'auto_riflessione', 0.95)
            pattern['memoria'] = self.genera_ritmo('memoria', 'recupero', 0.8)
            pattern['ragionamento'] = self.genera_ritmo('ragionamento', 'complesso', 0.85)
            pattern['emozione'] = self.genera_ritmo('emozione', 'valutazione', 0.7)
            
        elif task_corrente == 'azione':
            # Beta per controllo motorio
            pattern['motoria'] = self.genera_ritmo('motoria', 'esecuzione', 0.85)
            pattern['attenzione'] = self.genera_ritmo('attenzione', 'focus', 0.8)
            
        else:
            # Pattern default (tutte le aree moderate)
            pattern = self.genera_pattern_multi_ritmo()
        
        return pattern
    
    def simula_oscillazione(self, ritmo: RitmoCerebrale, durata_ms: float = 1000) -> List[float]:
        """
        Simula oscillazione nel tempo di un ritmo
        
        Args:
            ritmo: RitmoCerebrale da simulare
            durata_ms: Durata simulazione in millisecondi
            
        Returns:
            Lista di ampiezze nel tempo
        """
        samples_per_sec = 1000  # 1000 Hz sampling
        num_samples = int(durata_ms * samples_per_sec / 1000)
        
        oscillazioni = []
        for i in range(num_samples):
            t = i / samples_per_sec
            # Onda sinusoidale alla frequenza del ritmo
            ampiezza = ritmo.intensita * math.sin(2 * math.pi * ritmo.frequenza_hz * t + math.radians(ritmo.fase))
            oscillazioni.append(ampiezza)
        
        return oscillazioni
    
    def genera_report_completo(self, task: str) -> str:
        """Genera report dettagliato ritmi per task"""
        pattern = self.adatta_ritmo_a_task(task)
        
        lines = []
        lines.append(f"\n{'='*70}")
        lines.append(f"🧠 REPORT RITMI CEREBRALI - Task: {task.upper()}")
        lines.append(f"{'='*70}")
        
        lines.append(self.visualizza_pattern(pattern))
        
        # Statistiche
        freq_media = sum(r.frequenza_hz for r in pattern.values()) / len(pattern)
        intensita_media = sum(r.intensita for r in pattern.values()) / len(pattern)
        
        lines.append(f"\n📊 STATISTICHE:")
        lines.append(f"  • Aree attive: {len(pattern)}")
        lines.append(f"  • Frequenza media: {freq_media:.1f} Hz")
        lines.append(f"  • Intensità media: {intensita_media:.0%}")
        lines.append(f"  • Coherence: {self.calcola_coherence(pattern):.0%}")
        
        # Banda dominante
        bande_count = {}
        for r in pattern.values():
            bande_count[r.banda.value] = bande_count.get(r.banda.value, 0) + 1
        banda_dominante = max(bande_count.items(), key=lambda x: x[1])
        lines.append(f"  • Banda dominante: {banda_dominante[0]} ({banda_dominante[1]} aree)")
        
        lines.append(f"{'='*70}\n")
        
        return "\n".join(lines)


def test_ritmi_funzionali():
    """Test del sistema ritmi cerebrali"""
    
    print("\n" + "="*70)
    print("🧪 TEST RITMI CEREBRALI FUNZIONALI")
    print("="*70)
    
    gestore = GestoreRitmiCerebrali()
    
    # Test diversi task
    tasks = [
        'percezione',
        'ragionamento',
        'apprendimento',
        'creativita',
        'coscienza',
        'consolidamento'
    ]
    
    for task in tasks:
        report = gestore.genera_report_completo(task)
        print(report)
        time.sleep(0.5)
    
    print("\n" + "="*70)
    print("✅ TEST COMPLETATO!")
    print("="*70)
    
    print("\n💡 SPIEGAZIONE:")
    print("  Ogni area cerebrale ora opera alla sua frequenza naturale!")
    print("  Esattamente come nel cervello umano!")
    print("\n  • Delta (0.5-4 Hz): Riposo profondo, consolidamento")
    print("  • Theta (4-8 Hz): Creatività, memoria, immaginazione")
    print("  • Alpha (8-13 Hz): Rilassamento, integrazione")
    print("  • Beta (13-30 Hz): Attenzione, concentrazione")
    print("  • Gamma (30-100 Hz): Insight, apprendimento, coscienza")
    print()


if __name__ == "__main__":
    test_ritmi_funzionali()

