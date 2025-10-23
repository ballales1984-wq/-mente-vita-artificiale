"""
⚡ MODULO SEGNALI NEURALI - Codifica Binaria Bioelettrica
==========================================================
Sistema di codifica binaria per segnali bioelettrici neurali.
Ogni impulso è rappresentato da un singolo "1" circondato da zeri.

Concetti:
- Posizione del "1" = direzione/canale
- Numero di zeri = ampiezza/intensità
- Espansione temporale = propagazione segnale

Esempi:
  00       → Nessun segnale
  010      → Impulso base centrale
  00100    → Impulso ampio
  0001000  → Impulso molto ampio
  100      → Impulso sinistro
  001      → Impulso destro
"""

from typing import List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum


class Direzione(Enum):
    """Direzione di espansione del segnale"""
    SINISTRA = "sinistra"
    DESTRA = "destra"
    BILATERALE = "bilaterale"
    CENTRO = "centro"


class TipoSegnale(Enum):
    """Tipo di codifica segnale"""
    AMPIEZZA = "ampiezza"  # Numero di zeri = intensità
    DIREZIONE = "direzione"  # Posizione = canale
    TEMPORALE = "temporale"  # Espansione = tempo


@dataclass
class SegnaleBioelettrico:
    """
    Rappresentazione di un segnale bioelettrico
    
    Attributes:
        codice: Stringa binaria (es. "00100")
        posizione_impulso: Indice del "1"
        ampiezza: Numero totale di bit
        intensita: Calcolata come numero di zeri
        direzione: Direzione rispetto al centro
        timestamp: Momento creazione/propagazione
    """
    codice: str
    posizione_impulso: int
    ampiezza: int
    intensita: float
    direzione: Direzione
    timestamp: float
    
    def __str__(self):
        return f"{self.codice} [pos:{self.posizione_impulso}, amp:{self.ampiezza}, int:{self.intensita:.2f}]"


class CodificatoreSegnali:
    """
    Sistema di codifica/decodifica segnali bioelettrici
    
    Funzioni:
    - Crea impulso iniziale
    - Espande segnale (sinistra/destra)
    - Decodifica ampiezza, direzione, tempo
    - Propaga segnale nel tempo
    """
    
    def __init__(self):
        self.nome = "Codificatore Segnali Neurali"
        self.storia_segnali = []
        self.segnale_corrente = None
        
    def crea_impulso_base(self, posizione: str = "centro") -> SegnaleBioelettrico:
        """
        Crea impulso bioelettrico base
        
        Args:
            posizione: "centro", "sinistra", "destra"
            
        Returns:
            SegnaleBioelettrico base
        """
        if posizione == "centro":
            codice = "010"
            pos_impulso = 1
            direzione = Direzione.CENTRO
        elif posizione == "sinistra":
            codice = "100"
            pos_impulso = 0
            direzione = Direzione.SINISTRA
        elif posizione == "destra":
            codice = "001"
            pos_impulso = 2
            direzione = Direzione.DESTRA
        else:
            codice = "010"
            pos_impulso = 1
            direzione = Direzione.CENTRO
        
        segnale = SegnaleBioelettrico(
            codice=codice,
            posizione_impulso=pos_impulso,
            ampiezza=len(codice),
            intensita=self._calcola_intensita(codice),
            direzione=direzione,
            timestamp=__import__('time').time()
        )
        
        self.segnale_corrente = segnale
        self.storia_segnali.append(segnale)
        
        return segnale
    
    def espandi_segnale(self, segnale: SegnaleBioelettrico, 
                       direzione: Direzione = Direzione.BILATERALE,
                       n_zeri: int = 1) -> SegnaleBioelettrico:
        """
        Espande il segnale aggiungendo zeri
        
        Args:
            segnale: Segnale da espandere
            direzione: Dove espandere (sinistra/destra/bilaterale)
            n_zeri: Numero di zeri da aggiungere per lato
            
        Returns:
            Nuovo segnale espanso
        """
        codice = segnale.codice
        pos = segnale.posizione_impulso
        
        if direzione == Direzione.SINISTRA:
            # Aggiungi zeri a sinistra
            nuovo_codice = "0" * n_zeri + codice
            nuova_pos = pos + n_zeri
            
        elif direzione == Direzione.DESTRA:
            # Aggiungi zeri a destra
            nuovo_codice = codice + "0" * n_zeri
            nuova_pos = pos
            
        elif direzione == Direzione.BILATERALE:
            # Aggiungi zeri da entrambi i lati
            nuovo_codice = "0" * n_zeri + codice + "0" * n_zeri
            nuova_pos = pos + n_zeri
            
        else:  # CENTRO
            nuovo_codice = codice
            nuova_pos = pos
        
        # Crea nuovo segnale
        nuovo_segnale = SegnaleBioelettrico(
            codice=nuovo_codice,
            posizione_impulso=nuova_pos,
            ampiezza=len(nuovo_codice),
            intensita=self._calcola_intensita(nuovo_codice),
            direzione=direzione,
            timestamp=__import__('time').time()
        )
        
        self.segnale_corrente = nuovo_segnale
        self.storia_segnali.append(nuovo_segnale)
        
        return nuovo_segnale
    
    def sequenza_espansione(self, cicli: int = 5, 
                           direzione: Direzione = Direzione.BILATERALE) -> List[SegnaleBioelettrico]:
        """
        Genera sequenza di espansioni progressive
        
        Args:
            cicli: Numero di cicli di espansione
            direzione: Direzione espansione
            
        Returns:
            Lista di segnali progressivi
        """
        sequenza = []
        
        # Impulso iniziale
        segnale = self.crea_impulso_base("centro")
        sequenza.append(segnale)
        
        # Espansioni successive
        for i in range(cicli):
            segnale = self.espandi_segnale(segnale, direzione, n_zeri=1)
            sequenza.append(segnale)
        
        return sequenza
    
    def _calcola_intensita(self, codice: str) -> float:
        """
        Calcola intensità del segnale (numero di zeri = ampiezza onda)
        
        Args:
            codice: Stringa binaria
            
        Returns:
            Intensità normalizzata (0-1)
        """
        num_zeri = codice.count('0')
        num_uni = codice.count('1')
        
        if num_uni == 0:
            return 0.0
        
        # Più zeri attorno all'impulso = maggiore ampiezza
        # Normalizza: 2 zeri = 0.5, 4 zeri = 0.75, 6 zeri = 0.88
        intensita = num_zeri / (num_zeri + 2)
        
        return intensita
    
    def decodifica_ampiezza(self, segnale: SegnaleBioelettrico) -> float:
        """
        Decodifica ampiezza del segnale
        
        Returns:
            Ampiezza in unità arbitrarie (0-10)
        """
        # Ampiezza proporzionale al numero di zeri
        num_zeri = segnale.codice.count('0')
        ampiezza = num_zeri / 2.0  # Scala
        
        return min(10.0, ampiezza)
    
    def decodifica_direzione(self, segnale: SegnaleBioelettrico) -> Tuple[str, float]:
        """
        Decodifica direzione del segnale
        
        Returns:
            Tuple (direzione, offset_dal_centro)
        """
        centro = segnale.ampiezza // 2
        offset = segnale.posizione_impulso - centro
        
        if offset < -0.5:
            direzione = "sinistra"
        elif offset > 0.5:
            direzione = "destra"
        else:
            direzione = "centro"
        
        # Offset normalizzato
        offset_norm = offset / max(1, centro)
        
        return direzione, offset_norm
    
    def decodifica_tempo(self, segnale: SegnaleBioelettrico) -> float:
        """
        Decodifica componente temporale
        
        Returns:
            Ritardo/latenza in ms (simulato)
        """
        # Più lungo il segnale, maggiore il ritardo
        ritardo_ms = (segnale.ampiezza - 3) * 10  # 10ms per zero aggiunto
        
        return max(0, ritardo_ms)
    
    def decodifica_completa(self, segnale: SegnaleBioelettrico) -> dict:
        """
        Decodifica completa del segnale
        
        Returns:
            Dict con tutti i parametri decodificati
        """
        ampiezza = self.decodifica_ampiezza(segnale)
        direzione, offset = self.decodifica_direzione(segnale)
        tempo = self.decodifica_tempo(segnale)
        
        return {
            'codice_binario': segnale.codice,
            'ampiezza': ampiezza,
            'intensita': segnale.intensita,
            'direzione': direzione,
            'offset': offset,
            'latenza_ms': tempo,
            'posizione_impulso': segnale.posizione_impulso,
            'lunghezza_totale': segnale.ampiezza
        }
    
    def simula_potenziale_azione(self, ampiezza_iniziale: float = 0.5) -> List[SegnaleBioelettrico]:
        """
        Simula un potenziale d'azione neurale completo
        
        Fasi:
        1. Depolarizzazione (espansione rapida)
        2. Picco (massima ampiezza)
        3. Ripolarizzazione (contrazione)
        
        Args:
            ampiezza_iniziale: Ampiezza iniziale (0-1)
            
        Returns:
            Sequenza di segnali che rappresentano il potenziale d'azione
        """
        sequenza = []
        
        # Fase 1: Depolarizzazione (espansione)
        print(f"\n[{self.nome}] Fase 1: Depolarizzazione")
        segnale = self.crea_impulso_base("centro")
        sequenza.append(segnale)
        print(f"  {segnale}")
        
        for i in range(3):
            segnale = self.espandi_segnale(segnale, Direzione.BILATERALE, n_zeri=1)
            sequenza.append(segnale)
            print(f"  {segnale}")
        
        # Fase 2: Picco
        print(f"\n[{self.nome}] Fase 2: Picco massimo")
        print(f"  {segnale} <- PICCO")
        
        # Fase 3: Ripolarizzazione (contrazione simulata invertendo)
        print(f"\n[{self.nome}] Fase 3: Ripolarizzazione")
        for i in range(2):
            # Simula contrazione riducendo rappresentazione
            print(f"  Ritorno verso baseline...")
        
        return sequenza
    
    def converti_a_voltaggio(self, segnale: SegnaleBioelettrico, 
                            voltaggio_max: float = 100.0) -> float:
        """
        Converte segnale binario in voltaggio equivalente (mV)
        
        Args:
            segnale: Segnale binario
            voltaggio_max: Voltaggio massimo (mV)
            
        Returns:
            Voltaggio in mV
        """
        # Voltaggio proporzionale all'intensità
        voltaggio = segnale.intensita * voltaggio_max
        
        return voltaggio
    
    def get_pattern_visivo(self, segnale: SegnaleBioelettrico) -> str:
        """
        Rappresentazione visiva del segnale
        
        Returns:
            Stringa ASCII art del segnale
        """
        codice = segnale.codice
        
        # Crea barra visiva
        barra = ""
        for bit in codice:
            if bit == '1':
                barra += "█"  # Impulso
            else:
                barra += "░"  # Silenzio
        
        return barra


class ReteNeurale:
    """
    Rete di neuroni che comunicano via segnali bioelettrici
    
    Simula:
    - Propagazione segnale tra neuroni
    - Sommazione input multipli
    - Soglia di attivazione
    - Pattern di firing
    """
    
    def __init__(self, num_neuroni: int = 5):
        self.nome = "Rete Neurale Bioelettrica"
        self.num_neuroni = num_neuroni
        self.neuroni = [CodificatoreSegnali() for _ in range(num_neuroni)]
        self.segnali_attivi = []
        
    def propaga_segnale(self, neurone_sorgente: int, 
                       neurone_target: int,
                       ampiezza: float = 0.5) -> SegnaleBioelettrico:
        """
        Propaga segnale da un neurone all'altro
        
        Args:
            neurone_sorgente: Indice neurone che emette
            neurone_target: Indice neurone ricevente
            ampiezza: Ampiezza segnale
            
        Returns:
            Segnale propagato
        """
        # Calcola direzione relativa
        if neurone_target < neurone_sorgente:
            pos_iniziale = "sinistra"
        elif neurone_target > neurone_sorgente:
            pos_iniziale = "destra"
        else:
            pos_iniziale = "centro"
        
        # Crea impulso
        segnale = self.neuroni[neurone_sorgente].crea_impulso_base(pos_iniziale)
        
        # Espandi proporzionalmente alla distanza
        distanza = abs(neurone_target - neurone_sorgente)
        for _ in range(distanza):
            direzione = Direzione.DESTRA if neurone_target > neurone_sorgente else Direzione.SINISTRA
            segnale = self.neuroni[neurone_sorgente].espandi_segnale(segnale, direzione)
        
        self.segnali_attivi.append(segnale)
        
        return segnale
    
    def pattern_firing(self, pattern: str = "sequenziale") -> List[SegnaleBioelettrico]:
        """
        Genera pattern di firing neuronale
        
        Args:
            pattern: "sequenziale", "sincronizzato", "casuale"
            
        Returns:
            Lista di segnali generati
        """
        segnali = []
        
        if pattern == "sequenziale":
            # Firing sequenziale (cascata)
            for i in range(self.num_neuroni):
                segnale = self.neuroni[i].crea_impulso_base("centro")
                segnali.append(segnale)
                
        elif pattern == "sincronizzato":
            # Tutti i neuroni insieme
            for neurone in self.neuroni:
                segnale = neurone.crea_impulso_base("centro")
                segnali.append(segnale)
                
        elif pattern == "casuale":
            # Pattern casuale
            import random
            for i in range(self.num_neuroni // 2):
                idx = random.randint(0, self.num_neuroni - 1)
                segnale = self.neuroni[idx].crea_impulso_base("centro")
                segnali.append(segnale)
        
        return segnali


# ==================== SIMULATORE ATTIVITÀ NEURALE ====================

class SimulatoreAttvitaNeurale:
    """
    Simulatore completo di attività neurale con codifica binaria
    
    Simula:
    - Potenziali d'azione
    - Propagazione sinaptica
    - Pattern di attivazione
    - Codifica/decodifica segnali
    """
    
    def __init__(self):
        self.codificatore = CodificatoreSegnali()
        self.rete = ReteNeurale(num_neuroni=5)
        
    def simula_percezione_sensoriale(self, intensita: float = 0.7) -> SegnaleBioelettrico:
        """
        Simula segnale da input sensoriale
        
        Args:
            intensita: Intensità stimolo (0-1)
            
        Returns:
            Segnale codificato
        """
        # Crea impulso base
        segnale = self.codificatore.crea_impulso_base("centro")
        
        # Espandi proporzionalmente all'intensità
        num_espansioni = int(intensita * 5)
        
        for _ in range(num_espansioni):
            segnale = self.codificatore.espandi_segnale(segnale, Direzione.BILATERALE)
        
        return segnale
    
    def simula_comando_motorio(self, forza: float = 0.5, 
                              direzione: str = "centro") -> SegnaleBioelettrico:
        """
        Simula segnale di comando motorio
        
        Args:
            forza: Forza comando (0-1)
            direzione: Direzione movimento
            
        Returns:
            Segnale motorio codificato
        """
        # Mappa direzione
        dir_map = {
            "sinistra": "sinistra",
            "destra": "destra",
            "centro": "centro"
        }
        
        pos = dir_map.get(direzione, "centro")
        
        # Crea segnale
        segnale = self.codificatore.crea_impulso_base(pos)
        
        # Espandi in base alla forza
        espansioni = int(forza * 4)
        for _ in range(espansioni):
            segnale = self.codificatore.espandi_segnale(segnale, Direzione.BILATERALE)
        
        return segnale
    
    def decodifica_per_azione(self, segnale: SegnaleBioelettrico) -> dict:
        """
        Decodifica segnale per uso in azione motoria
        
        Returns:
            Parametri per controllo motorio
        """
        decodifica = self.codificatore.decodifica_completa(segnale)
        
        # Mappa a parametri motori
        return {
            'velocita': decodifica['ampiezza'] / 10.0,  # 0-1
            'direzione': decodifica['direzione'],
            'potenza': decodifica['intensita'],
            'ritardo_ms': decodifica['latenza_ms']
        }


# ==================== TEST E DEMO ====================

def demo_espansione():
    """Dimostra espansione segnale"""
    print("="*70)
    print("DEMO: Espansione Segnale Bioelettrico")
    print("="*70)
    
    codificatore = CodificatoreSegnali()
    
    print("\nSequenza espansione bilaterale:")
    print("-" * 70)
    
    sequenza = codificatore.sequenza_espansione(cicli=6, direzione=Direzione.BILATERALE)
    
    for i, segnale in enumerate(sequenza):
        decodifica = codificatore.decodifica_completa(segnale)
        print(f"\nCiclo {i}:")
        print(f"  Codice: {segnale.codice}")
        print(f"  Ampiezza: {decodifica['ampiezza']:.1f}")
        print(f"  Intensità: {decodifica['intensita']:.2f}")
        print(f"  Latenza: {decodifica['latenza_ms']:.0f}ms")


def demo_direzioni():
    """Dimostra segnali in direzioni diverse"""
    print("\n" + "="*70)
    print("DEMO: Direzioni Segnale")
    print("="*70)
    
    codificatore = CodificatoreSegnali()
    
    direzioni = ["sinistra", "centro", "destra"]
    
    for dir_name in direzioni:
        print(f"\nImpulso {dir_name}:")
        segnale = codificatore.crea_impulso_base(dir_name)
        decodifica = codificatore.decodifica_completa(segnale)
        
        print(f"  Codice: {segnale.codice}")
        print(f"  Direzione: {decodifica['direzione']}")
        print(f"  Offset: {decodifica['offset']:.2f}")


def demo_potenziale_azione():
    """Dimostra potenziale d'azione completo"""
    print("\n" + "="*70)
    print("DEMO: Potenziale d'Azione Neurale")
    print("="*70)
    
    codificatore = CodificatoreSegnali()
    sequenza = codificatore.simula_potenziale_azione(ampiezza_iniziale=0.6)
    
    print(f"\nSequenza completa ({len(sequenza)} fasi)")


def demo_rete_neurale():
    """Dimostra rete di neuroni comunicanti"""
    print("\n" + "="*70)
    print("DEMO: Rete Neurale con Propagazione")
    print("="*70)
    
    rete = ReteNeurale(num_neuroni=5)
    
    print("\nPropagazione segnale neurone 0 -> neurone 4:")
    segnale = rete.propaga_segnale(0, 4, ampiezza=0.8)
    
    decodifica = rete.neuroni[0].decodifica_completa(segnale)
    print(f"\nSegnale propagato:")
    print(f"  Codice: {segnale.codice}")
    print(f"  Ampiezza: {decodifica['ampiezza']:.1f}")
    print(f"  Latenza: {decodifica['latenza_ms']:.0f}ms")
    
    print("\nPattern firing sincronizzato:")
    segnali = rete.pattern_firing("sincronizzato")
    print(f"  {len(segnali)} neuroni attivati simultaneamente")


def demo_sensori_motori():
    """Dimostra uso per sensori e motori"""
    print("\n" + "="*70)
    print("DEMO: Integrazione Sensori-Motori")
    print("="*70)
    
    simulatore = SimulatoreAttvitaNeurale()
    
    # Simula input sensoriale
    print("\n1. Input Sensoriale (intensità 0.8):")
    segnale_input = simulatore.simula_percezione_sensoriale(intensita=0.8)
    print(f"   Codice: {segnale_input.codice}")
    print(f"   Intensità: {segnale_input.intensita:.2f}")
    
    # Simula output motorio
    print("\n2. Output Motorio (forza 0.6, direzione sinistra):")
    segnale_output = simulatore.simula_comando_motorio(forza=0.6, direzione="sinistra")
    print(f"   Codice: {segnale_output.codice}")
    
    # Decodifica per azione
    parametri = simulatore.decodifica_per_azione(segnale_output)
    print(f"\n3. Parametri Motori Decodificati:")
    print(f"   Velocità: {parametri['velocita']:.2f}")
    print(f"   Direzione: {parametri['direzione']}")
    print(f"   Potenza: {parametri['potenza']:.2f}")
    print(f"   Ritardo: {parametri['ritardo_ms']:.0f}ms")


if __name__ == "__main__":
    print("""
    ================================================================
    
           SISTEMA SEGNALI BIOELETTRICI NEURALI
           Codifica Binaria per Mente Artificiale
           
    ================================================================
    """)
    
    # Esegui tutte le demo
    demo_espansione()
    demo_direzioni()
    demo_potenziale_azione()
    demo_rete_neurale()
    demo_sensori_motori()
    
    print("\n" + "="*70)
    print("[OK] DEMO COMPLETATE")
    print("="*70)

