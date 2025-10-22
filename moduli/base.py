"""
🏗️ MODULO BASE - Interfacce Astratte
======================================
Definisce le interfacce base per tutti i moduli cerebrali.
Permette di sostituire facilmente implementazioni simulate con hardware reale.

Design Pattern: Abstract Factory + Strategy
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, Optional
from dataclasses import dataclass
from enum import Enum


class TipoModulo(Enum):
    """Tipi di moduli cerebrali"""
    SENSORIALE = "sensoriale"
    COGNITIVO = "cognitivo"
    MOTORIO = "motorio"
    MEMORIA = "memoria"
    REGOLAZIONE = "regolazione"


@dataclass
class RisultatoElaborazione:
    """
    Risultato standard di elaborazione di un modulo
    
    Attributes:
        tipo: Tipo di elaborazione (reale/simulata)
        successo: True se elaborazione riuscita
        dati: Dati risultanti
        errore: Messaggio errore (se fallimento)
        metadata: Informazioni aggiuntive
    """
    tipo: str
    successo: bool
    dati: Any
    errore: Optional[str] = None
    metadata: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}


class ModuloCerebrale(ABC):
    """
    Classe base astratta per tutti i moduli cerebrali.
    
    Ogni modulo deve implementare:
    - elabora(): metodo principale di elaborazione
    - inizializza(): setup iniziale
    - chiudi(): cleanup risorse
    """
    
    def __init__(self, nome: str, tipo_modulo: TipoModulo):
        """
        Inizializza modulo base
        
        Args:
            nome: Nome identificativo del modulo
            tipo_modulo: Categoria del modulo
        """
        self.nome = nome
        self.tipo = tipo_modulo
        self.attivo = False
        self.modalita_reale = False
        self.contatore_elaborazioni = 0
        
    @abstractmethod
    def inizializza(self) -> bool:
        """
        Inizializza il modulo (carica modelli, connette hardware, ecc.)
        
        Returns:
            bool: True se inizializzazione riuscita
        """
        pass
    
    @abstractmethod
    def elabora(self, input_data: Any) -> RisultatoElaborazione:
        """
        Elabora input e produce output
        
        Args:
            input_data: Dati di input (formato dipende dal modulo)
            
        Returns:
            RisultatoElaborazione: Risultato elaborazione
        """
        pass
    
    @abstractmethod
    def chiudi(self):
        """
        Chiude il modulo e rilascia risorse
        """
        pass
    
    def __enter__(self):
        """Context manager - entry"""
        self.inizializza()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager - exit"""
        self.chiudi()


class Sensore(ABC):
    """
    Interfaccia astratta per sensori hardware/software
    
    Permette di astrarre la fonte dati (file, camera, microfono, ecc.)
    """
    
    def __init__(self, nome: str):
        self.nome = nome
        self.attivo = False
        
    @abstractmethod
    def connetti(self) -> bool:
        """
        Connette al sensore
        
        Returns:
            bool: True se connessione riuscita
        """
        pass
    
    @abstractmethod
    def leggi(self) -> Optional[Any]:
        """
        Legge dati dal sensore
        
        Returns:
            Dati letti o None se errore
        """
        pass
    
    @abstractmethod
    def disconnetti(self):
        """Disconnette dal sensore"""
        pass
    
    def __enter__(self):
        self.connetti()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnetti()


class Attuatore(ABC):
    """
    Interfaccia astratta per attuatori hardware/software
    
    Permette di astrarre l'output (motori, servo, display, ecc.)
    """
    
    def __init__(self, nome: str):
        self.nome = nome
        self.attivo = False
        
    @abstractmethod
    def connetti(self) -> bool:
        """Connette all'attuatore"""
        pass
    
    @abstractmethod
    def esegui(self, comando: Any) -> bool:
        """
        Esegue comando sull'attuatore
        
        Args:
            comando: Comando da eseguire
            
        Returns:
            bool: True se esecuzione riuscita
        """
        pass
    
    @abstractmethod
    def stop(self):
        """Stop immediato"""
        pass
    
    @abstractmethod
    def disconnetti(self):
        """Disconnette dall'attuatore"""
        pass


class MemoriaAstratta(ABC):
    """
    Interfaccia per sistemi di memoria
    """
    
    @abstractmethod
    def memorizza(self, chiave: str, valore: Any, metadata: Dict = None) -> bool:
        """Salva in memoria"""
        pass
    
    @abstractmethod
    def richiama(self, chiave: str) -> Optional[Any]:
        """Recupera dalla memoria"""
        pass
    
    @abstractmethod
    def cerca(self, query: str, limite: int = 10) -> list:
        """Ricerca semantica"""
        pass
    
    @abstractmethod
    def dimentica(self, chiave: str) -> bool:
        """Elimina dalla memoria"""
        pass


class ProcessoreCognitivo(ABC):
    """
    Interfaccia per processori cognitivi di alto livello
    """
    
    @abstractmethod
    def ragiona(self, contesto: Dict[str, Any]) -> Dict[str, Any]:
        """
        Ragionamento di alto livello
        
        Args:
            contesto: Informazioni contestuali
            
        Returns:
            Dict con decisione/output
        """
        pass
    
    @abstractmethod
    def pianifica(self, obiettivo: str, vincoli: Dict = None) -> list:
        """
        Pianificazione sequenza azioni
        
        Args:
            obiettivo: Obiettivo da raggiungere
            vincoli: Vincoli da rispettare
            
        Returns:
            Lista di azioni pianificate
        """
        pass


# ==================== UTILITY FUNCTIONS ====================

def gestisci_eccezione_hardware(func):
    """
    Decorator per gestire eccezioni hardware
    Converte fallimenti hardware in modalità simulata
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"⚠️ Errore hardware: {e}")
            print(f"   Passaggio a modalità simulata")
            # Ritorna risultato simulato di default
            return RisultatoElaborazione(
                tipo="simulato",
                successo=True,
                dati=None,
                errore=str(e)
            )
    return wrapper


def richiede_inizializzazione(func):
    """
    Decorator che verifica che il modulo sia inizializzato
    """
    def wrapper(self, *args, **kwargs):
        if not hasattr(self, 'attivo') or not self.attivo:
            raise RuntimeError(f"Modulo {self.nome} non inizializzato. Chiamare inizializza() prima.")
        return func(self, *args, **kwargs)
    return wrapper


def log_elaborazione(func):
    """
    Decorator per logging automatico elaborazioni
    """
    def wrapper(self, *args, **kwargs):
        print(f"[{self.nome}] Inizio elaborazione...")
        risultato = func(self, *args, **kwargs)
        self.contatore_elaborazioni += 1
        print(f"[{self.nome}] Elaborazione #{self.contatore_elaborazioni} completata")
        return risultato
    return wrapper


# ==================== ESEMPI DI IMPLEMENTAZIONE ====================

class SensoreFile(Sensore):
    """Sensore che legge da file (immagini, audio)"""
    
    def __init__(self, path_file: str):
        super().__init__(f"SensoreFile({path_file})")
        self.path = path_file
        
    def connetti(self) -> bool:
        """Verifica esistenza file"""
        import os
        self.attivo = os.path.exists(self.path)
        return self.attivo
    
    def leggi(self) -> Optional[str]:
        """Leggi path file"""
        if self.attivo:
            return self.path
        return None
    
    def disconnetti(self):
        """Nessuna risorsa da rilasciare"""
        self.attivo = False


class SensoreCamera(Sensore):
    """Sensore camera (da implementare con hardware reale)"""
    
    def __init__(self, camera_id: int = 0):
        super().__init__(f"Camera({camera_id})")
        self.camera_id = camera_id
        self.camera = None
        
    def connetti(self) -> bool:
        """Connette alla camera"""
        try:
            import cv2
            self.camera = cv2.VideoCapture(self.camera_id)
            self.attivo = self.camera.isOpened()
            return self.attivo
        except Exception as e:
            print(f"Errore connessione camera: {e}")
            return False
    
    def leggi(self) -> Optional[Any]:
        """Leggi frame dalla camera"""
        if self.camera and self.attivo:
            ret, frame = self.camera.read()
            return frame if ret else None
        return None
    
    def disconnetti(self):
        """Rilascia camera"""
        if self.camera:
            self.camera.release()
        self.attivo = False


class AttuatoreConsole(Attuatore):
    """Attuatore che stampa su console (debug/simulazione)"""
    
    def __init__(self):
        super().__init__("Console")
        
    def connetti(self) -> bool:
        self.attivo = True
        return True
    
    def esegui(self, comando: Any) -> bool:
        if self.attivo:
            print(f"[Attuatore] Esecuzione: {comando}")
            return True
        return False
    
    def stop(self):
        print(f"[Attuatore] STOP")
    
    def disconnetti(self):
        self.attivo = False


# Test
if __name__ == "__main__":
    print("="*60)
    print("🧪 Test Interfacce Base")
    print("="*60)
    
    # Test sensore file
    print("\n--- Test SensoreFile ---")
    with SensoreFile("test.jpg") as sensore:
        data = sensore.leggi()
        print(f"Dati letti: {data}")
    
    # Test attuatore console
    print("\n--- Test AttuatoreConsole ---")
    with AttuatoreConsole() as attuatore:
        attuatore.esegui("movimento_avanti")
        attuatore.stop()
    
    print("\n✅ Test completato")

