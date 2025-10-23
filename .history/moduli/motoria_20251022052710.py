"""
🦿 MODULO MOTORIA - Corteccia Motoria
======================================
Simula l'esecuzione di azioni fisiche e movimenti
Equivalente: Corteccia motoria primaria (M1) e area premotoria
"""

import time
from typing import Dict, Any, List, Optional
from dataclasses import dataclass


@dataclass
class ComandoMotorio:
    """Comando per attuatori"""
    tipo: str  # rotazione, traslazione, manipolazione
    parametri: Dict[str, Any]
    priorita: int = 5
    timeout: float = 5.0


@dataclass
class FeedbackSensoriale:
    """Feedback dai sensori motori"""
    posizione: Dict[str, float]
    velocita: Dict[str, float]
    forza: Optional[float] = None
    errore: Optional[str] = None


class CortecciaMotoria:
    """
    Modulo di controllo motorio
    Funzioni:
    - Esecuzione movimenti
    - Controllo attuatori
    - Feedback propriocettivo
    - Coordinazione fine
    """
    
    def __init__(self):
        self.nome = "Corteccia Motoria"
        self.posizione_corrente = {"x": 0.0, "y": 0.0, "theta": 0.0}
        self.velocita_corrente = {"linear": 0.0, "angular": 0.0}
        self.stato_attuatori = {}
        self.cronologia_azioni = []
        self.modalita_simulazione = True  # True se hardware non disponibile
        
        print(f"[{self.nome}] ✅ Inizializzato (modalità: {'simulazione' if self.modalita_simulazione else 'reale'})")
    
    def agisci(self, decisione: Dict[str, Any]) -> bool:
        """
        Esegue azione basata su decisione cognitiva
        
        Args:
            decisione: Dict con 'azione' e 'parametri'
            
        Returns:
            bool: True se successo
        """
        azione = decisione.get('azione', 'noop')
        parametri = decisione.get('parametri', {})
        
        print(f"[{self.nome}] Esecuzione azione: {azione}")
        
        # Mappa azione -> metodo
        azioni_disponibili = {
            'avvicinati': self._avvicinati,
            'avvicinati_con_cautela': self._avvicinati,
            'allontanati': self._allontanati,
            'evita_ostacolo': self._evita_ostacolo,
            'fermati': self._fermati,
            'ruota': self._ruota,
            'segui': self._segui,
            'mantieni_distanza': self._mantieni_distanza,
            'monitora_ambiente': self._monitora,
            'esegui_comando': self._esegui_comando_custom,
            'noop': lambda p: True
        }
        
        # Esegui azione
        metodo = azioni_disponibili.get(azione, self._azione_sconosciuta)
        
        try:
            successo = metodo(parametri)
            
            # Registra in cronologia
            self.cronologia_azioni.append({
                'azione': azione,
                'parametri': parametri,
                'successo': successo,
                'timestamp': time.time()
            })
            
            return successo
        except Exception as e:
            print(f"[{self.nome}] ❌ Errore: {e}")
            return False
    
    def _avvicinati(self, params: Dict) -> bool:
        """Muovi verso un target"""
        velocita = params.get('velocita', 0.5)
        distanza = params.get('distanza', 1.0)
        cautela = params.get('modalita', 'normale') == 'cautela'
        
        if cautela:
            velocita *= 0.5
        
        print(f"  🏃 Avvicinamento a {velocita:.2f} m/s per {distanza:.2f}m")
        
        # Simula movimento
        durata = distanza / velocita
        self._simula_movimento(velocita, 0.0, durata)
        
        return True
    
    def _allontanati(self, params: Dict) -> bool:
        """Allontanati da pericolo"""
        velocita = params.get('velocita', 0.8)
        distanza = params.get('distanza', 2.0)
        
        print(f"  🏃 Allontanamento a {velocita:.2f} m/s per {distanza:.2f}m")
        
        # Movimento indietro
        self._simula_movimento(-velocita, 0.0, distanza / velocita)
        
        return True
    
    def _evita_ostacolo(self, params: Dict) -> bool:
        """Manovra evasiva"""
        direzione = params.get('direzione', 'destra')
        angolo = params.get('angolo', 45)
        
        print(f"  🔄 Evitamento: ruota {angolo}° verso {direzione}")
        
        # Ruota
        self._ruota({'angolo': angolo if direzione == 'destra' else -angolo})
        
        # Avanza
        self._simula_movimento(0.5, 0.0, 1.0)
        
        return True
    
    def _fermati(self, params: Dict) -> bool:
        """Stop immediato"""
        print(f"  🛑 STOP")
        
        self.velocita_corrente = {"linear": 0.0, "angular": 0.0}
        
        return True
    
    def _ruota(self, params: Dict) -> bool:
        """Rotazione sul posto"""
        angolo = params.get('angolo', 90)
        velocita_ang = params.get('velocita_angolare', 30)  # deg/s
        
        print(f"  🔄 Rotazione: {angolo}°")
        
        durata = abs(angolo) / velocita_ang
        self._simula_movimento(0.0, velocita_ang if angolo > 0 else -velocita_ang, durata)
        
        return True
    
    def _segui(self, params: Dict) -> bool:
        """Segui un target in movimento"""
        target = params.get('target', 'person')
        distanza = params.get('distanza_sicurezza', 1.5)
        
        print(f"  👣 Seguimento target: {target} (distanza: {distanza}m)")
        
        # Simula movimento adattivo
        self._simula_movimento(0.3, 0.0, 2.0)
        
        return True
    
    def _mantieni_distanza(self, params: Dict) -> bool:
        """Mantieni distanza di sicurezza"""
        distanza_target = params.get('distanza', 1.0)
        
        print(f"  📏 Mantenimento distanza: {distanza_target}m")
        
        # Regolazione fine posizione
        self._simula_movimento(0.1, 0.0, 0.5)
        
        return True
    
    def _monitora(self, params: Dict) -> bool:
        """Modalità monitoring (nessun movimento)"""
        print(f"  👁️ Monitoraggio ambiente")
        time.sleep(0.1)
        return True
    
    def _esegui_comando_custom(self, params: Dict) -> bool:
        """Esegui comando personalizzato"""
        comando = params.get('comando', 'unknown')
        print(f"  ⚙️ Comando custom: {comando}")
        
        # Interpreta comando
        if 'muovi' in comando.lower():
            return self._avvicinati(params)
        elif 'ruota' in comando.lower():
            return self._ruota(params)
        else:
            return True
    
    def _azione_sconosciuta(self, params: Dict) -> bool:
        """Fallback per azioni non riconosciute"""
        print(f"  ⚠️ Azione sconosciuta, nessun movimento")
        return False
    
    def _simula_movimento(self, vel_linear: float, vel_angular: float, durata: float):
        """Simula movimento con aggiornamento stato"""
        
        # Aggiorna velocità
        self.velocita_corrente = {
            "linear": vel_linear,
            "angular": vel_angular
        }
        
        # Simula delay movimento
        time.sleep(min(durata, 0.5))  # Max 0.5s per non bloccare
        
        # Aggiorna posizione (approssimata)
        self.posizione_corrente["x"] += vel_linear * durata
        self.posizione_corrente["theta"] += vel_angular * durata
        
        # Normalizza theta
        self.posizione_corrente["theta"] %= 360
        
        print(f"    Posizione: x={self.posizione_corrente['x']:.2f}, "
              f"y={self.posizione_corrente['y']:.2f}, "
              f"θ={self.posizione_corrente['theta']:.1f}°")
    
    def controlla_attuatore(self, attuatore_id: str, valore: float) -> bool:
        """
        Controlla singolo attuatore (servo, motor, ecc.)
        
        Args:
            attuatore_id: ID attuatore
            valore: Valore comando (0-100 o -100/+100)
        """
        print(f"[{self.nome}] Attuatore {attuatore_id}: {valore}")
        
        self.stato_attuatori[attuatore_id] = valore
        
        # TODO: Implementare controllo hardware reale
        # es: GPIO, serial, I2C, ecc.
        
        return True
    
    def leggi_sensori(self) -> FeedbackSensoriale:
        """Leggi feedback da sensori propriocettivi"""
        
        # TODO: Implementare lettura sensori reali
        # es: encoder, IMU, force sensors
        
        return FeedbackSensoriale(
            posizione=self.posizione_corrente.copy(),
            velocita=self.velocita_corrente.copy()
        )
    
    def reset_posizione(self):
        """Reset alla posizione iniziale"""
        print(f"[{self.nome}] Reset posizione")
        self.posizione_corrente = {"x": 0.0, "y": 0.0, "theta": 0.0}
        self.velocita_corrente = {"linear": 0.0, "angular": 0.0}
    
    def get_cronologia(self, ultimi_n: int = 10) -> List[Dict]:
        """Ottieni cronologia azioni"""
        return self.cronologia_azioni[-ultimi_n:]


# Istanza globale
_corteccia_motoria = None

def get_instance() -> CortecciaMotoria:
    """Ottieni istanza singleton"""
    global _corteccia_motoria
    if _corteccia_motoria is None:
        _corteccia_motoria = CortecciaMotoria()
    return _corteccia_motoria


# API semplificata
def agisci(decisione: Dict[str, Any]) -> bool:
    """Esegui azione"""
    return get_instance().agisci(decisione)


def fermati():
    """Stop immediato"""
    return get_instance()._fermati({})


def posizione() -> Dict[str, float]:
    """Leggi posizione corrente"""
    return get_instance().posizione_corrente.copy()


# Test del modulo
if __name__ == "__main__":
    print("="*60)
    print("🧪 Test Modulo Motoria")
    print("="*60)
    
    corteccia = CortecciaMotoria()
    
    # Test varie azioni
    azioni_test = [
        {'azione': 'avvicinati', 'parametri': {'velocita': 0.5, 'distanza': 2.0}},
        {'azione': 'ruota', 'parametri': {'angolo': 90}},
        {'azione': 'evita_ostacolo', 'parametri': {'direzione': 'sinistra'}},
        {'azione': 'fermati', 'parametri': {}}
    ]
    
    for azione in azioni_test:
        print(f"\n--- Test: {azione['azione']} ---")
        successo = corteccia.agisci(azione)
        print(f"Risultato: {'✅' if successo else '❌'}")
        time.sleep(0.5)
    
    print(f"\n📊 Cronologia: {len(corteccia.cronologia_azioni)} azioni eseguite")
    print("\n✅ Test completato")

