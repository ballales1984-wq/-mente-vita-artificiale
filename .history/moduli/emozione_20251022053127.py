"""
❤️ MODULO EMOZIONE - Amigdala Artificiale
===========================================
Sistema di valutazione affettiva e reward learning.
Equivalente: Amigdala e sistema limbico

Funzioni principali:
- Valutazione emotiva delle percezioni
- Sistema di reward/punizione
- Apprendimento per rinforzo
- Modulazione risposte comportamentali
"""

from typing import Dict, Any, List, Optional
from enum import Enum
from dataclasses import dataclass
from collections import deque
from .base import ModuloCerebrale, TipoModulo, RisultatoElaborazione
from .base import richiede_inizializzazione, log_elaborazione


class StatoEmotivo(Enum):
    """Stati emotivi base"""
    NEUTRO = "neutro"
    POSITIVO = "positivo"
    NEGATIVO = "negativo"
    ALLERTA = "allerta"
    CALMO = "calmo"
    ECCITATO = "eccitato"
    ANSIOSO = "ansioso"


@dataclass
class EventoReward:
    """Evento di ricompensa/punizione"""
    azione: str
    reward: float
    timestamp: float
    contesto: Dict[str, Any]


class Amigdala(ModuloCerebrale):
    """
    Sistema di valutazione emotiva e apprendimento per rinforzo
    
    Funzionalità:
    - Valuta valenza emotiva delle percezioni
    - Assegna reward/punizione alle azioni
    - Mantiene storia emotiva
    - Modula comportamento in base allo stato affettivo
    """
    
    def __init__(self, sensibilita: float = 1.0):
        """
        Inizializza amigdala
        
        Args:
            sensibilita: Moltiplicatore sensibilità emotiva (0.1-2.0)
        """
        super().__init__("Amigdala", TipoModulo.COGNITIVO)
        
        self.sensibilita = sensibilita
        self.stato_corrente = StatoEmotivo.NEUTRO
        self.valenza_corrente = 0.0  # -1.0 (molto negativo) a +1.0 (molto positivo)
        self.arousal_corrente = 0.5  # 0.0 (calmo) a 1.0 (eccitato)
        
        # Storia emotiva
        self.storia_emozioni = deque(maxlen=100)
        self.storia_reward = deque(maxlen=1000)
        
        # Pesi per valutazione
        self.pesi_valutazione = {
            'pericolo': -0.8,
            'persona': 0.3,
            'comando': 0.5,
            'successo': 0.9,
            'fallimento': -0.7,
            'novita': 0.4
        }
        
        # Reward cumulativo
        self.reward_totale = 0.0
        self.reward_medio = 0.0
    
    def inizializza(self) -> bool:
        """Inizializza sistema emotivo"""
        print(f"[{self.nome}] Inizializzazione...")
        print(f"[{self.nome}] Sensibilità: {self.sensibilita}")
        
        self.attivo = True
        self.modalita_reale = True
        
        print(f"[{self.nome}] ✅ Inizializzato")
        return True
    
    @richiede_inizializzazione
    @log_elaborazione
    def elabora(self, input_data: Dict[str, Any]) -> RisultatoElaborazione:
        """
        Valuta stato emotivo basato su percezioni
        
        Args:
            input_data: Dict con:
                - percezioni: Lista percezioni (visive/uditive)
                - memoria: Contesto dalla memoria
                - azione_precedente: Azione appena eseguita
                - successo_azione: Se azione riuscita
                
        Returns:
            RisultatoElaborazione con stato emotivo
        """
        percezioni = input_data.get('percezioni', [])
        memoria = input_data.get('memoria', {})
        azione = input_data.get('azione_precedente')
        successo = input_data.get('successo_azione', True)
        
        # Valuta valenza emotiva
        valenza = self._valuta_valenza(percezioni, memoria)
        
        # Calcola arousal
        arousal = self._calcola_arousal(percezioni)
        
        # Determina stato emotivo
        stato = self._determina_stato(valenza, arousal)
        
        # Aggiorna stato interno
        self.stato_corrente = stato
        self.valenza_corrente = valenza
        self.arousal_corrente = arousal
        
        # Registra in storia
        self.storia_emozioni.append({
            'stato': stato,
            'valenza': valenza,
            'arousal': arousal,
            'timestamp': __import__('time').time()
        })
        
        # Calcola reward se c'è stata un'azione
        reward = 0.0
        if azione:
            reward = self.assegna_reward(azione, successo, valenza)
        
        return RisultatoElaborazione(
            tipo="reale",
            successo=True,
            dati={
                'stato_emotivo': stato.value,
                'valenza': valenza,
                'arousal': arousal,
                'reward': reward,
                'modulazione_comportamentale': self._genera_modulazione(stato)
            },
            metadata={
                'reward_totale': self.reward_totale,
                'reward_medio': self.reward_medio
            }
        )
    
    def _valuta_valenza(self, percezioni: List[Dict], memoria: Dict) -> float:
        """
        Valuta valenza emotiva (positivo/negativo)
        
        Args:
            percezioni: Lista percezioni
            memoria: Contesto memoria
            
        Returns:
            float: Valenza da -1.0 a +1.0
        """
        valenza = 0.0
        
        # Valuta ogni percezione
        for percezione in percezioni:
            if isinstance(percezione, dict):
                # Percezioni visive
                if 'oggetti' in percezione:
                    for obj in percezione['oggetti']:
                        classe = obj.get('classe', '')
                        
                        # Check pericoli
                        if any(p in classe.lower() for p in ['car', 'truck', 'vehicle']):
                            valenza -= 0.5
                        
                        # Check positivi
                        if 'person' in classe.lower():
                            valenza += 0.3
                
                # Percezioni uditive
                if 'tono' in percezione:
                    tono = percezione['tono']
                    if tono == 'amichevole':
                        valenza += 0.4
                    elif tono == 'urgente':
                        valenza -= 0.2
                    elif tono == 'negativo':
                        valenza -= 0.5
                
                if 'emozione' in percezione:
                    emozione = percezione['emozione']
                    if emozione == 'gioia':
                        valenza += 0.6
                    elif emozione in ['tristezza', 'rabbia']:
                        valenza -= 0.5
                    elif emozione == 'paura':
                        valenza -= 0.7
        
        # Applica sensibilità
        valenza *= self.sensibilita
        
        # Clamp tra -1 e +1
        return max(-1.0, min(1.0, valenza))
    
    def _calcola_arousal(self, percezioni: List[Dict]) -> float:
        """
        Calcola livello di attivazione/eccitazione
        
        Args:
            percezioni: Lista percezioni
            
        Returns:
            float: Arousal da 0.0 (calmo) a 1.0 (eccitato)
        """
        arousal = 0.5  # baseline
        
        # Più percezioni = più arousal
        arousal += len(percezioni) * 0.1
        
        # Novità aumenta arousal
        for percezione in percezioni:
            if isinstance(percezione, dict):
                if percezione.get('rilevanza', 0) > 0.7:
                    arousal += 0.2
                
                # Comandi/pericoli aumentano arousal
                if any(k in percezione for k in ['comando', 'pericolo', 'urgente']):
                    arousal += 0.3
        
        return max(0.0, min(1.0, arousal))
    
    def _determina_stato(self, valenza: float, arousal: float) -> StatoEmotivo:
        """
        Determina stato emotivo da valenza e arousal (modello circomplesso)
        
        Args:
            valenza: Valenza emotiva (-1 a +1)
            arousal: Livello attivazione (0 a 1)
            
        Returns:
            StatoEmotivo
        """
        # Modello circomplesso delle emozioni
        if arousal < 0.4:  # Basso arousal
            if valenza > 0.2:
                return StatoEmotivo.CALMO
            elif valenza < -0.2:
                return StatoEmotivo.NEGATIVO
            else:
                return StatoEmotivo.NEUTRO
        
        elif arousal > 0.7:  # Alto arousal
            if valenza > 0.3:
                return StatoEmotivo.ECCITATO
            elif valenza < -0.3:
                return StatoEmotivo.ANSIOSO
            else:
                return StatoEmotivo.ALLERTA
        
        else:  # Arousal medio
            if valenza > 0.3:
                return StatoEmotivo.POSITIVO
            elif valenza < -0.3:
                return StatoEmotivo.NEGATIVO
            else:
                return StatoEmotivo.NEUTRO
    
    def assegna_reward(self, azione: str, successo: bool, valenza: float = 0.0) -> float:
        """
        Assegna reward/punizione per un'azione
        
        Args:
            azione: Nome azione eseguita
            successo: Se azione riuscita
            valenza: Valenza emotiva contesto
            
        Returns:
            float: Reward value
        """
        # Reward base
        if successo:
            reward = 1.0
        else:
            reward = -0.5
        
        # Modifica basata su valenza emotiva
        reward += valenza * 0.5
        
        # Bonus/penalità per azioni specifiche
        bonus_azioni = {
            'evita_ostacolo': 0.5,  # Bonus per sicurezza
            'esegui_comando': 0.3,  # Bonus per obbedienza
            'mantieni_distanza': 0.2,
            'allontanati': 0.1
        }
        
        reward += bonus_azioni.get(azione, 0.0)
        
        # Registra in storia
        evento = EventoReward(
            azione=azione,
            reward=reward,
            timestamp=__import__('time').time(),
            contesto={'successo': successo, 'valenza': valenza}
        )
        self.storia_reward.append(evento)
        
        # Aggiorna statistiche
        self.reward_totale += reward
        if len(self.storia_reward) > 0:
            self.reward_medio = sum(e.reward for e in self.storia_reward) / len(self.storia_reward)
        
        print(f"[{self.nome}] Reward: {reward:+.2f} per '{azione}' (totale: {self.reward_totale:.2f})")
        
        return reward
    
    def _genera_modulazione(self, stato: StatoEmotivo) -> Dict[str, Any]:
        """
        Genera suggerimenti di modulazione comportamentale
        
        Args:
            stato: Stato emotivo corrente
            
        Returns:
            Dict con parametri di modulazione
        """
        modulazioni = {
            StatoEmotivo.NEUTRO: {
                'velocita_modifier': 1.0,
                'cautela': 0.5,
                'esplorazione': 0.7
            },
            StatoEmotivo.POSITIVO: {
                'velocita_modifier': 1.2,
                'cautela': 0.3,
                'esplorazione': 0.9
            },
            StatoEmotivo.NEGATIVO: {
                'velocita_modifier': 0.7,
                'cautela': 0.8,
                'esplorazione': 0.3
            },
            StatoEmotivo.ALLERTA: {
                'velocita_modifier': 0.8,
                'cautela': 0.9,
                'esplorazione': 0.2
            },
            StatoEmotivo.CALMO: {
                'velocita_modifier': 0.9,
                'cautela': 0.4,
                'esplorazione': 0.6
            },
            StatoEmotivo.ECCITATO: {
                'velocita_modifier': 1.3,
                'cautela': 0.4,
                'esplorazione': 1.0
            },
            StatoEmotivo.ANSIOSO: {
                'velocita_modifier': 0.6,
                'cautela': 1.0,
                'esplorazione': 0.1
            }
        }
        
        return modulazioni.get(stato, modulazioni[StatoEmotivo.NEUTRO])
    
    def get_stato_emotivo(self) -> StatoEmotivo:
        """Ottieni stato emotivo corrente"""
        return self.stato_corrente
    
    def get_statistiche_reward(self) -> Dict[str, Any]:
        """Ottieni statistiche reward"""
        if not self.storia_reward:
            return {
                'reward_totale': 0.0,
                'reward_medio': 0.0,
                'num_eventi': 0
            }
        
        rewards = [e.reward for e in self.storia_reward]
        return {
            'reward_totale': self.reward_totale,
            'reward_medio': self.reward_medio,
            'reward_max': max(rewards),
            'reward_min': min(rewards),
            'num_eventi': len(self.storia_reward),
            'ultimi_10': list(self.storia_reward)[-10:]
        }
    
    def reset_stato(self):
        """Reset stato emotivo"""
        self.stato_corrente = StatoEmotivo.NEUTRO
        self.valenza_corrente = 0.0
        self.arousal_corrente = 0.5
    
    def chiudi(self):
        """Cleanup"""
        print(f"[{self.nome}] Chiusura...")
        print(f"[{self.nome}] Reward totale: {self.reward_totale:.2f}")
        self.attivo = False


# Istanza globale
_amigdala = None

def get_instance() -> Amigdala:
    """Ottieni istanza singleton"""
    global _amigdala
    if _amigdala is None:
        _amigdala = Amigdala()
        _amigdala.inizializza()
    return _amigdala


# API semplificata
def valuta_emozione(percezioni: List[Dict], memoria: Dict = None) -> Dict[str, Any]:
    """Valuta stato emotivo"""
    amigdala = get_instance()
    risultato = amigdala.elabora({
        'percezioni': percezioni,
        'memoria': memoria or {}
    })
    return risultato.dati


def assegna_reward(azione: str, successo: bool) -> float:
    """Assegna reward per azione"""
    return get_instance().assegna_reward(azione, successo)


# Test del modulo
if __name__ == "__main__":
    print("="*60)
    print("🧪 Test Modulo Emozione")
    print("="*60)
    
    # Crea istanza
    amigdala = Amigdala(sensibilita=1.0)
    amigdala.inizializza()
    
    # Test con percezioni simulate
    percezioni_test = [
        {
            'tipo': 'visivo',
            'oggetti': [
                {'classe': 'person', 'confidenza': 0.85}
            ]
        },
        {
            'tipo': 'uditivo',
            'testo': 'Ciao, vieni qui',
            'tono': 'amichevole',
            'emozione': 'gioia'
        }
    ]
    
    print("\n--- Test Valutazione Emotiva ---")
    risultato = amigdala.elabora({'percezioni': percezioni_test})
    
    print(f"\nRisultato:")
    print(f"  Stato: {risultato.dati['stato_emotivo']}")
    print(f"  Valenza: {risultato.dati['valenza']:.2f}")
    print(f"  Arousal: {risultato.dati['arousal']:.2f}")
    
    # Test reward
    print("\n--- Test Reward ---")
    reward1 = amigdala.assegna_reward('evita_ostacolo', True, valenza=0.3)
    reward2 = amigdala.assegna_reward('esegui_comando', True, valenza=0.8)
    reward3 = amigdala.assegna_reward('monitora_ambiente', False, valenza=-0.2)
    
    # Statistiche
    print("\n--- Statistiche ---")
    stats = amigdala.get_statistiche_reward()
    print(f"  Reward totale: {stats['reward_totale']:.2f}")
    print(f"  Reward medio: {stats['reward_medio']:.2f}")
    print(f"  Eventi: {stats['num_eventi']}")
    
    amigdala.chiudi()
    print("\n✅ Test completato")

