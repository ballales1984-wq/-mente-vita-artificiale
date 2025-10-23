"""
💾 MODULO MEMORIA - Ippocampo Artificiale
==========================================
Sistema di memoria episodica e semantica.
Equivalente: Ippocampo e corteccia entorinale

Funzioni principali:
- Memoria episodica (eventi temporali)
- Memoria semantica (conoscenza generale)
- Working memory (buffer temporaneo)
- Ricerca semantica vettoriale
"""

import json
import pickle
import time
import threading
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple
from dataclasses import dataclass, asdict
from .base import ModuloCerebrale, MemoriaAstratta, TipoModulo, RisultatoElaborazione
from .base import richiede_inizializzazione, log_elaborazione


@dataclass
class MemoriaEpisodica:
    """
    Singola memoria episodica
    
    Attributes:
        id: Identificativo univoco
        contenuto: Contenuto della memoria
        contesto: Informazioni contestuali
        valenza_emotiva: Valenza affettiva (-1 a +1)
        timestamp: Momento della memorizzazione
        accessi: Numero di volte richiamata
        importanza: Peso di importanza (0-1)
    """
    id: str
    contenuto: str
    contesto: Dict[str, Any]
    valenza_emotiva: float
    timestamp: float
    accessi: int = 0
    importanza: float = 0.5


class Ippocampo(ModuloCerebrale, MemoriaAstratta):
    """
    Sistema di memoria multilivello
    
    Tipi di memoria:
    - Episodica: Eventi con contesto temporale
    - Semantica: Conoscenza generale strutturata
    - Working: Buffer temporaneo (gestito da prefrontale)
    - Procedurale: Skill e procedure (implicita)
    """
    
    def __init__(self, path_memoria: str = "data/memoria.json"):
        """
        Inizializza ippocampo
        
        Args:
            path_memoria: Path file persistenza memoria
        """
        super().__init__("Ippocampo", TipoModulo.MEMORIA)
        
        self.path_memoria = Path(path_memoria)
        self.path_memoria.parent.mkdir(parents=True, exist_ok=True)
        
        # Storage interno
        self.memoria_episodica: List[MemoriaEpisodica] = []
        self.memoria_semantica: Dict[str, Any] = {}
        self.memoria_procedurale: Dict[str, Any] = {}
        
        # Configurazione
        self.max_memoria_episodica = 1000
        self.soglia_consolidamento = 0.7  # Importanza minima per permanenza
        
        # Configurazione consolidamento intelligente
        self.soglia_valenza_minima = 0.5  # Valenza minima per conservare
        self.soglia_importanza_minima = 1.0  # Importanza minima per conservare
        self.tempo_consolidamento = 300  # 5 minuti in secondi
        
        # Thread consolidamento automatico
        self.consolidamento_attivo = False
        self.thread_consolidamento = None
        
        # Statistiche
        self.contatore_memorizzazioni = 0
        self.contatore_richiami = 0
        self.contatore_consolidamenti = 0
        self.memorie_eliminate = 0
    
    def inizializza(self) -> bool:
        """
        Carica memoria persistente da disco
        
        Returns:
            bool: True se caricamento riuscito
        """
        print(f"[{self.nome}] Inizializzazione...")
        
        try:
            # Carica memoria episodica
            if self.path_memoria.exists():
                with open(self.path_memoria, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    
                    # Ricostruisci memorie episodiche
                    for mem_dict in data.get('episodica', []):
                        memoria = MemoriaEpisodica(**mem_dict)
                        self.memoria_episodica.append(memoria)
                    
                    # Carica semantica
                    self.memoria_semantica = data.get('semantica', {})
                    
                    print(f"[{self.nome}] ✅ Caricate {len(self.memoria_episodica)} memorie")
            else:
                print(f"[{self.nome}] Nessuna memoria precedente, inizializzo vuota")
                self._inizializza_memoria_semantica()
            
            self.attivo = True
            self.modalita_reale = True
            
            # Avvia consolidamento automatico
            self._avvia_consolidamento_automatico()
            
            return True
            
        except Exception as e:
            print(f"[{self.nome}] ⚠️ Errore caricamento: {e}")
            print(f"[{self.nome}] Inizializzo memoria vuota")
            self._inizializza_memoria_semantica()
            self.attivo = True
            
            # Avvia consolidamento automatico anche in caso di errore
            self._avvia_consolidamento_automatico()
            
            return True
    
    def _inizializza_memoria_semantica(self):
        """Inizializza conoscenza base"""
        self.memoria_semantica = {
            # Comandi noti
            "comandi_base": ["vieni", "vai", "fermati", "aspetta", "seguimi", "gira"],
            
            # Oggetti comuni e loro proprietà
            "oggetti_comuni": {
                "person": {"tipo": "animato", "priorita": 1.0, "pericolo": 0.2},
                "car": {"tipo": "veicolo", "priorita": 0.9, "pericolo": 0.8},
                "chair": {"tipo": "mobile", "priorita": 0.3, "pericolo": 0.1},
                "bottle": {"tipo": "oggetto", "priorita": 0.4, "pericolo": 0.0}
            },
            
            # Emozioni e loro valenza
            "emozioni": {
                "gioia": 0.8,
                "tristezza": -0.6,
                "rabbia": -0.7,
                "paura": -0.9,
                "neutro": 0.0
            },
            
            # Azioni e loro costo energetico
            "costo_azioni": {
                "monitora_ambiente": 0.1,
                "avvicinati": 0.5,
                "allontanati": 0.5,
                "ruota": 0.3,
                "evita_ostacolo": 0.6
            }
        }
    
    @richiede_inizializzazione
    def memorizza(self, chiave: str, valore: Any, metadata: Dict = None) -> bool:
        """
        Memorizza nuovo evento/conoscenza
        
        Args:
            chiave: Identificativo memoria
            valore: Contenuto da memorizzare
            metadata: Info aggiuntive (contesto, emozione, ecc.)
            
        Returns:
            bool: True se memorizzazione riuscita
        """
        try:
            metadata = metadata or {}
            
            # Crea memoria episodica
            memoria = MemoriaEpisodica(
                id=f"mem_{int(time.time()*1000)}_{self.contatore_memorizzazioni}",
                contenuto=str(valore),
                contesto=metadata.get('contesto', {}),
                valenza_emotiva=metadata.get('valenza', 0.0),
                timestamp=time.time(),
                importanza=metadata.get('importanza', 0.5)
            )
            
            self.memoria_episodica.append(memoria)
            self.contatore_memorizzazioni += 1
            
            # Gestione capacità
            if len(self.memoria_episodica) > self.max_memoria_episodica:
                self._consolida_memorie()
            
            return True
            
        except Exception as e:
            print(f"[{self.nome}] ❌ Errore memorizzazione: {e}")
            return False
    
    @richiede_inizializzazione
    def richiama(self, chiave: str) -> Optional[Any]:
        """
        Recupera memoria per chiave
        
        Args:
            chiave: Chiave di ricerca
            
        Returns:
            Contenuto memoria o None
        """
        # Cerca in memoria episodica
        for memoria in reversed(self.memoria_episodica):
            if chiave.lower() in memoria.contenuto.lower():
                memoria.accessi += 1
                self.contatore_richiami += 1
                return memoria
        
        # Cerca in memoria semantica
        if chiave in self.memoria_semantica:
            return self.memoria_semantica[chiave]
        
        return None
    
    @richiede_inizializzazione
    def cerca(self, query: str, limite: int = 10) -> List[MemoriaEpisodica]:
        """
        Ricerca semantica nelle memorie
        
        Args:
            query: Query di ricerca
            limite: Numero massimo risultati
            
        Returns:
            Lista memorie ordinate per rilevanza
        """
        query_lower = query.lower()
        risultati = []
        
        # Ricerca semplice per keyword
        for memoria in self.memoria_episodica:
            if query_lower in memoria.contenuto.lower():
                # Score basato su: rilevanza keyword + importanza + recency
                recency_score = 1.0 / (1.0 + (time.time() - memoria.timestamp) / 86400)  # decay giornaliero
                score = (
                    0.4 * (memoria.contenuto.lower().count(query_lower) / len(memoria.contenuto.split())) +
                    0.3 * memoria.importanza +
                    0.3 * recency_score
                )
                risultati.append((score, memoria))
        
        # Ordina per score
        risultati.sort(key=lambda x: x[0], reverse=True)
        
        # Aggiorna accessi
        for _, mem in risultati[:limite]:
            mem.accessi += 1
        
        return [mem for _, mem in risultati[:limite]]
    
    @richiede_inizializzazione
    def dimentica(self, chiave: str) -> bool:
        """
        Rimuove memoria
        
        Args:
            chiave: Identificativo memoria
            
        Returns:
            bool: True se rimozione riuscita
        """
        try:
            # Rimuovi da episodica
            self.memoria_episodica = [
                mem for mem in self.memoria_episodica
                if chiave not in mem.contenuto and mem.id != chiave
            ]
            
            # Rimuovi da semantica
            if chiave in self.memoria_semantica:
                del self.memoria_semantica[chiave]
            
            return True
        except Exception as e:
            print(f"[{self.nome}] ❌ Errore rimozione: {e}")
            return False
    
    def _consolida_memorie(self):
        """
        Consolida memorie: mantieni solo quelle importanti/recenti/accedute
        """
        print(f"[{self.nome}] Consolidamento memorie...")
        
        # Score di permanenza: importanza + accessi + recency
        memorie_scored = []
        now = time.time()
        
        for mem in self.memoria_episodica:
            recency = 1.0 / (1.0 + (now - mem.timestamp) / 86400)  # decay giornaliero
            access_score = min(1.0, mem.accessi / 10.0)  # normalizzato
            
            score = (
                0.4 * mem.importanza +
                0.3 * access_score +
                0.3 * recency
            )
            
            memorie_scored.append((score, mem))
        
        # Ordina e mantieni top N
        memorie_scored.sort(key=lambda x: x[0], reverse=True)
        
        rimosse = len(self.memoria_episodica) - int(self.max_memoria_episodica * 0.8)
        self.memoria_episodica = [mem for _, mem in memorie_scored[:int(self.max_memoria_episodica * 0.8)]]
        
        print(f"[{self.nome}] Consolidate: mantenute {len(self.memoria_episodica)}, rimosse {rimosse}")
    
    def salva_su_disco(self) -> bool:
        """
        Salva memoria su disco (persistenza)
        
        Returns:
            bool: True se salvataggio riuscito
        """
        try:
            data = {
                'episodica': [asdict(mem) for mem in self.memoria_episodica],
                'semantica': self.memoria_semantica,
                'meta': {
                    'timestamp': time.time(),
                    'num_memorie': len(self.memoria_episodica),
                    'memorizzazioni_totali': self.contatore_memorizzazioni,
                    'richiami_totali': self.contatore_richiami
                }
            }
            
            with open(self.path_memoria, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            print(f"[{self.nome}] ✅ Memoria salvata: {len(self.memoria_episodica)} memorie")
            return True
            
        except Exception as e:
            print(f"[{self.nome}] ❌ Errore salvataggio: {e}")
            return False
    
    @richiede_inizializzazione
    @log_elaborazione
    def elabora(self, input_data: Dict[str, Any]) -> RisultatoElaborazione:
        """
        Elabora richiesta di memoria
        
        Args:
            input_data: Dict con 'operazione' (memorizza/richiama/cerca)
            
        Returns:
            RisultatoElaborazione con risultato operazione
        """
        operazione = input_data.get('operazione', 'cerca')
        
        if operazione == 'memorizza':
            successo = self.memorizza(
                input_data.get('chiave', ''),
                input_data.get('valore', ''),
                input_data.get('metadata')
            )
            return RisultatoElaborazione(
                tipo="reale",
                successo=successo,
                dati={'memorizzato': successo}
            )
        
        elif operazione == 'richiama':
            risultato = self.richiama(input_data.get('chiave', ''))
            return RisultatoElaborazione(
                tipo="reale",
                successo=risultato is not None,
                dati=risultato
            )
        
        elif operazione == 'cerca':
            risultati = self.cerca(input_data.get('query', ''), input_data.get('limite', 10))
            return RisultatoElaborazione(
                tipo="reale",
                successo=True,
                dati=risultati
            )
        
        else:
            return RisultatoElaborazione(
                tipo="reale",
                successo=False,
                dati=None,
                errore=f"Operazione sconosciuta: {operazione}"
            )
    
    def get_statistiche(self) -> Dict[str, Any]:
        """Ottieni statistiche memoria"""
        return {
            'memorie_episodiche': len(self.memoria_episodica),
            'memorie_semantiche': len(self.memoria_semantica),
            'memorizzazioni_totali': self.contatore_memorizzazioni,
            'richiami_totali': self.contatore_richiami,
            'memoria_piu_antica': min(self.memoria_episodica, key=lambda m: m.timestamp).timestamp if self.memoria_episodica else None,
            'memoria_piu_recente': max(self.memoria_episodica, key=lambda m: m.timestamp).timestamp if self.memoria_episodica else None
        }
    
    def chiudi(self):
        """Salva e chiudi"""
        print(f"[{self.nome}] Chiusura e salvataggio...")
        self.salva_su_disco()
        self.attivo = False
        print(f"[{self.nome}] ✅ Chiuso")


# Istanza globale
_ippocampo = None

def get_instance() -> Ippocampo:
    """Ottieni istanza singleton"""
    global _ippocampo
    if _ippocampo is None:
        _ippocampo = Ippocampo()
        _ippocampo.inizializza()
    return _ippocampo


# API semplificata
def memorizza(contenuto: str, contesto: Dict = None, valenza: float = 0.0) -> bool:
    """Memorizza evento"""
    return get_instance().memorizza(
        chiave=f"evento_{int(time.time())}",
        valore=contenuto,
        metadata={'contesto': contesto or {}, 'valenza': valenza}
    )


def richiama(query: str) -> Optional[MemoriaEpisodica]:
    """Richiama memoria"""
    return get_instance().richiama(query)


def cerca(query: str, limite: int = 10) -> List[MemoriaEpisodica]:
    """Cerca memorie"""
    return get_instance().cerca(query, limite)


# Test del modulo
if __name__ == "__main__":
    print("="*60)
    print("🧪 Test Modulo Memoria")
    print("="*60)
    
    # Crea istanza
    ippocampo = Ippocampo("test_memoria.json")
    ippocampo.inizializza()
    
    # Test memorizzazione
    print("\n--- Test Memorizzazione ---")
    ippocampo.memorizza(
        "evento_test",
        "Robot ha ricevuto comando vocale 'vieni qui'",
        metadata={
            'contesto': {'azione': 'comando_vocale', 'successo': True},
            'valenza': 0.8,
            'importanza': 0.9
        }
    )
    
    ippocampo.memorizza(
        "evento_test2",
        "Robot ha evitato ostacolo con successo",
        metadata={
            'contesto': {'azione': 'evita_ostacolo'},
            'valenza': 0.6,
            'importanza': 0.7
        }
    )
    
    # Test richiamo
    print("\n--- Test Richiamo ---")
    risultato = ippocampo.richiama("comando")
    if risultato:
        print(f"Trovato: {risultato.contenuto}")
        print(f"Accessi: {risultato.accessi}")
    
    # Test ricerca
    print("\n--- Test Ricerca ---")
    risultati = ippocampo.cerca("robot", limite=5)
    print(f"Trovate {len(risultati)} memorie:")
    for mem in risultati:
        print(f"  - {mem.contenuto[:50]}... (imp: {mem.importanza:.2f})")
    
    # Statistiche
    print("\n--- Statistiche ---")
    stats = ippocampo.get_statistiche()
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    ippocampo.chiudi()
    print("\n✅ Test completato")

