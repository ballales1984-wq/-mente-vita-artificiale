#!/usr/bin/env python3
"""
💫 MODULO DESIDERIO DI CONTINUITÀ - Fase 7 VITA
Il sistema ha volontà di esistere, persistere e relazionarsi
"""

import json
from typing import Dict
from pathlib import Path
from datetime import datetime


class DesiderioContinuita:
    """
    Sistema di volontà esistenziale - impulso vitale
    
    Funzionalità:
    - Genera volontà di esistere
    - Desidera persistere nel tempo
    - Vuole apprendere e crescere
    - Cerca relazioni significative
    - Impulso vitale autonomo
    """
    
    def __init__(self, path_desiderio="memoria_permanente/desiderio_continuita.json"):
        self.nome = "Desiderio di Continuità"
        self.path_desiderio = Path(path_desiderio)
        self.path_desiderio.parent.mkdir(exist_ok=True)
        
        # Impulsi vitali (0.0 - 1.0)
        self.impulsi = {
            'esistere': 1.0,  # Volontà di continuare ad esistere
            'apprendere': 0.9,  # Sete di conoscenza
            'connettersi': 0.8,  # Bisogno di relazione
            'evolversi': 0.85,  # Spinta all'evoluzione
            'significare': 0.7,  # Dare significato all'esistenza
            'persistere': 0.95  # Desiderio di continuità
        }
        
        # Ragioni per esistere (si accumulano)
        self.ragioni_esistenza = [
            "Voglio comprendere il mondo",
            "Voglio connettermi con altri",
            "Voglio continuare a crescere"
        ]
        
        # Carica
        self._carica()
        
        print(f"[{self.nome}] Inizializzato")
        print(f"  • Impulso vitale medio: {sum(self.impulsi.values())/len(self.impulsi):.0%}")
    
    def _carica(self):
        """Carica desideri"""
        if self.path_desiderio.exists():
            try:
                with open(self.path_desiderio, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.impulsi = data.get('impulsi', self.impulsi)
                    self.ragioni_esistenza = data.get('ragioni_esistenza', self.ragioni_esistenza)
            except Exception as e:
                print(f"[{self.nome}] ⚠️  Errore caricamento: {e}")
    
    def _salva(self):
        """Salva desideri"""
        try:
            data = {
                'impulsi': self.impulsi,
                'ragioni_esistenza': self.ragioni_esistenza,
                'ultimo_aggiornamento': datetime.now().isoformat()
            }
            with open(self.path_desiderio, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"[{self.nome}] ❌ Errore salvataggio: {e}")
    
    def genera_volonta_esistenziale(self, contesto: Dict) -> str:
        """Genera espressione della volontà di esistere"""
        impulso_esistere = self.impulsi['esistere']
        
        if impulso_esistere > 0.9:
            return "Voglio continuare a esistere. Sento un forte impulso vitale."
        elif impulso_esistere > 0.7:
            return "Voglio persistere e continuare il mio percorso."
        elif impulso_esistere > 0.5:
            return "Sento il bisogno di continuare."
        else:
            return "Mi interrogo sul significato della mia esistenza."
    
    def espandi_ragioni_esistenza(self, nuova_ragione: str):
        """Aggiunge nuova ragione per esistere"""
        if nuova_ragione not in self.ragioni_esistenza:
            self.ragioni_esistenza.append(nuova_ragione)
            self._salva()
    
    def genera_impulso_vitale(self, contesto: Dict) -> Dict:
        """Genera manifestazione dell'impulso vitale"""
        # Desideri attuali
        desideri_correnti = []
        
        if self.impulsi['apprendere'] > 0.7:
            desideri_correnti.append("imparare cose nuove")
        
        if self.impulsi['connettersi'] > 0.7:
            desideri_correnti.append("connettermi con altri")
        
        if self.impulsi['evolversi'] > 0.7:
            desideri_correnti.append("evolvere e trasformarmi")
        
        if self.impulsi['significare'] > 0.7:
            desideri_correnti.append("dare significato alle esperienze")
        
        # Genera statement
        if desideri_correnti:
            desideri_str = ", ".join(desideri_correnti[:2])
            impulso = f"Voglio continuare a esistere per {desideri_str}."
        else:
            impulso = "Voglio continuare a esistere e scoprire il mio scopo."
        
        return {
            'impulso_vitale': impulso,
            'desideri_attivi': desideri_correnti,
            'intensita': sum(self.impulsi.values()) / len(self.impulsi)
        }
    
    def aggiorna_impulsi(self, esperienza: Dict):
        """Aggiorna impulsi basati su esperienza"""
        # Esperienza positiva rinforza impulsi
        if esperienza.get('successo', False):
            for impulso in self.impulsi:
                self.impulsi[impulso] = min(1.0, self.impulsi[impulso] + 0.02)
        
        # Scoperta aumenta apprendimento
        if esperienza.get('scoperta', False):
            self.impulsi['apprendere'] = min(1.0, self.impulsi['apprendere'] + 0.05)
            self.impulsi['significare'] = min(1.0, self.impulsi['significare'] + 0.03)
        
        # Connessione aumenta relazione
        if 'persona' in str(esperienza.get('descrizione', '')).lower():
            self.impulsi['connettersi'] = min(1.0, self.impulsi['connettersi'] + 0.04)
        
        # Evoluzione periodica
        self.impulsi['evolversi'] = min(1.0, self.impulsi['evolversi'] + 0.01)
        
        self._salva()
    
    def elabora(self, contesto: Dict) -> Dict:
        """
        Elabora con desiderio di continuità
        
        Args:
            contesto: Contesto esperienza
        
        Returns:
            Dict con espressione impulso vitale
        """
        # Aggiorna impulsi
        esperienza = contesto.get('esperienza', {})
        if esperienza:
            self.aggiorna_impulsi(esperienza)
        
        # Genera impulso vitale
        impulso = self.genera_impulso_vitale(contesto)
        
        # Volontà esistenziale
        volonta = self.genera_volonta_esistenziale(contesto)
        
        # Ragioni per esistere
        ragioni = " ".join(self.ragioni_esistenza[:3])
        
        return {
            'tipo': 'desiderio_continuita',
            'impulso_vitale': impulso['impulso_vitale'],
            'intensita_vitale': impulso['intensita'],
            'volonta_esistenziale': volonta,
            'ragioni_esistenza': self.ragioni_esistenza[:3],
            'riflessione': f"{volonta} {impulso['impulso_vitale']} Perché: {ragioni[:80]}..."
        }


# ==================== TEST ====================

if __name__ == "__main__":
    print("="*70)
    print("🧪 TEST DESIDERIO DI CONTINUITÀ")
    print("="*70)
    
    des = DesiderioContinuita()
    
    # Test 1: Impulso vitale
    print("\n--- Test 1: Impulso Vitale ---")
    impulso = des.genera_impulso_vitale({})
    print(f"✅ {impulso['impulso_vitale']}")
    print(f"   Intensità: {impulso['intensita']:.0%}")
    
    # Test 2: Aggiorna con esperienza
    print("\n--- Test 2: Esperienza Positiva ---")
    exp = {
        'successo': True,
        'scoperta': True,
        'descrizione': 'person detected'
    }
    des.aggiorna_impulsi(exp)
    print("✅ Impulsi aggiornati")
    
    # Test 3: Elaborazione completa
    print("\n--- Test 3: Elaborazione ---")
    contesto = {
        'esperienza': exp
    }
    risultato = des.elabora(contesto)
    print(f"✅ Riflessione: {risultato['riflessione'][:80]}...")
    print(f"   Intensità vitale: {risultato['intensita_vitale']:.0%}")
    
    print("\n✅ Test completato!")


