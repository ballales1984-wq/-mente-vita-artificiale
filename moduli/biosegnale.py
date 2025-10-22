"""
⚡ MODULO BIOSEGNALE - Propagazione Neurale Simmetrica
=======================================================
Sistema di codifica binaria dove neuroni attivi si propagano simmetricamente.

Pattern di propagazione:
  Ciclo 0:  0001000     (neurone centrale attivo)
  Ciclo 1:  0010100     (propagazione ai vicini)
  Ciclo 2:  0101010     (ulteriore propagazione)
  Ciclo 3:  1010101     (rete completamente attiva)

Caratteristiche:
- Propagazione simmetrica bidirezionale
- Ogni "1" = neurone attivo
- Distanza tra "1" = latenza sinaptica
- Visualizzazione grafica in tempo reale
"""

import time
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from enum import Enum


class StatoPropagazione(Enum):
    """Stato della propagazione"""
    INIZIALE = "iniziale"
    PROPAGAZIONE = "propagazione"
    SATURAZIONE = "saturazione"
    RIFRAZIONE = "rifrazione"


@dataclass
class OnataNeurale:
    """
    Rappresenta uno stato della propagazione neurale
    
    Attributes:
        pattern: Stringa binaria (es. "0010100")
        ciclo: Numero ciclo
        neuroni_attivi: Numero di "1"
        latenza_media: Distanza media tra neuroni attivi
        stato: Stato propagazione
    """
    pattern: str
    ciclo: int
    neuroni_attivi: int
    latenza_media: float
    stato: StatoPropagazione
    timestamp: float
    
    def __str__(self):
        return f"{self.pattern} | Attivi:{self.neuroni_attivi} | Latenza:{self.latenza_media:.1f}"


class PropagatoreNeurale:
    """
    Sistema di propagazione simmetrica neurale
    
    Funzionalità:
    - Propagazione bidirezionale da centro
    - Calcolo latenze sinaptiche
    - Visualizzazione pattern
    - Stati di saturazione/rifrazione
    """
    
    def __init__(self, dimensione: int = 15):
        """
        Inizializza propagatore
        
        Args:
            dimensione: Numero di neuroni (deve essere dispari)
        """
        self.nome = "Propagatore Neurale"
        
        # Assicura dimensione dispari per simmetria
        if dimensione % 2 == 0:
            dimensione += 1
        
        self.dimensione = dimensione
        self.centro = dimensione // 2
        
        # Stato corrente
        self.pattern_corrente = "0" * dimensione
        self.ciclo_corrente = 0
        self.storia_onde = []
        
        # Configurazione
        self.velocita_propagazione = 1  # neuroni per ciclo
        self.periodo_rifrazione = 2  # cicli
        self.neuroni_refrattari = set()
        
    def inizializza_impulso_centrale(self) -> OnataNeurale:
        """
        Crea impulso iniziale nel neurone centrale
        
        Returns:
            Prima onda neurale
        """
        # Reset
        pattern_list = ['0'] * self.dimensione
        pattern_list[self.centro] = '1'
        
        self.pattern_corrente = ''.join(pattern_list)
        self.ciclo_corrente = 0
        self.neuroni_refrattari = {self.centro}
        
        onda = OnataNeurale(
            pattern=self.pattern_corrente,
            ciclo=self.ciclo_corrente,
            neuroni_attivi=1,
            latenza_media=0.0,
            stato=StatoPropagazione.INIZIALE,
            timestamp=time.time()
        )
        
        self.storia_onde.append(onda)
        return onda
    
    def propaga_ciclo(self) -> OnataNeurale:
        """
        Esegue un ciclo di propagazione simmetrica
        
        Regola: Ogni "1" attiva i neuroni adiacenti nel ciclo successivo
        
        Returns:
            Nuova onda dopo propagazione
        """
        self.ciclo_corrente += 1
        
        pattern_list = list(self.pattern_corrente)
        nuovo_pattern = ['0'] * self.dimensione
        neuroni_attivati_ora = set()
        
        # Trova neuroni attivi correnti
        for i, bit in enumerate(pattern_list):
            if bit == '1':
                # Propaga a sinistra
                if i > 0 and i-1 not in self.neuroni_refrattari:
                    nuovo_pattern[i-1] = '1'
                    neuroni_attivati_ora.add(i-1)
                
                # Propaga a destra
                if i < self.dimensione - 1 and i+1 not in self.neuroni_refrattari:
                    nuovo_pattern[i+1] = '1'
                    neuroni_attivati_ora.add(i+1)
                
                # Il neurone corrente rimane attivo
                nuovo_pattern[i] = '1'
                neuroni_attivati_ora.add(i)
        
        self.pattern_corrente = ''.join(nuovo_pattern)
        
        # Aggiorna neuroni refrattari (quelli attivati ora)
        self.neuroni_refrattari = neuroni_attivati_ora
        
        # Determina stato
        neuroni_attivi = self.pattern_corrente.count('1')
        
        if neuroni_attivi == self.dimensione:
            stato = StatoPropagazione.SATURAZIONE
        elif neuroni_attivi > self.dimensione * 0.7:
            stato = StatoPropagazione.PROPAGAZIONE
        else:
            stato = StatoPropagazione.PROPAGAZIONE
        
        # Calcola latenza media
        latenza = self._calcola_latenza_media()
        
        onda = OnataNeurale(
            pattern=self.pattern_corrente,
            ciclo=self.ciclo_corrente,
            neuroni_attivi=neuroni_attivi,
            latenza_media=latenza,
            stato=stato,
            timestamp=time.time()
        )
        
        self.storia_onde.append(onda)
        return onda
    
    def propaga_n_cicli(self, n: int) -> List[OnataNeurale]:
        """
        Propaga per N cicli consecutivi
        
        Args:
            n: Numero di cicli
            
        Returns:
            Lista di onde generate
        """
        # Inizializza impulso centrale
        onde = [self.inizializza_impulso_centrale()]
        
        # Propaga N volte
        for _ in range(n):
            onda = self.propaga_ciclo()
            onde.append(onda)
            
            # Stop se saturazione
            if onda.stato == StatoPropagazione.SATURAZIONE:
                break
        
        return onde
    
    def _calcola_latenza_media(self) -> float:
        """
        Calcola latenza media tra neuroni attivi
        
        Returns:
            Latenza media (distanza tra "1")
        """
        posizioni_attivi = [i for i, bit in enumerate(self.pattern_corrente) if bit == '1']
        
        if len(posizioni_attivi) <= 1:
            return 0.0
        
        # Calcola distanze tra neuroni attivi consecutivi
        distanze = []
        for i in range(len(posizioni_attivi) - 1):
            dist = posizioni_attivi[i+1] - posizioni_attivi[i]
            distanze.append(dist)
        
        latenza_media = sum(distanze) / len(distanze) if distanze else 0.0
        
        return latenza_media
    
    def visualizza_onda(self, onda: OnataNeurale, con_dettagli: bool = True) -> str:
        """
        Crea visualizzazione ASCII dell'onda
        
        Args:
            onda: Onda da visualizzare
            con_dettagli: Se mostrare dettagli aggiuntivi
            
        Returns:
            Stringa con visualizzazione
        """
        # Pattern con caratteri grafici
        visual = ""
        for bit in onda.pattern:
            if bit == '1':
                visual += "█"  # Neurone attivo
            else:
                visual += "░"  # Neurone inattivo
        
        # Aggiungi dettagli
        if con_dettagli:
            info = f" | Ciclo {onda.ciclo} | Attivi: {onda.neuroni_attivi}/{self.dimensione} | Latenza: {onda.latenza_media:.1f}"
            return visual + info
        
        return visual
    
    def visualizza_sequenza(self, onde: List[OnataNeurale]):
        """
        Visualizza sequenza completa di propagazione
        
        Args:
            onde: Lista di onde da visualizzare
        """
        print(f"\n{'='*70}")
        print(f"VISUALIZZAZIONE PROPAGAZIONE NEURALE")
        print(f"{'='*70}\n")
        
        for onda in onde:
            vis = self.visualizza_onda(onda, con_dettagli=True)
            print(vis)
            
            # Indica stato speciale
            if onda.stato == StatoPropagazione.SATURAZIONE:
                print("  ^--- SATURAZIONE COMPLETA")
        
        print(f"\n{'='*70}")
    
    def reset(self):
        """Reset sistema"""
        self.pattern_corrente = "0" * self.dimensione
        self.ciclo_corrente = 0
        self.storia_onde = []
        self.neuroni_refrattari = set()


class RitmoNeurale:
    """
    Generatore di ritmi neurali periodici
    
    Simula:
    - Onde cerebrali (alfa, beta, gamma, theta, delta)
    - Oscillazioni periodiche
    - Sincronizzazione neurale
    """
    
    def __init__(self, dimensione: int = 15):
        self.propagatore = PropagatoreNeurale(dimensione)
        self.frequenza_hz = 10  # Default: ritmo alfa
        self.periodo_ms = 1000 / self.frequenza_hz
        
    def genera_ritmo_alfa(self, durata_cicli: int = 10) -> List[OnataNeurale]:
        """
        Genera ritmo alfa (8-12 Hz) - stato rilassato
        
        Args:
            durata_cicli: Numero di cicli
            
        Returns:
            Sequenza pattern alfa
        """
        self.frequenza_hz = 10
        return self.propagatore.propaga_n_cicli(durata_cicli)
    
    def genera_ritmo_beta(self, durata_cicli: int = 10) -> List[OnataNeurale]:
        """
        Genera ritmo beta (13-30 Hz) - stato attivo/concentrato
        Propagazione più rapida
        """
        self.frequenza_hz = 20
        self.propagatore.velocita_propagazione = 2
        return self.propagatore.propaga_n_cicli(durata_cicli)
    
    def genera_ritmo_gamma(self, durata_cicli: int = 10) -> List[OnataNeurale]:
        """
        Genera ritmo gamma (30-100 Hz) - elaborazione cognitiva intensa
        Propagazione molto rapida
        """
        self.frequenza_hz = 40
        self.propagatore.velocita_propagazione = 3
        return self.propagatore.propaga_n_cicli(durata_cicli)


class StimoloInterno:
    """
    Generatore di stimoli interni spontanei
    
    Simula pensieri spontanei, associazioni, insight
    """
    
    def __init__(self):
        self.propagatore = PropagatoreNeurale(dimensione=21)
        self.intensita_pensiero = 0.5
        
    def genera_pensiero_spontaneo(self) -> List[OnataNeurale]:
        """
        Genera pattern di attivazione spontanea
        
        Returns:
            Sequenza che rappresenta un "pensiero"
        """
        # Numero cicli proporzionale all'intensità
        cicli = int(self.intensita_pensiero * 8) + 2
        
        return self.propagatore.propaga_n_cicli(cicli)
    
    def genera_insight(self) -> OnataNeurale:
        """
        Genera pattern di "insight" (attivazione improvvisa)
        
        Returns:
            Pattern di insight
        """
        # Attivazione multipla simultanea
        pattern = list("0" * self.propagatore.dimensione)
        
        # Attiva neuroni in posizioni chiave
        for pos in [self.propagatore.centro - 2, 
                    self.propagatore.centro, 
                    self.propagatore.centro + 2]:
            if 0 <= pos < len(pattern):
                pattern[pos] = '1'
        
        pattern_str = ''.join(pattern)
        
        return OnataNeurale(
            pattern=pattern_str,
            ciclo=0,
            neuroni_attivi=pattern_str.count('1'),
            latenza_media=2.0,
            stato=StatoPropagazione.PROPAGAZIONE,
            timestamp=time.time()
        )


class InterfacciaCoerenzaCerebrale:
    """
    Interfaccia tra segnali neurali e moduli cognitivi
    
    Traduce pattern binari in stati cognitivi e viceversa
    """
    
    def __init__(self):
        self.nome = "Interfaccia Coerenza Cerebrale"
        self.propagatore = PropagatoreNeurale(dimensione=15)
        self.ultima_onda = None
        
    def percepisce_segnale(self, percezioni: List[Dict]) -> OnataNeurale:
        """
        Converte percezioni in segnale neurale
        
        Args:
            percezioni: Lista percezioni (da talamo)
            
        Returns:
            Onda neurale corrispondente
        """
        # Intensità basata su numero e rilevanza percezioni
        if not percezioni:
            intensita = 0.1
        else:
            intensita = min(1.0, len(percezioni) * 0.3 + 
                          sum(p.get('rilevanza', 0.5) for p in percezioni) / len(percezioni))
        
        # Genera onda
        cicli_propagazione = int(intensita * 5)
        onde = self.propagatore.propaga_n_cicli(cicli_propagazione)
        
        self.ultima_onda = onde[-1] if onde else None
        return self.ultima_onda
    
    def stato_emotivo_a_pattern(self, stato_emotivo: str, valenza: float) -> OnataNeurale:
        """
        Converte stato emotivo in pattern neurale
        
        Args:
            stato_emotivo: Stato (positivo, negativo, neutro, ecc.)
            valenza: Valenza emotiva (-1 a +1)
            
        Returns:
            Pattern neurale dell'emozione
        """
        self.propagatore.reset()
        
        # Pattern diversi per emozioni diverse
        if stato_emotivo.lower() == "positivo":
            # Pattern ampio e veloce
            cicli = 5
        elif stato_emotivo.lower() == "negativo":
            # Pattern ristretto
            cicli = 2
        elif stato_emotivo.lower() == "allerta":
            # Pattern molto rapido
            cicli = 7
        else:
            # Neutro
            cicli = 3
        
        onde = self.propagatore.propaga_n_cicli(cicli)
        return onde[-1] if onde else None
    
    def pattern_a_intensita(self, onda: OnataNeurale) -> float:
        """
        Converte pattern in intensità utilizzabile
        
        Args:
            onda: Onda neurale
            
        Returns:
            Intensità (0-1)
        """
        # Intensità = % neuroni attivi
        intensita = onda.neuroni_attivi / self.propagatore.dimensione
        
        return intensita
    
    def pattern_a_urgenza(self, onda: OnataNeurale) -> float:
        """
        Calcola urgenza basata su latenza
        
        Args:
            onda: Onda neurale
            
        Returns:
            Urgenza (0-1, più basso = più urgente)
        """
        # Latenza bassa = alta urgenza
        if onda.latenza_media == 0:
            return 1.0
        
        urgenza = 1.0 / (1.0 + onda.latenza_media)
        
        return min(1.0, urgenza)
    
    def decodifica_per_decisione(self, onda: OnataNeurale) -> Dict[str, Any]:
        """
        Decodifica onda per influenzare decisioni cognitive
        
        Returns:
            Parametri per decision making
        """
        return {
            'intensita_cognitiva': self.pattern_a_intensita(onda),
            'urgenza': self.pattern_a_urgenza(onda),
            'stato_rete': onda.stato.value,
            'saturazione': onda.neuroni_attivi / self.propagatore.dimensione,
            'consiglio': self._genera_consiglio_da_pattern(onda)
        }
    
    def _genera_consiglio_da_pattern(self, onda: OnataNeurale) -> str:
        """
        Genera consiglio basato su pattern
        
        Returns:
            Consiglio testuale
        """
        saturazione = onda.neuroni_attivi / self.propagatore.dimensione
        
        if saturazione > 0.8:
            return "azione_immediata"  # Rete satura = agisci
        elif saturazione > 0.5:
            return "valuta_opzioni"  # Rete attiva = pensa
        elif onda.latenza_media < 1.5:
            return "risposta_rapida"  # Latenza bassa = veloce
        else:
            return "monitoraggio"  # Rete calma = osserva
        
        return "neutro"


# ==================== VISUALIZZATORE AVANZATO ====================

class VisualizzatoreNeurale:
    """Visualizzatore avanzato di pattern neurali"""
    
    @staticmethod
    def visualizza_evoluzione(onde: List[OnataNeurale], delay: float = 0.3):
        """
        Visualizza evoluzione temporale della propagazione
        
        Args:
            onde: Sequenza di onde
            delay: Pausa tra frame (secondi)
        """
        print(f"\n{'='*70}")
        print(f"EVOLUZIONE PROPAGAZIONE NEURALE")
        print(f"{'='*70}\n")
        
        for onda in onde:
            # Pattern visivo
            visual = ""
            for bit in onda.pattern:
                if bit == '1':
                    visual += "█"
                else:
                    visual += "░"
            
            # Barra intensità
            barra_intensita = "█" * int(onda.neuroni_attivi / len(onda.pattern) * 20)
            
            print(f"Ciclo {onda.ciclo:2d}: {visual}")
            print(f"          [{barra_intensita:<20}] {onda.neuroni_attivi} attivi | Lat: {onda.latenza_media:.1f}")
            print()
            
            time.sleep(delay)
        
        print(f"{'='*70}")
    
    @staticmethod
    def visualizza_griglia_temporale(onde: List[OnataNeurale]):
        """
        Visualizzazione griglia spazio-temporale
        
        Args:
            onde: Sequenza di onde
        """
        print(f"\n{'='*70}")
        print(f"GRIGLIA SPAZIO-TEMPORALE")
        print(f"{'='*70}")
        print(f"\nTempo  | Pattern Neurale")
        print("-" * 70)
        
        for onda in onde:
            visual = onda.pattern.replace('1', '█').replace('0', '░')
            print(f"t={onda.ciclo:2d}    | {visual} | {onda.neuroni_attivi} neuroni")
        
        print(f"\n{'='*70}")


# ==================== DEMO E TEST ====================

def demo_propagazione_base():
    """Demo propagazione base"""
    print("="*70)
    print("DEMO 1: Propagazione Simmetrica Base")
    print("="*70)
    
    propagatore = PropagatoreNeurale(dimensione=15)
    
    print("\nPropagazione da impulso centrale:")
    onde = propagatore.propaga_n_cicli(6)
    
    for onda in onde:
        print(f"  {onda}")
    
    # Visualizza
    VisualizzatoreNeurale.visualizza_griglia_temporale(onde)


def demo_ritmi_cerebrali():
    """Demo ritmi cerebrali"""
    print("\n" + "="*70)
    print("DEMO 2: Ritmi Cerebrali")
    print("="*70)
    
    ritmo = RitmoNeurale(dimensione=15)
    
    print("\nRitmo ALFA (rilassato):")
    onde_alfa = ritmo.genera_ritmo_alfa(durata_cicli=5)
    print(f"  Cicli: {len(onde_alfa)}")
    print(f"  Pattern finale: {onde_alfa[-1].pattern}")
    
    ritmo.propagatore.reset()
    
    print("\nRitmo GAMMA (concentrato):")
    onde_gamma = ritmo.genera_ritmo_gamma(durata_cicli=5)
    print(f"  Cicli: {len(onde_gamma)}")
    print(f"  Pattern finale: {onde_gamma[-1].pattern}")


def demo_interfaccia_cognitiva():
    """Demo integrazione con sistema cognitivo"""
    print("\n" + "="*70)
    print("DEMO 3: Interfaccia Sistema Cognitivo")
    print("="*70)
    
    interfaccia = InterfacciaCoerenzaCerebrale()
    
    # Simula percezioni
    percezioni_test = [
        {'tipo': 'visivo', 'rilevanza': 0.8},
        {'tipo': 'uditivo', 'rilevanza': 0.6}
    ]
    
    print("\n1. Percezioni -> Segnale Neurale:")
    onda = interfaccia.percepisce_segnale(percezioni_test)
    print(f"   Pattern: {onda.pattern}")
    print(f"   Attivi: {onda.neuroni_attivi}")
    
    # Stato emotivo -> pattern
    print("\n2. Emozione -> Segnale Neurale:")
    onda_emozione = interfaccia.stato_emotivo_a_pattern("positivo", valenza=0.7)
    print(f"   Pattern: {onda_emozione.pattern}")
    
    # Pattern -> decisione
    print("\n3. Segnale -> Influenza Decisione:")
    decisione = interfaccia.decodifica_per_decisione(onda)
    for key, value in decisione.items():
        print(f"   {key}: {value}")


def demo_stimolo_interno():
    """Demo stimoli interni"""
    print("\n" + "="*70)
    print("DEMO 4: Stimoli Interni (Pensieri Spontanei)")
    print("="*70)
    
    stimolo = StimoloInterno()
    
    print("\nPensiero spontaneo:")
    pensiero = stimolo.genera_pensiero_spontaneo()
    print(f"  Evoluzione in {len(pensiero)} cicli")
    print(f"  Pattern finale: {pensiero[-1].pattern}")
    
    print("\nInsight improvviso:")
    insight = stimolo.genera_insight()
    print(f"  Pattern: {insight.pattern}")
    print(f"  Neuroni attivi: {insight.neuroni_attivi}")


if __name__ == "__main__":
    print("""
    ================================================================
    
           SISTEMA BIOSEGNALI NEURALI - PROPAGAZIONE SIMMETRICA
           
    ================================================================
    """)
    
    # Esegui demo
    demo_propagazione_base()
    
    demo_ritmi_cerebrali()
    
    demo_interfaccia_cognitiva()
    
    demo_stimolo_interno()
    
    print("\n" + "="*70)
    print("[OK] TUTTE LE DEMO COMPLETATE")
    print("="*70)
    
    # Visualizzazione animata finale
    print("\n\nVISUALIZZAZIONE ANIMATA:")
    input("\nPremi Enter per vedere l'animazione...")
    
    propagatore = PropagatoreNeurale(dimensione=21)
    onde = propagatore.propaga_n_cicli(8)
    
    VisualizzatoreNeurale.visualizza_evoluzione(onde, delay=0.5)

