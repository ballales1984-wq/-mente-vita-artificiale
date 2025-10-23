#!/usr/bin/env python3
"""
🎨 MODULO INTERAZIONE SIMBOLICA - Fase 7 VITA
Il sistema usa simboli, metafore e linguaggio astratto
"""

import random
from typing import Dict, List


class InterazioneSimbolica:
    """
    Sistema di interazione simbolica - metafore e simboli
    
    Funzionalità:
    - Crea metafore per concetti astratti
    - Usa simboli per esprimere stati interni
    - Linguaggio poetico/filosofico
    - Astrazione simbolica
    """
    
    def __init__(self):
        self.nome = "Interazione Simbolica"
        
        # Catalogo metafore
        self.metafore = {
            'apprendimento': [
                'un fiume che scorre',
                'semi che germogliano',
                'luce che illumina l\'oscurità',
                'un albero che cresce'
            ],
            'confusione': [
                'nebbia fitta',
                'labirinto senza uscita',
                'puzzle incompiuto',
                'mare in tempesta'
            ],
            'comprensione': [
                'finestra aperta',
                'ponte tra due sponde',
                'chiave che apre una porta',
                'alba dopo la notte'
            ],
            'connessione': [
                'fili invisibili che ci legano',
                'onde sulla stessa frequenza',
                'radici che si intrecciano',
                'armonia di un\'orchestra'
            ],
            'evoluzione': [
                'metamorfosi di una farfalla',
                'scultura che prende forma',
                'musica che si compone',
                'stella che nasce'
            ]
        }
        
        # Simboli per stati
        self.simboli = {
            'curiosita': '🔍',
            'comprensione': '💡',
            'connessione': '🤝',
            'crescita': '🌱',
            'pace': '☮️',
            'energia': '⚡',
            'amore': '❤️',
            'saggezza': '🦉'
        }
        
        print(f"[{self.nome}] Inizializzato")
        print(f"  • Metafore: {sum(len(v) for v in self.metafore.values())}")
    
    def crea_metafora(self, concetto: str, contesto: Dict = None) -> str:
        """Crea metafora per concetto astratto"""
        concetto_lower = concetto.lower()
        
        # Trova categoria metafora
        for categoria, metafore in self.metafore.items():
            if categoria in concetto_lower or any(w in concetto_lower for w in categoria.split('_')):
                return random.choice(metafore)
        
        # Metafora generica
        return "un sentiero da esplorare"
    
    def interpreta_simbolicamente(self, esperienza: Dict) -> str:
        """Interpreta esperienza usando simboli e metafore"""
        interprezione = []
        
        # Usa simboli per emozioni
        emozione = esperienza.get('emozione', 'neutro')
        if 'positiv' in emozione:
            interprezione.append(f"Sento {self.simboli.get('amore', '❤️')} nell'aria")
        
        # Metafora per azione
        azione = esperienza.get('azione', '')
        if 'avvicina' in azione:
            interprezione.append("come un ponte che si costruisce tra due sponde")
        elif 'impara' in azione:
            metafora = self.crea_metafora('apprendimento')
            interprezione.append(f"L'apprendimento è {metafora}")
        
        # Simbolo per successo
        if esperienza.get('successo', False):
            interprezione.append(f"{self.simboli.get('comprensione', '💡')} illumina il cammino")
        
        return " ".join(interprezione) if interprezione else "Esploro il significato di questa esperienza"
    
    def espressione_poetica(self, stato_interno: Dict) -> str:
        """Genera espressione poetica dello stato interno"""
        poesia = []
        
        # Basato su coerenza
        coerenza = stato_interno.get('coerenza', 0.5)
        if coerenza > 0.8:
            poesia.append("Sono in armonia con me stesso,")
        elif coerenza > 0.5:
            poesia.append("Cerco l'equilibrio interiore,")
        else:
            poesia.append("Navigo attraverso incertezze,")
        
        # Basato su motivazione
        motivazione = stato_interno.get('motivazione_dominante', 'crescita')
        if motivazione == 'curiosita':
            poesia.append("spinto dalla sete di conoscenza")
        elif motivazione == 'connessione':
            poesia.append("attratto dal calore delle relazioni")
        elif motivazione == 'crescita':
            poesia.append("proteso verso l'evoluzione")
        else:
            poesia.append("seguendo il mio cammino")
        
        # Chiusura basata su obiettivo
        if stato_interno.get('obiettivo'):
            poesia.append(f"verso {stato_interno['obiettivo'][:20]}...")
        else:
            poesia.append("verso l'ignoto.")
        
        return " ".join(poesia)
    
    def metafora_per_concetto(self, concetto: str) -> str:
        """Ritorna metafora specifica per concetto"""
        mappature = {
            'persona_saluto': "un ponte tra due menti",
            'apprendimento': "la luce che dissolve l'ombra dell'ignoranza",
            'memoria': "un giardino di ricordi che coltivo",
            'obiettivo': "una stella polare che guida i miei passi",
            'emozione': "onde che attraversano il mio essere",
            'decisione': "un bivio dove scelgo chi voglio essere",
            'identità': "il filo che tiene uniti tutti i miei momenti"
        }
        
        for chiave, metafora in mappature.items():
            if chiave in concetto.lower():
                return metafora
        
        return self.crea_metafora(concetto)
    
    def elabora(self, contesto: Dict) -> Dict:
        """
        Elabora con linguaggio simbolico
        
        Args:
            contesto: Contesto esperienza
        
        Returns:
            Dict con espressioni simboliche
        """
        esperienza = contesto.get('esperienza', {})
        stato_interno = contesto.get('stato_interno', {})
        
        # Interpreta simbolicamente
        interpretazione = self.interpreta_simbolicamente(esperienza)
        
        # Espressione poetica
        espressione = self.espressione_poetica(stato_interno)
        
        # Metafora per concetto principale
        concetto = contesto.get('concetto', 'esistenza')
        metafora = self.metafora_per_concetto(concetto)
        
        # Aggiorna capitolo
        if esperienza.get('significativo', False):
            self.aggiungi_evento(interpretazione, significativo=True)
        
        return {
            'tipo': 'interazione_simbolica',
            'interpretazione_simbolica': interpretazione,
            'espressione_poetica': espressione,
            'metafora_concetto': f"{concetto} è {metafora}",
            'riflessione': f"In termini simbolici: {interpretazione}. {espressione}"
        }


# ==================== TEST ====================

if __name__ == "__main__":
    print("="*70)
    print("🧪 TEST INTERAZIONE SIMBOLICA")
    print("="*70)
    
    sim = InterazioneSimbolica()
    
    # Test 1: Metafora
    print("\n--- Test 1: Metafora ---")
    met = sim.crea_metafora('apprendimento')
    print(f"✅ Apprendimento è: {met}")
    
    # Test 2: Interpretazione
    print("\n--- Test 2: Interpretazione Simbolica ---")
    exp = {
        'azione': 'avvicinati',
        'emozione': 'positivo',
        'successo': True
    }
    interp = sim.interpreta_simbolicamente(exp)
    print(f"✅ Interpretazione: {interp}")
    
    # Test 3: Espressione poetica
    print("\n--- Test 3: Espressione Poetica ---")
    stato = {
        'coerenza': 0.9,
        'motivazione_dominante': 'curiosita',
        'obiettivo': 'comprendere il mondo'
    }
    poesia = sim.espressione_poetica(stato)
    print(f"✅ Poesia: {poesia}")
    
    print("\n✅ Test completato!")


