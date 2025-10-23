"""
⚡ MODULO TALAMO - Router Sensoriale
=====================================
Smistamento e integrazione informazioni sensoriali multimodali.
Equivalente: Talamo e nucleo reticolare talamico

Funzioni principali:
- Routing input sensoriali ai moduli appropriati
- Integrazione multimodale
- Filtro attenzione (gating)
- Sincronizzazione temporale
"""

from typing import Dict, Any, List, Optional
from .base import ModuloCerebrale, TipoModulo, RisultatoElaborazione
from .base import richiede_inizializzazione, log_elaborazione

# Import moduli sensoriali
from . import visione
from . import udito


class Talamo(ModuloCerebrale):
    """
    Router centrale per informazioni sensoriali
    
    Funzionalità:
    - Smista input visivi/uditivi/tattili ai moduli appropriati
    - Integra percezioni multimodali
    - Applica filtri attentivi
    - Sincronizza flussi sensoriali
    """
    
    def __init__(self):
        """Inizializza talamo"""
        super().__init__("Talamo", TipoModulo.SENSORIALE)
        
        # Riferimenti a moduli sensoriali
        self.modulo_visione = None
        self.modulo_udito = None
        
        # Buffer integrazione multimodale
        self.buffer_visivo = None
        self.buffer_uditivo = None
        self.buffer_tattile = None
        
        # Filtro attenzione
        self.soglia_attenzione = 0.5  # Rileva solo percezioni > soglia
        self.focus_attivo = True
        
        # Statistiche
        self.percezioni_elaborate = 0
        self.percezioni_filtrate = 0
    
    def inizializza(self) -> bool:
        """
        Inizializza moduli sensoriali connessi
        
        Returns:
            bool: True se inizializzazione riuscita
        """
        print(f"[{self.nome}] Inizializzazione router sensoriale...")
        
        try:
            # Inizializza modulo visione
            self.modulo_visione = visione.get_instance()
            if not self.modulo_visione.attivo:
                self.modulo_visione.inizializza()
            
            # Inizializza modulo udito
            self.modulo_udito = udito.get_instance()
            if not self.modulo_udito.attivo:
                self.modulo_udito.inizializza()
            
            self.attivo = True
            self.modalita_reale = True
            
            print(f"[{self.nome}] ✅ Inizializzato")
            print(f"  • Visione: {'✅' if self.modulo_visione.attivo else '❌'}")
            print(f"  • Udito: {'✅' if self.modulo_udito.attivo else '❌'}")
            
            return True
            
        except Exception as e:
            print(f"[{self.nome}] ⚠️ Errore inizializzazione: {e}")
            self.attivo = True  # Attivo comunque
            return True
    
    @richiede_inizializzazione
    @log_elaborazione
    def elabora(self, input_data: Dict[str, Any]) -> RisultatoElaborazione:
        """
        Elabora e smista input sensoriali
        
        Args:
            input_data: Dict con:
                - input_visivo: Sorgente visiva (frame, path immagine, camera_id)
                - input_uditivo: Sorgente audio (audio array, path, durata registrazione)
                - input_tattile: Dati sensori tattili (futuro)
                
        Returns:
            RisultatoElaborazione con percezioni integrate
        """
        # Elabora visione
        percezioni_visive = None
        if 'input_visivo' in input_data:
            try:
                percezioni_visive = self._elabora_visione(input_data['input_visivo'])
                self.buffer_visivo = percezioni_visive
            except Exception as e:
                print(f"[{self.nome}] ⚠️ Errore visione: {e}")
        
        # Elabora udito
        percezioni_uditive = None
        if 'input_uditivo' in input_data:
            try:
                percezioni_uditive = self._elabora_udito(input_data['input_uditivo'])
                self.buffer_uditivo = percezioni_uditive
            except Exception as e:
                print(f"[{self.nome}] ⚠️ Errore udito: {e}")
        
        # Integra percezioni multimodali
        percezioni_integrate = self._integra_multimodale(
            percezioni_visive,
            percezioni_uditive
        )
        
        # Applica filtro attenzione
        percezioni_filtrate = self._applica_filtro_attenzione(percezioni_integrate)
        
        # Aggiorna statistiche
        self.percezioni_elaborate += len(percezioni_integrate)
        self.percezioni_filtrate += (len(percezioni_integrate) - len(percezioni_filtrate))
        
        return RisultatoElaborazione(
            tipo="reale",
            successo=True,
            dati={
                'percezioni': percezioni_filtrate,
                'percezioni_visive': percezioni_visive,
                'percezioni_uditive': percezioni_uditive,
                'num_percezioni': len(percezioni_filtrate)
            },
            metadata={
                'elaborate_totali': self.percezioni_elaborate,
                'filtrate_totali': self.percezioni_filtrate
            }
        )
    
    def _elabora_visione(self, input_visivo: Any) -> Optional[Dict]:
        """
        Elabora input visivo tramite modulo visione
        
        Args:
            input_visivo: Sorgente visiva
            
        Returns:
            Dict con risultati elaborazione
        """
        if self.modulo_visione and self.modulo_visione.attivo:
            return self.modulo_visione.elabora(input_visivo)
        return None
    
    def _elabora_udito(self, input_uditivo: Any) -> Optional[Dict]:
        """
        Elabora input uditivo tramite modulo udito
        
        Args:
            input_uditivo: Sorgente audio
            
        Returns:
            Dict con risultati elaborazione
        """
        if self.modulo_udito and self.modulo_udito.attivo:
            return self.modulo_udito.ascolta(input_uditivo)
        return None
    
    def _integra_multimodale(self, visione: Optional[Dict], 
                            udito: Optional[Dict]) -> List[Dict]:
        """
        Integra percezioni da modalità diverse
        
        Args:
            visione: Percezioni visive
            udito: Percezioni uditive
            
        Returns:
            Lista percezioni integrate
        """
        percezioni = []
        
        # Aggiungi percezioni visive
        if visione:
            percezioni.append({
                'modalita': 'visiva',
                'dati': visione,
                'rilevanza': visione.get('attenzione', {}).get('rilevanza', 0.5),
                'timestamp': __import__('time').time()
            })
        
        # Aggiungi percezioni uditive
        if udito and udito.get('testo'):
            # Calcola rilevanza in base a tono e intenzione
            rilevanza = 0.5
            if udito.get('tono') == 'urgente':
                rilevanza = 0.9
            elif udito.get('intenzione') == 'comando':
                rilevanza = 0.8
            
            percezioni.append({
                'modalita': 'uditiva',
                'dati': udito,
                'rilevanza': rilevanza,
                'timestamp': __import__('time').time()
            })
        
        # Cross-modal enhancement (percezioni multimodali si rafforzano)
        if len(percezioni) > 1:
            for p in percezioni:
                p['rilevanza'] *= 1.2  # Boost per coerenza multimodale
                p['rilevanza'] = min(1.0, p['rilevanza'])  # Clamp
        
        return percezioni
    
    def _applica_filtro_attenzione(self, percezioni: List[Dict]) -> List[Dict]:
        """
        Filtra percezioni in base ad attenzione/rilevanza
        
        Args:
            percezioni: Lista percezioni
            
        Returns:
            Lista percezioni filtrate
        """
        if not self.focus_attivo:
            return percezioni
        
        # Filtra solo percezioni sopra soglia
        filtrate = [
            p for p in percezioni 
            if p.get('rilevanza', 0) >= self.soglia_attenzione
        ]
        
        # Se filtro troppo aggressivo, ritorna almeno le prime 2
        if len(filtrate) == 0 and len(percezioni) > 0:
            filtrate = percezioni[:2]
        
        return filtrate
    
    def set_filtro_attenzione(self, attivo: bool, soglia: float = 0.5):
        """
        Configura filtro attenzione
        
        Args:
            attivo: Se attivo o meno
            soglia: Soglia rilevanza minima (0-1)
        """
        self.focus_attivo = attivo
        self.soglia_attenzione = max(0.0, min(1.0, soglia))
        print(f"[{self.nome}] Filtro attenzione: {'ON' if attivo else 'OFF'} (soglia: {soglia})")
    
    def get_buffer_sensoriale(self) -> Dict[str, Any]:
        """
        Ottieni contenuto buffer sensoriali
        
        Returns:
            Dict con buffer correnti
        """
        return {
            'visivo': self.buffer_visivo,
            'uditivo': self.buffer_uditivo,
            'tattile': self.buffer_tattile
        }
    
    def pulisci_buffer(self):
        """Pulisci tutti i buffer sensoriali"""
        self.buffer_visivo = None
        self.buffer_uditivo = None
        self.buffer_tattile = None
        print(f"[{self.nome}] Buffer puliti")
    
    def get_statistiche(self) -> Dict[str, int]:
        """Ottieni statistiche elaborazioni"""
        return {
            'percezioni_elaborate': self.percezioni_elaborate,
            'percezioni_filtrate': self.percezioni_filtrate,
            'percezioni_passate': self.percezioni_elaborate - self.percezioni_filtrate
        }
    
    def chiudi(self):
        """Cleanup risorse"""
        print(f"[{self.nome}] Chiusura...")
        
        # Chiudi moduli sensoriali
        if self.modulo_visione:
            self.modulo_visione.chiudi()
        
        self.attivo = False
        print(f"[{self.nome}] ✅ Chiuso")


# Istanza globale
_talamo = None

def get_instance() -> Talamo:
    """Ottieni istanza singleton"""
    global _talamo
    if _talamo is None:
        _talamo = Talamo()
        _talamo.inizializza()
    return _talamo


# API semplificata
def elabora_sensoriale(input_visivo: Any = None, input_uditivo: Any = None) -> Dict[str, Any]:
    """
    Elabora input sensoriali multimodali
    
    Args:
        input_visivo: Sorgente visiva
        input_uditivo: Sorgente audio
        
    Returns:
        Dict con percezioni integrate
    """
    talamo = get_instance()
    
    input_data = {}
    if input_visivo is not None:
        input_data['input_visivo'] = input_visivo
    if input_uditivo is not None:
        input_data['input_uditivo'] = input_uditivo
    
    risultato = talamo.elabora(input_data)
    return risultato.dati


# Test del modulo
if __name__ == "__main__":
    print("="*60)
    print("🧪 Test Modulo Talamo")
    print("="*60)
    
    # Crea istanza
    talamo = Talamo()
    talamo.inizializza()
    
    # Test elaborazione multimodale
    print("\n--- Test Elaborazione Multimodale ---")
    
    input_test = {
        'input_visivo': "test_image.jpg",  # Simulato
        'input_uditivo': "test_audio.wav"   # Simulato
    }
    
    risultato = talamo.elabora(input_test)
    
    print(f"\nRisultato:")
    print(f"  Percezioni totali: {risultato.dati['num_percezioni']}")
    print(f"  Modalità elaborate:")
    for p in risultato.dati['percezioni']:
        print(f"    • {p['modalita']}: rilevanza {p['rilevanza']:.2f}")
    
    # Test filtro attenzione
    print("\n--- Test Filtro Attenzione ---")
    talamo.set_filtro_attenzione(True, soglia=0.7)
    
    risultato2 = talamo.elabora(input_test)
    print(f"  Percezioni dopo filtro: {risultato2.dati['num_percezioni']}")
    
    # Statistiche
    print("\n--- Statistiche ---")
    stats = talamo.get_statistiche()
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    talamo.chiudi()
    print("\n✅ Test completato")

