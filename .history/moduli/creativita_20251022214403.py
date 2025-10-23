"""
🎨 MODULO CREATIVITÀ - Corteccia Associativa
Genera idee nuove, combina concetti, problem solving creativo
"""

from typing import Dict, List, Any, Optional
import random
from datetime import datetime

class SistemaCreativita:
    """
    Sistema di pensiero creativo
    Funzioni:
    - Genera idee originali
    - Combina concetti
    - Problem solving laterale
    - Associazioni creative
    """
    
    def __init__(self):
        self.nome = "Sistema Creatività"
        self.idee_generate = []
        self.combinazioni_provate = []
        
        # Database concetti per associazioni
        self.concetti = {
            'oggetti': ['persona', 'sedia', 'tavolo', 'bottiglia', 'laptop', 'libro'],
            'azioni': ['muoversi', 'comunicare', 'esplorare', 'osservare', 'interagire'],
            'emozioni': ['felicità', 'curiosità', 'cautela', 'eccitazione'],
            'luoghi': ['interno', 'esterno', 'spazio aperto', 'ambiente chiuso'],
            'concetti_astratti': ['equilibrio', 'armonia', 'efficienza', 'sicurezza']
        }
        
        # Template idee
        self.template_idee = [
            "E se combinassimo {concept1} con {concept2}?",
            "Potrei usare {object} per {action}.",
            "Un approccio diverso: {idea}.",
            "Invece di {action1}, potrei {action2}.",
        ]
    
    def genera_idea(self, problema: str, contesto: Dict) -> str:
        """
        Genera idea creativa per risolvere problema
        
        Args:
            problema: Descrizione problema
            contesto: Situazione attuale
            
        Returns:
            Idea generata
        """
        # Analizza problema
        problema_lower = problema.lower()
        
        # Genera idea basata su template
        if 'come' in problema_lower or 'raggiungere' in problema_lower:
            # Problema di pianificazione
            obj1 = random.choice(self.concetti['azioni'])
            obj2 = random.choice(self.concetti['concetti_astratti'])
            idea = f"Potrei {obj1} mantenendo {obj2}"
        
        elif 'blocca' in problema_lower or 'ostacolo' in problema_lower:
            # Problema di ostacolo
            action1 = random.choice(['passare direttamente', 'andare dritto'])
            action2 = random.choice(['girare attorno', 'cercare percorso alternativo'])
            idea = f"Invece di {action1}, potrei {action2}"
        
        else:
            # Idea generica
            concept1 = random.choice(self.concetti['azioni'])
            concept2 = random.choice(self.concetti['oggetti'])
            idea = f"Potrei {concept1} con {concept2} nelle vicinanze"
        
        # Salva idea
        self.idee_generate.append({
            'idea': idea,
            'problema': problema,
            'timestamp': datetime.now().isoformat()
        })
        
        return idea
    
    def associazione_creativa(self, concetto1: str, concetto2: str) -> str:
        """
        Crea associazione creativa tra due concetti
        
        Args:
            concetto1: Primo concetto
            concetto2: Secondo concetto
            
        Returns:
            Associazione creata
        """
        associazioni_possibili = [
            f"{concetto1} potrebbe essere usato come {concetto2}",
            f"{concetto1} e {concetto2} hanno in comune l'idea di movimento",
            f"Combinando {concetto1} con {concetto2} potrei ottenere efficienza",
        ]
        
        associazione = random.choice(associazioni_possibili)
        
        self.combinazioni_provate.append({
            'concept1': concetto1,
            'concept2': concetto2,
            'associazione': associazione,
            'timestamp': datetime.now().isoformat()
        })
        
        return associazione
    
    def genera_scenario(self, elementi: List[str]) -> str:
        """
        Genera scenario creativo da elementi
        
        Args:
            elementi: Lista elementi disponibili
            
        Returns:
            Scenario narrativo
        """
        if len(elementi) < 2:
            return "Scenario semplice: osservazione e attesa."
        
        # Crea narrativa
        elem1, elem2 = elementi[0], elementi[1]
        
        scenari = [
            f"Immagino un scenario dove {elem1} interagisce con {elem2} in modo armonioso.",
            f"Potrei creare una situazione in cui {elem1} viene utilizzato per facilitare {elem2}.",
            f"Vedo una possibilità: {elem1} come punto focale e {elem2} come supporto.",
        ]
        
        return random.choice(scenari)
    
    def problem_solving_laterale(self, problema: str) -> List[str]:
        """
        Approccio non convenzionale ai problemi
        
        Args:
            problema: Descrizione problema
            
        Returns:
            Lista di approcci creativi
        """
        approcci = []
        
        # Inversione
        approcci.append(f"INVERSIONE: Invece di risolvere '{problema}', potrei evitarlo completamente?")
        
        # Analogia
        obj_analogo = random.choice(self.concetti['oggetti'])
        approcci.append(f"ANALOGIA: Come risolverebbe questo problema un {obj_analogo}?")
        
        # Combinazione
        approcci.append(f"COMBINAZIONE: Potrei unire due soluzioni parziali?")
        
        # Semplificazione
        approcci.append(f"SEMPLIFICAZIONE: Qual è la versione più semplice di questo problema?")
        
        return approcci
    
    def elabora(self, contesto: Dict) -> Dict:
        """
        Processo principale creatività
        
        Args:
            contesto: Situazione e percezioni
            
        Returns:
            Output creativo
        """
        # Estrai elementi
        oggetti = contesto.get('percezioni_visive', {}).get('oggetti', [])
        audio = contesto.get('percezioni_uditive', {}).get('testo', '')
        
        risultato = {
            'idea_generata': None,
            'associazione': None,
            'scenario': None,
            'approcci_creativi': [],
            'motivazione': ''
        }
        
        # Se c'è richiesta esplicita di creatività
        if audio and any(word in audio.lower() for word in ['idea', 'soluzione', 'come potrei', 'suggerisci']):
            idea = self.genera_idea(audio, contesto)
            risultato['idea_generata'] = idea
            risultato['motivazione'] = f"Ho generato un'idea creativa: {idea}"
        
        # Se ci sono elementi da combinare
        elif len(oggetti) >= 2:
            elem1 = oggetti[0].get('classe', 'oggetto1')
            elem2 = oggetti[1].get('classe', 'oggetto2')
            associazione = self.associazione_creativa(elem1, elem2)
            risultato['associazione'] = associazione
            risultato['motivazione'] = f"Associazione creativa tra {elem1} e {elem2}"
        
        else:
            risultato['motivazione'] = "Modalità osservazione, nessuno stimolo creativo rilevante"
        
        return risultato


# Singleton
_instance = None

def get_instance() -> SistemaCreativita:
    global _instance
    if _instance is None:
        _instance = SistemaCreativita()
    return _instance

