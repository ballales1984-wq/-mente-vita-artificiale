"""
🧠 MODULO APPRENDIMENTO ONLINE - Apprendimento Incrementale
============================================================
Rete neurale che si aggiorna in tempo reale durante l'esecuzione.

Funzionalità:
- Apprendimento incrementale (online learning)
- Aggiornamento pesi in tempo reale
- Classificazione stimoli → azioni
- Salvataggio/caricamento modello
- Integrazione con sistema reward
"""

import os
from typing import List, Tuple, Optional
import numpy as np

# Import condizionali
try:
    import torch
    import torch.nn as nn
    import torch.optim as optim
    TORCH_AVAILABLE = True
    
    class ReteCognitiva(nn.Module):
    """
    Rete neurale per apprendimento cognitivo
    
    Architettura:
    - Input: 10 features (stimolo visivo + uditivo codificato)
    - Hidden: 32 neuroni
    - Output: 5 azioni possibili
    """
    
    def __init__(self, input_size: int = 10, hidden_size: int = 32, output_size: int = 5):
        super().__init__()
        
        self.fc = nn.Sequential(
            nn.Linear(input_size, hidden_size),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(hidden_size, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, output_size)
        )
    
    def forward(self, x):
        return self.fc(x)


class ApprendimentoOnline:
    """
    Sistema di apprendimento incrementale online
    
    Caratteristiche:
    - Apprende da ogni esperienza
    - Aggiorna modello in real-time
    - Integrato con sistema reward
    - Salvataggio automatico
    """
    
    def __init__(self, learning_rate: float = 0.001, path_modello: str = "data/modello_online.pt"):
        self.nome = "Apprendimento Online"
        
        # Configurazione
        self.learning_rate = learning_rate
        self.path_modello = path_modello
        
        # Mapping azioni
        self.azioni = [
            'monitora_ambiente',
            'avvicinati',
            'allontanati',
            'esegui_comando',
            'mantieni_distanza'
        ]
        
        self.num_azioni = len(self.azioni)
        
        # Modello
        self.modello = None
        self.ottimizzatore = None
        self.criterio = None
        
        # Statistiche
        self.cicli_apprendimento = 0
        self.loss_media = 0.0
        self.accuratezza = 0.0
        
        # Storia training
        self.storia_loss = []
        
        if TORCH_AVAILABLE:
            self._inizializza_modello()
        else:
            print(f"[{self.nome}] ⚠️ PyTorch non disponibile")
    
    def _inizializza_modello(self):
        """Inizializza rete neurale"""
        print(f"[{self.nome}] Inizializzazione rete neurale...")
        
        # Crea modello
        self.modello = ReteCognitiva(
            input_size=10,
            hidden_size=32,
            output_size=self.num_azioni
        )
        
        # Ottimizzatore
        self.ottimizzatore = optim.Adam(
            self.modello.parameters(),
            lr=self.learning_rate
        )
        
        # Loss function
        self.criterio = nn.CrossEntropyLoss()
        
        # Carica pesi se esistono
        if os.path.exists(self.path_modello):
            try:
                self.modello.load_state_dict(torch.load(self.path_modello))
                print(f"[{self.nome}] ✅ Modello caricato da: {self.path_modello}")
            except Exception as e:
                print(f"[{self.nome}] ⚠️ Impossibile caricare modello: {e}")
        else:
            print(f"[{self.nome}] ✅ Nuovo modello inizializzato")
        
        print(f"[{self.nome}]    → Input: 10 features")
        print(f"[{self.nome}]    → Hidden: 32 neuroni")
        print(f"[{self.nome}]    → Output: {self.num_azioni} azioni")
    
    def codifica_stimolo(self, percezioni_visive: dict, percezioni_uditive: dict) -> np.ndarray:
        """
        Codifica percezioni in vettore numerico
        
        Args:
            percezioni_visive: Output modulo visione
            percezioni_uditive: Output modulo udito
            
        Returns:
            Array numpy di 10 features
        """
        features = []
        
        # Features visive (5)
        features.append(percezioni_visive.get('num_oggetti', 0) / 10.0)  # Normalizzato
        
        attenzione = percezioni_visive.get('attenzione', {})
        features.append(attenzione.get('rilevanza', 0.0))
        
        # Presenza oggetti chiave
        oggetti = [obj.get('classe', '') for obj in percezioni_visive.get('oggetti', [])]
        features.append(1.0 if 'person' in oggetti else 0.0)
        features.append(1.0 if 'car' in oggetti else 0.0)
        features.append(1.0 if any(o in oggetti for o in ['chair', 'bottle', 'laptop']) else 0.0)
        
        # Features uditive (5)
        tono_map = {'amichevole': 1.0, 'urgente': 0.5, 'negativo': -1.0, 'neutro': 0.0}
        features.append(tono_map.get(percezioni_uditive.get('tono', 'neutro'), 0.0))
        
        intenzione_map = {'comando': 1.0, 'domanda': 0.5, 'affermazione': 0.0}
        features.append(intenzione_map.get(percezioni_uditive.get('intenzione', 'incerto'), 0.0))
        
        emozione_map = {'gioia': 1.0, 'neutro': 0.0, 'tristezza': -0.5, 'paura': -1.0}
        features.append(emozione_map.get(percezioni_uditive.get('emozione', 'neutro'), 0.0))
        
        # Lunghezza testo (normalizzata)
        testo_len = len(percezioni_uditive.get('testo', ''))
        features.append(min(1.0, testo_len / 50.0))
        
        # Presenza comando vocale
        testo_lower = percezioni_uditive.get('testo', '').lower()
        features.append(1.0 if any(cmd in testo_lower for cmd in ['vieni', 'vai', 'fermati']) else 0.0)
        
        return np.array(features, dtype=np.float32)
    
    def apprendi_da_esperienza(self, stimolo: np.ndarray, azione_eseguita: str, 
                               reward: float) -> float:
        """
        Apprende da un'esperienza (apprendimento incrementale)
        
        Args:
            stimolo: Vettore features (10 dimensioni)
            azione_eseguita: Nome azione
            reward: Reward ottenuto
            
        Returns:
            float: Loss dell'aggiornamento
        """
        if not TORCH_AVAILABLE or self.modello is None:
            return 0.0
        
        try:
            # Converti azione in indice
            if azione_eseguita in self.azioni:
                target_idx = self.azioni.index(azione_eseguita)
            else:
                target_idx = 0  # Default: monitora_ambiente
            
            # Converti in tensori
            input_tensor = torch.tensor(stimolo, dtype=torch.float32).unsqueeze(0)
            target_tensor = torch.tensor([target_idx], dtype=torch.long)
            
            # Forward pass
            self.modello.train()
            output = self.modello(input_tensor)
            
            # Calcola loss
            loss = self.criterio(output, target_tensor)
            
            # Modula loss con reward (se reward positivo, rafforza; se negativo, indebolisce)
            loss_modulata = loss * (2.0 - reward)  # reward alto → loss bassa
            
            # Backward pass
            self.ottimizzatore.zero_grad()
            loss_modulata.backward()
            self.ottimizzatore.step()
            
            # Statistiche
            self.cicli_apprendimento += 1
            self.storia_loss.append(loss.item())
            
            if len(self.storia_loss) > 100:
                self.storia_loss = self.storia_loss[-100:]
            
            self.loss_media = sum(self.storia_loss) / len(self.storia_loss)
            
            # Salva periodicamente
            if self.cicli_apprendimento % 10 == 0:
                self.salva_modello()
            
            return loss.item()
            
        except Exception as e:
            print(f"[{self.nome}] ⚠️ Errore apprendimento: {e}")
            return 0.0
    
    def predici_azione(self, stimolo: np.ndarray) -> Tuple[str, float]:
        """
        Predice miglior azione dato uno stimolo
        
        Args:
            stimolo: Vettore features
            
        Returns:
            Tuple (azione, confidence)
        """
        if not TORCH_AVAILABLE or self.modello is None:
            return 'monitora_ambiente', 0.5
        
        try:
            self.modello.eval()
            
            with torch.no_grad():
                input_tensor = torch.tensor(stimolo, dtype=torch.float32).unsqueeze(0)
                output = self.modello(input_tensor)
                
                # Softmax per probabilità
                probs = torch.softmax(output, dim=1)
                
                # Azione con probabilità maggiore
                max_prob, max_idx = torch.max(probs, dim=1)
                
                azione = self.azioni[max_idx.item()]
                confidence = max_prob.item()
            
            return azione, confidence
            
        except Exception as e:
            print(f"[{self.nome}] ⚠️ Errore predizione: {e}")
            return 'monitora_ambiente', 0.5
    
    def salva_modello(self):
        """Salva pesi del modello"""
        if not TORCH_AVAILABLE or self.modello is None:
            return
        
        try:
            # Crea directory se non esiste
            os.makedirs(os.path.dirname(self.path_modello), exist_ok=True)
            
            torch.save(self.modello.state_dict(), self.path_modello)
            
        except Exception as e:
            print(f"[{self.nome}] ⚠️ Errore salvataggio: {e}")
    
    def get_statistiche(self) -> dict:
        """Ottieni statistiche apprendimento"""
        return {
            'cicli_apprendimento': self.cicli_apprendimento,
            'loss_media': self.loss_media,
            'loss_corrente': self.storia_loss[-1] if self.storia_loss else 0.0,
            'modello_salvato': os.path.exists(self.path_modello)
        }


# Istanza globale
_apprendimento = None

def get_instance() -> ApprendimentoOnline:
    """Ottieni istanza singleton"""
    global _apprendimento
    if _apprendimento is None:
        _apprendimento = ApprendimentoOnline()
    return _apprendimento


# Test del modulo
if __name__ == "__main__":
    print("="*70)
    print("TEST APPRENDIMENTO ONLINE")
    print("="*70)
    
    if not TORCH_AVAILABLE:
        print("\n[ERROR] PyTorch non disponibile!")
        print("Installa con: pip install torch")
        exit(1)
    
    # Crea sistema
    sistema = ApprendimentoOnline()
    
    print("\n[TEST] Simulazione 10 cicli di apprendimento...\n")
    
    # Simula apprendimento
    import random
    
    for i in range(10):
        # Genera stimolo random
        stimolo = np.random.rand(10).astype(np.float32)
        
        # Azione e reward simulati
        azioni = ['monitora_ambiente', 'avvicinati', 'allontanati', 'esegui_comando']
        azione = random.choice(azioni)
        reward = random.uniform(0.5, 1.5)
        
        # Apprendi
        loss = sistema.apprendi_da_esperienza(stimolo, azione, reward)
        
        print(f"Ciclo {i+1}: Azione={azione}, Reward={reward:+.2f}, Loss={loss:.4f}")
    
    # Test predizione
    print("\n[TEST] Predizione azione...")
    stimolo_test = np.random.rand(10).astype(np.float32)
    azione_pred, conf = sistema.predici_azione(stimolo_test)
    
    print(f"  Azione predetta: {azione_pred}")
    print(f"  Confidence: {conf:.2%}")
    
    # Statistiche
    print("\n[STATISTICHE]")
    stats = sistema.get_statistiche()
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    print("\n[OK] Test completato")

